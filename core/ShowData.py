#import necessary modules
from datetime import datetime
import utils.LoadingData as LoadingData
import utils.InputingData as InputingData


def check_account():
    account_list = LoadingData.load_accounts()
    return InputingData.input_account(account_list)

def show_day_total(account: str, year: int, month: int, day: int):
    records = LoadingData.load_json()
    day_total = {"total_earn": 0, "total_cost": 0}
    for record in records:
        if record["account"] != account:
            continue
        date_str = record["date"]
        d = datetime.fromisoformat(date_str)
        year_record = d.year
        month_record = d.month
        day_record = d.day
        if year_record == year and month_record == month and day_record == day:
            if record["type"] == "支出":
                day_total["total_cost"] += int(record["amount"])
            elif record["type"] == "收入":
                day_total["total_earn"] += int(record["amount"])
    return day_total

def show_month_total(account: str, year: int, month: int):
    records = LoadingData.load_json()
    month_total = {"total_earn": 0, "total_cost": 0}
    for record in records:
        if record["account"] != account:
            continue
        date_str = record["date"]
        d = datetime.fromisoformat(date_str)
        year_record = d.year
        month_record = d.month
        if year_record == year and month_record == month:
            if record["type"] == "支出":
                month_total["total_cost"] += int(record["amount"])
            elif record["type"] == "收入":
                month_total["total_earn"] += int(record["amount"])
    return month_total

def show_year_total(account: str, year: int):
    records = LoadingData.load_json()
    year_total = {"total_earn": 0, "total_cost": 0}
    for record in records:
        if record["account"] != account:
            continue
        date_str = record["date"]
        d = datetime.fromisoformat(date_str)
        year_record = d.year
        if year_record == year:
            if record["type"] == "支出":
                year_total["total_cost"] += int(record["amount"])
            elif record["type"] == "收入":
                year_total["total_earn"] += int(record["amount"])
    return year_total


def show_data():
    print("歡迎使用記帳顯示系統！")
    account = check_account()
    time_type = InputingData.input_date()
    if time_type == "日":
        year = int(input("請輸入年份(YYYY): "))
        month = int(input("請輸入月份(MM): "))
        day = int(input("請輸入日期(DD): "))
        total = show_day_total(account, year, month, day)
        print(f"{year}年{month}月{day}日 總收入: {total['total_earn']} 總支出: {total['total_cost']}")
    elif time_type == "月":
        year = int(input("請輸入年份(YYYY): "))
        month = int(input("請輸入月份(MM): "))
        total = show_month_total(account, year, month)
        print(f"{year}年{month}月 總收入: {total['total_earn']} 總支出: {total['total_cost']}")
    elif time_type == "年":
        year = int(input("請輸入年份(YYYY): "))
        total = show_year_total(account, year)
        print(f"{year}年 總收入: {total['total_earn']} 總支出: {total['total_cost']}")




