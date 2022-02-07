
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FindIdForm #실제로는 user앱에서 이렇게 작성할것
from django.views.generic import View
from django.utils.decorators import method_decorator
from .decorators import login_message_required, admin_required, logout_message_required
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Store

def main(request):  # 메인 화면
    storebox = []
    for i in range(10):
        store = {'photo': '/static/img/333417_1640610154368611.jpg', 'store':i}
        storebox.append(store)

    return render(request, 'home.html', {'container' : storebox})


def detail(request):
    return render(request, 'detail.html', {})

def join(request):
    return render(request, 'sign-up.html',{})

def login(request):
    return render(request, 'login.html', {})

def findid(request):
    return render(request, 'find-id.html', {})


#접속중인 사용자의 접근을 방지하기 위해 decorator를 추가하고,
#GET으로 방금 생성한 form을 뿌려주는 RecoveryIdView 클래스를 views.py에 아래와 같이 추가합니다
@method_decorator(logout_message_required, name='dispatch')
class FindIdView(View):
    template_name = 'find-id.html'
    find_id = FindIdForm

    def get(self, request):
        if request.method=='GET':
            form = self.find_id(None)
        return render(request, self.template_name, { 'form':form, })


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
