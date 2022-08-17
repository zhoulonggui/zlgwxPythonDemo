# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/7 23:17
# file: close_max_min.py
# IDE: PyCharm
# desc: 
# version: v1.0
import win32api
from win32api import MonitorFromPoint
import wx

from comm.logger_util import ui_logger
from ui.components import color_comm
from ui.components.color_comm import ColorComm


class CloseMaxMinButton(wx.Panel):
    def __init__(self, parent, p_win, size=None):
        super(CloseMaxMinButton, self).__init__(parent, wx.ID_ANY, size=size)
        self.SetTransparent(200)
        self.old_size = p_win.GetSize()
        self.is_max = False
        self._parent = p_win
        _close_button = wx.Button(self, -1, label='X', size=(28, 28), style=wx.NO_BORDER)
        _min_button = wx.Button(self, wx.ID_ANY, label='一', size=(28, 28), style=wx.NO_BORDER)
        _max_button = wx.Button(self, wx.ID_ANY, label='口', size=(28, 28), style=wx.NO_BORDER)
        _close_button.SetBackgroundColour(ColorComm.WHITE)
        _min_button.SetBackgroundColour(ColorComm.WHITE)
        _max_button.SetBackgroundColour(ColorComm.WHITE)
        _sizer = wx.BoxSizer(wx.HORIZONTAL)
        _sizer.Add(_min_button, 0, wx.TOP, 2)
        _sizer.Add(_max_button, 0, wx.TOP, 2)
        _sizer.Add(_close_button, 0, wx.TOP, 2)
        self.SetSizer(_sizer)
        _close_button.Bind(wx.EVT_BUTTON, self._on_close)
        _close_button.Bind(wx.EVT_LEAVE_WINDOW, self._on_leave)
        _close_button.Bind(wx.EVT_ENTER_WINDOW, self._on_enter)
        _close_button.Bind(wx.EVT_SET_FOCUS, self._on_enter)
        _min_button.Bind(wx.EVT_BUTTON, self._on_min)
        _min_button.Bind(wx.EVT_LEAVE_WINDOW, self._on_leave)
        _min_button.Bind(wx.EVT_ENTER_WINDOW, self._on_enter)
        _max_button.Bind(wx.EVT_BUTTON, self._on_max)
        _max_button.Bind(wx.EVT_LEAVE_WINDOW, self._on_leave)
        _max_button.Bind(wx.EVT_ENTER_WINDOW, self._on_enter)
        self.Layout()

    def _on_close(self, event):
        ui_logger.info('close win')
        self._parent.Close()
        self._parent.Destroy()

    def _on_leave(self, event):
        _obj = event.GetEventObject()
        _obj.SetBackgroundColour(ColorComm.WHITE)

    def _on_enter(self, event):
        _obj = event.GetEventObject()
        _obj.SetBackgroundColour(ColorComm.ORANGE)

    def _on_max(self, event):
        ui_logger.info(f'max win')
        self.old_size = self._parent.GetSize()
        ui_logger.info(self.old_size)
        # _win_idx = wx.Display.GetFromWindow(self)
        # _rect = wx.Display(_win_idx).GetGeometry()
        # _monitor = win32api.GetMonitorInfo(MonitorFromPoint((0, 0)))
        # ui_logger.info(_monitor)
        if not self.is_max:
            self.is_max = True
            if not self._parent.IsShown():
                self._parent.Show()
            self._parent.Raise()
            self._parent.Maximize(True)
        else:
            self.is_max = False
            self._parent.SetSize(self.old_size)
            self._parent.Raise()
            self._parent.Maximize(False)

    def _on_min(self, event):
        ui_logger.info(f'min win')
        self.old_size = self.GetSize()
        self._parent.Iconize(True)
