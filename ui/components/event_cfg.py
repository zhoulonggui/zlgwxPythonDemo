# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/10 19:46
# file: event_cfg.py
# IDE: PyCharm
# desc: 
# version: v1.0
import wx

# 按钮点击事件
MY_EVT_LEFT_CLICK = wx.NewEventType()
MY_EVT_LEFT_CLICK_BINDER = wx.PyEventBinder(MY_EVT_LEFT_CLICK, 1)

# notebook change事件
MY_EVT_NOTEBOOK_CHANGE = wx.NewEventType()
MY_EVT_NOTEBOOK_CHANGE_BINDER = wx.PyEventBinder(MY_EVT_NOTEBOOK_CHANGE, 1)
