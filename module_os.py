# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from enum import Enum


def __get_platform():
    if sys.platform == __EnumPlatform.linux:
        try:
            proc_version = open('/proc/version').read()
            if 'Microsoft' in proc_version:
                return __EnumPlatform.wsl
        except:
            pass
    return __EnumPlatform[sys.platform]


def open_with_default_app(filename):
    platform = __get_platform()
    if platform == __EnumPlatform.win32 or platform == __EnumPlatform.win64:
        os.startfile(filename.replace('/', '\\'))
    elif platform == __EnumPlatform.darwin:
        subprocess.call(('open', filename))
    elif platform == __EnumPlatform.wsl:
        subprocess.call('cmd.exe /C start'.split() + filename)
    else:
        subprocess.call(('xdg-open', filename))


class __EnumPlatform(Enum):
    linux = 1
    win32 = 2
    win64 = 3
    darwin = 4
    wsl = 5
