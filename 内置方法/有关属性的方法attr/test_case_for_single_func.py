# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_case_for_single_func.py
# author: ScCcWe
# time: 2020/5/20 10:58


CSI = '\033['


def code_to_chars(code):
    print(CSI + str(code) + 'm')
    return CSI + str(code) + 'm'


code_to_chars(40)
