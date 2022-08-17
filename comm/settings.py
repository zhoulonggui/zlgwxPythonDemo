# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/7 20:55
# file: settings.py
# IDE: PyCharm
# desc: 
# version: v1.0
VERSION = 'v1.0'
PRO_NAME = 'ZLG'


class SettingUtil(object):

    @classmethod
    def get_ver(cls):
        return VERSION

    @classmethod
    def get_pro_name(cls):
        return PRO_NAME
