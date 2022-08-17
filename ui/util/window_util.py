# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/7 20:38
# file: window_util.py
# IDE: PyCharm
# desc: 
# version: v1.0
import win32api
from win32.lib import win32con
import win32gui
import win32print

from comm.logger_util import ui_logger


class WinUtil(object):

    @classmethod
    def get_screen_size(cls):
        # 获取缩放后的分辨率
        s_x = win32api.GetSystemMetrics(0)
        s_y = win32api.GetSystemMetrics(1)
        # 获取真实分辨率
        hdc = win32gui.GetDC(0)
        _w = win32print.GetDeviceCaps(hdc, win32con.DESKTOPHORZRES)
        _h = win32print.GetDeviceCaps(hdc, win32con.DESKTOPVERTRES)
        # 缩放比例
        screen_scale_rate = round(_w / s_x, 2)
        ui_logger.info(screen_scale_rate)
        return s_x * screen_scale_rate, (s_y - 60) * screen_scale_rate
