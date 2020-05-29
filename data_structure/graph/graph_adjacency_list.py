# !/usr/bin/python 
# -*- coding: utf-8 -*-
# file_name: graph_adjacency_list.py
# function：None
# need_module: None
# author: ScCcWe
# time: 2020/1/20 14:49

"""采用 邻接表表示法 创建 无向图
[算法步骤]：
    1.输入总顶点数和总边数
    2.依次输入点的信息存入顶点表中，使每个表头节点的指针域初始化为NULL
    3.创建邻接表。依次输入每条边依附的两个顶点，确定这两个顶点的序号i和j之后，将此边节点分别插入vi和vj对应的两个边链表的头部。
"""

import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        """增加一个邻接点"""
        self.adjacent[neighbor] = weight
    
    def get_connections(self):
        return self.adjacent.keys()
    
    def get_vertex_id(self):
        return self.id
    
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    def set_distance(self, dis):
        self.distance = dis
    
    def get_distance(self):
        return self.distance
    
    def set_previous(self, pre):
        self.previous = pre
    
    def set_visited(self):
        self.visited = True
    
    def __str__(self):
        return str(self.id) + "adjacent: " + str([x.id for x in self.adjacent])
    
    
class Graph:
    def __init__(self):
        
        # 存放新加入顶点的字典，故self.vertex_dictionary[n] 可以调用 Vertex()类的所有类方法
        #          比如下面用到的self.vertex_dictionary[frm]；self.vertex_dictionary[to]
        self.vertex_dictionary = {}
        
        # 顶点总数记录
        self.vertices_num_count = 0
    
    def __iter__(self):
        return iter(self.vertex_dictionary.values())
    
    def add_vertex(self, node):
        """输入一个新顶点，将其加入顶点字典"""
        self.vertices_num_count = self.vertices_num_count + 1  # 顶点总数 + 1
        new_vertex = Vertex(node)
        self.vertex_dictionary[node] = new_vertex  # 将 新顶点new_vertex 存入 顶点字典vertex_dictionary
        # print(self.vertex_dictionary)
        return new_vertex  # ？？？ 这个有什么用 ？？？
    
    def get_vertex_neighbor_list(self, n):
        """获取 n(id) 的 邻接列表
        注意: 这个方法需要在输入n的邻接点，也就是调用add_edge()之后，return才会不为空!!!
        :param n: 输入的一个 id 类似于 'a', 使用时和 index 用法相同
        :return: 输出 n(id) 的 邻接列表
        """
        if n in self.vertex_dictionary:
            return self.vertex_dictionary[n]
        else:
            return None
    
    def add_edge(self, frm, to, cost=0):
        """
        增加边的关系
        :param frm: 即from，该边的(一个/任意顶点。（无向图可以加上任意，有向图不行）
        :param to: 即to，该边的另一个/任意顶点。（无向图可以加上任意，有向图不行）
        :param cost:
        :return:
        """
        
        # 首先是一个判断，确保存在 frm 和 to 的存在
        if frm not in self.vertex_dictionary:
            self.add_vertex(frm)
        if to not in self.vertex_dictionary:
            self.add_vertex(to)
        
        # 方法的实体, 即调用 Vertex类 的 类方法add_neighbor()
        self.vertex_dictionary[frm].add_neighbor(self.vertex_dictionary[to], cost)
        self.vertex_dictionary[to].add_neighbor(self.vertex_dictionary[frm], cost)  # 有向图去掉本行即可
    
    def get_vertices(self):
        """输出顶点的id，好像没什么用。。。"""
        return self.vertex_dictionary.keys()
    
    def set_pre(self, current):
        self.pre = current
    
    def get_pre(self, current):
        return self.pre
    
    @staticmethod
    def get_edges():
        """
        
        :return:
        """
        edges = []
        for v in G:
            for w in v.get_connections():
                vid = v.get_vertex_id()
                wid = w.get_vertex_id()
                edges.append((vid, wid, v.get_weight(w)))
                # print((vid, wid, v.get_weight(w)))
        return edges
    

if __name__ == '__main__':
    G = Graph()
    
    # 依次输入点的信息 并且 将信息存入顶点字典中
    G.add_vertex('a')
    G.add_vertex('b')
    G.add_vertex('c')
    G.add_vertex('d')
    G.add_vertex('e')
    print('输入邻接点之前:')
    if G.get_vertex_neighbor_list('a') is not None:
        print(G.get_vertex_neighbor_list('a'))
    
    print('顶点的id：')
    print(G.get_vertices())
    
    # 依次输入每条边依附的2个顶点
    # 并且插入
    G.add_edge('a', 'b', 4)
    print('输入邻接点之后：')
    if G.get_vertex_neighbor_list('nihao') is not None:
        print(G.get_vertex_neighbor_list('a'))
    print('输入邻接点之后：')
    if G.get_vertex_neighbor_list('a') is not None:
        print(G.get_vertex_neighbor_list('a'))
    G.add_edge('a', 'c', 1)
    G.add_edge('c', 'b', 2)
    G.add_edge('b', 'e', 4)
    G.add_edge('c', 'd', 4)
    G.add_edge('d', 'e', 4)
    print('Graph data:')
    print(G.get_edges())
"""邻接表 表示 图
[算法步骤]：
    1.输入总顶点数和总边数
    2.依次输入点的信息存入顶点表中，使每个表头节点的指针域初始化为NULL
    3.创建邻接表。依次输入每条边依附的两个顶点，确定这两个顶点的序号i和j之后，将此边节点分别插入vi和vj对应的两个边链表的头部。
"""
