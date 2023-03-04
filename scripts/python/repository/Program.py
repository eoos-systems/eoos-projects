#!/usr/bin/env python3
# @file      Program.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023, Sergey Baigudin, Baigudin Software

import os
import time
import argparse
import shutil
import subprocess
from common.Message import Message

class Program():

    def __init__(self):
        self.__args = None


    def execute(self):
        time_start = time.time()
        error = 0
        try:
            Message.out(f'Welcome to {self.__PROGRAM_NAME}', Message.OK, True)
            self.__parse_args()
            self.__check_run_path()
            self.__print_args()
            if self.__args.init is True:
                self.__init_repo()
                self.__init_sub_repos('if-posix')
                self.__init_sub_sub_repos('if-posix')                
                self.__init_sub_repos('if-win32')
                self.__init_sub_sub_repos('if-win32')                
                self.__init_sub_repos('sample-applications')                
                self.__init_print_status()
        except Exception as e:
            Message.out(f'[EXCEPTION] {e}', Message.ERR)        
            error = 1
        finally:
            status = Message.OK
            not_word = ''
            if error != 0:
                status = Message.ERR
                not_word = ' NOT'
            time_execute = round(time.time() - time_start, 9)
            Message.out(f'{self.__PROGRAM_NAME} has{not_word} been completed in {str(time_execute)} seconds', status, is_block=True)
            return error


    def __init_repo(self):
        os.chdir('./../..')
        Message.out(f'[INFO] Inialize super-repository...', Message.INF)
        subprocess.run(['git', 'checkout', 'develop'])
        subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@gitflic.ru:baigudin-software/eoos-projects.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@github.com:baigudin-software/eoos-projects.git'])


    def __init_sub_repos(self, suffix_name):
        Message.out(f'[INFO] Inialize EOOS "{suffix_name}" project repositories...', Message.INF)
        os.chdir(f'./projects/eoos-{suffix_name}/')
        subprocess.run(['git', 'checkout', 'master'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', f'git@gitflic.ru:baigudin-software/eoos-project-{suffix_name}.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', f'git@github.com:baigudin-software/eoos-project-{suffix_name}.git'])
        os.chdir('./../..')


    def __init_sub_sub_repos(self, suffix_name):
        Message.out(f'[INFO] Inialize EOOS "{suffix_name}" project sub-repositories...', Message.INF)    
        os.chdir(f'./projects/eoos-{suffix_name}/')

        os.chdir('./codebase/interface/')
        subprocess.run(['git', 'checkout', 'master'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@gitflic.ru:baigudin-software/eoos-api.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@github.com:baigudin-software/eoos-api.git'])
        os.chdir('./../..')

        os.chdir('./codebase/library/')
        subprocess.run(['git', 'checkout', 'master'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@gitflic.ru:baigudin-software/eoos-library.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@github.com:baigudin-software/eoos-library.git'])
        os.chdir('./../..')

        os.chdir('./codebase/system/')
        subprocess.run(['git', 'checkout', 'master'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', f'git@gitflic.ru:baigudin-software/eoos-system-{suffix_name}.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', f'git@github.com:baigudin-software/eoos-system-{suffix_name}.git'])
        os.chdir('./../..')

        os.chdir('./codebase/tests/')
        subprocess.run(['git', 'checkout', 'master'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@gitflic.ru:baigudin-software/eoos-tests.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@github.com:baigudin-software/eoos-tests.git'])
        os.chdir('./../..')

        os.chdir('./scripts/')
        subprocess.run(['git', 'checkout', 'master'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@gitflic.ru:baigudin-software/eoos-scripts.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@github.com:baigudin-software/eoos-scripts.git'])
        os.chdir('./..')
        os.chdir('./../..')


    def __init_print_status(self):
        Message.out(f'[INFO] Repositories status:', Message.INF)
        subprocess.run(['git', 'status', '-b', '-s'])
        subprocess.run(['git', 'submodule', 'foreach', '--recursive', 'git', 'status', '-b', '-s'])
        
        Message.out(f'[INFO] Remote values:', Message.INF)
        subprocess.run(['git', 'remote', '-v'])
        subprocess.run(['git', 'submodule', 'foreach', '--recursive', 'git', 'remote', '-v'])


    def __check_run_path(self):
        if self.__is_correct_location() is not True:
            raise Exception(f'Script run directory is wrong. Please, run it from "\scripts\python\" directory')


    def __is_correct_location(self):
        if os.path.isdir(f'./../python') is not True:
            return False
        if os.path.isdir(f'./../../scripts') is not True:
            return False
        if os.path.isdir(f'./../../projects') is not True:
            return False
        return True


    def __parse_args(self):
        parser = argparse.ArgumentParser(prog=self.__PROGRAM_NAME\
            , description='Proceses EOOS Projects git repository'\
            , epilog='(c) 2023, Sergey Baigudin, Baigudin Software')
        parser.add_argument('--init'\
            , action='store_true'\
            , help='initialize just cloned repository to develop on it')
        parser.add_argument('--version'\
            , action='version'\
            , version=f'%(prog)s {self.__PROGRAM_VERSION}')
        self.__args = parser.parse_args()
 
 
    def __print_args(self):
        if self.__args.init is True:
            Message.out(f'[INFO] Argument INIT = {self.__args.init}', Message.INF)    
        return


    __PROGRAM_NAME = 'EOOS Automotive Repository Processor'
    __PROGRAM_VERSION = '1.0.0'    
