function test(event) {
    var current = event.currentTarget
    console.log(`evnet is ${event.type}`)
    console.log(`evnet is ${current.id}`)
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
    let category = ['한식', '중식', '일식', '한정식', '중국음식']

    $('#search').keyup(function (arg) {
        let txt = $(this).val();
        let auto_search = $('#auto-search');
        let count = 0;
        if (txt !== '') {
            auto_search.css('display', 'block')
            auto_search.children().remove();
            for (let i = 0; i < category.length; i++) {
                if (category[i].indexOf(txt) !== -1) {
                    console.log('txt is in!! value is ', category[i])
                    let word_list = category[i].split(txt)
                    console.log('slicing txt is', word_list)

                    auto_search.append(`
                    <div class="auto-search-content">${word_list[0]}<b style="color: #ec6f1f">${ txt }</b>${word_list[1]}</div>
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

function load_search_result(){
    let txt = $('#search').val();
    $.ajax({
        type: 'post',
        url: '/home/load_search',
        data: {'target': txt},
        success: function(response){

        }
    })
}


