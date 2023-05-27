#!/usr/bin/env python3
# @file      ProgramOnWin32.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023, Sergey Baigudin, Baigudin Software

from integrate.Program import Program

class ProgramOnWin32(Program):
    """
    Program on WIN32.
    """

    def _get_path_to_eoos_dir(self):
        return f'./../../projects/eoos-if-win32'


    def _get_name_interpreter(self):
        return 'python'


    def _is_to_run_eoos_ut(self, config, defines):
        if len(defines) == 0:
            return True
        else:
            return False
