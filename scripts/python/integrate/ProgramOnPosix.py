#!/usr/bin/env python3
# @file      ProgramOnPosix.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023-2023, Sergey Baigudin, Baigudin Software

from integrate.Program import Program
from common.System import System

class ProgramOnPosix(Program):
    """
    Program on POSIX.
    """

    def __init__(self, args):
        if System.is_linux() is not True:
            raise Exception(f'Unsuppoted host OS')
        super().__init__(args)


    def _get_path_to_eoos_dir(self):
        return f'./../../projects/eoos-if-posix'


    def _get_name_interpreter(self):
        return 'python3'


    def _is_to_run_eoos_ut(self, config, defines):
        return True
