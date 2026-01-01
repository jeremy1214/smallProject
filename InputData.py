#import necessary modules
import os
import json
from datetime import date

account_list = []
cost_record = []
earn_record = []

json_path = os.path.join(os.path.dirname(__file__), "records.json")

def load_accounts():
    with open("accountList.txt", "r", encoding="utf-8") as f:
        for line in f:
            account_list.append(line.strip())

def load_cost_types():
    with open("costTypeList.txt", "r", encoding="utf-8") as f:
        for line in f:
            cost_record.append(line.strip())

def load_earn_types():
    with open("earnTypeList.txt", "r", encoding="utf-8") as f:
        for line in f:
            earn_record.append(line.strip())

def check_input():
    while True:
        input_type = input("請輸入支出或收入: ")
        if input_type == "exit":
            exit()
        if input_type == "支出" or input_type == "收入":
            return input_type
        else:
            print("不合法的輸入。請輸入 '支出' 或 '收入'。")

def check_account():
    while True:
        account = input("輸入帳戶名稱: ")
        if account == "exit":
            exit()
        if account == "list":
            print("帳戶列表:")
            i = 1
            for record in account_list:
                print(i, record)
                i += 1
            continue
        is_available = False
        for record in account_list:
            if record == account:
                is_available = True
                break
        if not is_available:
            print("帳戶不存在。請檢查帳戶名稱並重試。")
        else:
            break
    return account

def load_records():
    if not os.path.exists(json_path):
        return []
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_records(records):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def add_record(date, input_type, account, amount, category, note=""):
    records = load_records()
    records.append({
        "date": date,
        "type": input_type,
        "account": account,
        "amount": amount,
        "category": category,
        "note": note
    })
    save_records(records)

# Load existing records
load_accounts()
load_cost_types()
load_earn_types()
input_type = check_input()
account = check_account()
type = ""

if input_type == "支出":
    while True:
        print("支出類型: ")
        i = 1
        for record in cost_record:
            print(i, record)
            i += 1
        type_index = input("選擇支出類型的編號: ")
        if type_index == "exit":
            exit()
        if not type_index.isdigit():
            print("不合法的輸入。請輸入數字。")
            continue
        type_index = int(type_index) - 1
        if 0 <= type_index < len(cost_record):
            type = cost_record[type_index]
            break
        else:
            print("選擇無效。請重試。")
elif input_type == "收入":
    while True:
        print("收入類型: ")
        i = 1
        for record in earn_record:
            print(i, record)
            i += 1
        type_index = input("選擇收入類型的編號: ")
        if type_index == "exit":
            exit()
        if not type_index.isdigit():
            print("不合法的輸入。請輸入數字。")
            continue
        type_index = int(type_index) - 1
        if 0 <= type_index < len(earn_record):
            type = earn_record[type_index]
            break
        else:
            print("選擇無效。請重試。")

amount = input("輸入金額: ")
if amount == "exit":
    exit()
note = input("輸入備註: ")
if note == "exit":
    exit()
add_record(date.today().isoformat(), input_type, account, amount, type, note)

print("記錄已新增。")