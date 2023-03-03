#!/usr/bin/env python3
# @file      Message.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023, Sergey Baigudin, Baigudin Software

import sys
from colorama import just_fix_windows_console

class Message:

    OK = 1
    ERR = 2
    INF = 3
    NOR = 4

    @staticmethod
    def out(string, status=None, is_block=None):
        just_fix_windows_console()
        color = Message.__COLOR_END
        if status == Message.OK:
            color = Message.__COLOR_OK
        elif  status == Message.ERR:
            color = Message.__COLOR_ERR
        elif status == Message.INF:
            color = Message.__COLOR_INF
        elif status == Message.NOR:
            color = Message.__COLOR_NOR
        else:
            color = Message.__COLOR_END
        if is_block is not True:
            print(color + string + Message.__COLOR_END, flush=True)
        else:
            print(color + '-------------------------------------------------------------------------------' + Message.__COLOR_END, flush=True)
            print(color + ' ' + string + Message.__COLOR_END, flush=True)
            print(color + '-------------------------------------------------------------------------------' + Message.__COLOR_END, flush=True)
            

    __COLOR_OK  = '\033[32m'
    __COLOR_ERR = '\033[31m'
    __COLOR_INF = '\033[93m'    
    __COLOR_NOR = '\033[0m'
    __COLOR_END = '\033[0m'
