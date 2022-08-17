# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/10 19:31
# file: rounded_button.py
# IDE: PyCharm
# desc: 
# version: v1.0
import os.path

import wx

from ui.components.color_comm import ColorComm
from ui.components.event_cfg import MY_EVT_LEFT_CLICK
from ui.components.font_comm import FontComm


class RoundedButton(wx.Panel):
    def __init__(self, parent, label, round_val=None, image_path=None, font=None, deep_bg_color=None, bg_color=None,
                 size=wx.DefaultSize):
        super(RoundedButton, self).__init__(parent, size=size, style=wx.NO_BORDER)
        self.SetTransparent(200)
        self.image_path = image_path
        self.deep_bg_color = deep_bg_color or parent.GetBackgroundColour()
        self.bg_color = bg_color or ColorComm.GLOBAL_BLUE
        self.label = label
        self.font = font or FontComm.FONT_NORMAL_11
        self.round_val = round_val or 4
        self.is_click = False
        self.button = wx.BitmapButton(self, wx.ID_ANY, style=wx.NO_BORDER, size=size)
        self.button.Bind(wx.EVT_BUTTON, self.on_click)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.on_enter)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave)
        self.cache_bt_map = {}
        self.init_button()
        self.re_draw('leave')
        self.Refresh()

    def init_button(self):
        self.cache_bt_map = {
            'leave': self.draw_button(self.deep_bg_color, self.bg_color, ColorComm.FONT_COLOR),
            'enter': self.draw_button(self.deep_bg_color, ColorComm.WHITE, ColorComm.FONT_COLOR)
        }

    def set_status(self, is_click=False):
        self.is_click = is_click
        if self.is_click:
            self.re_draw('enter')
        else:
            self.re_draw('leave')

    def re_draw(self, button_status='leave'):
        bit_map = self.cache_bt_map.get(button_status)
        self.button.SetBitmap(bit_map)
        self.Refresh()

    def on_click(self, event):
        self.re_draw('enter')
        client_event = wx.PyCommandEvent(MY_EVT_LEFT_CLICK, self.GetId())
        client_event.SetEventObject(self)
        self.GetEventHandler().ProcessEvent(client_event)

    def on_leave(self, event):
        self.re_draw('leave')

    def on_enter(self, event):
        self.re_draw('enter')

    def draw_bg(self, _deep_bg_color, _bg_color):
        _size = self.GetSize()
        bit_map = wx.Bitmap(_size)
        pdc = wx.MemoryDC(bit_map)
        gcdc = wx.GCDC(pdc)
        # 获取到图形上下文
        gc = gcdc.GetGraphicsContext()
        # 画矩形区域
        gc.SetBrush(wx.Brush(_deep_bg_color))
        gc.SetPen(wx.Pen(_deep_bg_color, 1))
        gc.DrawRectangle(0, 0, _size[0], _size[1])
        # 画圆角区域
        gc.SetBrush(wx.Brush(_bg_color))
        gc.SetPen(wx.Pen(_bg_color, 1))
        _pos = int(self.round_val / 2)
        gc.DrawRoundedRectangle(_pos, _pos, _size[0] - self.round_val, _size[1] - self.round_val, self.round_val)
        return bit_map

    def draw_button(self, _deep_bg_color, _bg_color, _font_color):
        _size = self.GetSize()
        bit_map = self.draw_bg(_deep_bg_color, _bg_color)
        pdc = wx.MemoryDC(bit_map)
        pdc.SetFont(self.font)
        # 图标
        icon = None
        if self.image_path and os.path.exists(self.image_path):
            icon = wx.Image(self.image_path).ConvertToBitmap()
            icon_size = icon.GetSize()
            pdc.DrawBitmap(icon, icon_size[0], icon_size[1])
        # 文本
        text_size = pdc.GetTextExtent(self.label)  # 文本范围
        # t_x 字体左上角原点x轴起始坐标 字体居中，如果有icon 扣除icon的宽度
        # t_y 字体左上角原点y轴起始坐标 字体居中，扣除字体本身高度
        t_x, t_y = int((_size[0] - text_size[0]) / 2), int((_size[1] - text_size[1]) / 2)
        if icon is not None:
            t_x, t_y = int((_size[0] - text_size[0]) / 2) - icon_size[0], icon_size[1] + 2 + t_y
        pdc.SetTextForeground(_font_color)
        pdc.DrawText(self.label, t_x, t_y)
        return bit_map

    def get_value(self):
        return self.label
