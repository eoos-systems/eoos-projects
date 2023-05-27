#!/usr/bin/env python3
# @file      ProgramOnPosix.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023, Sergey Baigudin, Baigudin Software

from integrate.Program import Program

class ProgramOnPosix(Program):
    """
    Program on POSIX.
    """

    def _get_path_to_eoos_dir(self):
        return f'./../../projects/eoos-if-posix'


    def _get_name_interpreter(self):
        return 'python3'


    def _is_to_run_eoos_ut(self, config, defines):
        return True
