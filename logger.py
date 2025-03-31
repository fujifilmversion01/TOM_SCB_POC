import logging
from logging.handlers import TimedRotatingFileHandler


class Logger:
    def __init__(self, log_filename='app.log', log_level=logging.DEBUG, backup_count=7):
        # 创建一个 TimedRotatingFileHandler，用于日志轮转
        self.handler = TimedRotatingFileHandler(
            log_filename,  # 日志文件名
            when='midnight',  # 每天午夜轮转
            interval=1,  # 每隔1天轮转
            backupCount=backup_count  # 保留最近7个日志文件
        )

        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)

        # 创建 Logger 实例
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)  # 设置日志级别
        self.logger.addHandler(self.handler)  # 添加 Handler

    def get_logger(self):
        """返回 logger 实例"""
        return self.logger

# 如果需要在其他模块中使用日志功能：
# logger = Logger().get_logger()
