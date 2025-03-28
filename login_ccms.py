# from common.InputHandler import InputHandler
# import pyautogui
# from common.execute_process import open_exe
# import time
# import pyperclip

class LoginCCMSService:
    def __init__(self, config, inputhandler,ccms_shortcut):
        self.config = config
        self.inputhandler = inputhandler
        self.ccms_shortcut = ccms_shortcut
        self.logon_applid=self.config["login"]["LOGON_APPLID"]
        self.logmode=self.config["login"]["LOGMODE"]
        self.username=""
        self.password=""
    def collect_login_data(self):
        self.username, self.password = self.inputhandler.get_credentials()
    def typeinto_login_data(self):
        self.ccms_shortcut.copy_and_paste(str=self.logon_applid)
        self.ccms_shortcut.press_tab()
        self.ccms_shortcut.copy_and_paste(str=self.logmode)
        self.ccms_shortcut.press_tab()
        self.ccms_shortcut.copy_and_paste(str=self.username)
        self.ccms_shortcut.press_tab()
        self.ccms_shortcut.copy_and_paste(str=self.password)
        self.ccms_shortcut.press_tab()
    def validate_user(self):
        current_text=self.ccms_shortcut.get_current_page_text()
        if self.config['login_page_string'] in current_text :
            return True
        else:
            return False
    def login_process(self):
        self.collect_login_data()
        self.typeinto_login_data()
        return self.validate_user()
        # open_ccms(config["ccms_path"])
        # time.sleep(1)
        #logon_applid = self.config["login"]["LOGON APPLID"]
        #self.ccms_shortcut.copy_and_paste(logon_applid)
        #pyautogui.press('tab')
        # pyautogui.write(config["login"]["LOGON APPLID"])

        # logmode = self.config["login"]["LOGMODE"]
        # self.copy_and_paste(logmode)
        # pyautogui.press('tab')
        # pyautogui.write(config["login"]["LOGMODE"])

# 打開CCMS程式
# def open_ccms(ccms_path):
#     is_exec_success, error_message = open_exe(ccms_path)
#     if not is_exec_success:
#         raise Exception(f"開啟CCMS時發生錯誤: {error_message}")





