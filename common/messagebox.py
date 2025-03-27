# message_box.py
import tkinter as tk
from tkinter import messagebox

class MessageBox:
    def __init__(self):
        # 初始化 Tkinter 視窗
        self.root = tk.Tk()
        self.root.withdraw()  # 不顯示主視窗

    def show_info(self, title, message):
        """顯示訊息框"""
        messagebox.showinfo(title, message)

    def show_warning(self, title, message):
        """顯示警告框"""
        messagebox.showwarning(title, message)

    def show_error(self, title, message):
        """顯示錯誤框"""
        messagebox.showerror(title, message)

    def ask_question(self, title, message):
        """顯示確認框，返回 'yes' 或 'no'"""
        return messagebox.askquestion(title, message)

    def ask_yes_no(self, title, message):
        """顯示是/否選項的訊息框，返回 True 或 False"""
        return messagebox.askyesno(title, message)

    def ask_retry_cancel(self, title, message):
        """顯示重試/取消選項的訊息框，返回 True 或 False"""
        return messagebox.askretrycancel(title, message)
