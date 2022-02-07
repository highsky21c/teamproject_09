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



$(document).ready(function() {
    //html의 body를 body라는 변수로 선언
    const body = document.querySelector("body");

    const IMG_NUMBER = 9;//이미지파일 개수가 9개

function genRandom(){//math.random*n 하면 0~n까지의 랜덤넘버가 소수점으로 뜸
    //소수점은 필요없으니 math.floor함수로 소수점버리고 정수만 리턴
    const number = Math.floor(Math.random()*IMG_NUMBER);
    return number;//0~9까지의 숫자가 랜덤하게 생성되어 반환됨
}

function paintImage(imgNumber){
    const image = new Image();
    image.src = `/static/img/${imgNumber + 1}.png`; //1~9가되도록 +1
    body.appendChild(image);//노드개념은 모르겠고 appendChild 를 통해 요소를 삽입하면 맨뒤에 위치하게 된다고함
    image.classList.add("bgImg");//image에 클래스값을 "bgimg"로 생성. CSS작업할수 있대.
}

function init(){
    const randomNumber = genRandom();//함수에서 랜덤숫자 받아와서 randomNumber에 저장
    paintImage(randomNumber);
}
init();

var csrftoken = getCookie('csrftoken');
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



$('#find-id').click(function () {
    var name = $("#username").val();
    var email = $("#email").val();

    $.ajax({
        type: "POST",
        url: "/find-id/find/",
        dataType: "json",
        data: {
            'name': name,
            'email': email,
        },
        success: function (response) {
            console.log(response)
            $('#result_id').replaceWith(
                '<div id="result_id"><hr><div style="text-align:center;"><span style="font-size: 16px;">입력된 정보로 가입된 아이디는 </span><span style="font-size: 20px; font-weight: bold;" id="result_id">' + response.result_id +
                '</span><span style="font-size: 16px;"> 입니다.</span></div><hr></div>')
        },
        error: function () {
            if (name == "" || email == "") {
                alert('이름와 이메일을 입력해주세요.');
            } else {
                alert('입력하신 정보가 일치하지 않거나 존재하지 않습니다.');
            }
        },
    });
});

});

// function show_modal(){
//     const modal = document.getElementById("modal");//html에서 id가 modal인애를 modal로 선언
//     const find_id_btn = document.getElementById("find-id");//html에서 id가 find-id인애를 btn로 선언
//     find_id_btn.addEventListener("click", e => {//버튼클릭했을때 모달을 띄우게.......?해도되는거니....
//         modal.style.display = "flex"; //get으로 다른url로 나타내야하느것 아니뉘..?
//     });
// }


