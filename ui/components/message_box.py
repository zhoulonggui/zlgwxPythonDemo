# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/23 13:06
# file: message_box.py
# IDE: PyCharm
# desc: 
# version: v1.0
import wx
import wx.richtext as rt

from comm.logger_util import ui_logger
from ui.components.close_max_min import CloseMaxMinButton
from ui.components.color_comm import ColorComm
from ui.components.event_cfg import MY_EVT_LEFT_CLICK_BINDER
from ui.components.rounded_button import RoundedButton


class MessageBox(wx.Dialog):
    def __init__(self, title=u'提示', message=u'提示信息', btn_lst=[u'确定', u'取消'], size=wx.DefaultSize):
        app = wx.GetApp()
        frame = app.GetTopWindow()
        wx.Dialog.__init__(self, frame, -1, size=size, style=wx.FRAME_SHAPED | wx.NO_BORDER | wx.FRAME_NO_TASKBAR)
        self.SetSize(frame.GetSize())
        self.SetPosition(frame.GetPosition())
        self.SetTransparent(255 * 0.3)
        self.SetBackgroundColour(wx.RED)
        self.select = None
        self.Show()
        dlg = ZScrollDialog(self, title, message, btn_lst)
        # dlg.Show()
        # if dlg.ShowModal() == wx.ID_OK:
        #     self.select = dlg.select
        #     dlg.Destroy()
        #     self.Destroy()
        # else:
        #     try:
        #         self.Destroy()
        #     except Exception:
        #         pass
        dlg.ShowWindowModal()
        self.select = dlg.select
        ui_logger.info(f'MessageBox.select {self.select}')
        dlg.Destroy()
        self.Destroy()


class ZScrollDialog(wx.Dialog):
    def __init__(self, parent, title, message, btn_lst):
        wx.Dialog.__init__(self, parent, -1, size=(420, 300),
                           style=wx.FRAME_SHAPED | wx.NO_BORDER | wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP)
        self.Centre(wx.BOTH)
        self.parent = parent
        self.title = title
        self.message = message
        self.btn_lst = btn_lst
        self.delta = (0, 0)
        self.select = None
        self.set_shape()
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_MOTION, self.on_motion)
        self.load_page()
        # self.Show()

    def load_page(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        top_text = wx.StaticText(self, id=wx.ID_ANY, label=self.title, size=(self.GetSize()[0] - 45, 32))
        right_btn = CloseMaxMinButton(self, size=(40, 32))
        right_btn._min_button.Hide()
        right_btn._max_button.Hide()
        top_sizer.Add(top_text, 0, wx.LEFT | wx.CENTER, 5)
        # top_sizer.Add((-1, -1), 1)
        top_sizer.Add(right_btn, 0)
        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        content_text = self.create_message()
        for btn_name in self.btn_lst:
            _button = RoundedButton(self, label=btn_name, size=(50, 28))
            _button.Bind(MY_EVT_LEFT_CLICK_BINDER, self.on_btn_click)
            bottom_sizer.Add(_button, 0, wx.ALL, 10)
        main_sizer.Add(top_sizer, 0, wx.CENTER)
        main_sizer.Add(content_text, 1, wx.EXPAND)
        main_sizer.Add(bottom_sizer, 0, wx.CENTER)
        self.SetSizer(main_sizer)

    def create_message(self):
        ct = rt.RichTextCtrl(self, style=wx.NO_BORDER | wx.TE_NO_VSCROLL | wx.TE_READONLY | wx.TE_AUTO_URL)
        ct.Freeze()
        ct.BeginSuppressUndo()

        ct.BeginParagraphSpacing(0, 20)
        ct.BeginAlignment(wx.TEXT_ALIGNMENT_CENTRE)
        ct.BeginFontSize(11)
        ct.WriteText(self.message)
        ct.EndFontSize()

        ct.EndSuppressUndo()
        ct.Thaw()
        return ct

    def on_btn_click(self, event):
        btn_name = event.GetEventObject().get_value()
        self.select = btn_name
        self.EndModal(wx.ID_OK)

    def on_left_down(self, event):
        x, y = self.ClientToScreen(event.GetPosition())
        ox, oy = self.GetPosition()
        self.delta = (x - ox, y - oy)

    def on_motion(self, event):
        if event.Dragging() and event.LeftIsDown() and self.delta != (0, 0):
            x, y = self.ClientToScreen(event.GetPosition())
            fp = (x - self.delta[0], y - self.delta[1])
            self.Move(fp)

    def set_shape(self):
        w, h = self.GetSize()
        bmp = wx.Bitmap(w, h)
        dc = wx.BufferedDC(None, bmp)
        dc.SetBackground(wx.Brush(ColorComm.GLOBAL_BG))
        dc.Clear()
        dc.DrawRoundedRectangle(0, 0, w - 1, w - 1, 4)
        self.SetShape(wx.Region(bmp, wx.GREEN))
