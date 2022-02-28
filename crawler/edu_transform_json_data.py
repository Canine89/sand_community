import json
from datetime import datetime
from unicodedata import category

_file = input()
results = {}
with open("yes_crawler/" + _file, encoding="utf-8") as json_file:
    json_data = json.load(json_file)
    for data in json_data:
        # print(data)
        if data["isbn"] == " ":
            data["isbn"] = -1

        results[data["category"] + "_bookinfo" + str(data["rank"])] = data


with open(
    "edu_yes24_" + datetime.today().strftime("%Y_%m%d_%H") + ".json",
    "w",
    encoding="UTF-8",
) as outfile:
    json.dump(results, outfile, ensure_ascii=False)
