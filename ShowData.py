import json
import os

json_path = os.path.join(os.path.dirname(__file__), "records.json")
cost_record = ["吃飯", "交通", "娛樂", "購物", "其他"]
earn_record = ["薪水", "獎金", "投資", "其他"]

def load_records():
    if not os.path.exists(json_path):
        return []
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
show_type = ""
records = load_records()
while True:
    show_type = input("請選擇要顯示的紀錄類型(總計或平均): ")
    if show_type not in ["總計", "平均"]:
        print("不合法的類型。請輸入 '總計' 或 '平均'。")
        continue
    break

total_month = [[0]*12]*2
total_year = 0
count_month = 0
count_year = 0
avg_cost = 0
avg_earn = 0

month = 0
current_year = 0

for record in records:
    print(record["type"])
    if current_year == 0:
        current_year = int(record["date"].split("-")[0])
    if current_year != int(record["date"].split("-")[0]) or record == records[-1]:
        count_year += 1
        print(f"{current_year} 年統計累計:", total_year, "元")
        for i in range(12):
            if show_type == "總計":
                print(f"{i+1} 月: 支出 {total_month[0][i]} 元, 收入 {total_month[1][i]} 元")
            elif show_type == "平均":
                if count_year == 0:
                    avg_cost = total_month[0][i]
                    avg_earn = total_month[1][i]
                else:
                    avg_cost = total_month[0][i] // count_year
                    avg_earn = total_month[1][i] // count_year
                print(f"{i+1} 月平均: 支出 {avg_cost} 元, 收入 {avg_earn} 元")
        current_year = int(record["date"].split("-")[0])
    if record["type"] == "支出":
        month = int(record["date"].split("-")[1]) - 1
        total_month[0][month] += int(record["amount"])
        total_year -= int(record["amount"])
    elif record["type"] == "收入":
        month = int(record["date"].split("-")[1]) - 1
        total_month[1][month] += int(record["amount"])
        total_year += int(record["amount"])