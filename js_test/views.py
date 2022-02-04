from django.shortcuts import render, redirect
from django.http import HttpResponse


def main(request):  # 메인 화면
    storebox = []
    for i in range(10):
        store = {'photo': '/static/img/333417_1640610154368611.jpg', 'store':i}
        storebox.append(store)

    return render(request, 'home.html', {'container' : storebox})


def detail(request):
    return render(request, 'detail.html', {})
