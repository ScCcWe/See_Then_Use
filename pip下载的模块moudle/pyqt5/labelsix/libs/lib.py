# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: lib.py
# author: ScCcWe
# time: 2020/5/29 22:59
from math import sqrt


def distance(p):
    return sqrt(p.x() * p.x() + p.y() * p.y())
