
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


def detail(request, store_name):
    # user = request.user
    user = 'js'
    store = Store.objects.filter(store_name=store_name)[0]
    favorite = Favorite.objects.filter(user=user, content=store_name)
    if len(favorite)==0:
        favorite_value = 'off'
    else:
        favorite_value = 'on'

    comments = []
    for i in range(10):
        comment = {'avatar': '/static/img/333417_1640610154368611.jpg', 'username': 'username', 'comment_id': i, 'comment_content':'asdfadfadfadf'}
        comments.append(comment)
    return render(request, 'detail.html', {'comments': comments, 'store': store})


def join(request):
    return render(request, 'sign-up.html', {})


def login(request):
    return render(request, 'login.html', {})


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


def profile(request):
    return render(request, 'profile.html', {})


def test(request):
    a=request.POST.getlist('food')
    return a
