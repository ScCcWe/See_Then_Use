# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: 2.py
# author: ScCcWe
# time: 2020/5/20 10:22


from colorama import Fore, Back, Style, init
print(Fore.RED + 'some red text')
print(Fore.MAGENTA + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Back.WHITE + 'and with a green background')
print(Back.CYAN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.BRIGHT + 'and in dim text')

print(Style.RESET_ALL)  # close

print('back to normal now')
init(autoreset=True)  # in windows

print(Fore.RED + 'some red text')
print(Fore.MAGENTA + 'some red text')
print(Back.BLACK + 'and with a green background' + Back.WHITE + 'and with a green background')
print(Back.RED + 'and with a green background')
print(Back.GREEN + 'and with a green background')
print(Back.YELLOW + 'and with a green background')
print(Back.BLUE + 'and with a green background')
print(Back.MAGENTA + 'and with a green background')
print(Back.CYAN + 'and with a green background')
print(Back.WHITE + 'and with a green background')
print(Back.RESET + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.BRIGHT + 'and in dim text')

print('back to normal now')
