# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/13 16:29
# file: home_page.py
# IDE: PyCharm
# desc: 
# version: v1.0
import wx

from ui.components.color_comm import ColorComm
from ui.components.event_cfg import MY_EVT_LEFT_CLICK_BINDER
from ui.components.rounded_button import RoundedButton
from ui.components.rounded_panel import RoundedPanel


class HomePage(wx.Panel):
    def __init__(self, parent, bg_color=None):
        super(wx.Panel, self).__init__(parent, size=wx.DefaultSize)
        self.SetBackgroundColour(bg_color or parent.GetBackgroundColour())
        home_page = self
        _label = wx.StaticText(home_page, label='TestABC')
        _b1 = RoundedButton(home_page, '测试123', size=(80, 28))
        _b1.Bind(MY_EVT_LEFT_CLICK_BINDER, self.test_click)
        content_sizer = wx.BoxSizer(wx.VERTICAL)
        content_sizer.Add(_label, 0, wx.ALIGN_LEFT | wx.ALL, 20)
        content_sizer.Add(_b1, 0, wx.ALIGN_LEFT | wx.ALL, 20)
        home_page.SetSizer(content_sizer)

    def test_click(self, event):
        wx.MessageBox(f'Click...{event.GetEventObject().get_value()}')
