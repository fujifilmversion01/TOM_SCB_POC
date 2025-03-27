from  common.dialog import  custom_input_dialog
import sys  # 用於退出程式
from common.messagebox import  MessageBox
import tkinter as tk
from tkinter import ttk
from common.selectitem import DropdownDialog
#import selectitem2
class InputHandler:
    def __init__(self):
        self.msg_box = MessageBox()
        self.dropdown_dialog = DropdownDialog()  # Create an instance of DropdownDialog
    def show_exit_message_and_exit(self, message):
        """顯示退出訊息並退出程式"""
        self.msg_box.show_info("提示", message)
        sys.exit()

    def get_non_empty_input(self, prompt, show=""):
        """輸入對話框，直到用戶輸入有效內容"""
        while True:
            user_input = custom_input_dialog(prompt=prompt, show=show)
            res=self.dialog_result_handler(res=user_input, prompt=prompt)
            if res:
                return res
            # if user_input:
            #     return user_input
            # elif user_input is None :
            #     self.show_exit_message_and_exit(message=f"程式已關閉。")
            # else:
            #     self.msg_box.show_info("提示", f"{prompt} 不能為空，請重新輸入。")

    def get_credentials(self):
        """獲取帳號和密碼"""
        username = self.get_non_empty_input(prompt="帳號:")
        password = self.get_non_empty_input(prompt="密碼:", show="*")
        return username, password

    def set_dropdown_options(self,title='選擇對話框', prompt='請選擇:', options=None, width=400, height=300, x=600, y=250):
        """設定下拉選項"""
        self.dropdown_dialog.set_dropdown_options(title='選擇對話框', prompt='請選擇:', options=options, width=400, height=300, x=600, y=250)  # Set options for the dropdown dialog
        #.set_dropdown_options(title='選擇對話框', prompt='請選擇:', options=options, width=400, height=300, x=600, y=250)  # Set options for the dropdown dialog

    def get_dropdown_selection(self, prompt):
        while True:
            res = self.dropdown_dialog.get_dropdown_selection(prompt)
            #res = selectitem2.get_dropdown_selection(prompt)
            return self.dialog_result_handler(res=res,prompt=prompt)
            # if res:
            #     return res
            # elif res is None :
            #     self.show_exit_message_and_exit(message=f"程式已關閉。")
            # else:
            #     self.msg_box.show_info("提示", f"{prompt} 不能為空，請重新輸入。")
        #"""調用DropdownDialog來顯示下拉選擇對話框"""
        #return self.dropdown_dialog.get_dropdown_selection(prompt)  # Get selected option from dropdown
    def dialog_result_handler(self,res,prompt):
        if res:
            return res
        elif res is None:
            self.show_exit_message_and_exit(message=f"程式已關閉。")
        else:
            self.msg_box.show_info("提示", f"{prompt} 不能為空，請重新輸入。")

