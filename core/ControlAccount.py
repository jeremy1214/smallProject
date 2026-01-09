import utils.LoadingData as LoadingData
import utils.InputingData as InputingData



def load_account():
    return LoadingData.load_json(LoadingData.ACCOUNT_LIST_PATH)

def get_account_names():
    accounts = load_account()
    return [account["name"] for account in accounts]

def control_account():

    print("選擇要對帳戶進行的操作: ")
    for i in range(4):
        print(f"{i+1}. {['新增帳戶', '刪除帳戶', '查看帳戶', '轉帳'][i]}")
    while True:
        action = input("請輸入操作編號 (1-4): ")
        InputingData.exit_command(action)
        InputingData.list_command(action, ['新增帳戶', '刪除帳戶', '查看帳戶', '轉帳'], "操作")
        if action not in ["1", "2", "3", "4"]:
            print("不合法的輸入，請輸入 1、2、3 或 4。")
            continue
        break

    account_list = load_account()
    account_name_list = get_account_names()

    if action == "1":
        new_account = InputingData.input_account_name(account_name_list)
        account_type = InputingData.input_account_type()
        balance = InputingData.input_balance()
        LoadingData.add_account(new_account, account_type, balance)
        print(f"帳戶 '{new_account}' 已新增。")
    elif action == "2":
        del_account = InputingData.input_account(account_name_list)
        account_list = [acc for acc in account_list if acc["name"] != del_account]
        LoadingData.save_json(account_list, LoadingData.ACCOUNT_LIST_PATH)
        print(f"帳戶 '{del_account}' 已刪除。")
    elif action == "3":
        print("現有帳戶列表:")
        for account in account_list:
            print(f"名稱: {account['name']}, 類型: {account['type']}, 餘額: {account['balance']}")
    elif action == "4":
        print("選擇轉出帳戶: ")
        from_account = InputingData.input_account(account_name_list)
        print("選擇轉入帳戶: ")
        to_account = InputingData.input_account(account_name_list, exclude=from_account)
        amout = InputingData.input_amount()
        LoadingData.transfer_between_accounts(from_account, to_account, amout)
        print(f"已從 '{from_account}' 轉帳 {amout} 到 '{to_account}'。")