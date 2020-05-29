# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: use_colorama.py
# author: ScCcWe
# time: 2020/5/29 21:49

from colorama import Back, init

init(autoreset=True)  # in windows
print(Back.BLACK + 'and with a green background')
