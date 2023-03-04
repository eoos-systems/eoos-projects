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
            self.__init_repo()
            self.__init_sub_repos()
            self.__init_sub_sub_repos_for('posix')
            self.__init_sub_sub_repos_for('win32')
            self.__output_status()
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
        subprocess.run(['git', 'status', '-b', '-s'])
        subprocess.run(['git', 'checkout', 'develop'])
        subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@gitflic.ru:baigudin-software/eoos-projects.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@github.com:baigudin-software/eoos-projects.git'])


    def __init_sub_repos(self):
        os.chdir('./projects/eoos-if-posix/')
        subprocess.run(['git', 'checkout', 'master'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@gitflic.ru:baigudin-software/eoos-project-if-posix.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@github.com:baigudin-software/eoos-project-if-posix.git'])
        os.chdir('./../..')

        os.chdir('./projects/eoos-if-win32/')
        subprocess.run(['git', 'checkout', 'master'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@gitflic.ru:baigudin-software/eoos-project-if-win32.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@github.com:baigudin-software/eoos-project-if-win32.git'])
        os.chdir('./../..')

        os.chdir('./projects/eoos-sample-applications/')
        subprocess.run(['git', 'checkout', 'master'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@gitflic.ru:baigudin-software/eoos-project-sample-applications.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@github.com:baigudin-software/eoos-project-sample-applications.git'])
        os.chdir('./../..')


    def __init_sub_sub_repos_for(self, api):
        os.chdir(f'./projects/eoos-if-{api}/')

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
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@gitflic.ru:baigudin-software/eoos-system-if-{api}.git'])
        subprocess.run(['git', 'remote', 'set-url', 'origin', '--push', '--add', 'git@github.com:baigudin-software/eoos-system-if-{api}.git'])
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


    def __output_status(self):
        subprocess.run(['git', 'status', '-b', '-s'])
        subprocess.run(['git', 'submodule', 'foreach', '--recursive', 'git', 'status', '-b', '-s'])
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
            , description='Runs EOOS Projects git repository initialization'\
            , epilog='(c) 2023, Sergey Baigudin, Baigudin Software' )
        parser.add_argument('--version'\
            , action='version'\
            , version=f'%(prog)s {self.__PROGRAM_VERSION}')
        self.__args = parser.parse_args()
 
 
    def __print_args(self):
        return


    __PROGRAM_NAME = 'EOOS Automotive Repository Initializer'
    __PROGRAM_VERSION = '1.0.0'    
