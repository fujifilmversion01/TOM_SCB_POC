import tkinter as tk
from tkinter import ttk
from messagebox import MessageBox

class CustomCheckboxDialog:
    def __init__(self, title='選擇對話框', prompt='請選擇:', options=None, width=400, height=300, x=600, y=250):
        """初始化對話框屬性"""
        self.title = title
        self.prompt = prompt
        self.options = options or []  # 預設空的選項列表
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.selected_options = []

        self.var_dict = {}  # 用來儲存選擇結果的變數字典
        self.dialog = None  # 用來儲存Toplevel視窗

    def _create_dialog(self):
        """建立和顯示自定義複選框對話框"""
        # 建立主視窗
        root = tk.Tk()
        root.withdraw()  # 隱藏主視窗

        # 創建新視窗
        self.dialog = tk.Toplevel(root)
        self.dialog.title(self.title)
        self.dialog.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")  # 設定大小與位置
        self.dialog.resizable(False, False)  # 禁止調整大小

        # 設定對話框樣式
        self.dialog.config(bg="#f0f0f0")  # 背景顏色
        # 顯示提示訊息
        tk.Label(self.dialog, text=self.prompt, font=('Helvetica', 12, 'bold'), bg="#f0f0f0").pack(pady=15)

        # 創建複選框
        for option in self.options:
            self.var_dict[option] = tk.BooleanVar()  # 使用 BooleanVar
            checkbutton = ttk.Checkbutton(self.dialog, text=option, variable=self.var_dict[option], style="Custom.TCheckbutton")
            checkbutton.pack(anchor='w', padx=20, pady=5)

        # 設定自定義樣式
        style = ttk.Style()
        style.configure("Custom.TCheckbutton",
                        padding=5,
                        font=('Helvetica', 10),
                        foreground="#333",
                        background="#f0f0f0")

        # 設定確認按鈕
        ttk.Button(self.dialog, text="確定", command=self.submit, style="FB.TButton").pack(pady=15)

        # 設定自定義按鈕樣式，模仿Facebook按鈕
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")

        self.dialog.grab_set()  # 讓對話框保持在最上層
        self.dialog.wait_window()  # 等待視窗關閉後繼續執行

    def submit(self):
        """處理用戶提交的選項"""
        self.selected_options = [option for option, var in self.var_dict.items() if var.get()]  # 檢查 BooleanVar 是否為 True
        if not self.selected_options:
            MessageBox().show_info("提示", "請選擇至少一項選項。")
        else:
            self.dialog.destroy()  # 關閉視窗

    def show(self):
        """顯示對話框並返回選擇的結果"""
        self._create_dialog()
        return self.selected_options


# # 使用範例
if __name__ == "__main__":
    options = ["選項 1", "選項 2", "選項 3"]
    dialog = CustomCheckboxDialog(title="自訂複選框", prompt="請選擇您的選項:", options=options)
    selected = dialog.show()
    print("選擇的項目:", selected)
