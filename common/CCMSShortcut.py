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
    def get_current_page_text(self):
        page_text=""
        pyautogui.hotkey('ctrl', 'c')
        page_text = pyperclip.paste()
        return page_text
