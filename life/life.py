# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: life.py
# author: ScCcWe
# time: 2020/4/18 16:57


def what_is_life(want, life):
    for year, get in enumerate(life):
        if get in want:
            return
        with open('wants.txt', 'a+', encoding='utf-8') as f:
            f.write(get + '\n')
        print(str(year + 1) + 'year will actually get!')
        continue
