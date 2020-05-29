# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: insert_create_linked_list.py
# author: ScCcWe
# time: 2020/3/5 15:15
from linked_list import LinkedList, Node


def create_list_from_head(node_list):
    """前插法
    时间复杂度：n x 1
    """
    link_list = LinkedList()  # 创建一个长度为0，只有头节点的链表
    head = link_list.head     # 一个用于连接的头结点
    
    for node_data in node_list:
        new_node = Node(node_data)
        
        new_node.next = head.next
        head.next = new_node
        link_list.length += 1
    
    return link_list.print_list()


def create_list_from_tail(node_list):
    """后插法
    时间复杂度：n x 1
    """
    link_list = LinkedList()
    head = link_list.head
    
    for node_data in node_list:
        new_node = Node(node_data)
        
        head.next = new_node
        head = head.next
        link_list.length += 1
        
    return link_list.print_list()


if __name__ == '__main__':
    create_list_from_tail([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    create_list_from_head([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    
    """简单总结
    前插法和后插法并没有很明显的优劣之分。
    按照正常人的思维，还是后插比较好用。
    """
