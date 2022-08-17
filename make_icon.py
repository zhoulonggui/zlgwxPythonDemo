# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/14 18:49
# file: make_icon.py
# IDE: PyCharm
# desc: 
# version: v1.0

import PythonMagick

img = PythonMagick.Image('images/icon.png')
img.sample('16x16')
img.write('images/image_16x16.ico')

img.sample('32x32')
img.write('images/image_32x32.ico')

img.sample('48x48')
img.write('images/image_48x48.ico')

img.sample('248x248')
img.write('images/image_248x248.ico')
