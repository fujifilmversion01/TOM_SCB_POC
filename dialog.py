import tkinter as tk
from tkinter import ttk

def custom_input_dialog(title='輸入對話框', prompt='請輸入',show=None, width=400, height=200, x=600, y=250):
    user_input = None  # 預設值

    # 建立主視窗
    root = tk.Tk()
    root.withdraw()  # 隱藏主視窗
    # 創建新視窗
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry(f"{width}x{height}+{x}+{y}")  # 設定大小與位置
    dialog.resizable(False, False)  # 禁止調整大小
    # 標籤與輸入框
    tk.Label(dialog, text=prompt).pack(pady=10)
    entry = tk.Entry(dialog,show=show)
    entry.pack(pady=5)

    # 儲存輸入值
    def submit():
        nonlocal user_input  # 讓內部函式修改外部變數
        user_input = entry.get()
        dialog.destroy()  # 關閉視窗
        # 這個函式會在用戶點擊視窗的關閉按鈕時觸發

   # def on_close():
   #     dialog.destroy()

    ttk.Style().configure("TButton", padding=6, relief="flat",
                          background="#ccc")
    ttk.Button(dialog, text="確定", command=submit, style="FB.TButton").pack(pady=15)
    #tk.Button(dialog, text="確定", command=submit).pack(pady=5)

    dialog.grab_set()  # 讓對話框保持在最上層
    dialog.wait_window()  # 等待視窗關閉後繼續執行

    return user_input



