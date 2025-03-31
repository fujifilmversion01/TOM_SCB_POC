import subprocess
import time
import psutil

class ProcessManager:
    def __init__(self,config):
        self.process = None
        self.config=config
    def open_exe(self, exe_path):

        # 測試根據進程名稱終止 Notepad++
        success, close_process_by_name_err_message = self.close_process_by_name(self.config['processname'])
        if not success:
            return success, close_process_by_name_err_message
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

    def close_process_by_name(self, process_name):
        """根據進程名稱終止進程，例如 Notepad++"""
        try:
            # 使用 psutil 遍歷所有運行中的進程
            for proc in psutil.process_iter(['pid', 'name']):
                if process_name.lower() in proc.info['name'].lower():
                    proc.terminate()  # 終止進程
                    print(f"已終止進程: {proc.info['name']}，PID: {proc.info['pid']}")
                    return True, f"進程 {proc.info['name']} 已被終止"
            return False, f"未找到進程 {process_name}"
        except psutil.NoSuchProcess:
            return False, "指定的進程不存在"
        except Exception as e:
            return False, f"終止進程時出錯: {e}"
