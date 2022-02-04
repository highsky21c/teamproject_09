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