from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FindIdForm  # 실제로는 user앱에서 이렇게 작성할것
from django.views.generic import View
from django.utils.decorators import method_decorator
from .decorators import login_message_required, admin_required, logout_message_required
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Store
from favorite.models import Favorite
from bs4 import BeautifulSoup
import requests
from storeapp.models import SaveStore


def main(request):  # 메인 화면
    storebox = []
    for i in range(10):
        store = {'photo': '/static/img/333417_1640610154368611.jpg', 'store': i}
        storebox.append(store)

    return render(request, 'home.html', {'container': storebox})


def detail(request, store_name):
    # user = request.user
    user = 'js'
    store = Store.objects.filter(store_name=store_name)
    # favorite = Favorite.objects.filter(user=user, content=store_name)
    # if len(favorite) == 0:
    #     favorite_value = 'off'
    # else:
    #     favorite_value = 'on'

    comments = []
    for i in range(10):
        comment = {'avatar': '/static/img/333417_1640610154368611.jpg', 'username': 'username', 'comment_id': i,
                   'comment_content': 'asdfadfadfadf'}
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
    all_Store = Store.objects.all()
    return render(request, 'profile.html', {'stores': all_Store})


def test(request):
    a = request.POST.getlist('food')
    return a


def test_Store_data(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    for i in range(1, 11):

        data_seoul = requests.get(
            f'https://www.mangoplate.com/search/%EC%84%9C%EC%9A%B8?keyword=%EC%84%9C%EC%9A%B8&page={i}',
            headers=headers)
        soup_seoul = BeautifulSoup(data_seoul.text, 'html.parser')

        # 공통부분
        full_seoul_items = soup_seoul.select(
            'article.contents > div.column-wrapper > div.column-contents > div.inner > section.module > div.search-list-restaurants-inner-wrap > .list-restaurants > .list-restaurant > .list-restaurant-item > .restaurant-item')

        seoul_href_list = []  # 대표 사진
        seoul_href_pic = []  # 해당 링크
        for detail in full_seoul_items:
            temp_href = 'https://www.mangoplate.com'

            seoul_item_href = detail.select_one('a')['href']
            temp_href += seoul_item_href
            seoul_href_list.append(temp_href)

            seoul_item_pic = detail.select_one('a > div.thumb > img.center-croping')['data-original']
            seoul_href_pic.append(seoul_item_pic)

        print(f"현재 {i}번째 페이지의 음식점을 크롤링합니다.")
        print()

        # 크롤링을 통해 저장할 정보
        for page in seoul_href_list:
            # print(page)

            page_detail = {
                'store_name': '',
                'address': '',
                'phone_num': '',
                'menu': '',
                'kind_of_food': '',
                'price_range': '',
                'operating_time': '',
                'break_time': '',
                'pic': '',
                'holiday': '',
                'parking': '',
                'last_order': '',
                'web_link': '',
            }

            # 음식점 상세페이지
            data_page = requests.get(page, headers=headers)
            soup_page = BeautifulSoup(data_page.text, 'html.parser')

            temp_object = SaveStore()

            # 이미지 부분
            image_detail = soup_page.select(
                'main.pg-restaurant > .contents > .restaurant-photos > .list-photo_wrap > .list-photo')
            detail_imgs = []
            for detail in image_detail:
                img_list = detail.select_one('meta')['content']
                detail_imgs.append(img_list)
            page_detail['pic'] = detail_imgs

            # 텍스트부분
            common_page = soup_page.select(
                'article.contents > div.column-wrapper > div.column-contents > div.inner > .restaurant-detail')
            for detail in common_page:
                store_name = detail.select_one('header > .restaurant_title_wrap > .title > .restaurant_name').text
                page_detail['store_name'] = store_name

                infos = detail.select('.info > tbody > tr')
                for info in infos:

                    info_title = info.select_one('th').text.replace('\n', '')
                    if info_title == '':
                        break
                    # print('현재정보: ', info_title)

                    # 항목 별, 나누기(항목 : 주소, 전화번호, 음식 종류, 가격대, 주차, 영업시간, 쉬는시간, 마지막주문, 휴일, 메뉴, 웹사이트)

                    if info_title == '주소':
                        use_info = info.select_one("td").text.replace('\n', '')
                        if use_info == '':
                            continue
                        else:
                            if "지번" in use_info:
                                use_info = use_info.replace('지번', ',지번 : ').split(',')
                                page_detail['address'] = use_info

                    elif info_title == '전화번호':
                        use_info = info.select_one("td").text.replace('\n', '')
                        if use_info == '':
                            continue
                        else:
                            page_detail['phone_num'] = use_info

                    elif info_title == '음식 종류':
                        use_info = info.select_one("td").text.replace('\n', '')
                        page_detail['kind_of_food'] = use_info


                    elif info_title == '가격대':
                        use_info = info.select_one("td").text.replace('\n', '')
                        if use_info == '':
                            continue
                        else:
                            page_detail['price_range'] = use_info

                    elif info_title == '주차':
                        use_info = info.select_one("td").text.replace('\n', '')
                        if use_info == '':
                            continue
                        else:
                            page_detail['parking'] = use_info

                    elif info_title == '영업시간':
                        use_info = info.select_one("td").text.replace('\n', '')
                        if use_info == '':
                            continue
                        else:
                            page_detail['operating_time'] = use_info

                    elif info_title == '쉬는시간':
                        use_info = info.select_one("td").text.replace('\n', '')
                        if use_info == '':
                            continue
                        else:
                            page_detail['break_time'] = use_info

                    elif info_title == '마지막주문':
                        use_info = info.select_one("td").text.replace('\n', '')
                        if use_info == '':
                            continue
                        else:
                            page_detail['last_order'] = use_info

                    elif info_title == '휴일':
                        use_info = info.select_one("td").text.replace('\n', '')
                        if use_info == '':
                            continue
                        else:
                            page_detail['holiday'] = use_info

                    elif info_title == '메뉴':
                        food_info = info.select("td > .Restaurant_MenuList > li")
                        menu = {}
                        for idx, detail_food in enumerate(food_info):
                            food_name = detail_food.select_one('.Restaurant_Menu').text
                            food_price = detail_food.select_one('.Restaurant_MenuPrice').text
                            menu[idx] = [food_name, food_price]
                        page_detail['menu'] = menu

                    elif info_title == '웹 사이트':
                        use_info = info.select_one("td > a")['href']
                        if use_info == '':
                            continue
                        else:
                            page_detail['web_link'] = use_info

                    else:
                        use_info = ''
                        info_title = ''

                        # print(info_title, use_info)
            store_detail = page_detail

            print(store_detail)
            # temp_object.store = json.dumps(store_detail)
            # temp_object.save()
            # print(page_detail)
    return HttpResponse('성공')  # 나중에 render()로 메인페이지로 연결
