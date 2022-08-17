# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/13 16:24
# file: demo_page.py
# IDE: PyCharm
# desc: 
# version: v1.0

import wx

from ui.components.color_comm import ColorComm
from ui.components.event_cfg import MY_EVT_LEFT_CLICK_BINDER
from ui.components.font_comm import FontComm
from ui.components.menu_button import TopMenuButton
from ui.components.rounded_panel import RoundedPanel


class DemoPage(wx.Panel):
    def __init__(self, parent, bg_color=None, size=None):
        super(wx.Panel, self).__init__(parent)
        self.SetBackgroundColour(bg_color or ColorComm.WHITE_BG)
        self.SetSize(size or parent.GetSize())
        self.left_menu_cache = {}
        self.right_pages = {}

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.left_menu = self.load_left_menu()
        self.right_content = wx.Panel(self, id=wx.ID_ANY)
        self.right_content_sizer = wx.BoxSizer(wx.VERTICAL)
        self.load_right_content()
        self.right_content.SetSizer(self.right_content_sizer)

        sizer.Add(self.left_menu, 0, wx.RIGHT | wx.EXPAND, 10)
        sizer.Add(self.right_content, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Layout()

    def load_left_menu(self):
        left_menu_panel = wx.Panel(self, id=wx.ID_ANY, size=(180, -1))
        left_menu_panel.SetBackgroundColour(ColorComm.GLOBAL_DEEP_BG)
        menu_sizer = wx.BoxSizer(wx.VERTICAL)
        menu_lst = ['颜色面板', '按钮组件', '弹窗组件', '文本组件', '面板组件']
        for menu_name in menu_lst:
            _button = TopMenuButton(left_menu_panel, bg_color=ColorComm.WHITE_BLUE_BG,
                                    deep_bg_color=ColorComm.GLOBAL_DEEP_BG, label=menu_name, round_val=4,
                                    size=(160, 60), font=FontComm.FONT_BOLD_15, need_hover=True)
            self.left_menu_cache[menu_name] = _button
            _button.Bind(MY_EVT_LEFT_CLICK_BINDER, self.on_menu_click)
            menu_sizer.Add(_button, 0, wx.ALL, 5)
        menu_sizer.Add((-1, -1), 1)
        left_menu_panel.SetSizer(menu_sizer)
        return left_menu_panel

    def on_menu_click(self, event):
        btn = event.GetEventObject()
        btn_name = btn.get_value()
        for menu_name, _page in self.right_pages.items():
            if menu_name == btn_name:
                self.right_content_sizer.Show(_page)
                self.left_menu_cache.get(menu_name).set_click_status(True)
            else:
                self.right_content_sizer.Hide(_page)
                self.left_menu_cache.get(menu_name).set_click_status(False)

    def load_right_content(self):
        self.right_pages = {
            '颜色面板': self.load_color_panel(),
            '按钮组件': RoundedPanel(self.right_content, round_val=100, bg_color=ColorComm.LITTLE_BLUE,
                                     size=(500, 500)),
            '弹窗组件': RoundedPanel(self.right_content, round_val=200, bg_color=ColorComm.LITTLE_ORANGE,
                                     size=(500, 500)),
            '文本组件': RoundedPanel(self.right_content, round_val=300, bg_color=ColorComm.LITTLE_PURPLE,
                                     size=(500, 500)),
            '面板组件': RoundedPanel(self.right_content, round_val=400, bg_color=ColorComm.LIGHT_GREEN, size=(500, 500))
        }
        idx = 0
        for menu_name, _page in self.right_pages.items():
            self.right_content_sizer.Add(_page, 0, wx.EXPAND)
            if idx == 0:
                self.right_content_sizer.Show(_page)
            else:
                self.right_content_sizer.Hide(_page)
            idx += 1

    def load_color_panel(self):
        color_panel = RoundedPanel(self.right_content, round_val=2)
        color_sizer = wx.BoxSizer(wx.VERTICAL)
        name_sizer = wx.BoxSizer(wx.HORIZONTAL)
        show_color_sizer = wx.BoxSizer(wx.HORIZONTAL)
        all_colors_key = [i for i in ColorComm.__dict__ if '__' not in i]
        idx = 0
        for _idx, _key in enumerate(all_colors_key):
            idx += 1
            _color = wx.Panel(color_panel, size=(150, 32), style=wx.BORDER_SIMPLE)
            _color.SetBackgroundColour(getattr(ColorComm, _key))
            _name = wx.StaticText(color_panel, label=f'{_key}\n{getattr(ColorComm, _key)}', size=(150, 32))
            _name.SetBackgroundColour(ColorComm.WHITE)
            show_color_sizer.Add(_color, 0, wx.RIGHT | wx.LEFT, 10)
            name_sizer.Add(_name, 0, wx.RIGHT | wx.LEFT, 10)
            # 每行显示五个
            if idx == 5:
                color_sizer.Add(show_color_sizer, 0)
                color_sizer.Add(name_sizer, 0, wx.BOTTOM, 10)
                show_color_sizer = wx.BoxSizer(wx.HORIZONTAL)
                name_sizer = wx.BoxSizer(wx.HORIZONTAL)
                idx = 0
            if _idx == len(all_colors_key) - 1:
                color_sizer.Add(show_color_sizer, 0)
                color_sizer.Add(name_sizer, 0, wx.BOTTOM, 10)

        color_panel.SetSizer(color_sizer)
        return color_panel
