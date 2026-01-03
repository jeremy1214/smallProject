import os
import utils.LoadingData as LoadingData

json_path = os.path.join(os.path.dirname(__file__), "records.json")
cost_record = LoadingData.load_cost_types()
earn_record = LoadingData.load_earn_types()

def load_records():
    return LoadingData.load_records()

def save_records(records):
    LoadingData.save_records(records)

def delete_record(index):
    records = load_records()
    if 0 <= index < len(records):
        del records[index]
        save_records(records)
        print(f"已刪除索引 {index} 的記錄。")
    else:
        print("無效的索引，無法刪除記錄。")

def delete_by_index():
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

def delete_by_type():
    while True:
        type = input("請輸入要刪除的紀錄類型(支出/收入): ")
        if type not in ["支出", "收入"]:
            print("不合法的類型。請輸入 '支出' 或 '收入'。")
            continue
        if type == "支出":
            records = input("請輸入要刪除支出類型編號")
            while True:
                if(records.lower() == "exit"):
                    exit()
                if not records.isdigit():
                    print("不合法的輸入。請輸入數字。")
                    records = input("請輸入要刪除支出類型編號")
                    continue
                record_index = int(records) - 1
                if 0 <= record_index < len(cost_record):
                    type_to_delete = cost_record[record_index]
                    all_records = load_records()
                    filtered_records = [r for r in all_records if not (r["type"] == "支出" and r["category"] == type_to_delete)]
                    save_records(filtered_records)
                    print(f"已刪除所有支出類型為 '{type_to_delete}' 的記錄。")
                    break
                else:
                    print("選擇無效。請重試。")
                    records = input("請輸入要刪除支出類型編號")
            break
        elif type == "收入":
            records = input("請輸入要刪除收入類型編號")
            while True:
                if(records.lower() == "exit"):
                    exit()
                if not records.isdigit():
                    print("不合法的輸入。請輸入數字。")
                    records = input("請輸入要刪除收入類型編號")
                    continue
                record_index = int(records) - 1
                if 0 <= record_index < len(earn_record):
                    type_to_delete = earn_record[record_index]
                    all_records = load_records()
                    filtered_records = [r for r in all_records if not (r["type"] == "收入" and r["category"] == type_to_delete)]
                    save_records(filtered_records)
                    print(f"已刪除所有收入類型為 '{type_to_delete}' 的記錄。")
                    break
                else:
                    print("選擇無效。請重試。")
                    records = input("請輸入要刪除收入類型編號")
    
def delete_data():
    delete_number_type = input("請選擇要刪除的紀錄的量(輸入多筆或單筆): ")

    if delete_number_type == "單筆":
        delete_by_index()
    elif delete_number_type == "多筆":
        delete_by_type()

if __name__ == "__main__":
    delete_data()