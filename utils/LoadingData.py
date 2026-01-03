import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
if not DATA_DIR.exists():
    DATA_DIR.mkdir(parents=True)
JSON_PATH = DATA_DIR / "records.json"
ACCOUNT_LIST_PATH = DATA_DIR / "accountList.txt"
COST_RECORD_PATH = DATA_DIR / "costTypeList.txt"
EARN_RECORD_PATH = DATA_DIR / "earnTypeList.txt"

account_list = []
cost_record = []
earn_record = []

def load_accounts():
    if not os.path.exists(ACCOUNT_LIST_PATH):
        print("帳戶列表檔案不存在，返回error。")
        exit()
    with open(ACCOUNT_LIST_PATH, "r", encoding="utf-8") as f:
        for line in f:
            account_list.append(line.strip())
    return account_list

def load_cost_types():
    if not os.path.exists(COST_RECORD_PATH):
        print("支出類型列表檔案不存在，返回error。")
        exit()
    with open(COST_RECORD_PATH, "r", encoding="utf-8") as f:
        for line in f:
            cost_record.append(line.strip())
    return cost_record

def load_earn_types():
    if not os.path.exists(EARN_RECORD_PATH):
        print("收入類型列表檔案不存在，返回error。")
        exit()
    with open(EARN_RECORD_PATH, "r", encoding="utf-8") as f:
        for line in f:
            earn_record.append(line.strip())
    return earn_record

def load_records():
    if not os.path.exists(JSON_PATH):
        return []
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_records(records):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
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