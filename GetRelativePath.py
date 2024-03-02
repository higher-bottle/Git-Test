#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 03:45:41 2024

@author: bingtinghuangfu
"""
import os
import sys

class GetRelativePath:
    def __init__(self,relative_path):
        self.relative_path=relative_path
        
        
    def read_relative(self):
        executable_dir = os.path.dirname(sys.executable)
        self.file_path = os.path.join(executable_dir, self.relative_path)
        return self.file_path