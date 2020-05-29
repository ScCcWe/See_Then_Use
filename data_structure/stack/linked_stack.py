# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: linked_stack.py
# author: ScCcWe
# time: 2020/4/7 19:38


class Node:
    def __init__(self, data):
        self.item = data
        self.next = None


class LinkedStack:
    """
    以链表的头部作为栈顶，
        第一个指针指向栈顶，之后以此类推
    """
    def __init__(self):
        self.length = 0
        self.null_stack = None
    
    def __del__(self):
        # 析构方法
        # 当对象被删除时，会自动被调用
        class_name = self.__class__.__name__
        print(class_name, "销毁")
    
    def clear(self):
        if self.is_null():
            return
        # 除最后一个以外的全部
        while self.null_stack.next is not None:
            self.null_stack = self.null_stack.next
            self.length -= 1
        # 最后一个
        self.null_stack = None
        self.length -= 1
    
    def is_null(self):
        return self.length == 0
    
    def get_top_item(self):
        if self.is_null():
            return "Stack is None."
        return self.null_stack.item
    
    def get_length(self):
        return self.length
    
    def push(self, data):
        """
        入栈
        :param data: 需要入栈的节点的值, 这里没有进行类型判断
        """
        # if variable's type is Node, this below can increase
        # if isinstance(data, Node):
        #     raise TypeError
        node = Node(data)
        node.next = self.null_stack
        self.null_stack = node  # 修改栈顶指针为node
        self.length += 1
    
    def pop(self):
        """
        弹出栈顶元素
        :return: 栈顶元素的值
        """
        if self.is_null():
            return "current stack is none"
        value = self.null_stack.item            # 取出栈顶元素的值
        self.null_stack = self.null_stack.next  # 栈顶元素脱钩
        self.length -= 1
        return value
    
    def traverse(self):
        """
        遍历
        """
        list = []
        if self.is_null():
            return
        while self.null_stack.next is not None:
            list.append(self.null_stack.item)
            self.null_stack = self.null_stack.next
        list.append(self.null_stack.item)
        return list


if __name__ == '__main__':
    
    # init a stack
    ins_stack = LinkedStack()
    ins_stack.push(1)
    ins_stack.push(2)
    ins_stack.push(3)
    ins_stack.push(4)
    ins_stack.push(5)
    
    # test func traverse()
    # print(ins_stack.length)
    # print(ins_stack.traverse())
    
    # test func pop()
    # print(ins_stack.pop())
    # print(ins_stack.length)
    # print(ins_stack.traverse())
    
    # test func get_top_item()
    # print(ins_stack.pop())
    # print(ins_stack.get_top_item())
    
    # test func clear()
    # ins_stack.clear()
    # print(ins_stack.length)
    # print(ins_stack.traverse())
    
    # test magic __del__
    print(ins_stack.length)
    print(ins_stack.traverse())
    del ins_stack
    print('class stack over')
    
    # test magic __del__
    # a = ins_stack
    # print(ins_stack.length)
    # print(ins_stack.traverse())
    # del ins_stack
    # print('class stack over')
