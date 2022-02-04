from django.shortcuts import render, redirect
from django.http import HttpResponse


def main(request):  # 메인 화면
    return render(request, 'home.html', {})


def detail(request):
    return render(request, 'detail.html', {})

def join(request):
    return render(request, 'sign-up.html',{})

def login(request):
    return render(request, 'login.html', {})

def findid(request):
    return render(request, 'find-id.html', {})

def findpw(request):
    return render(request, 'find-pw.html', {})

def profile(request):
    return render(request, 'profile.html', {})

def test(request):
    a=request.POST.getlist('food')
    return a
