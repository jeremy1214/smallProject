#import necessary modules
from datetime import date
import utils.LoadingData as LoadingData

account_list = LoadingData.load_accounts()
cost_record = LoadingData.load_cost_types()
earn_record = LoadingData.load_earn_types()
type = ""


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

def add_cost_record():
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

def add_earn_record():
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

def input_record():
    # Load existing records
    input_type = check_input()
    account = check_account()

    if input_type == "支出":
        add_cost_record()
    elif input_type == "收入":
        add_earn_record()

    amount = input("輸入金額: ")
    if amount == "exit":
        exit()
    note = input("輸入備註: ")
    if note == "exit":
        exit()
    LoadingData.add_record(date.today().isoformat(), input_type, account, amount, type, note)

    print("記錄已新增。")

if __name__ == "__main__":
    input_record()