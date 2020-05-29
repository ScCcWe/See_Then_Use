# !/usr/bin/python 
# -*- coding: utf-8 -*-
# file_name: graph_adjacency_matrix.py
# function：图的邻接矩阵表示
# need_module: None
# author: ScCcWe
# time: 2020/1/19 9:40
"""图的邻接矩阵表示
算法步骤：
    1.输入总顶点数和总边数
    2.依次输入点的信息存入顶点表中
    3.初始化邻接矩阵，使每个权值初始化为极大值
    4.构造邻接矩阵。依次输入每条边依附的顶点和其权值，确定两个顶点在图中的位置之后，使相应变赋予相应的权值，同时使其对称边赋予
    相同的权值。
"""


class Vertex(object):
    def __init__(self, node):
        self.name = node
        
        # 将所有节点标记为未访问
        self.visited = False
    
    def __str__(self):
        return str(self.name)
    
    def add_neighbor(self, neighbor, g):
        g.add_edge(self.name, neighbor)
    
    def get_connections(self, g):
        return g.adj_matrix[self.name]
    
    def get_vertex_name(self):
        return self.name
    
    def set_vertex_name(self, name):
        self.name = name
    
    def set_visited(self):
        self.visited = True
    

class Graph(object):
    def __init__(self, num_vertices):
        """
        初始化图
            1.二维列表提供邻接矩阵
            2.一维列表提供顶点信息
        :param num_vertices: 总顶点数
        :param cost: 边的值
        """
        
        # 邻接矩阵(二维列表存储)
        self.adj_matrix = [[-1] * num_vertices for _ in range(num_vertices)]  # 这里的 _ 只是控制循环进行，不会实际被引用
        # print(self.adj_matrix)
        
        # 总顶点数
        self.num_vertices = num_vertices
        
        # 顶点信息(一维列表存储)
        self.vertices = []
        for i in range(0, num_vertices):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)
        # print(self.vertices)
    
    def set_vertex(self, index, name):
        """
        输入顶点的信息
        :param index: 顶点的序号(从多少开始自己定义, 这里是从0, 从1也行, 就是代码要改, 最后, 不建议从1开始!)
        :param name: 顶点的名称
        """
        # 这边就是从0开始，因为这里是 <=
        # 从 0 开始的好处有很多，这里不再赘述
        if 0 <= index < self.num_vertices:
            # 从 0 开始符合 list 的 index 取值
            self.vertices[index].set_vertex_name(name)
    
    def get_vertex_index(self, name):
        """
        根据顶点名字获取顶点序号
        :param name: 顶点名字
        :return: index or -1
        """
        for index in range(0, self.num_vertices):
            if name == self.vertices[index].get_vertex_name():
                return index
        return -1  # 这里的 -1 在方法 add_edge 中还会用到
    
    def add_edge(self, frm, to, cost=0):
        """
        输入边信息
        :param frm: 一个顶点
        :param to: 另一个顶点(在无向图中，先后是无所谓的)
        :param cost: 边的权值
        :return:
        """
        if self.get_vertex_index(frm) != -1 and self.get_vertex_index(to) != -1:  # 当前后2个顶点都存在时：
            self.adj_matrix[self.get_vertex_index(frm)][self.get_vertex_index(to)] = cost
            
            # 有向图不需要添加
            self.adj_matrix[self.get_vertex_index(to)][self.get_vertex_index(frm)] = cost
    
    """
    输出
    """
    
    def print_matrix(self):
        """以邻接矩阵的存储方式输出图"""
        row_whole = []
        for u in range(0, self.num_vertices):
            row = []
            for v in range(0, self.num_vertices):
                row.append(self.adj_matrix[u][v])
                row_whole.append(self.adj_matrix[u][v])
            print(row)
        # print(row_whole)

    def get_edges(self):
        """输出边的信息"""
        edges = []
        for v in range(0, self.num_vertices):
            for u in range(0, self.num_vertices):
                if self.adj_matrix[u][v] != -1:
                    vid = self.vertices[v].get_vertex_name()
                    wid = self.vertices[u].get_vertex_name()
                    edges.append((vid, wid, self.adj_matrix[u][v]))
        return edges
    
    def get_vertices(self):
        """输出 当前 的顶点信息"""
        vertices = []
        for vertxin in range(0, self.num_vertices):
            vertices.append(self.vertices[vertxin].get_vertex_name())
        return vertices
    

if __name__ == '__main__':
    G = Graph(5)
    G.set_vertex(0, 'a')
    G.set_vertex(1, 'b')
    G.set_vertex(2, 'c')
    G.set_vertex(3, 'd')
    G.set_vertex(4, 'e')
    print(G.get_vertex_index('b'))
    print(G.get_vertex_index('F'))
    print('Graph data:')
    G.add_edge('a', 'e', 10)
    G.add_edge('a', 'c', 20)
    G.add_edge('c', 'b', 30)
    G.add_edge('b', 'e', 40)
    G.add_edge('e', 'd', 50)
    G.add_edge('f', 'e', 60)
    print(G.print_matrix())
    print(G.get_edges())
    print(G.get_vertices())
"""
可以看到，我们创建一个具有五个顶点的无向图，用了 5x5 共 25 步
确实，该算法的时间复杂度为O(n2)
"""
