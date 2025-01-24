#!/usr/bin/env python3
# @file      Integrate.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023-2025, Sergey Baigudin, Baigudin Software

import sys
import time
import argparse

from common.System import System
from common.Message import Message
from integrate.ProgramOnPosix import ProgramOnPosix
from integrate.ProgramOnWin32 import ProgramOnWin32


class Integrate:
    """
    Integrate program.
    """

    def __init__(self):
        self.__args = None


    def build(self):
        """
        Builds EOOS system.
        """
        time_start = time.time()
        res = True
        try:
            Message.out(f'Welcome to {self.__PROGRAM_NAME}', Message.OK, True)
            self.__parse_args()
            self.__print_args()
            program = None
            if self.__get_args().eoos == f'POSIX':
                program = ProgramOnPosix( self.__get_args() )
            elif self.__get_args().eoos == f'WIN32':
                program = ProgramOnWin32( self.__get_args() )
            else:
                raise Exception(f'EOOS project not supported')
            if program is not None:
                program.execute()
            else:
                raise Exception(f'Program is not set')
        except Exception as e:
            Message.out(f'[EXCEPTION] {e}', Message.ERR)
            res = False
        finally:
            status = Message.OK
            not_word = ''
            if res == False:
                status = Message.ERR
                not_word = ' NOT'
            time_execute = round(time.time() - time_start, 9)
            Message.out(f'{self.__PROGRAM_NAME} has{not_word} been completed in {str(time_execute)} seconds', status, is_block=True)
            return res


    def __get_args(self):
        return self.__args


    def __parse_args(self):
        parser = argparse.ArgumentParser(prog=self.__PROGRAM_NAME \
            , description='Runs the EOOS intergation build' \
            , epilog='(c) 2023-2025, Sergey Baigudin, Baigudin Software' \
        )
        parser.add_argument('-e', '--eoos' \
            , choices=['POSIX', 'WIN32', 'FreeRTOS'] \
            , help='select a target EOOS project' \
            , required=True \
        )
        parser.add_argument('-b', '--build' \
            , choices=['EOOS', 'APPS', 'ALL'] \
            , default='ALL' \
            , help='compile an appropriate target of projects' \
        )
        parser.add_argument('--no-install' \
            , action='store_true' \
            , help='do not install EOOS on OS' \
        )
        parser.add_argument('--interpreter' \
            , default=self.__get_name_interpreter() \
            , metavar='PYTHON_EXECUTABLE' \
            , help='set Python interpreter' \
        )
        parser.add_argument('--version' \
            , action='version' \
            , version=f'%(prog)s {self.__PROGRAM_VERSION}' \
        )
        self.__args = parser.parse_args()


    def __get_name_interpreter(self):
        """
        Returns python interpreter name.
        """
        if System.is_linux() is True:
            return 'python3'
        if System.is_win32() is True:
            return 'python'
        super().__init__(args)


    def __print_args(self):
        Message.out(f'[INFO] Argument BUILD = {self.__args.build}', Message.INF)
        Message.out(f'[INFO] Argument NO-INSTALL = {self.__args.no_install}', Message.INF)


    __PROGRAM_NAME = 'EOOS Safe Intergator'
    __PROGRAM_VERSION = '1.1.0'


def main():
    if Integrate().build() is True:
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit( main() )
