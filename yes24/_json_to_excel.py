import json
import pandas as pd

# JSON 파일 이름
json_file = input()

# JSON 파일 읽기
with open("./" + json_file, encoding="utf-8") as f:
    data = json.load(f)

# DataFrame 생성
df = pd.DataFrame(data)

# 엑셀로 저장
excel_file = json_file + "_data.xlsx"
df.to_excel(excel_file, index=False)
