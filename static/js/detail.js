// csrf 토큰 받아오는 과정 - Ajax 사용하기 위함
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

///////////////////////


//javascript 시작 부분
$(document).ready(function () {
    //CSRF Token 관련
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    document.getElementById('favorite_off').style.display = 'flex'
    document.getElementById('favorite_on').style.display = 'none'
    document.getElementById('like_off').style.display = 'flex'
    document.getElementById('like_on').style.display = 'none'

    var comments = document.getElementsByClassName('comment_row')

    for(let i=0; i<comments.length; i++){
        const comment = comments[0]
        if(i>=3){
            comments[i].style.display='none'
        }
    }
});

//Map Loading
var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

// 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);

var geocoder = new kakao.maps.services.Geocoder();

let store_address = $('#store_address').text()

let storename = $('#store_name').text()

console.log(store_address)

geocoder.addressSearch(store_address, function (result, status) {

    // 정상적으로 검색이 완료됐으면
    if (status === kakao.maps.services.Status.OK) {

        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

        // 결과값으로 받은 위치를 마커로 표시합니다
        var marker = new kakao.maps.Marker({
            map: map,
            position: coords
        });

        // 인포윈도우로 장소에 대한 설명을 표시합니다
        var infowindow = new kakao.maps.InfoWindow({
            content: `<div style="width:150px;text-align:center;padding:6px 0;">${storename}</div>`
        });

        infowindow.open(map, marker);

        // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
        map.setCenter(coords);
    } else {
    }
});


// 즐겨 찾기 추가 함수
function favorite() {
    var favorite_off = document.getElementById('favorite_off')
    var favorite_on = document.getElementById('favorite_on')
    let storename = $('#store_name').text()
    if (favorite_off.style.display === 'flex') {
        //favorite off 상태
        favorite_off.style.display = 'none'
        favorite_on.style.display = 'flex'
        $.ajax({
            type: 'POST',
            url: '/favorite/add',
            data: {'store_name': storename},
            success: function (response) {
                console.log(response['result'])
            }
        })
    } else {
        favorite_off.style.display = 'flex'
        favorite_on.style.display = 'none'
        $.ajax({
            type: 'POST',
            url: '/favorite/delete',
            data: {'store_name': storename},
            success: function (response) {
                console.log(response['result'])
            }
        })
    }
}

// 좋아요 추가 및 삭제 함수
function like() {
    var like_off = document.getElementById('like_off')
    var like_on = document.getElementById('like_on')
    let storename = $('#store_name').text()
    if (like_off.style.display === 'flex') {
        //favorite off 상태
        like_off.style.display = 'none'
        like_on.style.display = 'flex'
        // $.ajax({
        //     type: 'POST',
        //     url: '/favorite/add',
        //     data: {'store_name': storename},
        //     success: function (response) {
        //         console.log(response['result'])
        //     }
        // })
    } else {
        like_off.style.display = 'flex'
        like_on.style.display = 'none'
        // $.ajax({
        //     type: 'POST',
        //     url: '/favorite/delete',
        //     data: {'store_name': storename},
        //     success: function (response) {
        //         console.log(response['result'])
        //     }
        // })
    }
}

function comment_like(id) {
    let check = document.getElementById(id)
    let comment_id = id.split('_').pop()

    var comment_like_on = document.getElementById('comment_'+ comment_id +'_on')
    var comment_like_off = document.getElementById('comment_'+ comment_id +'_off')

    if(comment_like_off.style.display ==='flex'){
        comment_like_off.style.display = 'none'
        comment_like_on.style.display = 'flex'
    }
    else{
        comment_like_off.style.display = 'flex'
        comment_like_on.style.display = 'none'
    }
    console.log(comment_like_on)

}

//슬라이더 함수
var swiper = new Swiper(".content_photo_container", {
    slidesPerView: 4,
    spaceBetween: 5,
    navigation: {
        nextEl: ".right",
        prevEl: ".left",
    },
});

var swiper = new Swiper(".recommend_another", {
    slidesPerView: 3,
    spaceBetween: 5,
    navigation: {
        nextEl: ".right",
        prevEl: ".left",
    },
});

function more(id){
    let comments = document.getElementsByClassName('comment_row')
    let comment_cnt = 0
    let more_button = document.getElementById(id)
    for(let i =0; i<=comments.length; i++){
        if(comments[i].style.display==='none'){
            comment_cnt=i;
            break;
        }
    }
    for(let k=comment_cnt; k<comment_cnt+3;k++){
        if(k>=comments.length){
            more_button.style.display='none'
            return
        }
        comments[k].style.display ='flex'
    }
}

function write_comments(){
    const textarea = document.getElementById('comment_text')
    let text = textarea.value
    let scroll_value = $(document).scrollTop();
    console.log(scroll_value)
    $.ajax({
        type:'post',
        url: '/comment/write',
        data: {'comment': text},
        success: function(response){
            console.log(response['result'])
        }
    })
    window.location.reload()
    window.scrollTo(0, scroll_value)
    textarea.value = ''
}
