from django.shortcuts import render, redirect
from django.http import HttpResponse


def main(request):  # 메인 화면
    return render(request, 'home.html', {})


def detail(request):
    return render(request, 'detail.html', {})

def join(request):
    return render(request, 'sign-up.html',{})