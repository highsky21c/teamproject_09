function test(event) {
    var current = event.currentTarget
    console.log(`evnet is ${event.type}`)
    console.log(`evnet is ${current.id}`)
}

const test_scroll_right = document.getElementById('slider_right')
test_scroll_right.addEventListener('click', function () {
    scroll('right')
})

const test_scroll_left = document.getElementById('slider_left')
test_scroll_left.addEventListener('click', function () {
    scroll('left')
})


function scroll(dir) {
    const row = document.getElementById('recommend_row')
    const left_slider = document.getElementById('slider_left')
    const right_slider = document.getElementById('slider_right')
    if (dir === 'right') {
        value = 1000;
    } else {
        value = -1000;
    }
    // row.scrollLeft += value;
    if (row.scrollLeft <= 100) {
        left_slider.style.display = 'none'
        right_slider.style.display = 'flex'
    } else if (row.scrollLeft <= 1450) {
        left_slider.style.display = 'flex'
        right_slider.style.display = 'flex'
    } else {
        left_slider.style.display = 'flex'
        right_slider.style.display = 'none'
    }
    console.log(row.scrollLeft)
}

function zoomIn(event) {
    event.target.style.width = "600px";
    event.target.style.height = "336px";
    event.target.style.transition = "all 0.5s";
}

function zoomOut(event) {
    event.target.style.width = "500px";
    event.target.style.height = "280px";
    event.target.style.transition = "all 0.5s";
}


var swiper = new Swiper(".mySwiper", {
    slidesPerView: 4,
    spaceBetween: 10,
    navigation: {
        nextEl: ".right",
        prevEl: ".left",
    },
});

