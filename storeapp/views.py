import random

import requests
from bs4 import BeautifulSoup
import simplejson as json
from django.http import HttpResponse
from django.shortcuts import render
from .models import SaveStore
# Create your views here.

from gensim.models.doc2vec import Doc2Vec, TaggedDocument

main_sub_category = {
    '0': ['오리요리', '퓨전 한식', '기타 한식', '백반', '찌개', '철판 요리', '해산물요리', '탕', '전골', '국수', '전통한식', '뷔페'],
    '1': ['정통일식', '면요리', '스시', '라멘', '일반 일식', '기타 일식', '까스요리', '회', '오뎅', '일본카레', '소바', '벤토', '돈부리', ' 꼬치', '우동',
          '이자카야'],
    '2': ['퓨전양식', '기타양식', '스테이크', '바베큐', '버거'],
    '3': ['기타 중식', '딤섬', '정통 중식', '만두', '일반 중식'],
    '4': ['다국적 퓨전', '와인', '세계음식 기타', '이탈리안', '고기', '프랑스 음식', '닭', '다국적아시아음식', '태국 음식', '베트남음식', '인도 음식'],
    '5': ['와인', '전통주점', '칵테일', '포차'],
    '6': ['브런치', '디저트', '베이커리', '샌드위치', '카페']
}


# 메인페이지
def Show_Store(request):
    if request.POST:
        input_food = request.POST.get('input_food', '')

        # 대분류로 데이터를 추론
        main_category_model = Doc2Vec.load('static/model/main_category_model')
        main_infer_data = main_category_model.infer_vector(input_food)
        most_similar_docs = main_category_model.docvecs.most_similar([main_infer_data], topn=1)

        # 대분류에서 소분류로 분류
        sec_documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(main_sub_category[most_similar_docs[0[0]]])]
        sub_category_model = Doc2Vec(sec_documents, vector_size=100, window=3, epochs=10, min_count=0, workers=4)
        sec_inferred_doc_vec = sub_category_model.infer_vector(input_food)
        sub_most_similar_docs = sub_category_model.docvecs.most_similar([sec_inferred_doc_vec], topn=3)

        recommand_stores = []
        for sec_index, sec_similarity in sub_most_similar_docs:
            print('subcategory :', main_sub_category[most_similar_docs[0][0]][sec_index], '//', 'similarity:',
                  sec_similarity)

            # "main_sub_category[most_similar_docs[0][0]][sec_index]" 는 main_sub_category의 @번째(0~6)에 해당하는 리스트 들 중
            # sec_index번째의 요소임

            # key값을 디코딩하여, db에서 해당하는 데이터를 가져옴
            key = json.dumps(most_similar_docs[0][0][sec_index])
            store = SaveStore.objects.filter(kind_of_food=main_sub_category[key])

            decode_store = json.decoder.JSONDecoder()
            decoded_store = decode_store.decode(store)

            recommand_stores.append(decoded_store)

        return render(request, '../storeapp/temp_home.html', stores_POST=recommand_stores)

    else:
        # GET일 경우, 랜덤으로 10개 뽑아 보여줌.
        ran_stores = []
        for _ in range(11):
            idx = random.randrange(0, 201)
            random_store = SaveStore.objects.get(id=idx)

        return render(request, '../storeapp/temp_home.html', store_GET=ran_stores)


def Save_Store_Data(request):
    if SaveStore.objects.all() is not None:
        return HttpResponse('이미처리되었습니다.')  # 나중에 render로 바로 홈으로

    else:
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
                temp_object.store = json.dumps(store_detail)
                temp_object.save()
                # print(page_detail)
        return HttpResponse('성공')  # 나중에 rneder()로 메인페이지로 연결
