from logging import exception
import re

class BusinessProcessManager:
    def __init__(self,ExcelProcessor,ccmsshortcut,config,Logger):
        self.ExcelProcessor=ExcelProcessor
        self.ccmsshortcut=ccmsshortcut
        self.config=config
        self.logger=Logger
    def ipl_min_adj_process(self):
        modified_excel_data=self.ExcelProcessor.get_valid_data()
        excel_card_number_column_name=self.config['excel_card_number_column_name']#卡號
        for index, row in self.modified_excel_data.iterrows():
            self.ccmsshortcut.goto_homepage()#一律先回首頁
            try:
                self.logger.info(f"卡號{row[excel_card_number_column_name]}開始執行")
                #進去PCIH
                self.ccmsshortcut.goto_page("PCIH")
                if not self.ccmsshortcut.check_page_in_specify_page("PCIH("):
                    self.logger.error("目前頁面不為PCIH")
                    continue
                self.ccmsshortcut.press_tab()
                self.ccmsshortcut.press_tab()
                self.ccmsshortcut.typeinto_string(row[excel_card_number_column_name])
                self.ccmsshortcut.press_enter()

                #抓取PMT-TYPE
                PCIH_current_page_text=self.ccmsshortcut.get_current_page_text().replace(",","").replace(".","")
                match_result=re.search('PAYMENTTYPE[\d\,\.]+',PCIH_current_page_text)
                if match_result:
                     modified_excel_data.loc[index, "PMT-TYPE"] = match_result.group(1)
                else:
                    self.logger.error("PMT-TYPE找不到匹配的資料")
                    continue

                #NEW-BAL # TOT-AMT-DUE
                self.ccmsshortcut.goto_page("PCSD")
                #最左邊打X 總共用三個選項直接最左邊三次
                self.ccmsshortcut.press_left()
                self.ccmsshortcut.press_left()
                self.ccmsshortcut.press_left()
                self.ccmsshortcut.typeinto_string("X")
                self.ccmsshortcut.press_enter()
                PCSD_current_page_text = self.ccmsshortcut.get_current_page_text(replace_white_space=False)
                PCSD_current_page_text=PCSD_current_page_text.split("PREV-BAL")(1)
                PCSD_current_page_text=PCSD_current_page_text.split("C POST")(0)
                int_NEW_BAL = int(PCSD_current_page_text.split("NEW-BAL")(0))
                if int_NEW_BAL < 0:
                    int_NEW_BAL = 0
                int_TOT_AMT_DUE = int(PCSD_current_page_text.split("TOT-AMT_DUE")(1))
                if int_TOT_AMT_DUE < 0:
                    int_TOT_AMT_DUE = 0
                modified_excel_data.loc[index, "PMT-TYPE"] = int_NEW_BAL
                modified_excel_data.loc[index, "TOT-AMT-DUE"] = int_TOT_AMT_DUE

                #PAYMENTS
                self.ccmsshortcut.goto_page("PCIQ")
                PCIQ_current_page_text = self.ccmsshortcut.get_current_page_text().replace(",","").replace(".","")
                match_result = re.search('PAYMENTS[\d\,\.]+', PCIQ_current_page_text)
                if match_result:
                    int_PAYMENTS = int(match_result.group(1))
                    if int_PAYMENTS < 0:
                        int_PAYMENTS = 0
                    modified_excel_data.loc[index, "PAYMENTS"] = int_PAYMENTS
                else:
                    self.logger.error("PAYMENTS找不到匹配的資料")
                    continue
                self.logger.info(f"卡號{row[excel_card_number_column_name]}執行結束")
            except Exception as e:
                self.logger.error(f"發生錯誤{e},跳下一筆")
                continue
        self.ExcelProcessor.saveas_result(org_file_path=self.config['input_excel_path'],new_file_path=self.config['output_excel_path'],modified_dataframe=modified_excel_data)
