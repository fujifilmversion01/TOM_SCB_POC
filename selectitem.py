import tkinter as tk
from tkinter import ttk
from messagebox import MessageBox

class DropdownDialog:
    def __init__(self):
        self.msg_box = MessageBox()
        self.dropdown_options = []  # Initialize an empty list for options
        self.title = ''
        self.prompt = ''
        self.width = 400
        self.height = 200
        self.x = 100
        self.y = 100
        self.selected_item=None
    def set_dropdown_options(self,title='選擇對話框', prompt='請選擇:', options=None, width=400, height=300, x=600, y=250):
        """設定下拉選項"""
        self.dropdown_options = options
        self.title = title
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_dropdown_selection(self, prompt):
        """顯示選擇下拉菜單的對話框"""
        if not self.dropdown_options:
            self.msg_box.show_info("提示", "沒有設定下拉選項，請先設置選項。")
            return None

        root = tk.Tk()
        root.withdraw()  # Hide the main window

        # Create a dialog window
        dialog = tk.Toplevel(root)
        dialog.title(self.title)
        dialog.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")  # 設定大小與位置
        dialog.resizable(False, False)  # 禁止調整大小

        # Create a label
        #label = tk.Label(dialog, text=prompt)
        #label.pack(padx=10, pady=10)
        # 顯示提示訊息
        tk.Label(dialog, text=prompt, font=('Helvetica', 12, 'bold'), bg="#f0f0f0").pack(pady=15)

        # Create a combobox (dropdown list) with the pre-set options
        combobox = ttk.Combobox(dialog, values=self.dropdown_options)
        combobox.set(self.dropdown_options[0])  # Set the default value (optional)
        combobox.pack(padx=10, pady=10)

        # Function to handle the selection
        def on_select():
            # selected_item = combobox.get()
            # dialog.selected_item = selected_item  # Store the selected item in the dialog
            self.selected_item = combobox.get()
            dialog.quit()  # Quit the main loop before destroying the dialog
            dialog.destroy()  # Close the dialog after selection


        # Create a button to confirm the selection
        #button = tk.Button(dialog, text="Confirm", command=on_select)
        #button.pack(padx=10, pady=10)
        ttk.Button(dialog, text="確定", command=on_select, style="FB.TButton").pack(pady=15)
        ttk.Style().configure("TButton", padding=6, relief="flat",
                              background="#ccc")

        # Function to handle the window close event
        def on_close():
            dialog.quit()  # Quit the main loop before destroying the dialog
            dialog.destroy()  # Close the dialog after selection
        # Bind the window close (X) button to the on_close function
        dialog.protocol("WM_DELETE_WINDOW", on_close)

        # Start the dialog loop
        dialog.mainloop()  # Start the Tkinter main loop for the dialog

        # Return the selected item after the dialog is closed
        #return getattr(dialog, 'selected_item', None)  # Use `selected_item` if it exists
        return self.selected_item  # Use `selected_item` if it exists



