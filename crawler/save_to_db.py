import json
import datetime
from django.utils import timezone
import re
import os
import django
import sys
from django.conf import settings
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from book import models as book_models


def print_data(datas):
    for key, value in datas.items():
        print(key)
        print(value)


def make_integer_from_string(string_data):
    print(string_data)
    if str(type(string_data)) == "<class 'str'>":
        try:
            return int(re.findall("\d+", string_data)[0])
        except:
            return -1
    return -1


def make_datetime_from_string(string_data):
    year = make_integer_from_string(re.findall("\d+년", string_data)[0])
    month = make_integer_from_string(re.findall("\d+월", string_data)[0])

    return datetime.datetime(year=year, month=month, day=1)


def make_right_price(sales_price):
    sales_price = int(sales_price.replace(",", ""))
    return sales_price + sales_price * 0.1


def make_nospace_string(string_data):
    return string_data.replace(" ", "")


def save(datas, fileName):
    for key, value in datas.items():
        title = value["title"]
        try:
            author = value["author"]
        except:
            author = "미정"

        try:
            publisher = value["publisher"]
        except:
            publisher = "미정"

        try:
            publish_date = make_datetime_from_string(value["publish_date"])
        except:
            publish_date = datetime.datetime(year=1999, month=1, day=1)

        try:
            right_price = value["right_price"]
        except:
            right_price = 0

        try:
            sales_price = value["sales_price"]
        except:
            sales_price = 0

        try:
            isbn = value["isbn"]
        except:
            isbn = 0

        url = value["url"]

        try:
            page = value["page"]
        except:
            page = 0

        try:
            tags = value["tags"]
        except:
            tags = ["미정"]

        rank = value["rank"]

        try:
            sales_point = value["sales_point"]
        except:
            sales_point = 0

        # 임시로 yes24로 등록(크롤러 업데이트 후 다음 코드로 변경 예정)
        # market = value["market"]
        market = "yes24"

        try:
            book = book_models.Book.objects.get(isbn=isbn)
            print("이미 등록된 책이므로 DB 등록을 넘어갑니다.")
        except:
            print(
                fileName[6:10],
                fileName[11:13],
                fileName[13:15],
            )
            book = book_models.Book.objects.create(
                title=title,
                author=author,
                publisher=publisher,
                publish_date=publish_date,
                right_price=right_price,
                sales_price=sales_price,
                isbn=isbn,
                url=url,
                page=page,
                crawl_date=datetime.datetime(
                    year=int(fileName[6:10]),
                    month=int(fileName[11:13]),
                    day=int(fileName[13:15]),
                    hour=12,
                ),
            )

            for tag in tags:
                book.tags.add(tag)

            print("새 책의 DB 등록을 마쳤습니다.")

        if book is not None:
            book_models.Metadata.objects.create(
                market=market,
                rank=rank,
                sales_point=sales_point,
                book=book,
                crawl_date=datetime.datetime(
                    year=int(fileName[6:10]),
                    month=int(fileName[11:13]),
                    day=int(fileName[13:15]),
                    hour=12,
                ),
            )
            print(book.title, "의 Metadata 등록을 마쳤습니다.")
        else:
            print("책 정보가 없어 Metadata를 DB에 등록할 수 없습니다.")


if __name__ == "__main__":
    # for _file in os.listdir(folderName):
    #     print(_file)
    #     with open(folderName + _file, encoding="utf-8") as json_file:
    #         json_data = json.load(json_file)
    #         save_data(json_data, _file)

    _file = input()
    with open("datas/yes24_json_dump/" + _file, encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        save(json_data, _file)
