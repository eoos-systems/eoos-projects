#!/usr/bin/env python3
# @file      IProgram.py
# @author    Sergey Baigudin, sergey@baigudin.software
# @copyright 2023, Sergey Baigudin, Baigudin Software

from abc import ABC, abstractmethod

class IProgram(ABC):
    """
    Interface of a program.
    """

    @abstractmethod
    def execute(self):
        """
        Executes a program.
        
        Returns: 
            int: zero on success, or any other number on failure.
        """
        pass
