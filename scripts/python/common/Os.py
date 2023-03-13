#!/usr/bin/env python3
# @file      Os.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023, Sergey Baigudin, Baigudin Software

from sys import platform

class Os:

    @staticmethod
    def is_posix():
        return platform == 'linux' or platform == 'linux2'

    @staticmethod
    def is_win32():
        return platform == 'win32'

