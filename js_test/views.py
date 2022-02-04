from django.shortcuts import render, redirect
from django.http import HttpResponse


def main(request):  # 메인 화면
    storebox = []
    for i in range(10):
        store = {'photo': '/static/img/333417_1640610154368611.jpg', 'store': i}
        storebox.append(store)

    return render(request, 'home.html', {'container': storebox})


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
