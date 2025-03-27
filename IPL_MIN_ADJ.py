from logging import exception
from common.messagebox import MessageBox
from init import load_config
from init import load_input_excel
from login_ccms import LoginCCMSService
from common.execute_process import open_exe
from common.InputHandler import InputHandler
from common.CCMSShortcut import CCMSShortcut
def main():
    # 初始化
    config = load_config()
    input_excel=load_input_excel(config['input_excel_path'])
    _inputhandler=InputHandler()
    _ccms_shortcut=CCMSShortcut(config=config)

    # 登入 scope-----start
    open_exe(config["ccms_path"])#開啟CCMS
    _login_ccms_service=LoginCCMSService(config=config,inputhandler=_inputhandler,ccms_shortcut=_ccms_shortcut)
    _login_ccms_service.login_process()
    #login_process(config=config,inputhandler=_inputhandler,ccms_shortcut=_ccms_shortcut)#登入CCMS
    # 登入 scope-----end


if __name__ == "__main__":
    msg_box=MessageBox()
    try:
        main()
    except exception as e:
        error_message = f"發生錯誤: {e}"
        msg_box.show_info(title="錯誤訊息",message=error_message)
