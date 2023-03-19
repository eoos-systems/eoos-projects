#!/usr/bin/env python3
# @file      Integrate.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023, Sergey Baigudin, Baigudin Software

import sys

from common.System import System
from integrate.ProgramOnPosix import ProgramOnPosix
from integrate.ProgramOnWin32 import ProgramOnWin32


def main():
    try:
        program = None
        if System.is_posix():
            program = ProgramOnPosix()
        elif System.is_win32():
            program = ProgramOnWin32()
        else:
            raise Exception(f'Unknown host operating system')
        return program.execute()
    except BaseException as e:
        print(e)    
        return 1


if __name__ == "__main__":
    sys.exit( main() )
