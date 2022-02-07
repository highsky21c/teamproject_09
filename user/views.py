#실제 기능 동작
from django.contrib import auth #장고 기본 제공 모듈
from django.contrib.auth import get_user_model #사용자가 DB안에 있는 지 검사하는 함수
from django.shortcuts import render, redirect  # render는 html 보여주는 것.
from .models import UserModel #동일한 위치에 있는 models 파일에서 UserModel을 import
from django.contrib.auth.decorators import login_required
import json


def sign_up_view(request): #회원가입 화면이 실행될 때,
    if request.method == 'GET': #GET 방식으로
        user = request.user.is_authenticated #유저가 로그인&인증이 되었는 지 모두 확인
        if user: #유저가 있으면
            return redirect('/user/') #기본페이지로 이동
        else: #없으면
            return render(request, 'sign-up.html') #회원가입 페이지만을 보여줌
    elif request.method == 'POST': #POST 방식이면 아래 정보를 가져옴
        #아래 데이터를 가져오고, 없으면 빈 문자열 처리 후 변수에 저장
        last_name = request.POST.get('last_name', '') #이름
        username = request.POST.get('username', '') #아이디
        password = request.POST.get('password', '') #비밀번호
        password2 = request.POST.get('password2', '') #비밀번호 확인
        email = request.POST.get('email', '') # 이메일
        bio = request.POST.get('bio', '') #선택사항 물음(inch)
        # like_food = request.POST.get('like_food', '')

        checklist = ['한식', '이탈리안', '중식', '국수', '일식', '고기요리'] #배열 -> 장고에서는 배열 X -> 문자화
        #검색 : 장고 list 데이터 처리

        json_checklist = json.dumps(checklist) #dumps가 문자화 하는 method

        if password != password2: #패스워드 체크 : 같지 않다면
            return render(request, 'sign-up.html', {'error': '비밀번호 재확인'}) #회원가입 페이지
        else: #같다면
            if last_name == '' or username == '' or password == '' or email == '':
                return render(request, 'sign-up.html', {'error': '이름,아이디,비밀번호,이메일 필수'})

            exist_username = get_user_model().objects.filter(username=username)  #내가 입력한 username(좌)이 username에 있는 지 get_user_model() 함수로 확인
            exist_email = get_user_model().objects.filter(email=email)
            if exist_username: # ID 중복이면
                return render(request, 'sign-up.html', {'error':'아이디 존재'}) #회원가입화면
            elif exist_email:  # email 중복이면
                return render(request, 'sign-up.html', {'error': '이메일 존재'}) #회원가입화면
            else: #중복이 아니면
                UserModel.objects.create_user(last_name=last_name, username=username, password=password, email=email, bio=bio, like_food=json_checklist ) #유저생성
                return render(request,'sign-in.html',{}) #회원가입(사용자 저장) 완료후 로그인페이지로 이동


def sign_in_view(request): #로그인 화면이 실행될 때,
    if request.method == 'POST':
        username = request.POST.get('username', None) #아이디 ('username'는 sign-in page의 input의 name과 동일하게 작성)
        password = request.POST.get('password', None) #비밀번호

        me =auth.authenticate(request, username=username, password=password) #장고인증기능 모듈 (현재 비번과 암호화된 비번 일치 여부 확인)
        #user앱의 UserModel에서 username=username가져옴. 좌: UserModel(DB)안에 있는 username값 우: POST에서 받아온 데이터
        if me is not None: #사용자가 있다면(is not None)
            auth.login(request,me) #변수 me 정보로 로그인
            return redirect('/user/') # 기본url(기본페이지)
        else: #없다면
            return redirect('/user/sign-in') #로그인 페이지로
    elif request.method == 'GET':
        user = request.user.is_authenticated  # 유저가 로그인&인증이 되었는 지 모두 확인
        if user: #user가 있으면
            return redirect('/user/') #기본페이지
        else: #없으면
            return render(request, 'user/sign-in.html') #로그인화면

@login_required #사용자가 로그인되어야 가능
def logout(request):
    auth.logout(request)
    return redirect('/user/') #tweet의 home -> 사용자가 없으면 -> 로그인 화면

# @login_required #사용자가 로그인되어야 가능
def show_profile(request):
    if request.method == 'GET':
        return render(request, 'profile.html', {})

def show_home(request):
    if request.method == 'GET':
        return render(request, 'home.html', {})