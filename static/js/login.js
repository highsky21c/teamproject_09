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
});