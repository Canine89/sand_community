import scrapy
import re
from cssselect import GenericTranslator


class YesSpider(scrapy.Spider):
    name = "edus_yes_spider"

    def make_integer_from_string_except_comma(self, string_data):
        if str(type(string_data)) == "<class 'str'>":
            try:
                return int(re.findall("\d+", string_data.replace(",", ""))[0])
            except:
                return -1
        return -1

    def start_requests(self):
        base_urls = {
            "초등참고서": "http://www.yes24.com/24/Category/More/001001044?ElemNo=104&ElemSeq=1",
            # "미취학아동/국어/한글": "http://www.yes24.com/24/Category/More/001001044007008?ElemNo=104&ElemSeq=1",
            # "미취학아동/수학": "http://www.yes24.com/24/Category/More/001001044007009?ElemNo=104&ElemSeq=1",
            # "미취학아동/영어": "http://www.yes24.com/24/Category/More/001001044007010?ElemNo=104&ElemSeq=1",
            # "미취학아동/기타": "http://www.yes24.com/24/Category/More/001001044007011?ElemNo=104&ElemSeq=1",
            # "미취학아동/기탄 시리즈": "http://www.yes24.com/24/Category/More/001001044007005?ElemNo=104&ElemSeq=1",
            # "미취학아동/7세 초능력 시리즈": "http://www.yes24.com/24/Category/Display/001001044007006",
            "1학년/국어(초등1)": "http://www.yes24.com/24/Category/More/001001044001001?ElemNo=104&ElemSeq=1",
            # "1학년/수학(초등1)": "http://www.yes24.com/24/Category/More/001001044001002?ElemNo=104&ElemSeq=1",
            # "1학년/기타(초등1)": "http://www.yes24.com/24/Category/More/001001044001003?ElemNo=104&ElemSeq=1",
            # "2학년/국어(초등2)": "http://www.yes24.com/24/Category/More/001001044002001?ElemNo=104&ElemSeq=1",
            # "2학년/수학(초등2)": "http://www.yes24.com/24/Category/More/001001044002002?ElemNo=104&ElemSeq=1",
            # "2학년/기타(초등2)": "http://www.yes24.com/24/Category/More/001001044002003?ElemNo=104&ElemSeq=1",
            # "3학년/국어(초등3)": "http://www.yes24.com/24/Category/More/001001044003001?ElemNo=104&ElemSeq=1",
            # "3학년/수학(초등3)": "http://www.yes24.com/24/Category/More/001001044003002?ElemNo=104&ElemSeq=1",
            # "3학년/과학(초등3)": "http://www.yes24.com/24/Category/More/001001044003003?ElemNo=104&ElemSeq=1",
            # "3학년/사회(초등3)": "http://www.yes24.com/24/Category/More/001001044003004?ElemNo=104&ElemSeq=1",
            # "3학년/영어(초등3)": "http://www.yes24.com/24/Category/More/001001044003006?ElemNo=104&ElemSeq=1",
            # "3학년/기타(초등3)": "http://www.yes24.com/24/Category/More/001001044003005?ElemNo=104&ElemSeq=1",
            # "4학년/국어(초등4)": "http://www.yes24.com/24/Category/More/001001044004001?ElemNo=104&ElemSeq=1",
            # "4학년/수학(초등4)": "http://www.yes24.com/24/Category/More/001001044004002?ElemNo=104&ElemSeq=1",
            # "4학년/과학(초등4)": "http://www.yes24.com/24/Category/More/001001044004003?ElemNo=104&ElemSeq=1",
            # "4학년/사회(초등4)": "http://www.yes24.com/24/Category/More/001001044004004?ElemNo=104&ElemSeq=1",
            # "4학년/영어(초등4)": "http://www.yes24.com/24/Category/More/001001044004006?ElemNo=104&ElemSeq=1",
            # "4학년/기타(초등4)": "http://www.yes24.com/24/Category/More/001001044004005?ElemNo=104&ElemSeq=1",
            # "5학년/국어(초등5)": "http://www.yes24.com/24/Category/More/001001044005001?ElemNo=104&ElemSeq=1",
            # "5학년/수학(초등5)": "http://www.yes24.com/24/Category/More/001001044005002?ElemNo=104&ElemSeq=1",
            # "5학년/과학(초등5)": "http://www.yes24.com/24/Category/More/001001044005003?ElemNo=104&ElemSeq=1",
            # "5학년/사회(초등5)": "http://www.yes24.com/24/Category/More/001001044005004?ElemNo=104&ElemSeq=1",
            # "5학년/영어(초등5)": "http://www.yes24.com/24/Category/More/001001044005006?ElemNo=104&ElemSeq=1",
            # "5학년/기타(초등5)": "http://www.yes24.com/24/Category/More/001001044005005?ElemNo=104&ElemSeq=1",
            # "6학년/국어(초등6)": "http://www.yes24.com/24/Category/More/001001044006001?ElemNo=104&ElemSeq=1",
            # "6학년/수학(초등6)": "http://www.yes24.com/24/Category/More/001001044006002?ElemNo=104&ElemSeq=1",
            # "6학년/과학(초등6)": "http://www.yes24.com/24/Category/More/001001044006003?ElemNo=104&ElemSeq=1",
            # "6학년/사회(초등6)": "http://www.yes24.com/24/Category/More/001001044006004?ElemNo=104&ElemSeq=1",
            # "6학년/영어(초등6)": "http://www.yes24.com/24/Category/More/001001044006006?ElemNo=104&ElemSeq=1",
            # "6학년/기타(초등6)": "http://www.yes24.com/24/Category/More/001001044006005?ElemNo=104&ElemSeq=1",
            # "예비중": "http://www.yes24.com/24/Category/More/001001044011?ElemNo=104&ElemSeq=1",
            # "수학전문교재/단계별 계산력/연산력 교재": "http://www.yes24.com/24/Category/More/001001044009001?ElemNo=104&ElemSeq=1",
            # "수학전문교재/초등 경시/올림피아드": "http://www.yes24.com/24/Category/More/001001044009002?ElemNo=104&ElemSeq=1",
            # "수학전문교재/기타": "http://www.yes24.com/24/Category/More/001001044009003?ElemNo=104&ElemSeq=1",
            # "국어전문교재/단계별 독해력/어휘력": "http://www.yes24.com/24/Category/More/001001044010001?ElemNo=104&ElemSeq=1",
            # "국어전문교재/독서/논술": "http://www.yes24.com/24/Category/More/001001044010002?ElemNo=104&ElemSeq=1",
            # "국어전문교재/받아쓰기/맞춤법": "http://www.yes24.com/24/Category/More/001001044010003?ElemNo=104&ElemSeq=1",
            # "한자": "http://www.yes24.com/24/Category/More/001001044014?ElemNo=104&ElemSeq=1",
            # "한국사": "http://www.yes24.com/24/Category/More/001001044018?ElemNo=104&ElemSeq=1",
            # "영재교육원대비": "http://www.yes24.com/24/Category/More/001001044015?ElemNo=104&ElemSeq=1",
        }
        page_number_str = "&PageNumber="

        for category in base_urls:
            for page_idx in range(0, 50):
                try:
                    yield scrapy.Request(
                        url=base_urls[category] + page_number_str + str(page_idx + 1),
                        callback=self.parse,
                        cb_kwargs=dict(page_idx=page_idx, category=category),
                    )
                except:
                    print("there is no pages...")

    def parse(self, response, page_idx, category):
        urls = response.css(
            "#category_layout > ul > li > div > div.goods_info > div.goods_name > a:nth-child(2)::attr(href)"
        ).getall()

        if len(urls) <= 0:
            print("there is no urls")
            return

        for idx in range(0, 20):
            try:
                yield scrapy.Request(
                    url="http://www.yes24.com/" + urls[idx],
                    callback=self.infoParse,
                    cb_kwargs=dict(
                        rank=(page_idx * 20 + idx + 1),
                        url="http://www.yes24.com" + urls[idx],
                        category=category,
                    ),
                )
            except:
                print("there is no datas...")

    def infoParse(self, response, rank, url, category):
        result = {
            "category": category,
            "title": response.css(
                "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > div > h2::text"
            ).get(),
            "url": url,
            "rank": rank,
            "publisher": response.css(
                "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_pub > a::text"
            ).get(),
            "publish_date": response.css(
                "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_date::text"
            ).get(),
            "right_price": self.make_integer_from_string_except_comma(
                response.css(
                    "#yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div > table > tbody > tr > td > span > em::text"
                ).get()
            ),
            "sales_price": int(
                self.make_integer_from_string_except_comma(
                    response.css(
                        "#yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div > table > tbody > tr > td > span > em::text"
                    ).get()
                )
                * 0.9
            ),
            "isbn": response.css(
                " #infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-of-type(3) > td::text"
            ).get(),
            "page": self.make_integer_from_string_except_comma(
                response.css(
                    "#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(2) > td::text"
                ).get()
            ),
            "sales_point": self.make_integer_from_string_except_comma(
                response.css(
                    "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum::text"
                ).getall()[1]
            ),
            "author": response.css(
                "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_auth > a::text"
            ).getall()
            + response.css(
                "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_auth > span::text"
            ).getall(),
            "tags": response.css(
                "#infoset_goodsCate > div.infoSetCont_wrap > dl > dd > ul > li > a::text"
            ).getall()
            + response.css("#tagArea > span > a::text").getall(),
        }

        yield result
