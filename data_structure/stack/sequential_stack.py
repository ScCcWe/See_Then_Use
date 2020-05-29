# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: sequential_stack.py
# author: ScCcWe
# time: 2020/4/8 16:36


class SequentialStack(object):
    def __init__(self):
        self.length = 0
        self.seq_list = []
    
    def __del__(self):
        print(self.__class__.__name__ + "被销毁。")
    
    def is_null(self):
        return self.length == 0
    
    def clear(self):
        self.seq_list.clear()
    
    def push(self, data):
        if self.is_null():
            self.seq_list.append(data)
            self.length += 1
        else:
            self.seq_list.insert(0, data)
            self.length += 1
    
    def pop(self):
        if self.is_null():
            return
        self.seq_list.pop(0)
        self.length -= 1
    
    def get_top_data(self):
        return self.seq_list[0]
    
    def traverse(self):
        trav_list = []
        if self.is_null():
            return
        for item in self.seq_list:
            trav_list.append(item)
        return trav_list
    
    
if __name__ == '__main__':
    ins_seq_list = SequentialStack()
    ins_seq_list.push('1')
    ins_seq_list.push('2')
    ins_seq_list.push('3')
    ins_seq_list.push('4')
    ins_seq_list.push('5')
    print(ins_seq_list.traverse())
    print(ins_seq_list.get_top_data())
    ins_seq_list.pop()
    ins_seq_list.pop()
    ins_seq_list.pop()
    ins_seq_list.pop()
    ins_seq_list.pop()
    print(ins_seq_list.traverse())
