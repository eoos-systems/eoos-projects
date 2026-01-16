#!/usr/bin/env python3
# @file      Program.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023-2026, Sergey Baigudin, Baigudin Software

import os
import time
import argparse
import shutil
import subprocess

from abc import ABC, abstractmethod
from common.IProgram import IProgram
from common.Message import Message


class Program(IProgram):
    """
    Abstatact base program.
    """

    def __init__(self, args):
        self.__args = args


    def execute(self):
        defines = [
            'EOOS_GLOBAL_SYS_MUTEX_AMOUNT=4',
            'EOOS_GLOBAL_SYS_SEMAPHORE_AMOUNT=4',
            'EOOS_GLOBAL_SYS_THREAD_AMOUNT=5'
        ]
        self.__check_run_path()
        self.__do_run_eoos_ut('Release')
        self.__do_run_eoos_ut('Release', defines)
        self.__do_run_eoos_ut('Debug')
        self.__do_run_eoos_ut('Debug', defines)
        self.__do_run_eoos_ut('RelWithDebInfo')
        self.__do_run_eoos_ut('RelWithDebInfo', defines)
        self.__do_run_eoos_ut('MinSizeRel')
        self.__do_run_eoos_ut('MinSizeRel', defines)
        self.__do_install_eoos('RelWithDebInfo')
        self.__do_run_eoos_sample_applications('RelWithDebInfo')
        self.__do_clean()


    @abstractmethod
    def _get_path_to_eoos_dir(self):
        """
        Returns path to an eoos project directory.
        """
        pass


    @abstractmethod
    def _get_name_interpreter(self):
        """
        Returns python interpreter name.
        """
        pass


    @abstractmethod
    def _is_to_run_eoos_ut(self, config, defines):
        """
        Tests if `__do_run_eoos_ut` method must be executed.
        """
        pass


    def __get_args(self):
        """
        Returns program arguments.
        """
        return self.__args


    def __do_run_eoos_ut(self, config, defines=[]):
        if self.__get_args().build != 'EOOS' and self.__get_args().build != 'ALL':
            return
        if self._is_to_run_eoos_ut(config, defines) is False:
            return
        args = [self.__get_args().interpreter, 'Make.py', '-e', self.__get_args().eoos, '-c', '-b', 'ALL', '-r', '--config', config]
        args_define = []
        args_define_message = ''
        if len(defines) > 0:
            args_define_message = ' with build global defines'
            args_define.append('--define')
            for d in defines:
                args_define.append(d);
        args.extend(args_define)
        if self.__get_args().jobs is not None:
            args.extend(['-j', str(self.__get_args().jobs)])
        Message.out(f'Run EOOS Unit Tests for "{config}" configuration{args_define_message}', Message.INF, True)
        os.chdir(f'{self._get_path_to_eoos_dir()}/scripts/python')
        ret = subprocess.run(args).returncode
        os.chdir(self.__PATH_FROM_A_PROJECT_DIR)
        if ret != 0:
            raise Exception(f'EOOS build error with exit code [{ret}]')


    def __do_install_eoos(self, config):
        if self.__get_args().no_install is True:
            return
        Message.out(f'Install EOOS for "{config}" configuration', Message.INF, True)
        os.chdir(f'{self._get_path_to_eoos_dir()}/scripts/python')
        ret = subprocess.run([self.__get_args().interpreter, 'Make.py', '-e', self.__get_args().eoos, '-c', '-b', 'EOOS', '--install', '--config', config]).returncode
        os.chdir(self.__PATH_FROM_A_PROJECT_DIR)
        if ret != 0:
            raise Exception(f'EOOS install error with exit code [{ret}]')


    def __do_run_eoos_sample_applications(self, config):
        if self.__get_args().build != 'APPS' and self.__get_args().build != 'ALL':
            return
        Message.out(f'Run EOOS Sample Applications for "{config}" configuration', Message.INF, True)
        os.chdir(f'{self.__PATH_TO_APPS_DIR}/scripts/python')
        ret = subprocess.run([self.__get_args().interpreter, 'Make.py', '-c', '-b', '-r', '--config', config]).returncode
        os.chdir(self.__PATH_FROM_A_PROJECT_DIR)
        if ret != 0:
            raise Exception(f'APP build error with exit code [{ret}]')


    def __do_clean(self):
        if os.path.isdir(f'{self._get_path_to_eoos_dir()}/build'):
            Message.out(f'[BUILD] Deleting EOOS "build" directory...', Message.INF)
            shutil.rmtree(f'{self._get_path_to_eoos_dir()}/build')
        if os.path.isdir(f'{self.__PATH_TO_APPS_DIR}/build'):
            Message.out(f'[BUILD] Deleting APPS "build" directory...', Message.INF)
            shutil.rmtree(f'{self.__PATH_TO_APPS_DIR}/build')


    def __check_run_path(self):
        if self.__is_correct_location() is not True:
            raise Exception(f'Script run directory is wrong. Please, run it from "\scripts\python\" directory')


    def __is_correct_location(self):
        if os.path.isdir(f'./../python') is not True:
            return False
        if os.path.isdir(f'./../../scripts') is not True:
            return False
        if os.path.isdir(f'./../../projects/eoos-if-posix') is not True:
            return False
        if os.path.isdir(f'./../../projects/eoos-if-win32') is not True:
            return False
        if os.path.isdir(f'./../../projects/eoos-sample-applications') is not True:
            return False
        return True


    __PATH_TO_APPS_DIR = './../../projects/eoos-sample-applications'
    __PATH_FROM_A_PROJECT_DIR = './../../../../scripts/python'
