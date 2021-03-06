import scrapy
import re
from cssselect import GenericTranslator
from scrapy.crawler import CrawlerProcess
from datetime import datetime


class YesSpider(scrapy.Spider):
    name = "yes_spider"

    def make_integer_from_string_except_comma(self, string_data):
        if str(type(string_data)) == "<class 'str'>":
            try:
                return int(re.findall("\d+", string_data.replace(",", ""))[0])
            except:
                return -1
        return -1

    def start_requests(self):
        base_urls = "http://www.yes24.com/24/Category/More/001001003?ElemNo=104&ElemSeq=7&PageNumber="
        for page_idx in range(0, 50):
            yield scrapy.Request(
                url=base_urls + str(page_idx + 1),
                callback=self.parse,
                cb_kwargs=dict(page_idx=page_idx),
            )

    def parse(self, response, page_idx):
        urls = response.css(
            "#category_layout > ul > li > div > div.goods_info > div.goods_name > a:nth-child(2)::attr(href)"
        ).getall()

        for idx in range(0, 20):
            yield scrapy.Request(
                url="http://www.yes24.com/" + urls[idx],
                callback=self.infoParse,
                cb_kwargs=dict(
                    rank=(page_idx * 20 + idx + 1),
                    url="http://www.yes24.com" + urls[idx],
                ),
            )

    def infoParse(self, response, rank, url):
        result = {
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
            + response.css("span.tag > a::text").getall(),
        }

        yield result


if __name__ == "__main__":
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "doit"
                + datetime.today().strftime("%Y_%m%d_%H%M_%S")
                + ".json": {"format": "json"},
            },
            "FEED_EXPORT_ENCODING": "utf-8",
        }
    )
    process.crawl(YesSpider)
    process.start()

    # print(
    #     "??????: ",
    #     response.css(
    #         "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > div > h2::text"
    #     ).get(),
    # )
    # print("??????: ", rank)
    # print(
    #     "?????????: ",
    #     response.css(
    #         "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_pub > a::text"
    #     ).get(),
    # )
    # print(
    #     "??????: ",
    #     response.css(
    #         "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_auth > a::text"
    #     ).getall(),
    # )
    # print(
    #     "?????????: ",
    #     response.css(
    #         "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_date::text"
    #     ).get(),
    # )
    # print(
    #     "????????????: ",
    #     self.make_integer_from_string_except_comma(
    #         response.css(
    #             "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum::text"
    #         ).getall()[1]
    #     ),
    # )
    # print(
    #     "??????: ",
    #     self.make_integer_from_string_except_comma(
    #         response.css(
    #             "#yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div > table > tbody > tr > td > span > em::text"
    #         ).get()
    #     ),
    # )
    # print(
    #     "ISBN: ",
    #     response.css(
    #         " #infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-of-type(3) > td::text"
    #     ).get(),
    # )
    # print(
    #     "??????: ",
    #     self.make_integer_from_string_except_comma(
    #         response.css(
    #             "#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(2) > td::text"
    #         ).get()
    #     ),
    # )
    # print(
    #     "????????????: ",
    #     response.css(
    #         "#infoset_goodsCate > div.infoSetCont_wrap > dl > dd > ul > li > a::text"
    #     ).getall(),
    # )
    # print("??????: ", response.css("span.tag > a::text").getall())
