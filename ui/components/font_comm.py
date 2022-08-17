# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/7 22:13
# file: font_comm.py
# IDE: PyCharm
# desc: 
# version: v1.0
import wx


class FontComm(object):
    PPW = 96
    FONT_NORMAL_9 = wx.Font(9 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Microsoft YaHei UI')
    FONT_NORMAL_11 = wx.Font(11 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Microsoft YaHei UI')
    FONT_NORMAL_12 = wx.Font(12 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Microsoft YaHei UI')
    FONT_NORMAL_13 = wx.Font(13 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Microsoft YaHei UI')
    FONT_NORMAL_14 = wx.Font(14 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Microsoft YaHei UI')
    FONT_NORMAL_15 = wx.Font(15 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Microsoft YaHei UI')

    FONT_BOLD_9 = wx.Font(9 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.BOLD, False, 'Microsoft YaHei UI')
    FONT_BOLD_11 = wx.Font(11 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.BOLD, False, 'Microsoft YaHei UI')
    FONT_BOLD_12 = wx.Font(12 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.BOLD, False, 'Microsoft YaHei UI')
    FONT_BOLD_13 = wx.Font(13 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.BOLD, False, 'Microsoft YaHei UI')
    FONT_BOLD_14 = wx.Font(14 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.BOLD, False, 'Microsoft YaHei UI')
    FONT_BOLD_15 = wx.Font(15 * 72 / PPW, wx.DEFAULT, wx.NORMAL, wx.BOLD, False, 'Microsoft YaHei UI')
