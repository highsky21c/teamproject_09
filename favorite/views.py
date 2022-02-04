from django.shortcuts import render, HttpResponse
from .models import Favorite
import json
from django.core import serializers
from django.http import JsonResponse


# Create your views here.
def load_favorite(request):
    # user = request.user.is_authenticated
    user = 'js'
    my_favorite = Favorite.objects.filter(user=user).order_by('date')
    print(my_favorite)
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
    # return JsonResponse(context)


def add_favorite(request):
    user = 'js'
    new_favorite = Favorite.objects.create(user=user, content='Ramen')
    new_favorite.save()
    return HttpResponse('db저장!')

