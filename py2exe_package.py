# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/14 16:20
# file: py2exe_package.py
# IDE: PyCharm
# desc: 
# version: v1.0
from distutils.core import setup
import py2exe
import sys

# 双击能够打开
sys.argv.append('py2exe')

py2exe_options = {
    "includes": ["wx"],  # 引入界面库，需要额外添加
    "dll_excludes": ["MSVCP90.dll"],  # 找不到dll时需要添加缺少的dll
    "compressed": 1,  # 默认为0,1为指定压缩文件（library.zip）的行为；0为不压缩。
    "optimize": 2,
    # 打包优化，合法值是字符串（'','O','OO'）或者整型数字 (0, 1, or 2)。0时，不进行优化，压缩包大小较大，打包的编译文件为 .pyc；1时，进行少量优化，压缩包大小略小，打包的编译文件为 .pyo；2时，优化级别最高，压缩包大小也明显变小，打包的编译文件为 .pyo
    "ascii": 1,  # 0：不包含编码和解释器
    "bundle_files": 3,
    # 打包绑定，64位不支持此属性。 0：pyd和dll文件不会被打包到exe文件中; 1：pyd和dll文件会被打包到exe文件中，且不能从文件系统中加载python模块; 2：pyd和dll文件会被打包到exe文件中，但是可以从文件系统中加载python模块
}
# setup(
#     windows=[
#         {"script": 'zlg.py', "icon_resources": [(1, "images/image_32x32.ico")], "uac_info": "requireAdministrator"}],
#     name='ZLG Demo',
#     version='1.0',
#     zipfile='lib/library.zip',
#     options={'py2exe': py2exe_options},
# )
setup(
    windows=[
        {"script": 'zlg.py', "icon_resources": [(1, "images/image_32x32.ico")]}],
    name='ZLG Demo',
    version='1.0',
    zipfile='lib/library.zip',
    options={'py2exe': py2exe_options},
)
