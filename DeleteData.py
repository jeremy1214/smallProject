import json
import os

json_path = os.path.join(os.path.dirname(__file__), "records.json")

def load_records():
    if not os.path.exists(json_path):
        return []
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_records(records):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def delete_record(index):
    records = load_records()
    if 0 <= index < len(records):
        del records[index]
        save_records(records)
        print(f"已刪除索引 {index} 的記錄。")
    else:
        print("無效的索引，無法刪除記錄。")

delete_number_type = input("請選擇要刪除的紀錄的量(輸入多筆或單筆): ")
if delete_number_type == "單筆":
    while True:
        record_index = input("請輸入要刪除的紀錄索引(從0開始): ")
        if(record_index.lower() == "exit"):
            exit()
        if(record_index.lower() == "list"):
            records = load_records()
            print("目前的紀錄列表:")
            for i, record in enumerate(records):
                print(f"{i}: {record}")
            continue
        try:
            record_index = int(record_index)
            delete_record(record_index)
            break
        except ValueError:
            print("請輸入有效的整數索引。")