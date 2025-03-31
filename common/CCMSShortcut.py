from math import trunc, factorial

import pyautogui
import pyperclip
import time
class CCMSShortcut:
    def __init__(self,config):
        self.config=config
    def press_tab(self):
        pyautogui.press('tab')
        time.sleep(1)
    def copy_and_paste(self,str):
        pyperclip.copy(str)
        pyautogui.hotkey('ctrl', 'v')  # 模擬 Ctrl + V 貼上
        time.sleep(1)
    def get_current_page_text(self,replace_white_space=True):
        page_text=""
        pyautogui.hotkey('ctrl', 'c')
        page_text = pyperclip.paste()
        if replace_white_space:
            page_text=page_text.replace(" ","")
        return page_text
    def press_enter(self):
        pyautogui.press('Enter')
        time.sleep(1)
    def press_home(self):
        pyautogui.press('Home')
        time.sleep(1)
    def goto_homepage(self):
        self.press_home()
        pyautogui.press('PCON')
        self.press_enter()
    def goto_page(self,page_name):
        pyautogui.press(page_name)
        time.sleep(1)
        self.press_enter()
    def check_page_in_specify_page(self,page_name):
        current_page_text=self.get_current_page_text().replace(" ","")
        if page_name in current_page_text:
            return  True
        else:
            return  False
    def typeinto_string(self,str):
        pyautogui.press(str)
    def press_left(self):
        pyautogui.press("Left")
