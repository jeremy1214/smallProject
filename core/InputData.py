#import necessary modules
from datetime import date
import utils.LoadingData as LoadingData
import utils.InputingData as InputingData


def check_input():
    return InputingData.input_record_type()

def check_account():
    account_list = LoadingData.load_accounts()
    return InputingData.input_account(account_list)

def add_cost_record():
    cost_record = LoadingData.load_cost_types()
    return InputingData.input_cost_type(cost_record)

def add_earn_record():
    earn_record = LoadingData.load_earn_types()
    return InputingData.input_earn_type(earn_record)

def input_data():
    # Load existing records
    input_type = check_input()
    account = check_account()

    if input_type == "支出":
        type = add_cost_record()
    elif input_type == "收入":
        type = add_earn_record()

    amount = InputingData.input_amount()
    note = InputingData.input_note()
    LoadingData.add_record(date.today().isoformat(), input_type, account, amount, type, note)

    print("記錄已新增。")
