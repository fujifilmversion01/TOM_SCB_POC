import win32api
import win32con
import time
import keyboard  # 確保先導入keyboard庫


# 獲取當前的語言代碼
def get_input_language():
    # 獲取當前語言的代碼
    lang_code = win32api.GetKeyboardLayout(0)
    # 提取低位部分來判斷語言代碼
    lang_code = lang_code & 0xFFFF  # 只保留低位的部分
    return lang_code


def switch_to_english(shortcut):
    # 模擬按下 Alt+Shift 切換輸入法
    keyboard.press_and_release(shortcut)
    time.sleep(1)


# 測試
if __name__ == "__main__":
    keyboard.write('a')  # 嘗試輸入 "a" 鍵
    #
    # print("正在強制切換為英文輸入法...")
    # arr_shortcut = ['alt+shift', 'shift+space', 'shift']
    #
    # for shortcut in arr_shortcut:
    #     switch_to_english(shortcut)
    #     current_lang = get_input_language()
    #     print(f"當前輸入法代碼: {current_lang}")
    #
    #     if current_lang == 1033:  # 1033 是英文的語言代碼
    #         print("輸入法已切換為英文")
    #         break
    #     else:
    #         # 測試是否能夠輸入英文字符aaa
    #         keyboard.write('a')  # 嘗試輸入 "a" 鍵
    #         print("如果輸入了英文字符，則輸入法處於英文模式。")
    #         print("輸入法切換失敗，當前語言代碼不是英文")
