# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 2:24
# @Author  : MaxLong
# @Project : codenumbers
# @FileName: main.py
# @Software: PyCharm
# @Contact : MaxLongGlobal

import os


# -*- function -*-
def run_pyinstaller(cmd):
    """
    run pyinstaller to get .exe file
    :param cmd:
    :return:
    """
    # cmd = "pyinstaller -F -w -i my_icon.ico --add-data='xxxx.gif;.' gift.py"
    op = os.popen(cmd=cmd, mode='r')
    print(op.read())


# -*- main -*-
if __name__ == '__main__':
    cmd = "pyinstaller -F -w -i OneDrive.ico codelines.py"
    run_pyinstaller(cmd)
