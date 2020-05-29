# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: double_linked_list.py
# author: ScCcWe
# time: 2020/3/9 16:06


"""
双向链表 Double Linked List
目的：
    克服单链表单向性的缺点，使得查找直接前驱的执行时间为O(1)
说明：
    和单链表大同小异，区别在insert和del
"""


class Node:
    def __init__(self, data):
        self.prior = None  # 直接前驱
        self.next = None   # 直接后继
        self.item = data
    
    
class DoubleLinkedList:
    def __init__(self):
        self._head = Node('head')  # 带头结点
        self._length = 0
    
    def is_empty(self):
        return self._length == 0
    
    def empty_add(self, node):
        self._head.next = node   # 1
        node.prior = self._head  # 2
        self._length += 1
    
    def add_beg(self, node):
        """在开头添加节点，两种情况
            1）为空时，添加在self._head之后即可
            2）不为空，添加在self._head之后，并且还要连接起之后的部分
        """
        if self.is_empty():
            self._head.next = node   # 1
            node.prior = self._head  # 2
            self._length += 1
        else:
            # 这边的1234怎么区分，有一个技巧，已知的节点只能是34，未知的是12
            node.next = self._head.next  # 3
            self._head.next.prior = node  # 4
            node.prior = self._head  # 1
            self._head.next = node  # 2
            self._length += 1
    
    def add_last(self, node):
        """在结尾添加节点，两种情况
            1）为空时，情况同 func add_beg() 1) 一致，我们直接使用func empty_add()
            1) 不为空，先找到最后一个节点的pointer，用该pointer连接node即可
        """
        if self.is_empty():
            self.empty_add(node)
        else:
            pointer = self._head.next
            while pointer.next is not None:
                pointer = pointer.next
            
            pointer.next = node
            node.prior = pointer
            node.next = None
            self._length += 1
    
    def __setitem__(self, index, value):
        ...
    
    def __delitem__(self, index):
        ...
    
    def travel(self):
        bottle = []
        pointer = self._head.next
        
        for _ in range(self._length):
            bottle.append(pointer.item)
            pointer = pointer.next
        
        return bottle


if __name__ == "__main__":
    double_list = DoubleLinkedList()
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    
    # 前插法创建双向链表
    double_list.add_beg(node_1)
    double_list.add_beg(node_2)
    double_list.add_beg(node_3)
    double_list.add_beg(node_4)
    double_list.add_beg(node_5)
    print(double_list.travel())
    print(node_1.prior.item)
    print(node_1.next)
    print(node_2.prior.item)
    print(node_2.next.item)
    
    # 后插法创建双向链表
    # double_list.add_last(node_1)
    # double_list.add_last(node_2)
    # double_list.add_last(node_3)
    # double_list.add_last(node_4)
    # double_list.add_last(node_5)
    # print(double_list._length)
    # print(double_list.travel())
    # print(node_2.prior.item)
    # print(node_2.next.item)
