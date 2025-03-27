import yaml
import pandas as pd
def load_config(config_path="config.yaml"):
    """讀取並返回配置資料"""
    with open(config_path, "r") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config
def load_input_excel(input_excel_path):
    # 1️⃣ 用 pandas 讀取 Excel（只讀取數據，不影響公式）
    df = pd.read_excel(input_excel_path, sheet_name=0)
    return df