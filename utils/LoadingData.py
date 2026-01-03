import os
import json

account_list = []
cost_record = []
earn_record = []

json_path = os.path.join(os.path.dirname(__file__), "records.json")

def load_accounts():
    with open("accountList.txt", "r", encoding="utf-8") as f:
        for line in f:
            account_list.append(line.strip())
    return account_list

def load_cost_types():
    with open("costTypeList.txt", "r", encoding="utf-8") as f:
        for line in f:
            cost_record.append(line.strip())
    return cost_record

def load_earn_types():
    with open("earnTypeList.txt", "r", encoding="utf-8") as f:
        for line in f:
            earn_record.append(line.strip())
    return earn_record

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