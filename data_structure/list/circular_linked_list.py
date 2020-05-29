# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: circular_linked_list.py
# author: ScCcWe
# time: 2020/3/9 11:29


"""
循环链表 Circular Linked List
特点：
    最后一个结点指向头结点，整个链形成一个环。由此，从表中任一节点出发皆可到达表中其他节点。
说明：
    带有头节点，头节点不存储数据，只是为了方便代码编写。
"""


class Node:
    # 节点类
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    # 循环列表类
    def __init__(self):
        self._head = Node('head')  # 一个不存储数据的头结点，名为"head"
        self.length = 0            # 头结点是不算在length里面的, 所以从0开始
    
    def add_node(self, node):
        # 类型判断
        if not isinstance(node, Node):
            raise TypeError
        
        if self.length == 0:
            self.add_begin(node)
        else:
            self.add_last(node)
    
    def add_begin(self, node):
        """add_begin有两种情况：
            1) 只有头结点时，和头结点串联即可
            2）增加在头结点之后
        """
        if self.length == 0:
            # 将新结点和头结点串联起来
            self._head.next = node
            node.next = self._head
            self.length += 1
        else:
            node.next = self._head.next
            self._head.next = node
            self.length += 1
    
    def add_last(self, node):
        """add_last分两步：
            1）定位到当前链表的最后一位
            2）在最后一位 的 后一位 插入 node
        """
        # 定位到当前链表的最后一位
        cur = self._head.next          # 开始定位的第一个节点(cur)
        while cur.next != self._head:  # 当定位的点(cur)不是尾巴时:
            cur = cur.next
        
        # 在最后一位 的 后一位 插入 node
        cur.next = node
        node.next = self._head
        self.length += 1
    
    def print_list(self):
        bottle = []
        cur = self._head.next  # 头结点不存储数据
        
        while cur.next != self._head:  # 当下一个节点不等于头结点时（即除最后一个节点外）(这样分开是为了防止一直循环)
            bottle.append(cur.data)
            cur = cur.next
        
        if cur.next == self._head:  # 最后一个节点
            bottle.append(cur.data)
        
        return bottle
    
    def get_tail_node(self):
        """得到尾结点
            1）注意：循环链表和单链表判别的条件不同，循环链表中：!=self._head; 单链表中：!=None
        """
        cur = self._head.next          # 定位(判别)的第一个节点
        while cur.next != self._head:  # 当下一个节点不等于头结点时（即除最后一个节点外）
            cur = cur.next
        return cur
    
    def print_tail_node_next(self):
        tail_node = self.get_tail_node()
        return tail_node.next
        # if node.next:
        #     return node.next.data
    
    def print_node(self):
        tail_node = self.get_tail_node()
        return tail_node.next.data
        # if node.next:
        #     return node.next.data


if __name__ == '__main__':
    cir_list = CircularLinkedList()
    cir_list.add_node(Node(1))
    cir_list.add_node(Node(2))
    cir_list.add_node(Node(3))
    cir_list.add_node(Node(4))
    cir_list.add_node(Node(5))
    print(cir_list.print_list())
    print(cir_list.length)
    
    cir_list.add_begin(Node(0))
    print(cir_list.print_list())
    
    cir_list.add_last(Node(6))
    print(cir_list.print_list())
    
    # 输出尾结点的next节点 的data
    print(cir_list.print_tail_node_next().data)
    # 输出尾结点的next的next 的data
    print(cir_list.print_tail_node_next().next.data)
