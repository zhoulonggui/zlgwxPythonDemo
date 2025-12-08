# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/7 20:36
# file: start_ui.py
# IDE: PyCharm
# desc: 
# version: v1.0
import wx

from comm.settings import SettingUtil
# from ui.components.font_comm import FONT_BOLD_15
from ui.components.close_max_min import CloseMaxMinButton
from ui.components.color_comm import ColorComm
from ui.components.event_cfg import MY_EVT_LEFT_CLICK_BINDER
from ui.components.font_comm import FontComm
from ui.components.menu_button import TopMenuButton
from ui.components.my_notebook import NoteBook
from ui.page.mainwin.demo_page import DemoPage
from ui.page.mainwin.home_page import HomePage
from ui.util.window_util import WinUtil
from comm.logger_util import ui_logger


class StartUI(wx.Frame):
    def __init__(self, title='ABC', _args=None):
        _size, _pos = WinUtil.get_screen_size()
        # style=0 去掉顶部菜单栏 工具栏 自定义实现 style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER
        super(StartUI, self).__init__(None, wx.ID_ANY, title=title, size=_size, pos=_pos if _pos else (100, 100),
                                      style=0)
        self.page_cache = {}
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.old_size = _size
        self.is_max = False
        _top = self.init_top()
        self.content_book = self.init_content()
        _bottom = self.init_bottom()
        main_sizer.Add(_top, 0, wx.EXPAND)
        main_sizer.Add(self.content_book, 1, wx.EXPAND)
        main_sizer.Add(_bottom, 0, wx.EXPAND)
        self.SetSizer(main_sizer)
        self.Refresh()
        self.Layout()
        _top.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_down)
        _top.Bind(wx.EVT_LEFT_UP, self.on_mouse_up)
        _top.Bind(wx.EVT_MOTION, self.on_mouse_motion)
        self.dragging = False
        self.offset = wx.Point()

    def on_mouse_down(self, event):
        self.dragging = True
        self.offset = event.GetPosition()

    def on_mouse_up(self, event):
        self.dragging = False

    def on_mouse_motion(self, event):
        if not self.dragging:
            return
        if event.Dragging() and event.LeftIsDown():
            # 计算新的位置
            x, y = self.ClientToScreen(event.GetPosition())
            x -= self.offset.x
            y -= self.offset.y
            # 调整偏移量以匹配窗口的实际移动，这里-10和-30是示例偏移，根据需要调整
            # self.Move(x - 10, y - 30)
            self.Move(x, y)
            # 刷新窗口以显示新的位置
            # self.Refresh()

    def init_top(self):
        top_panel = wx.Panel(self, wx.ID_ANY, size=(-1, 42))
        top_panel.SetBackgroundColour(ColorComm.WHITE)
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        icon = wx.StaticBitmap(top_panel, wx.ID_ANY, wx.Image('images/icon.png').ConvertToBitmap())
        # icon.SetBackgroundColour(ColorComm.BLUE_PURPLE)
        top_sizer.Add(icon, 0, wx.CENTER | wx.LEFT, 5)

        top_left_panel = wx.Panel(top_panel, wx.ID_ANY)
        _app_name = SettingUtil.get_pro_name()
        _app_name_static = wx.StaticText(top_left_panel, label=_app_name)
        _app_name_static.SetFont(FontComm.FONT_BOLD_13)
        top_sizer.Add(top_left_panel, 0, wx.CENTER | wx.LEFT, 5)

        menu_lst = ['样例', '设置', '帮助']
        for menu_name in menu_lst:
            menu_btn = TopMenuButton(top_panel, size=(55, 28), label=menu_name, font=FontComm.FONT_NORMAL_14)
            menu_btn.Bind(MY_EVT_LEFT_CLICK_BINDER, self.on_top_menu_click)
            top_sizer.Add(menu_btn, 0, wx.CENTER | wx.LEFT, 5)

        close_max_min_btn = CloseMaxMinButton(top_panel, p_win=self, size=(84, 32))

        top_sizer.Add((-1, -1), 1)
        top_sizer.Add(close_max_min_btn, 0, wx.CENTER | wx.RIGHT, 5)
        top_panel.SetSizer(top_sizer)
        return top_panel

    def on_top_menu_click(self, event):
        btn_obj = event.GetEventObject()
        page_name = btn_obj.get_value()
        if page_name in self.page_cache and self.content_book.get_page_index(page_name) != -1:
            self.content_book.set_selection_by_name(page_name)
            return
        if page_name == '样例':
            demo_page = DemoPage(self.content_book)
            self.add_page(demo_page, page_name)
        elif page_name == '设置':
            self.add_page(wx.Panel(self.content_book, size=self.GetSize()), page_name)
        elif page_name == '帮助':
            self.add_page(wx.Panel(self.content_book, size=self.GetSize()), page_name)

    def add_page(self, page_win, page_name):
        if page_name in self.page_cache and self.content_book.get_page_index(page_name) != -1:
            # 删除没有效果
            del page_win
            return
        self.page_cache[page_name] = page_win
        self.content_book.AddPage(page_win, page_name)
        self.Layout()
        self.Refresh()

    def init_content(self):
        content_book = NoteBook(self)
        # 默认添加首页
        home_page = HomePage(content_book)
        content_book.AddPage(home_page, '首页')
        content_book.add_fixed_page('首页')
        return content_book

    def init_bottom(self):
        bottom_panel = wx.Panel(self, wx.ID_ANY, size=(-1, 32))
        bottom_panel.SetBackgroundColour(ColorComm.WHITE)
        _version = wx.StaticText(bottom_panel, label=SettingUtil.get_pro_name() + SettingUtil.get_ver())
        _version.SetFont(FontComm.FONT_NORMAL_11)
        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bottom_sizer.Add(_version, 0, wx.CENTER | wx.LEFT, 5)
        bottom_panel.SetSizer(bottom_sizer)
        return bottom_panel
