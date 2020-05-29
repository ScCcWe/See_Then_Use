# !/usr/bin/python
# -*- coding: utf-8 -*-
# file_name: 03_class_bintree.py
# function：None
# need_module: None
# author: ScCcWe
# time: 2020/1/13 15:36


class BinTree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    """三个赋值"""
    
    def set_bin_tree_ins(self, bin_tree_ins_node_value):
        self.data = bin_tree_ins_node_value
    
    def set_left(self, left_child):
        self.left = left_child
    
    def set_right(self, right_child):
        self.right = right_child
    
    """三个取值"""
    
    def get_data(self):
        return self.data
    
    def left_child(self):
        return self.left
    
    def right_child(self):
        return self.right
    
    """判断为空"""
    
    def is_empty(self):
        return self.data is None
    
    """insert(插入)操作"""
    
    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinTree(new_node)
        else:
            temp = BinTree(new_node)
            temp.left = self.left  # 如果当前插入的节点存在左子树，则该存在的左子树变成即将要插入的节点的左子树；
            self.left = temp
            
    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinTree(new_node)
        else:
            bottle = BinTree(new_node)
            bottle.right = self.right
            self.right = bottle


def sequence_traverse(t):
    """
    层序遍历（按照层次进行遍历，没有办法使用递归。可以通过不断的添加 left 和 right）
    这里使用队列来进行层序遍历（先进先出符合层序遍历的要求）
    """
    if t is None:
        return
    seq_list = []
    import queue
    q = queue.Queue()  # 使用队列来进行层序遍历，先进先出，符合层序遍历的要求
    q.put(t)
    while not q.empty():
        node = q.get()
        seq_list.append(node.data)
        
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    
    return seq_list


def in_order_traverse(t):
    """
    中序遍历（先左，后根，右）
    非递归（通过创建一个类似于栈的逻辑实现 -> 通过 append 进 list，左子树全部 append 之后，在进行 pop 即可实现）
    """
    if t is None:
        return []
    stack = []
    node = t
    in_order_list = []
    while stack or node:
        if node:                # 当有左子树时
            stack.append(node)  # 不断的append
            node = node.left    # 一直 left 到最左下角的 叶子
        else:                   # 没有左子树之后
            node = stack.pop()  # 弹出最后一个append的左叶子
            in_order_list.append(node.data)  # append 左叶子的值
            node = node.right   # 如果这个append的左叶子有右叶子，则将右叶子加入stack，然后弹出，取值。
    return in_order_list        # 因为 append 是在上面，所以永远不需要担心，根节点没有被append的问题


def data_left_right_traverse(t):
    """
    前序遍历
    非递归
    说明：二叉树的前序和中序遍历基本一样，稍作修改即可，这里不再给出注释。
    """
    if t is None:
        return []
    stack = []
    node = t
    DLR_list = []
    while stack or node:
        if node:
            stack.append(node)
            DLR_list.append(node.data)  # 只需要将 append 修改到 left 之前即可
            node = node.left
        else:
            node = stack.pop()
            node = node.right
    return DLR_list


def left_right_data_reverse(t):
    """
    后续遍历
    非递归
    说明：二叉树的后续遍历和前序，中序有点不太一样。后续遍历中，具有右子树的节点需要使用2次！
    """
    if t is None:
        return []
    visited = set()
    stack = []
    node = t
    LRD_list = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and node.right not in visited:  # 具有右子树的节点第二次使用时，就不要在考虑右子树了
                stack.append(node)  # 需要通过节点连接右子树，所以具有右子树的节点，要使用2次！这里将其加上
                node = node.right
            else:
                visited.add(node)
                LRD_list.append(node.data)
                node = None  # 防止进入 if node 条件
    return LRD_list


mid_list = []


def mid_traverse(t):
    """
    中序遍历(先左，后根，右)
    递归
    """
    if t is None:
        return []
    if t.left:
        mid_traverse(t.left)
    if t.data:
        mid_list.append(t.data)
    if t.right:
        mid_traverse(t.right)
    return mid_list


pre_list = []


def pre_traverse(t):
    """
    先序遍历(先根，后左，右)
    递归
    """
    if t is None:
        return
    pre_list.append(t.data)
    if t.left:
        pre_traverse(t.left)
    if t.right:
        pre_traverse(t.right)
    return pre_list


aft_list = []


def aft_traverse(t):
    """
    后续遍历（先左，后右，根）
    递归
    """
    if t is None:
        return
    aft_traverse(t.left)
    aft_traverse(t.right)
    aft_list.append(t.data)
    return aft_list


def num_nodes_recursive(t):
    """计算节点数量
    算法步骤：
        如果是空树，则为0；
            否则节点个数为左子树的节点个数 + 右子树的节点个数 + 1 （这个1是根节点，如果递归来看的话，是每一个根节点）
    说明：
        1.关于 1 的说明和简单的理解：
        这个1是每一个根节点，也是之所以能使用递归的原因。
        因为每一个子树都有一个跟节点，
        而这里的递归就是将所有树变成只有一个跟节点的树叶就是叶子。
        
        2.对待递归的态度和方法：
        递归是不容易理解的，当你遇到不是很清除的递归方法时。
        可以使用纸笔进行简单演示，例如这里的递归计算节点数量。
        如果用纸笔稍微演示一下，便很清楚了。
    """
    if t is None:
        return 0
    else:
        return 1 + num_nodes_recursive(t.left) + num_nodes_recursive(t.right)


def copy_tree(t):
    """复制树
    说明：直接使用深拷贝，可能有一些欠妥，因为完全没有什么实现逻辑
    """
    assert (isinstance(t, BinTree))
    if t is None:
        return None
    else:
        import copy
        tree = copy.deepcopy(t)
        return tree


def get_tree_deep(t):
    """获取二叉树的深度
    算法步骤：
        如果是空树，深度为0；否则：
            递归计算左子树的深度记为 m；
            递归计算右子树的深度记为 n；
            如果 m 大于 n ，二叉树的深度为 m+1 , 反之为 n+1
    
    说明：
        光是看算法步骤的话，这个递归很容易不能理解。
    
    个人的理解：
        只要在向上走；就会一直循环一个+1，别管什么 m，n，它们的初始值都是 0 ，所以根本不需要考虑谁大！
        这是因为最小树(即叶子)是没有子树的，所以输出为1(m，n 的初始值为0，就有 0 = 0 -> 0 + 1 = 1 此处执行的是 else 下的 return n + 1)
        而跟着叶子往上走的路线，永远都会+1，因为它永远比不是叶子的路线大(最少)1;
        所以实际上，真正计算的从来都只有一条路线。
    """
    if t is None:
        return 0
    else:
        m = get_tree_deep(t.left)
        # print('m: {}'.format(m))
        n = get_tree_deep(t.right)
        # print('n: {}'.format(n))
        if m > n:
            return m + 1
        else:
            return n + 1


def reverse_tree(t):
    """镜像反转二叉树
    说明：逻辑参考层序遍历，将每一个节点的左右子树(即 node.left 和 node.right)调换即可
    """
    if t is None:
        return None
    import queue
    q = queue.Queue()
    q.put(t)
    while not q.empty():
        node = q.get()
        node.left, node.right = node.right, node.left
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    
    return t


# bintree instance
bin_tree_ins = BinTree(1)
# print(bin_tree_ins.get_data())
bin_tree_ins.insert_left(4)
bin_tree_ins.insert_right(3)
bin_tree_ins.insert_left(2)

print('总节点数: {}'.format(num_nodes_recursive(bin_tree_ins)))
copy_tree = copy_tree(bin_tree_ins)
copy_tree.set_bin_tree_ins(10)
print("先序遍历复制树: {}".format(data_left_right_traverse(copy_tree)))
reverse_tree(copy_tree)
print("先序遍历反转树: {}".format(data_left_right_traverse(copy_tree)))
print('树的深度：{}'.format(get_tree_deep(BinTree(2))))
print('树的深度：{}'.format(get_tree_deep(bin_tree_ins)))
print()
print('层序遍历: {}'.format(sequence_traverse(bin_tree_ins)))
print('递归先序遍历: {}'.format(pre_traverse(bin_tree_ins)))
print('递归中序遍历: {}'.format(mid_traverse(bin_tree_ins)))
print('递归后序遍历: {}'.format(aft_traverse(bin_tree_ins)))
print("非递归先序遍历: {}".format(data_left_right_traverse(bin_tree_ins)))
print("非递归中序遍历: {}".format(in_order_traverse(bin_tree_ins)))
print("非递归后序遍历: {}".format(left_right_data_reverse(bin_tree_ins)))
