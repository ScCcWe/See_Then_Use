#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

DEFAULT_LINE_COLOR = QColor(0, 255, 0, 128)
DEFAULT_FILL_COLOR = QColor(255, 0, 0, 128)
DEFAULT_SELECT_LINE_COLOR = QColor(255, 255, 255)
DEFAULT_SELECT_FILL_COLOR = QColor(0, 128, 255, 155)
DEFAULT_VERTEX_FILL_COLOR = QColor(0, 255, 0, 255)  # 第四个参数255，代表完全不透明。如果改成100.则是透明。这里的0，255，0表示绿色
DEFAULT_HVERTEX_FILL_COLOR = QColor(255, 0, 0)  # 红色
MIN_Y_LABEL = 10


class Shape(object):
    P_SQUARE, P_ROUND = range(2)

    MOVE_VERTEX, NEAR_VERTEX = range(2)  # MOVE_VERTEX, NEAR_VERTEX = 0， 1

    # The following class variables influence the drawing
    # of _all_ shape objects.
    line_color = DEFAULT_LINE_COLOR
    fill_color = DEFAULT_FILL_COLOR
    select_line_color = DEFAULT_SELECT_LINE_COLOR  # 默认颜色
    select_fill_color = DEFAULT_SELECT_FILL_COLOR
    vertex_fill_color = DEFAULT_VERTEX_FILL_COLOR  # QColor(0, 255, 0, 255)
    hvertex_fill_color = DEFAULT_HVERTEX_FILL_COLOR
    point_type = P_ROUND
    point_size = 8
    scale = 1.0

    def __init__(self, label=None, line_color=None, difficult=False, paintLabel=False):
        self.label = label
        self.points = []  # 列表
        self.fill = False
        self.selected = False
        self.difficult = difficult
        self.paintLabel = paintLabel

        self._highlightIndex = None
        self._highlightMode = self.NEAR_VERTEX
        self._highlightSettings = {
            self.NEAR_VERTEX: (4, self.P_ROUND),
            self.MOVE_VERTEX: (1.5, self.P_SQUARE),
        }

        self._closed = False  # 私有属性，不建议在类的外面调用

        if line_color is not None:
            # Override the class line_color attribute
            # with an object attribute. Currently this
            # is used for drawing the pending line a different color.
            self.line_color = line_color

    def close(self):
        self._closed = True

    def reachMaxPoints(self):
        # 到达最大点数？
        # 列表数量超过2，输出为True，有什么用呢？做一个标记吗？
        if len(self.points) >= 4:
            return True
        return False

    def addPoint(self, point):
        # 只有列表不大于2时，才可以加入点
        if not self.reachMaxPoints():  # if not False:  执行下面的append，只有列表没大于4的时候，才可以加入点
            self.points.append(point)

    def popPoint(self):
        # 列表存在即可弹出值
        if self.points:
            return self.points.pop()  # return 弹出的值
        return None

    def isClosed(self):
        return self._closed  # self._closed默认为False

    def setOpen(self):
        self._closed = False

    def paint(self, painter):
        try:
            if self.points:
                color = self.select_line_color if self.selected else self.line_color
                # 这里颜色默认为self.line_color，也就是用户输入
                # 改变self.selected为True时，颜色为self.select_line_color
    
                pen = QPen(color)
                # Try using integer sizes for smoother drawing(?)
                pen.setWidth(max(1, int(round(2.0 / self.scale))))
                painter.setPen(pen)
    
                line_path = QPainterPath()
                vrtx_path = QPainterPath()
                line_path.moveTo(self.points[0])  # 从鼠标点击的第一个点开始
                # Uncommenting the following line will draw 2 paths
                # for the 1st vertex, and make it non-filled, which
                # may be desirable.
                # self.drawVertex(vrtx_path, 0)

                # 这里是鼠标拖拽结束了，画出那个成品图
                for i, p in enumerate(self.points):
                    line_path.lineTo(p)  # p: type: QPointF  画出线  这里是顺时针方向画三条， 下面会补上一条
                    self.drawVertex(vrtx_path, i)  # 画出顶点
                if self.isClosed():  # 默认为False，没关闭，
                    # 最后一个点跟矩阵的第一个点相连
                    line_path.lineTo(self.points[0])

                painter.drawPath(line_path)
                painter.drawPath(vrtx_path)
                painter.fillPath(vrtx_path, self.vertex_fill_color)  # 填充路径，前面是路径，后面是Qcolor

                # Draw text at the top-left
                if self.paintLabel:
                    min_x = sys.maxsize
                    min_y = sys.maxsize
                    for point in self.points:
                        min_x = min(min_x, point.x())
                        min_y = min(min_y, point.y())
                    if min_x != sys.maxsize and min_y != sys.maxsize:
                        font = QFont()
                        font.setPointSize(8)
                        font.setBold(True)
                        painter.setFont(font)
                        if(self.label == None):
                            self.label = ""
                        if(min_y < MIN_Y_LABEL):
                            min_y += MIN_Y_LABEL
                        painter.drawText(min_x, min_y, self.label)
    
                if self.fill:
                    color = self.select_fill_color if self.selected else self.fill_color
                    painter.fillPath(line_path, color)
        except Exception as e:
            print('Error in paint:', e)

    def drawVertex(self, path, i):
        d = self.point_size / self.scale  # 8.0
        shape = self.point_type
        point = self.points[i]
        if i == self._highlightIndex:
            size, shape = self._highlightSettings[self._highlightMode]
            d *= size
        if self._highlightIndex is not None:
            self.vertex_fill_color = self.hvertex_fill_color
        else:
            self.vertex_fill_color = Shape.vertex_fill_color
        # 画出四个点
        if shape == self.P_SQUARE:
            path.addRect(point.x() - d / 2, point.y() - d / 2, d, d)
        elif shape == self.P_ROUND:
            path.addEllipse(point, d / 2.0, d / 2.0)
        else:
            assert False, "unsupported vertex shape"

    def nearestVertex(self, point, epsilon):
        """寻找最近的点，也就是识别一个可以拖动的点"""
        for i, p in enumerate(self.points):
            # enumerate枚举
            # i = index, p = value
            # print(i, p)
            if distance(p - point) <= epsilon:
                # print(i)
                return i
        return None

    def containsPoint(self, point):
        return self.makePath().contains(point)

    def makePath(self):
        path = QPainterPath(self.points[0])
        for p in self.points[1:]:
            path.lineTo(p)
        return path

    def boundingRect(self):
        return self.makePath().boundingRect()

    def moveBy(self, offset):
        self.points = [p + offset for p in self.points]

    def moveVertexBy(self, i, offset):  # offset?
        self.points[i] = self.points[i] + offset

    def highlightVertex(self, i, action):
        # 顶点高亮
        self._highlightIndex = i
        self._highlightMode = action

    def highlightClear(self):
        self._highlightIndex = None

    def copy(self):
        shape = Shape("%s" % self.label)
        shape.points = [p for p in self.points]
        shape.fill = self.fill
        shape.selected = self.selected
        shape._closed = self._closed
        if self.line_color != Shape.line_color:
            shape.line_color = self.line_color
        if self.fill_color != Shape.fill_color:
            shape.fill_color = self.fill_color
        shape.difficult = self.difficult
        return shape

    def __len__(self):
        return len(self.points)

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, value):
        self.points[key] = value
