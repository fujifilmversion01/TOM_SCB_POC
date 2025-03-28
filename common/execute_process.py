import subprocess
import time


class ProcessManager:
    def __init__(self,config):
        self.process = None
        self.config=config
    def open_exe(self, exe_path):
        """啟動指定路徑的EXE程序"""
        is_exec_success = False
        error_message = ""
        # 嘗試啟動EXE程序
        try:
            self.process = subprocess.Popen(exe_path)
            print(f"{exe_path} 執行成功")
            is_exec_success = True
            time.sleep(int(self.config['open_exe_delay_after_seconds']))  # 可以根據需要調整等待時間
        except subprocess.CalledProcessError as e:
            error_message = f"執行 {exe_path} 時發生錯誤: {e}"
        except FileNotFoundError:
            error_message = f"找不到 {exe_path}，請確認路徑正確"
        except Exception as e:
            error_message = f"未知錯誤: {e}"

        return is_exec_success, error_message

    def close_exe(self):
        is_close_success = False
        error_message = ""
        """關閉啟動的EXE程序"""
        if self.process:
            try:
                self.process.terminate()  # 或使用 self.process.kill() 強制終止進程
                error_message = f"進程已被終止."
                is_close_success = True
                self.process=None
            except Exception as e:
                error_message = f"無法終止進程: {e}"
        else:
            error_message = "沒有活動的進程"
        return is_close_success, error_message
