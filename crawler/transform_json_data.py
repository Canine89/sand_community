import json
from datetime import datetime

_file = input()
results = {}
with open("yes_crawler/" + _file, encoding="utf-8") as json_file:
    json_data = json.load(json_file)
    for data in json_data:
        results["bookinfo" + str(data["rank"])] = data

with open(
    "yes24_" + datetime.today().strftime("%Y_%m%d_%H%M_%S") + ".json",
    "w",
    encoding="UTF-8",
) as outfile:
    json.dump(results, outfile, ensure_ascii=False)
