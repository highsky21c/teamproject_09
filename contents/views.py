# contents/views.py
from django.shortcuts import render, redirect
from .models import ContentsModel, ContentsComment # 글쓰기 모델
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from storeapp.models import Store


# Create your views here.
def home(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    #print("user:",user) True 라고 나옴
    if user:
        return redirect('/contents/')
    else:
        return redirect('/sign-in/')


def contents(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면

            return render(request, 'home.html', {})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in/')
    elif request.method == 'POST':  # 요청 방식이 POST 일때
        search_words = request.POST.get['search_words']

        all_stores = Store().objects.filter(kind_of_food=search_words)

        return HttpResponse(json.dumps(all_stores), content_type="application/json")


@login_required
def delete_contents(request, id):
    my_contents = ContentsModel.objects.get(id=id)
    my_contents.delete()
    return redirect('/contents/')

@login_required
def detail_contents(request, id):
    my_contents = ContentsModel.objects.get(id=id)
    contents_comment = ContentsComment.objects.filter(contents_id=id).order_by('-created_at')
    return render(request, 'contents/contents_detail1.html', {'contents':my_contents, 'comment':contents_comment})


@login_required
def write_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment","")
        current_contents = ContentsModel.objects.get(id=id)

        TC = ContentsComment()
        TC.comment = comment
        TC.author = request.user
        TC.contents = current_contents
        TC.save()

        return redirect('/contents/'+str(id))


@login_required
def delete_comment(request, id):
    comment = ContentsComment.objects.get(id=id)
    current_contents = comment.contents.id
    comment.delete()
    return redirect('/contents/'+str(current_contents))

@login_required
@require_POST
def like(request):
    pk = request.POST.get('pk', None)
    contents = ContentsModel.objects.get(pk=pk)
    user = request.user
    print("pk:",pk)
    print("tw:",contents)
    print("user:",user)

    if contents.likes_user.filter(id=user.id).exists():
        contents.likes_user.remove(user)
        message = '좋아요 취소'
    else:
        contents.likes_user.add(user)
        message = '좋아요'

    context = {'likes_count':contents.count_likes_user(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required
@require_POST
def hate(request):
    pk = request.POST.get('pk', None)
    contents = ContentsModel.objects.get(pk=pk)
    user = request.user
    print("pk:",pk)
    print("tw:",contents)
    print("user:",user)

    if contents.hates_user.filter(id=user.id).exists():
        contents.hates_user.remove(user)
        message = '싫어요 취소'
    else:
        contents.hates_user.add(user)
        message = '싫어요'

    context = {'hates_count':contents.count_hates_user(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required
@require_POST
def cmt_like(request):
    pk = request.POST.get('pk', None)
    contents_cmt = ContentsComment.objects.get(pk=pk)
    user = request.user
    print("pk:",pk)
    print("tw:",contents_cmt)
    print("user:",user)

    if contents_cmt.cmt_likes_user.filter(id=user.id).exists():
        contents_cmt.cmt_likes_user.remove(user)
        message = '좋아요 취소'
    else:
        contents_cmt.cmt_likes_user.add(user)
        message = '좋아요'

    context = {'cmt_likes_count':contents_cmt.cmt_count_likes_user(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

@login_required
@require_POST
def cmt_hate(request):
    pk = request.POST.get('pk', None)
    contents_cmt = ContentsComment.objects.get(pk=pk)
    user = request.user
    print("pk:",pk)
    print("tw:",contents_cmt)
    print("user:",user)

    if contents_cmt.cmt_hates_user.filter(id=user.id).exists():
        contents_cmt.cmt_hates_user.remove(user)
        message = '싫어요 취소'
    else:
        contents_cmt.cmt_hates_user.add(user)
        message = '싫어'

    context = {'cmt_hates_count':contents_cmt.cmt_count_hates_user(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")