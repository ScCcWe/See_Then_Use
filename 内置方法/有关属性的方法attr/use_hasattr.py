# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: use_hasattr.py
# author: ScCcWe
# time: 2020/5/29 21:47


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog_bai = Animal("dog_bai", 12)
print(hasattr(dog_bai, 'name'))
print(hasattr(dog_bai, 'age'))
print(hasattr(dog_bai, 'jump'))
