from common.messagebox import MessageBox
from excelprocess import ExcelProcessor
from init import load_config
from init import load_input_excel
from login_ccms import LoginCCMSService
from common.execute_process import ProcessManager
from common.InputHandler import InputHandler
from common.CCMSShortcut import CCMSShortcut
from excelprocess import ExcelProcessor
from businessprocessmanager import BusinessProcessManager
from logger import Logger
def main_close_exe(InputHandler,ProcessManager,exit_message):
    if ProcessManager.process:
        is_close_success, close_exe_error_message = ProcessManager.close_exe()
        if not is_close_success:
            InputHandler.msg_box(close_exe_error_message)
    InputHandler.show_exit_message_and_exit(exit_message)
def main():
    # 初始化
    config = load_config()
    _logger = Logger().get_logger()
    _logger.info("RPA執行完成")
    input_excel=load_input_excel(config['input_excel_path'])
    _inputhandler=InputHandler()
    _ccms_shortcut=CCMSShortcut(config=config)
    _processmanager=ProcessManager(config=config)

    # 開啟CCMS-----start
    _logger.info("開啟CCMS-----start")
    is_exec_success,open_exe_error_message=_processmanager.open_exe(config["ccms_path"])
    if not is_exec_success:
        error_message=f"開啟CCMS時發生錯誤: {open_exe_error_message}"
        _logger.error(error_message)
        raise Exception(error_message)
    # 開啟CCMS-----end
    _logger.info("開啟CCMS-----end")
    try:
        # 登入CCMS scope-----start
        _logger.info("# 登入CCMS scope-----start")
        _login_ccms_service = LoginCCMSService(config=config, inputhandler=_inputhandler, ccms_shortcut=_ccms_shortcut)
        if _login_ccms_service.login_process() is False:
          _logger.error("# 登入CCMS失敗")
          return  main_close_exe(InputHandler=_inputhandler, ProcessManager=_processmanager,exit_message=config['login_failed_message'])
        # 登入CCMS scope-----end
        _logger.info("# 登入CCMS scope-----end")
        # Excel 處理
        _excelprocessor = ExcelProcessor(config=config, input_excel_data=input_excel)
        valid, _excelprocessor_get_valid_data_error_messages = _excelprocessor.validate_data()
        if not valid:
           _logger.error("# Excel整理失敗")
           return main_close_exe(InputHandler=_inputhandler, ProcessManager=_processmanager,exit_message=_excelprocessor_get_valid_data_error_messages)

        # Proceess
        _logger.info("IPL_MIN_ADJ流程開始")
        _businessprocessmanager=BusinessProcessManager( ExcelProcessor=_excelprocessor,ccmsshortcut=_ccms_shortcut,Logger=_logger)
        _businessprocessmanager.ipl_min_adj_process()
        _logger.info("IPL_MIN_ADJ流程結束")
        #結束
        _logger.info("RPA執行完成")
        main_close_exe(InputHandler=_inputhandler, ProcessManager=_processmanager, exit_message="RPA執行完成")
    except Exception as ex:
        main_close_exe(InputHandler=_inputhandler, ProcessManager=_processmanager,exit_message=ex)
if __name__ == "__main__":
    msg_box = MessageBox()
    try:
        main()
    except Exception as e:
        error_message = f"發生錯誤: {e}"
        msg_box.show_info(title="錯誤訊息",message=error_message)
