# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/13 14:25
# file: notebook.py
# IDE: PyCharm
# desc: 
# version: v1.0
import wx
import wx.lib.agw.flatnotebook as fnb

from ui.components.color_comm import ColorComm
from ui.components.event_cfg import MY_EVT_NOTEBOOK_CHANGE


class NoteBook(fnb.FlatNotebook):
    def __init__(self, parent, bg_color=None):
        fnb.FlatNotebook.__init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize,
                                  style=fnb.FNB_NODRAG | fnb.FNB_DCLICK_CLOSES_TABS | fnb.FNB_NAV_BUTTONS_WHEN_NEEDED)
        self.fixed_page = []
        self._parent = parent
        self.SetBackgroundColour(parent.GetBackgroundColour())
        self.SetActiveTabColour(ColorComm.WHITE_GRAY_BG)
        self.SetTabAreaColour(ColorComm.WHITE_BG)
        self.SetNonActiveTabTextColour(ColorComm.NORMAL_BLACK)
        self.SetBackgroundColour(bg_color or ColorComm.WHITE_BG)
        self.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CLOSING, self.on_page_close)
        self.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CHANGED, self.on_page_changed)

    def set_selection(self, page_idx):
        super().SetSelection(page_idx)

    def set_selection_by_name(self, page_name):
        for i in range(self.GetPageCount()):
            if page_name == self.GetPageText(i):
                self.set_selection(i)

    def add_fixed_page(self, page_name):
        if page_name not in self.fixed_page:
            self.fixed_page.append(page_name)

    def AddPage(self, page, page_name, is_select=True, image_id=-1):
        is_exist = False
        for i in range(self.GetPageCount()):
            if self.GetPageText(i) == page_name:
                if is_select:
                    self.set_selection(i)
                is_exist = True
                break
        if not is_exist:
            super().AddPage(page, page_name, select=is_select, imageId=image_id)
        else:
            del page
        self.Layout()
        self.Refresh()

    def remove_page(self, page_name):
        if page_name not in self.fixed_page:
            for i in range(self.GetPageCount()):
                if self.GetPageText(i) == page_name:
                    self.RemovePage(i)

    def get_page_index(self, page_name):
        for i in range(self.GetPageCount()):
            if self.GetPageText(i) == page_name:
                return i
        return -1

    def set_property(self, can_close=True, show_nav=False):
        _style = self.GetAGWWindowStyleFlag()
        if can_close:
            _style |= fnb.FNB_NO_X_BUTTON
        if show_nav:
            _style |= fnb.FNB_NO_NAV_BUTTONS
        self.SetAGWWindowStyleFlag(_style)

    def get_all_pages(self):
        pages = []
        for i in range(self.GetPageCount()):
            pages.append(self.GetPage(i))
        return pages

    def get_all_page_names(self):
        page_names = []
        for i in range(self.GetPageCount()):
            page_names.append(self.GetPageText(i))
        return page_names

    def on_page_close(self, event):
        _page = event.GetEventObject()
        page_name = self.GetPageText(self.GetSelection())
        if page_name in self.fixed_page:
            event.Veto()
            return

    def on_page_changed(self, event):
        client_event = wx.PyCommandEvent(MY_EVT_NOTEBOOK_CHANGE, self.GetId())
        client_event.SetEventObject(self)
        self.GetEventHandler().ProcessEvent(client_event)
