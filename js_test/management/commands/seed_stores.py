from random import randint
from faker import Faker
from django.core.management.base import BaseCommand
from django_seed import Seed
from js_test.models import Store

class Command(BaseCommand):
    help = '이 커맨드를 통해 랜덤한 가게 데이터 생성.'

    def add_arguments(self, parser):#어떤 명령어를 통해 더미데이터 생성을 반복할지지
       parser.add_argument(
            "--total",#반복횟수를 int로 한거래...그래서 10번 반복하는거임
            default=10,
            type=int,
            help='몇개의 가게 데이터를 만드냐.',
            )
    def handle(self, *args, **options):
        total = options.get("total")
        seeder = Seed.seeder()

        seeder.add_entity(
                Store,
                total,
                {
                    "store_name" : lambda x: Faker("ko_KR").name()[1:4],
                    "address": lambda x: Faker("ko_KR").street_address(),
                    "phone_num" : lambda x: "070"+str(randint(10000000,99999999)),
                    "last_order" : lambda x: str(randint(0,24))+"시",
                    "web_link" : lambda x: Faker("ko_KR").sentence(),
                    "operating_time" : lambda x: str(randint(0,12))+"시-"+str(randint(12,24))+"시",
                    "break_time" : lambda x: str(randint(0,12))+"시-"+str(randint(12,24))+"시",
                    "holiday" : lambda x: "매월"+ str(randint(1,30)),
                    "pic" : "http://res.heraldm.com/phpwas/restmb_idxmake.php?idx=507&simg=/content/image/2019/09/27/20190927000594_0.jpg",
                    "menu" : lambda x: Faker("ko_KR").sentence(),
                    "kind_of_food" : lambda x: Faker("ko_KR").sentence(),
                    "price_range": lambda x: str(randint(1,8))+"원대",
                    "parking": lambda x: Faker("ko_KR").street_address(),
                },
        )
        seeder.execute()
