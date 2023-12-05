import scrapy
from scrapy.crawler import CrawlerProcess
import re

from datetime import datetime
import hashlib


def get_hash_value(in_str, in_digest_bytes_size=64, in_return_type="digest"):
    """
    해시값을 구한다
    참고: https://m.blog.naver.com/wideeyed/221472745532
        Parameter: in_str: 해싱할 문자열
        in_digest_bytes_size: 다이제스트 바이트 크기
        n_return_type: 반환 형태(digest/hexdigest/number)
    """
    assert 1 <= in_digest_bytes_size and in_digest_bytes_size <= 64
    blake = hashlib.blake2b(in_str.encode("utf-8"), digest_size=in_digest_bytes_size)
    if in_return_type == "hexdigest":
        return blake.hexdigest()
    elif in_return_type == "number":
        return int(blake.hexdigest(), base=16)

    return blake.digest()


class YesSpider(scrapy.Spider):
    name = "bookinfos"

    def make_integer_from_string_except_comma(self, string_data):
        if str(type(string_data)) == "<class 'str'>":
            print(string_data)
            try:
                return int(re.findall("\d+", string_data.replace(",", ""))[0])
            except:
                return -1
        return -1

    def start_requests(self):
        base_urls = "http://www.yes24.com/Product/Category/BestSeller?categoryNumber=001001003&pageNumber="
        for page_idx in range(0, 40):
            yield scrapy.Request(
                url=base_urls + str(page_idx + 1) + "&pageSize=24",
                callback=self.parse,
                cb_kwargs=dict(page_idx=page_idx),
            )

    # yesBestList > li:nth-child(23) > div > div.item_info > div.info_row.info_name > a.gd_name
    def parse(self, response, page_idx):
        urls = response.css(
            "#yesBestList > li > div > div.item_info > div.info_row.info_name > a.gd_name::attr(href)"
        ).getall()

        print(urls)

        for idx in range(0, 24):
            try:
                yield scrapy.Request(
                    url="http://www.yes24.com/" + urls[idx],
                    callback=self.infoParse,
                    cb_kwargs=dict(
                        rank=(page_idx * 24 + idx + 1),
                        url="http://www.yes24.com" + urls[idx],
                    ),
                )
            except:
                pass

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
                    "#yDetailTopWrap > div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div > table > tbody > tr:nth-child(1) > td > span > em::text"
                ).get()
            ),
            "fake_isbn": get_hash_value(
                response.css(
                    "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > div > h2::text"
                ).get(),
                5,
                "number",
            ),
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
                + datetime.today().strftime("%Y%m%d_%H%M_%S")
                + ".json": {"format": "json"},
            },
            "FEED_EXPORT_ENCODING": "utf-8",
        }
    )
    process.crawl(YesSpider)
    process.start()
