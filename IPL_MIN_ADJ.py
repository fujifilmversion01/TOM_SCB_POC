from common.messagebox import MessageBox
from init import load_config
from init import load_input_excel
from login_ccms import LoginCCMSService
from common.execute_process import ProcessManager
from common.InputHandler import InputHandler
from common.CCMSShortcut import CCMSShortcut

def close_exe(InputHandler,ProcessManager):
    if ProcessManager.process:
        is_close_success, close_exe_error_message = ProcessManager.close_exe()
        if not is_close_success:
            InputHandler.msg_box(close_exe_error_message)
def main():
    # 初始化
    config = load_config()
    input_excel=load_input_excel(config['input_excel_path'])
    _inputhandler=InputHandler()
    _ccms_shortcut=CCMSShortcut(config=config)
    _processmanager=ProcessManager(config=config)

    # 開啟CCMS-----start
    is_exec_success,open_exe_error_message=_processmanager.open_exe(config["ccms_path"])
    if not is_exec_success:
        raise Exception(f"開啟CCMS時發生錯誤: {open_exe_error_message}")
    # 開啟CCMS-----end
    try:
        # 登入CCMS scope-----start
        _login_ccms_service = LoginCCMSService(config=config, inputhandler=_inputhandler, ccms_shortcut=_ccms_shortcut)
        if _login_ccms_service.login_process() is False:
            close_exe(InputHandler=_inputhandler, ProcessManager=_processmanager)
            _inputhandler.show_exit_message_and_exit(config['login_failed_message'])
        # 登入CCMS scope-----end

        # Excel 處理


        # Proceess

    except Exception as ex:
        raise Exception(ex)
    finally:
        close_exe(InputHandler=_inputhandler, ProcessManager=_processmanager)
if __name__ == "__main__":
    msg_box = MessageBox()
    try:
        main()
    except Exception as e:
        error_message = f"發生錯誤: {e}"
        msg_box.show_info(title="錯誤訊息",message=error_message)
