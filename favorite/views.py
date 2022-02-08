from django.shortcuts import render, HttpResponse
from .models import Favorite
import json
from django.core import serializers
from django.http import JsonResponse
from user.models import UserModel
from storeapp.models import Store
from datetime import datetime


# Create your views here.
def load_favorite(request):
    user = request.user.id
    my_favorite = Favorite.objects.filter(user=user).order_by('date')
    print(my_favorite.user)
    json_favorite = serializers.serialize("json", my_favorite)
    if my_favorite.count() == 0:
        context = {
            'result': 'none'
        }
    else:
        context = {
            'result': json_favorite
        }
    return HttpResponse(json.dumps(context), content_type='application/json')


def add_favorite(request):
    storename = request.POST.get['store_name']
    user_id = request.user.id
    user = UserModel.objects.get(id=user_id)
    store = Store.objects.get(store_name=storename)
    new_favorite = Favorite()
    new_favorite.user = user
    new_favorite.store = store
    new_favorite.date = datetime.now()

    new_favorite.save()
    context = {
        'result': 'DB 추가!',
    }

    return HttpResponse(json.dumps(context), content_type='application/json')


def delete_favorite(request):
    storename = request.POST['store_name']
    user = request.user.id
    store = Store.objects.get(store_name=storename)
    new_favorite = Favorite.objects.get(user=user, store=store)
    new_favorite.delete()
    context = {
        'result': '삭제 완료'
    }
    return HttpResponse(json.dumps(context), content_type='application/json')