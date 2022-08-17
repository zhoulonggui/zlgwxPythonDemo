# _*_coding:utf-8_*_
# author: zlg
# create time: 2022/8/14 23:06
# file: reg_util.py
# IDE: PyCharm
# desc: 
# version: v1.0
import os
import sys

import win32api, win32con
import winreg


class RegUtil(object):

    @classmethod
    def get_reg_key(cls):
        reg_root, reg_path, reg_flags = cls.get_root()
        try:
            _key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)  # 打开注册表
            # 参数1 主键
            # 参数2 子健路径
            # 参数4 权限
            # 若该键存在，即可以顺利打开。若不存在，则会报错
        except Exception as e:
            _key = None
        return _key

    @classmethod
    def get_reg_root(cls, reg_path):
        reg_root = win32con.HKEY_LOCAL_MACHINE  # 根节点
        # reg_path = r"SOFTWARE\Microsoft\.NETFramework\AssemblyFolders"  # 键的路径
        reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS  # 权限设置
        return reg_root, reg_path, reg_flags

    @classmethod
    def close_reg_key(cls, _key):
        win32api.RegCloseKey(_key)

    @classmethod
    def get_all_reg(cls, _key):
        result = []
        try:  # 遍历键值
            i = 0
            while True:  # 由于无法获取一个键下面有多少个值项。所以只能弄个循环处理
                result.append(win32api.RegEnumValue(_key, i))
                i += 1
        except Exception as e:
            pass
        return result

    @classmethod
    def delete_reg_value(cls, _key, _value):
        win32api.RegDeleteValue(_key, _value)

    @classmethod
    def delete_reg_key(cls, _key, reg_root, reg_path, reg_flags):
        reg_parent, subkey_name = os.path.split(reg_path)  # 获取其父键，通过父键删除子键
        key = win32api.RegOpenKeyEx(reg_root, reg_parent, 0, reg_flags)  # 打开父键
        win32api.RegDeleteKeyEx(key, subkey_name)  # 删除键
        # 参数1 父键句柄
        # 不需要先删除其中的值才删除键。直接删除键即可

    @classmethod
    def get_reg_key_value(cls, _key, _value):
        value, key_type = win32api.RegQueryValueEx(_key, _value)  # 直接获取某个值的数据
        return value, key_type

    @classmethod
    def set_reg_key_value(cls, _key, _value, _val):
        win32api.RegSetValueEx(_key, _value, 0, win32con.REG_SZ, _val)  # 给键赋值

    @classmethod
    def create_reg_key(cls, reg_path):
        import win32con, win32api
        reg_root = win32con.HKEY_LOCAL_MACHINE
        # reg_path = r"SOFTWARE\lm"
        reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
        key, _ = win32api.RegCreateKeyEx(reg_root, reg_path, reg_flags)  # 创建子健
        # 参数1 主键
        # 参数2 子健路径
        # 参数3 权限

    @classmethod
    def winreg_close_key(cls, _key):
        winreg.CloseKey(_key)

    @classmethod
    def winreg_add_key_value(cls, _key, _value, _val):
        winreg.SetValueEx(_key, _value, 0, winreg.REG_SZ, _val)  # 给键添加值或修改值

    @classmethod
    def winreg_get_key_value(cls, _key, _value):
        value = winreg.QueryValueEx(_key, _value)  # 获取当前名称对应的值
        return value

    @classmethod
    def winreg_right_menu(cls):
        project_file_name = sys.argv[0]
        file_name = os.path.basename(project_file_name)
        if file_name == 'zlg.py':
            command = f'"{sys.executable}" "{project_file_name}" "%1"'
            _key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Open ZLG\command")
            winreg.SetValue(_key, "", winreg.REG_SZ, command)
        elif file_name == 'zlg.exe':
            command = f'"{project_file_name}" "%1"'
            _key = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, r"*\shell\Open ZLG\command", reserved=0,
                                      access=winreg.KEY_WRITE | winreg.KEY_SET_VALUE)
            winreg.SetValue(_key, "", winreg.REG_SZ, command)
            icon_command = f'"{project_file_name}"'
            icon_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\Open ZLG")
            winreg.SetValueEx(icon_key, "Icon", 0, winreg.REG_SZ, icon_command)
