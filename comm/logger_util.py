# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/7 21:07
# file: logger_util.py
# IDE: PyCharm
# desc: 
# version: v1.0
import logging

ui_logger = logging.getLogger(__file__)
ui_logger.setLevel(logging.DEBUG)
# 建立一个filehandler来把日志记录在文件里，级别为debug以上
fh = logging.FileHandler("log/access.log")
fh.setLevel(logging.DEBUG)
# 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# 设置日志格式
formatter = logging.Formatter('[%(asctime)s][%(module)s.%(funcName)s %(lineno)d] %(levelname)s:%(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# 将相应的handler添加在logger对象中
ui_logger.addHandler(ch)
ui_logger.addHandler(fh)
