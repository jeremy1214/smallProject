from core import InputData, DeleteData, ShowData
from core import ControlAccount as ControlAccount

while True:
    print("歡迎使用記帳系統！")
    print("請選擇操作:")
    print("1. 輸入記錄")
    print("2. 刪除記錄")
    print("3. 顯示記錄")
    print("4. 帳戶管理")
    print("5. 退出系統")

    choice = input("輸入選項編號 (1-5): ")

    if choice == "1":
        InputData.input_data()
    elif choice == "2":
        DeleteData.delete_data()
    elif choice == "3":
        ShowData.show_data()
    elif choice == "4":
        ControlAccount.control_account()
    elif choice == "5":
        print("感謝使用，再見！")
        break
    else:
        print("無效的選項，請重試。")