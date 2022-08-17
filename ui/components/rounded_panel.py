# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/9 19:05
# file: rounded_panel.py
# IDE: PyCharm
# desc: 
# version: v1.0

import wx

from ui.components.color_comm import ColorComm


class RoundedPanel(wx.Panel):
    def __init__(self, parent, round_val=None, size=None, deep_bg_color=None, bg_color=None):
        super(RoundedPanel, self).__init__(parent, wx.ID_ANY, size=size or wx.DefaultSize)
        self.deep_bg_color = deep_bg_color or ColorComm.WHITE_GRAY_BG
        self.bg_color = bg_color or ColorComm.WHITE_BG
        self.bit_map = None
        self.round_val = round_val or 8
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.draw_panel)

    def draw_panel(self, event):
        dc = event.GetDC()
        if self.bit_map is not None and self.bit_map.GetSize() == dc.GetSize():
            dc.DrawBitmap(self.bit_map, 0, 0)
            return
        _size = self.GetSize()
        bit_map = wx.Bitmap(_size)
        pdc = wx.MemoryDC(bit_map)
        gcdc = wx.GCDC(pdc)
        # 获取到图形上下文
        gc = gcdc.GetGraphicsContext()
        # 画矩形区域
        gc.SetBrush(wx.Brush(self.deep_bg_color))
        gc.SetPen(wx.Pen(self.deep_bg_color, 1))
        gc.DrawRectangle(0, 0, _size[0], _size[1])
        # 画圆角区域
        gc.SetBrush(wx.Brush(self.bg_color))
        gc.SetPen(wx.Pen(self.bg_color, 1))
        _pos = int(self.round_val / 2)
        gc.DrawRoundedRectangle(_pos, _pos, _size[0] - self.round_val, _size[1] - self.round_val, self.round_val)
        # 将位图给当前画布
        dc.DrawBitmap(bit_map, 0, 0)
        self.bit_map = bit_map
        self.Refresh()
