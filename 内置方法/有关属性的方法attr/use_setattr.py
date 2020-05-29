# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: use_setattr.py
# author: ScCcWe
# time: 2019/12/30 9:50


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog_bai = Animal("dog_bai", 12)
print(getattr(dog_bai, "name"))
setattr(dog_bai, "name", "dog_black")
print(getattr(dog_bai, 'name'))

# 当属性不存在时，会自动创建
setattr(dog_bai, "height", 12)
print(getattr(dog_bai, "height"))
