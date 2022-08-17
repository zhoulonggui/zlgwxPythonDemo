# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/13 16:49
# file: bg_util.py
# IDE: PyCharm
# desc: 
# version: v1.0
import os

import wx


class BitMapUtil(object):

    @classmethod
    def draw_bg(cls, _deep_bg_color, _bg_color, _size, _round_val):
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
        _pos = int(_round_val / 2)
        gc.DrawRoundedRectangle(_pos, _pos, _size[0] - _round_val, _size[1] - _round_val, _round_val)
        return bit_map

    @classmethod
    def draw_text(cls, bit_map, _font, _image_path, _label, _size, _font_color):
        pdc = wx.MemoryDC(bit_map)
        if _font:
            pdc.SetFont(_font)
        # 图标
        icon = None
        if _image_path and os.path.exists(_image_path):
            icon = wx.Image(_image_path).ConvertToBitmap()
            icon_size = icon.GetSize()
            pdc.DrawBitmap(icon, icon_size[0], icon_size[1])
        # 文本
        text_size = pdc.GetTextExtent(_label)  # 文本范围
        # t_x 字体左上角原点x轴起始坐标 字体居中，如果有icon 扣除icon的宽度
        # t_y 字体左上角原点y轴起始坐标 字体居中，扣除字体本身高度
        t_x, t_y = int((_size[0] - text_size[0]) / 2), int((_size[1] - text_size[1]) / 2)
        if icon is not None:
            t_x, t_y = int((_size[0] - text_size[0]) / 2) - icon_size[0], icon_size[1] + 2 + t_y
        pdc.SetTextForeground(_font_color)
        pdc.DrawText(_label, t_x, t_y)
