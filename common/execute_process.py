import subprocess
import time
def open_exe(exe_path):
    # 指定你想執行的 EXE 檔案路徑
    is_exec_success=False
    error_message=""
    # 執行 EXE 檔案
    try:
        subprocess.Popen(exe_path)
        print(f"{exe_path} 執行成功")
        is_exec_success=True
        time.sleep(3)
    except subprocess.CalledProcessError as e:
        error_message=f"執行 {exe_path} 時發生錯誤: {e}"
    except FileNotFoundError:
        error_message=f"找不到 {exe_path}，請確認路徑正確"
    return  is_exec_success,error_message

