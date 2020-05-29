# -*- coding: utf-8 -*-
# file_name: linked_list.py
# author: ScCcWe
# time: 2020/2/27 19:13

"""
关于此处定义的LinkedList类的一些说明：
    1.LinkedList类的head节点不存储任何数据，数据存储统一从head.next开始。
    2.LinkedList类可以删除数据头节点(head.next)，尾结点。
"""


# Node of a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_next(self, next_node):
        self.next = next_node
    
    def get_next(self):
        return self.next
    
    def has_next(self):
        return self.next is not None
        # return self.next != None


# class for defining a linked list
class LinkedList(object):
    
    def __init__(self):
        self.length = 0
        self.head = Node('head')
    
    """create
    说明：
        1.前插法
        2.后插法
    这里没有在一个func中实现，insert_create_linked_list.py中有.
    """
    
    def add_node(self, node):
        """给链表添加一个新的结点
        说明：
            1.按照此处的实现逻辑，是后插法创建单链表。
            2.创建链表时候插入节点有两种情况：1.添加在头 2.添加在尾
        """
        if self.length == 0:
            self.add_begin(node)
        else:
            self.add_last(node)
    
    def add_begin(self, node):
        if self.length == 0:
            # 将新的头结点 添加 到头部
            self.head.next = node
            self.length += 1
        else:
            node.next = self.head.next
            self.head.next = node
            self.length += 1
    
    def add_last(self, node):
        # 确定最后一个 是 最后一个
        cur = self.head.next
        while cur.next is not None:
            cur = cur.next
        
        # 定义出一个新的 尾结点
        node.next = None
        
        # 将新定义的尾节点 添加在 尾部
        cur.next = node
        self.length += 1
    
    """insert or delete
    func add_node_after_value()
    func add_node_at_pos()
    func del_begin()
    func del_last()
    func del_value()
    func del_at_pos()
    """
    
    def add_node_after_value(self, value, node):
        """输入value，在value匹配节点的后一位处插入node
        增加了对于最后一个节点的适应！！！但是实际上的链表是不能在最后插入的！！！
        """
        insert = node
        cur = self.head

        # 除最后一个节点外的所有节点
        while cur.next is not None:
            if cur.data == value:
                # 在cur和cur.next之间插入mid
                insert.next = cur.next
                cur.next = insert

                self.length += 1
                return  # 结束符
            else:
                cur = cur.next

        # 最后一个节点单独讨论
        if not cur.next and cur.data == value:
            cur.next = insert
            self.length += 1
            return

        # 所有节点都不满足
        print('提供的value值不存在匹配情况!')
    
    def add_node_at_pos(self, pos, node):
        """在指定的位置pos处插入一个node
        """
        count = 0  # 计数，用于判断是否达到pos; 表头是不存储数据的
        cur_node = self.head.next
        pre_node = self.head
        
        # 当输入的 pos 不符合要求
        if pos > self.length or pos < 0:
            print('输入的位置不符合要求，请重新输入！')
        
        # 当输入的 pos 符合要求
        else:
            
            # 当存在下一个node 或者 用于计数的count小于pos
            # 通俗的说：当能够往下走
            while cur_node.next is not None or count < pos:
                count = count + 1
                
                # 到达了输入位置
                if count == pos:
                    
                    # 相当于在 pre 和 cur 之间插入一个node
                    #  #######  #######        #######  ########  #######
                    #  # pre #  # cur #  --->  # pre #  # node #  # cur #
                    #  #######  #######        #######  ########  #######
                    
                    pre_node.next = node
                    node.next = cur_node
                    
                    self.length += 1
                    return
                
                # 未到达输入位置（一般都是先执行，而且点数越多概率越大）
                else:
                    
                    # 相当于整体往后平移一个结点, 以便于while循环反复判断
                    #  #######  #######        ######  #######  #######
                    #  # pre #  # cur #  --->  #    #  # pre #  # cur #
                    #  #######  #######        ######  #######  #######
                    pre_node = cur_node
                    cur_node = cur_node.next
    
    def del_begin(self):
        """删除链表的第一个"""
        if self.length == 0:
            print('链表为空，无法进行删除操作。')
        else:
            self.head = self.head.next
            self.length -= 1
    
    def del_last(self):
        """删除链表的最后一个"""
        if self.length == 0:
            print('链表为空，无需进行删除操作。')
        else:
            
            pre_node = self.head
            cur_node = self.head
            
            while cur_node.next is not None:
                pre_node = cur_node
                cur_node = cur_node.next
            else:
                pre_node.next = None
                self.length -= 1
    
    def del_value(self, value):
        """输入一个value，删除一个对应的点
        可以删除最后一个！
        也可以删除第一个！
        """
        pre = self.head
        cur = self.head.next  # 从这个节点开始比较
        
        while cur.next is not None:
            if cur.data == value:
                pre.next = cur.next
                self.length -= 1
                return  # 结束符
            else:
                pre = cur
                cur = cur.next
        
        # last node
        if not cur.next and cur.data == value:
            pre.next = None
            self.length -= 1
            return
        
        print('不存在值对应为' + str(value) + '的点')
    
    def del_at_pos(self, pos):
        """输入一个pos，删除一个对应的点"""
        count = 0
        pre = self.head
        cur = self.head
        
        if pos > self.length or pos < 0:
            print('输入了不符合要求的pos')
        # 这里可加对于1的判断，也可以不加
        else:
            while cur.next is not None or pos > count:
                count += 1
                if pos == count:
                    pre.next = cur.next
                    self.length -= 1
                    return  # 结束符
                else:
                    pre = cur
                    cur = cur.next
    
    def get_length(self):
        return self.length
    
    def get_first_node_value(self):
        if self.length == 0:
            return None  # 链表为空，输出头结点
        return self.head.next.data
    
    def get_last_node_value(self):
        if self.length == 0:
            return None  # 链表为空，输出头结点
        
        cur = self.head.next
        while cur.next is not None:
            cur = cur.next
        else:
            return cur.data
    
    def get_at_pos(self, pos):
        """输入一个pos，返回一个点"""
        cur = self.head.next
        count = 0
        
        if pos > self.length or pos < 0:
            return None
        elif pos == 0:
            return self.head.data
        else:
            while cur.next is not None or count < pos:
                count += 1
                if count == pos:
                    return cur.data
                else:
                    cur = cur.next
    
    def print_list(self):
        """输出链表(以值的方式)"""
        node_list = []
        cur = self.head.next
        
        while cur is not None:
            node_list.append(cur.data)
            cur = cur.next
        
        print(node_list)


if __name__ == '__main__':
    
    node_1 = Node(2)
    node_2 = Node(4)
    node_3 = Node(6)
    node_4 = Node(8)
    node_5 = Node(10)
    node_6 = Node(12)
    # 使用后插法，创建
    link_list_one = LinkedList()
    link_list_one.add_node(node_1)
    link_list_one.add_node(node_2)
    link_list_one.add_node(node_3)
    link_list_one.add_node(node_4)
    link_list_one.add_node(node_5)
    link_list_one.add_node(node_6)
    
    
    
    print('func print_list() test:')
    link_list_one.print_list()
    print()
    
    
    
    # print('func add_begin() test:')
    # link_list_one.add_begin(Node(1))
    # link_list_one.print_list()
    # print()
    
    
    
    # print('func add_last() test:')
    # link_list_one.add_last(Node(100))
    # link_list_one.print_list()
    # print()
    
    
    
    # print('func add_node_after_value() test:')
    # print("原: ")
    # link_list_one.print_list()
    # print()
    #
    # print("value: 6" + '\n' + "node: Node(11)")
    # link_list_one.add_node_after_value(6, Node(11))
    # link_list_one.print_list()
    # print()
    #
    # print("value: 12" + '\n' + "node: Node(13)")
    # link_list_one.add_node_after_value(12, Node(13))
    # link_list_one.print_list()
    # print()
    #
    # print("value: 2" + '\n' + "node: Node(1)")
    # link_list_one.add_node_after_value(2, Node(1))
    # link_list_one.print_list()
    # print()
    #
    # print("value: 13" + '\n' + "node: Node(88)")
    # link_list_one.add_node_after_value(13, Node(88))
    # link_list_one.print_list()
    # print()
    #
    # print("value: 512" + '\n' + "node: Node(102)")
    # link_list_one.add_node_after_value(512, Node(102))
    # link_list_one.print_list()
    # print()
    
    
    
    # print('func add_node_at_pos test')
    # print("原：")
    # link_list_one.print_list()
    # print()
    #
    # print('pos: 6' + "\n" + "node: Node(41)")
    # link_list_one.add_node_at_pos(6, Node(41))
    # link_list_one.print_list()
    # print()
    #
    # print('pos: 12' + "\n" + "node: Node(42)")
    # link_list_one.add_node_at_pos(12, Node(42))
    # link_list_one.print_list()
    # print()
    #
    # print('pos: 6' + "\n" + "node: Node(43)")
    # link_list_one.add_node_at_pos(6, Node(43))
    # link_list_one.print_list()
    # print()
    
    
    
    # print('func del_begin test:')
    # print('原：')
    # link_list_one.print_list()
    # link_list_one.del_begin()
    # print('del_begin之后：')
    # link_list_one.print_list()
    # print()
    #
    # print('原：')
    # LinkedList().print_list()
    # LinkedList().del_begin()
    # print('del_begin之后：')
    # link_list_one.print_list()
    # print()
    
    
    
    # print('func del_last test:')
    # print('原：')
    # link_list_one.print_list()
    # link_list_one.del_last()
    # print('del_last之后：')
    # link_list_one.print_list()
    # print()
    #
    # print('原：')
    # LinkedList().print_list()
    # LinkedList().del_last()
    # print('del_begin之后：')
    # link_list_one.print_list()
    # print()
    
    
    
    # print('func del_value test:')
    # print('原：')
    # link_list_one.print_list()
    # print()
    #
    # print('value: 1')
    # link_list_one.del_value(1)
    # link_list_one.print_list()
    # print(link_list_one.get_length())
    # print()
    #
    # print('value: 2')
    # link_list_one.del_value(2)
    # link_list_one.print_list()
    # print(link_list_one.get_length())
    # print()
    #
    # print('value: 4')
    # link_list_one.del_value(4)
    # link_list_one.print_list()
    # print(link_list_one.get_length())
    # print()
    #
    # print('value: 10')
    # link_list_one.del_value(10)
    # link_list_one.print_list()
    # print(link_list_one.get_length())
    # print()
    #
    # print('value: 12')
    # link_list_one.del_value(12)
    # link_list_one.print_list()
    # print(link_list_one.get_length())
    # print()
    
    
    
    # print('func get_at_pos test: ')
    # print('原：')
    # link_list_one.print_list()
    # print()
    #
    # print('pos: 0')
    # print(link_list_one.get_at_pos(0))
    # print()
    #
    # print('pos: 1')
    # print(link_list_one.get_at_pos(1))
    # print()
    #
    # print('pos: 6')
    # print(link_list_one.get_at_pos(6))
    # print()
    #
    # print('pos: 7')
    # print(link_list_one.get_at_pos(7))
    # print()
    
    
    
    
    # print('func get_first_node_value test: ')
    # print('原：')
    # link_list_one.print_list()
    # print()
    # print('执行get_first_node_value()后: ')
    # print(link_list_one.get_first_node_value())
    # print()
    #
    # print('只带有头结点的链表: ')
    # print(LinkedList().get_first_node_value())
    # print()
    
    
    
    
    # print('func get_last_node_value test: ')
    # print('原：')
    # link_list_one.print_list()
    # print()
    # print('get_last_node_value后: ')
    # print(link_list_one.get_last_node_value())
    # print()
    #
    # print('只带有头结点的链表: ')
    # print(LinkedList().get_last_node_value())
    # print()
