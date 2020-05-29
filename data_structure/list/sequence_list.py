# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: sequence_list.py
# author: ScCcWe
# time: 2020/3/9 9:32


class SeqList(object):
    def __init__(self, size):
        self.max_size = size
        self.num = 0
        self.data = [None] * self.max_size
    
    def is_empty(self):
        return self.num is 0
    
    def is_full(self):
        return self.num is self.max_size
    
    def count(self):
        return self.num
    
    def __getitem__(self, index):
        """根据指定的位置序号index，获取顺序表中第index个数据元素的值"""
        if not isinstance(index, int):
            raise TypeError
        
        if 0 <= index < self.num:
            return self.data[index]
        else:
            raise IndexError
    
    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError
        
        if 0 <= index < self.num:
            self.data[index] = value
        else:
            raise IndexError
    
    def locate_item(self, value):
        """查找
        根据指定的元素值value，查找顺序表中第1个于value相等的元素。
        若查找成功，则返回改元素在表中的位置序号；若查找失败，返回-1
        """
        for i in range(self.max_size):
            if self.data[i] == value:
                return i
        return -1
    
    def insert_item(self, index, value):
        """输入index，value；在指定的index位置插入value"""
        if not isinstance(index, int):
            raise TypeError
        if index < 0 or index > self.num:
            raise IndexError
        for i in range(self.num, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value
        self.num += 1
    
    def append_last(self, value):
        if self.num > self.max_size:
            return 'Full List!!!'
        self.data[self.num] = value
        self.num += 1
    
    def del_item(self, index):
        """输入一个index，删除指定位置的item"""
        # judge
        if index < 0 or index > self.num:
            raise IndexError
        if not isinstance(index, int):
            raise TypeError
        
        # func
        for i in range(index, self.num):
            self.data[i] = self.data[i+1]
        self.num -= 1
    
    def print_list(self):
        """以列表的方式输出顺序表"""
        bottle = []
        for i in range(self.num):
            bottle.append(self.data[i])
        return bottle
    
    def print_data(self):
        return self.data
    
    
if __name__ == '__main__':
    seq_list = SeqList(50)
    print('is_empty: {}'.format(seq_list.is_empty()))
    print("count: ", seq_list.count())
    print("is_full: ", seq_list.is_full())
    print("print_list(): {}".format(seq_list.print_list()))
    seq_list.append_last(1)
    seq_list.append_last(2)
    seq_list.append_last(4)
    seq_list.append_last(8)
    seq_list.append_last(16)
    seq_list.append_last(32)
    print()
    print('is_empty: {}'.format(seq_list.is_empty()))
    print("count: ", seq_list.count())
    print("is_full: ", seq_list.is_full())
    print("print_list(): {}".format(seq_list.print_list()))
    
    # print(seq_list.__getitem__(0))
    # print(seq_list.__getitem__(2))
    # print(seq_list.__getitem__(5))
    # # print(seq_list.__getitem__(6))
    # # print(seq_list.__getitem__("nihao"))
    #
    # seq_list.__setitem__(0, 10)
    # seq_list.__setitem__(2, 40)
    # seq_list.__setitem__(5, 320)
    # # seq_list.__setitem__(6, 10)
    # print(seq_list.count())
    # print(seq_list.print_data())
    #
    # print('__setitem__后: ')
    # print(seq_list.__getitem__(0))
    # print(seq_list.__getitem__(2))
    # print(seq_list.__getitem__(5))
    # # print(seq_list.__getitem__(6))
    # print(seq_list.print_list())
    # print(seq_list.count())
    
    # print()
    # print(seq_list.locate_item(32))
    #     # print(seq_list.locate_item(1))
    #     # print(seq_list.locate_item(33))
    
    # print()
    # # seq_list.insert_item(2, 10)
    # # print(seq_list.print_list())
    # seq_list.insert_item(6, 10)
    # print(seq_list.print_list())
    
    # print()
    # seq_list.del_item(5)
    # print(seq_list.print_list())
    
