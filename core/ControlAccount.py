import utils.LoadingData as LoadingData
import utils.InputingData as InputingData



def load_account():
    return LoadingData.load_json(LoadingData.ACCOUNT_LIST_PATH)

def get_account_names():
    accounts = load_account()
    return [account["name"] for account in accounts]

print("選擇要對帳戶進行的操作: ")
for i in range(3):
    print(f"{i+1}. {['新增帳戶', '刪除帳戶', '查看帳戶'][i]}")
while True:
    action = input("請輸入操作編號 (1-3): ")
    InputingData.exit_command(action)
    InputingData.list_command(action, ['新增帳戶', '刪除帳戶', '查看帳戶'], "操作")
    if action not in ["1", "2", "3"]:
        print("不合法的輸入，請輸入 1、2 或 3。")
        continue
    break

account_list = load_account()
account_name_list = get_account_names()
if action == "1":
    new_account = InputingData.input_account_name(account_name_list)
    account_type = InputingData.input_account_type()
    LoadingData.add_account(new_account)
    print(f"帳戶 '{new_account}' 已新增。")