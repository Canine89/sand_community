import requests
import pprint
from bs4 import BeautifulSoup
import json
import os
import re
import time
import sys
from datetime import datetime


def make_integer_from_string(string_data):
    if str(type(string_data)) == "<class 'str'>":
        try:
            return int(re.findall("\d+", string_data)[0])
        except:
            return -1
    return -1


class Crawler:
    def crawlData(self, MAX_PAGE=int(sys.argv[1])):
        # 초기화
        END_NUMBER = MAX_PAGE * 20 + 1
        QUERY_SET = {
            "title": "div.goods_info > div.goods_name > a",
        }
        PP = pprint.PrettyPrinter(indent=4, sort_dicts=False)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        result_data = {}
        for info_number in range(1, END_NUMBER):
            bookinfo_key = "bookinfo" + str(info_number)
            result_data[bookinfo_key] = {}

        # 크롤링
        for page in range(1, MAX_PAGE + 1):

            """
            여기 주소만 바꾸면 됩니다
            """
            req = requests.get(
                "http://www.yes24.com/24/Category/More/001001003?ElemNo=104&ElemSeq=7&PageNumber="
                + str(page)
            )
            html = req.text
            soup = BeautifulSoup(html, "lxml")

            suffix_info_number = (page - 1) * 20 + 1
            result = soup.select(QUERY_SET["title"])

            # title, URL
            for item in result:
                if len(item.text) > 0:
                    bookinfo_key = "bookinfo" + str(suffix_info_number)
                    result_data[bookinfo_key]["title"] = item.text
                    result_data[bookinfo_key]["url"] = (
                        "https://www.yes24.com" + item.attrs["href"]
                    )
                    result_data[bookinfo_key]["rank"] = suffix_info_number
                    suffix_info_number = suffix_info_number + 1

            suffix_info_number = (page - 1) * 20 + 1
            # author, publisher, publish_date, right_price, sales_price, isbn, page
            for number in range(suffix_info_number, suffix_info_number + 20):
                bookinfo_key = "bookinfo" + str(number)

                print(result_data[bookinfo_key]["title"] + "을 처리하는 중입니다...")
                req = requests.get(result_data[bookinfo_key]["url"])
                print("성공적으로 요청했음.", req.status_code)

                html = req.text
                soup = BeautifulSoup(html, "lxml")

                result_data[bookinfo_key]["publisher"] = soup.select(
                    "span.gd_pub > a"
                )[0].text
                print("출판사", result_data[bookinfo_key]["publisher"])

                result_data[bookinfo_key]["publish_date"] = soup.select(
                    "span.gd_pubArea > span.gd_date"
                )[0].text
                print("출간일", result_data[bookinfo_key]["publish_date"])

                result_data[bookinfo_key]["right_price"] = make_integer_from_string(
                    soup.select(
                        "#yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div > table > tbody > tr > td > span > em"
                    )[0].text.replace(",", "")
                )

                result_data[bookinfo_key]["sales_price"] = int(
                    result_data[bookinfo_key]["right_price"] * 0.9
                )
                result_data[bookinfo_key]["isbn"] = make_integer_from_string(
                    soup.select(
                        "#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-of-type(3) > td"
                    )[0].text
                    # //*[@id="infoset_specific"]/div[2]/div/table/tbody/tr[3]/td
                    # #infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-of-type(3) > td
                )

                # 쪽수확인중 값 처리를 위해 try...except 문 삽입
                try:
                    result_data[bookinfo_key]["page"] = make_integer_from_string(
                        re.findall(
                            "\d+쪽",
                            soup.select("#infoset_specific > div.infoSetCont_wrap")[
                                0
                            ].text,
                        )[0]
                    )
                except:
                    result_data[bookinfo_key]["page"] = -1

                result_data[bookinfo_key]["sales_point"] = (
                    make_integer_from_string(
                        soup.select("#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum")[
                            0
                        ].text.replace(",", "")
                    )
                    or "none"
                )

                # publisher
                # span으로 처리한 링크 없는 저자 이름을 위해 try...except 문 삽입
                result_data[bookinfo_key]["author"] = []
                try:
                    authors = soup.select(
                        "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_auth > a"
                    )
                    for author in authors:
                        result_data[bookinfo_key]["author"].append(author.text)
                except:
                    authors2 = soup.select(
                        "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_auth > span"
                    )
                    for author in authors2:
                        result_data[bookinfo_key]["author"].append(author.text)

                # tags
                result_data[bookinfo_key]["tags"] = []
                tags = (
                    soup.select(
                        "#infoset_goodsCate > div.infoSetCont_wrap > dl > dd > ul > li > a"
                    )
                    or "none"
                )
                tags2 = soup.select("span.tag > a") or "none"
                for tag in tags:
                    if str(type(tag)) != "<class 'str'>":
                        result_data[bookinfo_key]["tags"].append(tag.text)
                for tag in tags2:
                    if str(type(tag)) != "<class 'str'>":
                        result_data[bookinfo_key]["tags"].append(tag.text)

        with open(
            "yes24_" + datetime.today().strftime("%Y_%m%d_%H%M_%S") + ".json",
            "w",
            encoding="UTF-8",
        ) as outfile:
            json.dump(result_data, outfile, ensure_ascii=False)


if __name__ == "__main__":
    cralwer = Crawler()
    cralwer.crawlData()
