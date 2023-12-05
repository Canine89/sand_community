import json
import datetime
from django.utils import timezone
import re
import os
import django
import sys
from django.conf import settings
from pathlib import Path

folderName = "./yes24/linting_dump_datas/"

sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from book import models as book_models


def make_integer_from_string(string_data):
    if str(type(string_data)) == "<class 'str'>":
        try:
            return int(re.findall("\d+", string_data)[0])
        except:
            return -1
    return -1


def make_datetime_from_string(string_data):
    year = make_integer_from_string(re.findall("\d+년", string_data)[0])
    month = make_integer_from_string(re.findall("\d+월", string_data)[0])

    return timezone.make_aware(datetime.datetime(year=year, month=month, day=1))


def make_right_price(sales_price):
    sales_price = int(sales_price.replace(",", ""))
    return sales_price + sales_price * 0.1


def make_nospace_string(string_data):
    return string_data.replace(" ", "")


def save_data(datas, fileName):
    file_year = int(fileName[6:10])
    file_month = int(fileName[11:13])
    file_day = int(fileName[13:15])

    if (
        book_models.Metadata.objects.filter(
            crawl_date__range=(
                timezone.make_aware(
                    datetime.datetime(
                        year=file_year,
                        month=file_month,
                        day=file_day,
                    )
                ),
                timezone.make_aware(
                    datetime.datetime(
                        year=file_year,
                        month=file_month,
                        day=file_day,
                        hour=23,
                        minute=59,
                        second=59,
                    )
                ),
            ),
        ).count()
        >= 600
    ):
        print(file_year, file_month, file_day, " Metadata already saved.")
        return -1

    for key, value in datas.items():
        title = value["title"]
        print(file_year, file_month, file_day, "의", title, "처리 중...")
        try:
            author = value["author"]
        except:
            author = "저자 없음"

        publisher = value["publisher"]
        publish_date = make_datetime_from_string(value["publish_date"])
        right_price = value["right_price"]
        fake_isbn = value["fake_isbn"]
        url = value["url"]
        rank = value["rank"]
        sales_point = value["sales_point"]

        try:
            book = book_models.Book.objects.get(fake_isbn=fake_isbn)
        except:
            book = book_models.Book.objects.create(
                title=title,
                author=author,
                publisher=publisher,
                publish_date=publish_date,
                right_price=right_price,
                fake_isbn=fake_isbn,
                url=url,
                crawl_date=timezone.make_aware(
                    datetime.datetime(
                        year=file_year,
                        month=file_month,
                        day=file_day,
                        hour=12,
                    )
                ),
            )
            print("새 책의 DB 등록을 마쳤습니다.")

        if book is not None:
            book_models.Metadata.objects.create(
                rank=rank,
                sales_point=sales_point,
                book=book,
                crawl_date=timezone.make_aware(
                    datetime.datetime(
                        year=file_year,
                        month=file_month,
                        day=file_day,
                        hour=12,
                    )
                ),
            )
            print(book.title, "의 Metadata 등록을 마쳤습니다.")
        else:
            print("책 정보가 없어 Metadata를 DB에 등록할 수 없습니다.")


if __name__ == "__main__":
    now_datetime = datetime.datetime.now()
    start_datetime = now_datetime - datetime.timedelta(
        hours=now_datetime.hour,
        minutes=now_datetime.minute,
        seconds=now_datetime.second,
    )

    for _file in os.listdir(folderName):
        if _file == ".DS_Store":
            continue
        with open(folderName + _file, encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            save_data(json_data, _file)
