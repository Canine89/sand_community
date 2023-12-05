import json, os
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


for filename in os.listdir("./json_dump_datas"):
    _filename = filename
    if _filename == ".DS_Store":
        continue
    print(filename, " 처리 중...")
    results = {}
    with open("./json_dump_datas/" + _filename, encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        for key in json_data.keys():
            # print(json_data[key]["title"], " 처리 중...")
            results[key] = {
                "title": json_data[key]["title"],
                "author": json_data[key]["author"],
                "publisher": json_data[key]["publisher"],
                "publish_date": json_data[key]["publish_date"],
                "right_price": json_data[key]["right_price"],
                "fake_isbn": get_hash_value(json_data[key]["title"], 5, "number"),
                "url": json_data[key]["url"],
                "rank": json_data[key]["rank"],
                "sales_point": json_data[key]["sales_point"],
            }

    with open(
        "./linting_dump_datas/yes24_" + _filename[6:15] + ".json",
        "w",
        encoding="UTF-8",
    ) as outfile:
        json.dump(results, outfile, ensure_ascii=False)
