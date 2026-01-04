def exit_command(user_input):
    if user_input.lower() == "exit":
        exit()

def list_command(user_input, items, item_name):
    if user_input.lower() == "list":
        print(f"{item_name} 列表:")
        for i, item in enumerate(items):
            print(f"{i + 1}: {item}")

def input_record_type():
    while True:
        print("不合法的類型。請輸入 '支出' 或 '收入'。")
        tmp = input("請輸入記錄類型(支出/收入): ")
        exit_command(tmp)
        if tmp not in ["支出", "收入"]:
            print("不合法的類型。請輸入 '支出' 或 '收入'。")
            continue
        return tmp
def input_account(account_list):
    print("可用帳戶列表:")
    for i, account in enumerate(account_list):
        print(f"{i + 1}: {account}")
    while True:
        acc_input = input("請輸入帳戶編號: ")
        list_command(acc_input, account_list, "帳戶")
        exit_command(acc_input)
        if not acc_input.isdigit():
            print("不合法的輸入。請輸入數字。")
            continue
        acc_index = int(acc_input) - 1
        if 0 <= acc_index < len(account_list):
            return account_list[acc_index]
        else:
            print("不合法的帳戶編號，請重試。")

def input_amount():
    while True:
        amount_input = input("請輸入金額: ")
        exit_command(amount_input)
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("金額必須為正數，請重試。")
                continue
            return amount
        except ValueError:
            print("不合法的金額，請輸入數字。")

def input_cost_type(cost_record, is_index=False):
    print("支出類型列表:")
    for i, record in enumerate(cost_record):
        print(f"{i + 1}: {record}")
    while True:
        type_input = input("請輸入支出類型編號: ")
        list_command(type_input, cost_record, "支出類型")
        exit_command(type_input)
        if not type_input.isdigit():
            print("不合法的輸入。請輸入數字。")
            continue
        type_index = int(type_input) - 1
        if 0 <= type_index < len(cost_record):
            if is_index:
                return type_index
            return cost_record[type_index]
        else:
            print("不合法的支出類型編號，請重試。")

def input_earn_type(earn_record, is_index=False):
    print("收入類型列表:")
    for i, record in enumerate(earn_record):
        print(f"{i + 1}: {record}")
    while True:
        type_input = input("請輸入收入類型編號: ")
        list_command(type_input, earn_record, "收入類型")
        exit_command(type_input)
        if not type_input.isdigit():
            print("不合法的輸入。請輸入數字。")
            continue
        type_index = int(type_input) - 1
        if 0 <= type_index < len(earn_record):
            if is_index:
                return type_index
            return earn_record[type_index]
        else:
            print("不合法的收入類型編號，請重試。")

def input_note():
    note = input("輸入備註: ")
    exit_command(note)
    return note

def input_date():
    while True:
        time_type = input("請選擇要顯示的時間範圍(日、月、年): ")
        exit_command(time_type)
        if time_type not in ["日", "月", "年"]:
            print("不合法的時間範圍。請輸入 '日'、'月' 或 '年'。")
            continue
        return time_type
    
def input_delete_type():
    while True:
        type_input = input("請輸入要刪除的紀錄類型(支出/收入): ")
        exit_command(type_input)
        if type_input not in ["支出", "收入"]:
            print("不合法的類型。請輸入 '支出' 或 '收入'。")
            continue
        return type_input
    