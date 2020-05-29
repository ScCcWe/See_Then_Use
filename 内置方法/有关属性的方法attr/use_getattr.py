# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: use_getattr.py
# author: ScCcWe
# time: 2019/12/30 9:35


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog_bai = Animal("dog_bai", 12)
print(getattr(dog_bai, "name"))
print(getattr(dog_bai, 'age'))
print(getattr(dog_bai, 'width'))
