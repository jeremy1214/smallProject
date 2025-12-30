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

show_type = input("請選擇要顯示的紀錄類型(總計或平均): ")
if show_type == "總計":
    records = load_records()
    total_expense = 0
    total_income = 0
    for record in records:
        if record["type"] == "支出":
            total_expense += record["amount"]
        elif record["type"] == "收入":
            total_income += record["amount"]
    print(f"總支出: {total_expense}")
    print(f"總收入: {total_income}")