import utils.LoadingData as LoadingData
import utils.InputingData as InputingData


def load_records():
    return LoadingData.load_json()

def save_records(records):
    LoadingData.save_json(records)

def delete_record(index):
    records = load_records()
    if 0 <= index < len(records):
        del records[index]
        save_records(records)
        print(f"已刪除索引 {index} 的記錄。")
        return True
    else:
        print("無效的索引，無法刪除記錄。")
        return False

def delete_by_index():
    while True:
        record_index = input("請輸入要刪除的紀錄索引(從1開始): ")
        InputingData.exit_command(record_index)
        InputingData.list_command(record_index, load_records(), "記錄")
        try:
            record_index = int(record_index)-1
            delete_record(record_index)
            break
        except ValueError:
            print("請輸入有效的整數索引。")

def delete_by_type():
    cost_record = LoadingData.load_cost_types()
    earn_record = LoadingData.load_earn_types()
    type = InputingData.input_record_type()

    if type == "支出":
        type_to_delete = InputingData.input_cost_type(cost_record)
        all_records = load_records()
        filtered_records = [r for r in all_records if not (r["type"] == "支出" and r["category"] == type_to_delete)]
        save_records(filtered_records)
        print(f"已刪除所有支出類型為 '{type_to_delete}' 的記錄。")
    elif type == "收入":
        type_to_delete = InputingData.input_earn_type(earn_record)
        all_records = load_records()
        filtered_records = [r for r in all_records if not (r["type"] == "收入" and r["category"] == type_to_delete)]
        save_records(filtered_records)
        print(f"已刪除所有收入類型為 '{type_to_delete}' 的記錄。")
    
def delete_data():
    while True:
        delete_number_type = input("請選擇要刪除的紀錄的量(輸入多筆或單筆): ")
        InputingData.exit_command(delete_number_type)
        if delete_number_type not in ["單筆", "多筆"]:
            print("不合法的輸入，請輸入 '單筆' 或 '多筆'。")
            continue
        break
    if delete_number_type == "單筆":
        delete_by_index()
    elif delete_number_type == "多筆":
        delete_by_type()
