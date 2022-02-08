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

// const test_scroll_right = document.getElementById('slider_right')
// test_scroll_right.addEventListener('click', function () {
//     scroll('right')
// })
//
// const test_scroll_left = document.getElementById('slider_left')
// test_scroll_left.addEventListener('click', function () {
//     scroll('left')
// })


// function scroll(dir) {
//     const row = document.getElementById('recommend_row')
//     const left_slider = document.getElementById('slider_left')
//     const right_slider = document.getElementById('slider_right')
//     if (dir === 'right') {
//         value = 1000;
//     } else {
//         value = -1000;
//     }
//     // row.scrollLeft += value;
//     if (row.scrollLeft <= 100) {
//         left_slider.style.display = 'none'
//         right_slider.style.display = 'flex'
//     } else if (row.scrollLeft <= 1450) {
//         left_slider.style.display = 'flex'
//         right_slider.style.display = 'flex'
//     } else {
//         left_slider.style.display = 'flex'
//         right_slider.style.display = 'none'
//     }
//     console.log(row.scrollLeft)
// }

function zoomIn(event) {
    event.target.style.width = "600px";
    event.target.style.height = "336px";
    event.target.style.transition = "all 0.5s";
}

function zoomOut(event) {

    event.target.style.width = "500px";
    event.target.style.height = "280px";
    event.target.style.transition = "all 0.5s";
    event.target.style.zIndex = '10';
    event.target.style.display = 'static';
}


var swiper = new Swiper(".recommend_content", {
    slidesPerView: 3,
    spaceBetween: 10,
    navigation: {
        nextEl: ".right",
        prevEl: ".left",
    },
});

$(function () {
    let category = [
        '오리요리', '퓨전 한식', '기타 한식', '백반', '찌개', '철판 요리', '해산물요리', '탕', '전골', '국수', '전통한식', '뷔페',
        '정통 일식', '면요리', '스시', '라멘', '일반 일식', '기타 일식', '까스요리', '회', '오뎅', '일본카레', '소바', '벤토', '돈부리', ' 꼬치', '우동',
          '이자카야',
        '퓨전 양식', '기타양식', '스테이크', '바베큐', '버거',
        '기타 중식', '딤섬', '정통 중식', '만두', '일반 중식',
        '다국적 퓨전', '와인', '세계음식 기타', '이탈리안', '고기', '프랑스 음식', '닭', '다국적아시아음식', '태국 음식', '베트남음식', '인도 음식',
        '전통주점', '칵테일', '포차',
        '브런치', '디저트', '베이커리', '샌드위치', '카페'
    ]

    $('#search').keyup(function (arg) {
        let txt = $(this).val();
        let auto_search = $('#auto-search');
        let count = 0;
        if (txt !== '') {
            auto_search.css('display', 'block')
            auto_search.children().remove();
            for (let i = 0; i < category.length; i++) {
                if (category[i].indexOf(txt) !== -1) {
                    let word_list = category[i].split(txt)
                    auto_search.append(`
                    <div class="auto-search-content" onclick="auto_click(this.text)">${word_list[0]}<b style="color: #ec6f1f">${ txt }</b>${word_list[1]}</div>
                    `)
                    count +=1
                }
            }
            if(count <=0){
                auto_search.css('display', 'none')
            }
        } else {
            auto_search.css('display', 'none')
        }

    })

});

function auto_click(text){
    console.log(text)
}

function load_search_result(){
    let txt = $('#search').val();
    window.scrollTo(0,800)
    $.ajax({
        type: 'post',
        url: '/home/load_search',
        data: {'target': txt},
        success: function(response){
        }
    })
}


