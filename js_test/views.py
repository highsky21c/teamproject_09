
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FindIdForm #실제로는 user앱에서 이렇게 작성할것
from django.views.generic import View
from django.utils.decorators import method_decorator
from .decorators import login_message_required, admin_required, logout_message_required
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Store
from favorite.models import Favorite


def main(request):  # 메인 화면
    storebox = []
    for i in range(10):
        store = {'photo': '/static/img/333417_1640610154368611.jpg', 'store': i}
        storebox.append(store)

    return render(request, 'home.html', {'container': storebox})


def detail(request):
    storebox = []
    for i in range(10):
        store = {'avatar': '/static/img/333417_1640610154368611.jpg', 'username': 'username', 'comment_id': i, 'comment_content':'asdfadfadfadf'}
        storebox.append(store)
    return render(request, 'detail.html', {'container': storebox})

def join(request):
    return render(request, 'sign-up.html',{})

def login(request):
    return render(request, 'sign-in.html', {})

def findid(request):
    return render(request, 'find-id.html', {})

def ajax_find_id_view(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    result_id = Store.objects.get(store_name=name, last_order=email)

    return HttpResponse(json.dumps({"result_id": result_id.store_name}, cls=DjangoJSONEncoder),
                        content_type="application/json")


def findpw(request):
    return render(request, 'find-pw.html', {})

def profile(request, id):
    all_Store = Store.objects.filter(id=id).order_by('id')
    # kind_of_food = Store.objects.filter('kind_of_food')
    # foods = kind_of_food.split(',')
    return render(request, 'profile.html', {'stores' : all_Store},)

def test(request): #체크박스 값들 받아오는것.
    a=request.POST.getlist('food')
    return a
