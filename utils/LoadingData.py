import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
if not DATA_DIR.exists():
    DATA_DIR.mkdir(parents=True)
JSON_PATH = DATA_DIR / "records.json"
# ACCOUNT_LIST_PATH = DATA_DIR / "accountList.txt"
ACCOUNT_LIST_PATH = DATA_DIR / "accountList.json"
COST_RECORD_PATH = DATA_DIR / "costTypeList.txt"
EARN_RECORD_PATH = DATA_DIR / "earnTypeList.txt"

def load_accounts():
    account_list = []
    with open(ACCOUNT_LIST_PATH, "r", encoding="utf-8") as f:
        for line in f:
            account_list.append(line.strip())
    return account_list

def load_cost_types():
    cost_record = []
    with open(COST_RECORD_PATH, "r", encoding="utf-8") as f:
        for line in f:
            cost_record.append(line.strip())
    return cost_record

def load_earn_types():
    earn_record = []
    with open(EARN_RECORD_PATH, "r", encoding="utf-8") as f:
        for line in f:
            earn_record.append(line.strip())
    return earn_record

def load_json(JSON_PATH=JSON_PATH):
    if not os.path.exists(JSON_PATH):
        return []
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(records, JSON_PATH=JSON_PATH):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def add_record(date, input_type, account, amount, category, note=""):
    records = load_json()
    records.append({
        "date": date,
        "type": input_type,
        "account": account,
        "amount": amount,
        "category": category,
        "note": note
    })
    save_json(records)

def add_account(account_name, type, balance=0):
    account_list = load_json(ACCOUNT_LIST_PATH)
    account_list.append(
        {
            "name": account_name,
            "type": type,
            "balance": balance
        }
    )
    save_json(account_list, ACCOUNT_LIST_PATH)