# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/7 23:17
# file: close_max_min.py
# IDE: PyCharm
# desc: 
# version: v1.0
from win32api import MonitorFromPoint, GetMonitorInfo
import wx

from comm.logger_util import ui_logger
from ui.components import color_comm
from ui.components.color_comm import ColorComm


class CloseMaxMinButton(wx.Panel):
    def __init__(self, parent, size=None):
        super(CloseMaxMinButton, self).__init__(parent, wx.ID_ANY, size=size)
        self.SetTransparent(200)
        self._parent = parent
        self._close_button = wx.Button(self, -1, label='X', size=(28, 28), style=wx.NO_BORDER)
        self._min_button = wx.Button(self, wx.ID_ANY, label='一', size=(28, 28), style=wx.NO_BORDER)
        self._max_button = wx.Button(self, wx.ID_ANY, label='口', size=(28, 28), style=wx.NO_BORDER)
        self._close_button.SetBackgroundColour(ColorComm.WHITE)
        self._min_button.SetBackgroundColour(ColorComm.WHITE)
        self._max_button.SetBackgroundColour(ColorComm.WHITE)
        _sizer = wx.BoxSizer(wx.HORIZONTAL)
        _sizer.Add(self._min_button, 0, wx.TOP, 2)
        _sizer.Add(self._max_button, 0, wx.TOP, 2)
        _sizer.Add(self._close_button, 0, wx.TOP, 2)
        self.SetSizer(_sizer)
        self._close_button.Bind(wx.EVT_BUTTON, self._on_close)
        self._close_button.Bind(wx.EVT_LEAVE_WINDOW, self._on_leave)
        self._close_button.Bind(wx.EVT_ENTER_WINDOW, self._on_enter)
        self._close_button.Bind(wx.EVT_SET_FOCUS, self._on_enter)
        self._min_button.Bind(wx.EVT_BUTTON, self._on_min)
        self._min_button.Bind(wx.EVT_LEAVE_WINDOW, self._on_leave)
        self._min_button.Bind(wx.EVT_ENTER_WINDOW, self._on_enter)
        self._max_button.Bind(wx.EVT_BUTTON, self._on_max)
        self._max_button.Bind(wx.EVT_LEAVE_WINDOW, self._on_leave)
        self._max_button.Bind(wx.EVT_ENTER_WINDOW, self._on_enter)
        self.Layout()

    def _on_close(self, event):
        ui_logger.info('close win')
        self._parent.Close()

    def _on_leave(self, event):
        _obj = event.GetEventObject()
        _obj.SetBackgroundColour(ColorComm.WHITE)

    def _on_enter(self, event):
        _obj = event.GetEventObject()
        _obj.SetBackgroundColour(ColorComm.ORANGE)

    def _on_max(self, event):
        ui_logger.info(f'max win')
        rtx = wx.Display.GetFromWindow(self)
        rect = wx.Display(rtx).GetGeometry()
        monitor_info = GetMonitorInfo(MonitorFromPoint((rect[0], rect[1])))
        work = monitor_info.get('Work')
        self._parent.SetSize((work[2] - work[0], work[3]))
        self._parent.SetWindowStyle(style=wx.SIMPLE_BORDER | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        self._parent.Layout()

    def _on_min(self, event):
        ui_logger.info(f'min win')
        self._parent.Iconize()
