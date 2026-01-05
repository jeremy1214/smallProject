import ctypes
import utils.LoadingData as LoadingData
from datetime import date

def send_reminder():
    ctypes.windll.user32.MessageBoxW(
        0,
        "今天還沒有記帳，記得打開你的記帳程式！",
        "記帳提醒",
        0
    )

def send():
    records = LoadingData.load_json()
    today_str = date.today().isoformat()
    has_record_today = any(record["date"] == today_str for record in records)
    if not has_record_today:
        send_reminder()
    else:
        exit()