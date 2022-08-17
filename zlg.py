# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/7 20:14
# file: zlg.py
# IDE: PyCharm
# desc: 
# version: v1.0

import sys
import time
import traceback

import wx

from comm.logger_util import ui_logger
from comm.reg_util import RegUtil
from comm.settings import SettingUtil


def start_project(_args):
    app = wx.App()
    t1 = time.time()
    ui_logger.info('start ui...')
    pro_name = SettingUtil.get_pro_name()
    try:
        RegUtil.winreg_right_menu()
    except Exception:
        # ui_logger.error(traceback.format_exc())
        pass
    from ui.page.mainwin.start_ui import StartUI
    _win = StartUI(title=pro_name, _args=_args)
    _win.Show(True)
    ui_logger.info(f'start ui {time.time() - t1}...')
    app.MainLoop()


if __name__ == '__main__':
    args = sys.argv
    ui_logger.info(f'args {args}')
    ui_logger.info('normal start')
    start_project(args)
