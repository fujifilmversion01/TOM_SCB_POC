# checkbox.py
# checkbox.py
import tkinter as tk
from tkinter import ttk
from messagebox import MessageBox

import tkinter as tk
from tkinter import ttk
from messagebox import MessageBox

def custom_checkbox_dialog(title='選擇對話框', prompt='請選擇:', options=None, width=400, height=300, x=600, y=250):
    """顯示複選框對話框，直到用戶選擇至少一項選項"""
    if options is None:
        options = []  # 預設空的選項列表

    # 建立主視窗
    root = tk.Tk()
    root.withdraw()  # 隱藏主視窗

    # 創建新視窗
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry(f"{width}x{height}+{x}+{y}")  # 設定大小與位置
    dialog.resizable(False, False)  # 禁止調整大小

    # 設定對話框樣式
    dialog.config(bg="#f0f0f0")  # 背景顏色
    # 顯示提示訊息
    tk.Label(dialog, text=prompt, font=('Helvetica', 12, 'bold'), bg="#f0f0f0").pack(pady=15)

    # 用來儲存選擇結果的變數
    var_dict = {}

    # 創建複選框
    for option in options:
        var_dict[option] = tk.BooleanVar()  # 使用 BooleanVar
        checkbutton = ttk.Checkbutton(dialog, text=option, variable=var_dict[option], style="Custom.TCheckbutton")
        checkbutton.pack(anchor='w', padx=20, pady=5)

    # 設定自定義樣式
    style = ttk.Style()
    style.configure("Custom.TCheckbutton",
                    padding=5,
                    font=('Helvetica', 10),
                    foreground="#333",
                    background="#f0f0f0")
    # 儲存選擇的項目
    selected_options = []  # 這裡會儲存選中的選項
    # 儲存選擇的項目
    def submit():
        nonlocal selected_options  # 使用外部的 selected_options
        selected_options = [option for option, var in var_dict.items() if var.get()]  # 檢查 BooleanVar 是否為 True
        print("選擇的項目:", selected_options)  # 打印選擇的項目，調試用

        if not selected_options:
            MessageBox().show_info("提示", "請選擇至少一項選項。")
        else:
            dialog.destroy()  # 關閉視窗
            print("選擇的項目:", selected_options)  # 處理選擇的項目
            return selected_options  # 返回選中的項目

    # 設定確認按鈕
    ttk.Button(dialog, text="確定", command=submit, style="FB.TButton").pack(pady=15)

    # 設定自定義按鈕樣式，模仿Facebook按鈕
    ttk.Style().configure("TButton", padding=6, relief="flat",
                          background="#ccc")

    dialog.grab_set()  # 讓對話框保持在最上層
    dialog.wait_window()  # 等待視窗關閉後繼續執行

    return selected_options  # 這裡返回選中的項目而不是 var_dict





def custom_checkbox_dialog2(title='選擇對話框', prompt='請選擇:', options=None, width=400, height=300, x=600, y=250):
    if options is None:
        options = []  # 預設空的選項列表

    # 建立主視窗
    root = tk.Tk()
    root.withdraw()  # 隱藏主視窗

    # 創建新視窗
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry(f"{width}x{height}+{x}+{y}")  # 設定大小與位置
    dialog.resizable(False, False)  # 禁止調整大小

    # 設定對話框樣式
    dialog.config(bg="#f0f0f0")  # 背景顏色
    # 顯示提示訊息
    tk.Label(dialog, text=prompt, font=('Helvetica', 12, 'bold'), bg="#f0f0f0").pack(pady=15)

    # 用來儲存選擇結果的變數
    var_dict = {}

    # 創建複選框
    for option in options:
        var_dict[option] = tk.BooleanVar()
        ttk.Checkbutton(dialog, text=option, variable=var_dict[option], style="Custom.TCheckbutton").pack(anchor='w',
                                                                                                          padx=20,
                                                                                                          pady=5)

    # 設定自定義樣式
    style = ttk.Style()
    style.configure("Custom.TCheckbutton",
                    padding=5,
                    font=('Helvetica', 10),
                    foreground="#333",
                    background="#f0f0f0")

    # 儲存選擇的項目
    selected_options = []  # 這裡會儲存選中的選項

    # 儲存選擇的項目
    def submit():
        nonlocal selected_options  # 使用外部的 selected_options
        selected_options = [option for option, var in var_dict.items() if var.get()]
        dialog.destroy()  # 關閉視窗
        print("選擇的項目:", selected_options)  # 您可以根據需求處理這些選擇項目

    # 設定確認按鈕（像Facebook的藍底白字樣式）
    ttk.Button(dialog, text="確定", command=submit, style="FB.TButton").pack(pady=15)

    # 設定自定義按鈕樣式，模仿Facebook按鈕
    # style.configure("FB.TButton",
    #                 font=('Helvetica', 10, 'bold'),
    #                 padding=10,
    #                 relief="flat",
    #                 background="#1877f2",  # Facebook的藍色（normal狀態背景）
    #                 foreground="#fff",  # 白色文字
    #                 borderwidth=1,
    #                 focusthickness=0,
    #                 anchor='center')
    ttk.Style().configure("TButton", padding=6, relief="flat",
                          background="#ccc")

    # 設定按鈕的懸停和按下顏色
    # style.map("FB.TButton",
    #           foreground=[('pressed', 'white'), ('active', 'white')],
    #           background=[('pressed', '#145db1'), ('active', '#1877f2')])  # 讓normal也有藍色背景

    dialog.grab_set()  # 讓對話框保持在最上層
    dialog.wait_window()  # 等待視窗關閉後繼續執行

    #return var_dict
    return selected_options


# # 示範用法
options = ["選項 1", "選項 2", "選項 3", "選項 4"]
custom_checkbox_dialog2(options=options)
