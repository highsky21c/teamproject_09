from django.shortcuts import render, HttpResponse
from .models import Favorite
import json
from django.core import serializers
from django.http import JsonResponse
from user.models import UserModel


# Create your views here.
def load_favorite(request):
    # user = request.user.is_authenticated
    user = 'js'
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
    storename = request.POST['store_name']
    user = request.user.is_authenticated
    new_favorite = Favorite.objects.create(user=user, content=storename)
    new_favorite.save()
    context = {
        'result': 'DB 추가!'
    }
    return HttpResponse(json.dumps(context), content_type='application/json')


def delete_favorite(request):
    storename = request.POST['store_name']
    user = request.user.is_authenticated
    new_favorite = Favorite.objects.filter(user=user, content=storename)
    new_favorite.delete()
    context = {
        'result': '삭제 완료'
    }
    return HttpResponse(json.dumps(context), content_type='application/json')