# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/13 16:40
# file: top_button.py
# IDE: PyCharm
# desc: 
# version: v1.0
import wx

from ui.components.bitmap_util import BitMapUtil
from ui.components.color_comm import ColorComm
from ui.components.event_cfg import MY_EVT_LEFT_CLICK
from ui.components.font_comm import FontComm


class TopMenuButton(wx.Panel):
    def __init__(self, parent, bg_color=None, deep_bg_color=None, label='', round_val=None, size=None, font=None,
                 need_hover=False):
        _size = size or (80, 28)
        super(TopMenuButton, self).__init__(parent, size=_size)
        self.round_val = round_val or 2
        self.need_hover = need_hover
        self.clicked_status = False
        self.font = font or FontComm.FONT_NORMAL_11
        self.label = label
        self.deep_bg_color = deep_bg_color or parent.GetBackgroundColour()
        self.bg_color = bg_color or parent.GetBackgroundColour()
        self.SetBackgroundColour(self.deep_bg_color)
        self.button = wx.BitmapButton(self, wx.ID_ANY, style=wx.NO_BORDER, size=size)
        self.button.Bind(wx.EVT_BUTTON, self.on_click)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.on_enter)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave)
        self.cache_bt_map = {}
        self.init_button()
        self.re_draw('leave')

    def get_value(self):
        return self.label

    def init_button(self):
        self.cache_bt_map = {
            'leave': self.draw_button(self.deep_bg_color, self.bg_color, ColorComm.FONT_COLOR),
            'enter': self.draw_button(self.deep_bg_color, ColorComm.LITTLE_BLUE, ColorComm.FONT_COLOR)
        }

    def draw_button(self, _deep_bg_color, _bg_color, _font_color):
        bit_map = BitMapUtil.draw_bg(_deep_bg_color, _bg_color, self.GetSize(), self.round_val)
        BitMapUtil.draw_text(bit_map, self.font, '', self.label, self.GetSize(), _font_color)
        return bit_map

    def on_click(self, evnet):
        self.re_draw('enter')
        self.clicked_status = True
        client_event = wx.PyCommandEvent(MY_EVT_LEFT_CLICK, self.GetId())
        client_event.SetEventObject(self)
        self.GetEventHandler().ProcessEvent(client_event)

    def on_leave(self, event):
        if self.need_hover and self.clicked_status:
            return
        self.re_draw('leave')

    def set_click_status(self, click_status=False):
        self.clicked_status = click_status
        if self.clicked_status:
            self.re_draw('enter')
        else:
            self.re_draw('leave')

    def on_enter(self, event):
        self.re_draw('enter')

    def re_draw(self, button_status):
        bit_map = self.cache_bt_map.get(button_status)
        self.button.SetBitmap(bit_map)
        self.Refresh()
