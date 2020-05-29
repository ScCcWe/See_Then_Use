from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from shape import Shape

CURSOR_DEFAULT = Qt.ArrowCursor  # 0
CURSOR_POINT = Qt.PointingHandCursor  # 13
CURSOR_DRAW = Qt.CrossCursor  # 2
CURSOR_MOVE = Qt.ClosedHandCursor  # 18
CURSOR_GRAB = Qt.OpenHandCursor  # 17


class Canvas(QWidget):
    selectionChanged = pyqtSignal(bool)
    shapeMoved = pyqtSignal()
    newShape = pyqtSignal()
    CREATE, EDIT = list(range(2))  # CREATE, EDIT = [0, 1]
    epsilon = 11.0
    
    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)
        self.painter = QPainter()
        self.pixmap = QPixmap()
        # self = MyLabel(self)
        self.mode = self.EDIT  # 默认模式为编辑
        self.cursor = CURSOR_DEFAULT  # 默认为鼠标手型
        
        # 初始点，move位置，结束点
        self.start_point = None
        self.pos = None
        self.end_point = None
        
        self.drawingLineColor = QColor(0, 0, 255)  #
        
        # 用于保存正在画的rect的2个顶点
        # 长度最大为2
        # 实时变化(指[1]位置)
        # 画下一个时会进行re操作
        self.current = []
        self.points = Shape(line_color=self.drawingLineColor)
        self.point_four = Shape(line_color=self.drawingLineColor)
        
        # 存储画好的rect
        # 例如：存储了两个已经画好的rect：
        # print(self.shapes)
        # [<AAA_labelImg_copy.shape.Shape object at 0x000002403CA45508>,
        # <AAA_labelImg_copy.shape.Shape object at 0x0000024043553FC8>]
        self.shapes = []
        self.shapes_remove = []
        
        # 未实现的功能
        # self.ten_bottle = QPointF()
        
        # 高亮的顶点
        self.hVertex = None
        
        self.visible = {}
        self.hShape = None
        
        self.selectedShape = None  # 存放选择的rect
        
        self.scale = 1.0  # 用于同一刻度
        
        self.offsets = QPointF(), QPointF()
        
        # 2019-11-19
        # for move shape
        self.prevPoint = QPointF()
        # 2019-11-20
        # for move shape
        self._hideBackround = False
        self.hideBackround = False
        
        self.setMouseTracking(True)
    
    def currentCursor(self):
        """输出当前手型"""
        cursor = QApplication.overrideCursor()
        if cursor is not None:
            cursor = cursor.shape()  # 默认输出的是0，
            # print('cursor in current: ', cursor)  # eg_print：18，17 具体可以参考最上面的默认
        return cursor
    
    def overrideCursor(self, cursor):
        # 使用input的cursor覆盖掉当前的手型
        self.cursor = cursor
        if self.currentCursor() is None:
            QApplication.setOverrideCursor(cursor)
            # print('cursor in 1: ', cursor)
        else:
            QApplication.changeOverrideCursor(cursor)
            # print('cursor in 2: ', cursor)
    
    def mode_to_create(self):
        self.mode = self.CREATE
        return self.mode
    
    def mode_to_edit(self):
        self.mode = self.EDIT
        return self.mode
    
    def creating(self):
        return self.mode == self.CREATE
    
    def editing(self):
        return self.mode == self.EDIT
    
    def out_of_pixmap(self, p):
        width, height = self.pixmap.width(), self.pixmap.height()
        # print(width, height)
        
        if 0 <= p.x() <= width and 0 <= p.y() <= height:
            return False
        return True
    
    def un_highlight(self):
        self.hVertex = None
    
    def selected_vertex(self):
        # 选中的顶点会高亮，这里判断hVertex即可
        return self.hVertex is not None
    
    def bounded_move_vertex(self, pos):
        """通过一个鼠标实时位置pos来移动这个选中的顶点，当然他是高亮的"""
        index, shape = self.hVertex, self.hShape  #
        # print('index, shape:', index, shape)
        point = shape[index]
        # print('point:', point)
        # if self.out_of_pixmap(pos):
        #     pos = self.intersectionPoint(point, pos)
        
        shiftPos = pos - point
        
        shape.moveVertexBy(index, shiftPos)
        
        lindex = (index + 1) % 4
        rindex = (index + 3) % 4
        lshift = None
        rshift = None
        if index % 2 == 0:  # index: 2, 4, 6, 8
            rshift = QPointF(shiftPos.x(), 0)
            lshift = QPointF(0, shiftPos.y())
        else:
            lshift = QPointF(shiftPos.x(), 0)
            rshift = QPointF(0, shiftPos.y())
        shape.moveVertexBy(rindex, rshift)
        shape.moveVertexBy(lindex, lshift)
    
    def isVisible(self, shape):
        # visable：可见
        # 是否可见
        return self.visible.get(shape, True)
    
    def selectedVertex(self):
        return self.hVertex is not None
    
    def setLastLabel(self, text):
        # 从这里添加label
        assert text  # 断言
        self.shapes[-1].label = text
        return self.shapes[-1]
    
    def mouseMoveEvent(self, event):
        # 通过第一个点和当前坐标更新线条
        # vertex和shape的移动也在这个方法中实现
        try:
            pos = self.transformPos(event.pos())
            # print(pos)
            
            # # 在状态栏实时的显示鼠标的位置
            # window = self.parent().window()
            # if window is not None:
            #     self.parent().window().labelCoordinates.setText(
            #         'X: %d; Y: %d' % (pos.x(), pos.y()))
            
            # 创建rect
            # 实现逻辑：将实时变化的第二个点存储在self.points中
            #          配合上paintEvent方法，就可以做到实时展示
            if self.creating():
                self.overrideCursor(CURSOR_DRAW)  # 出现十字手型
                if not self.out_of_pixmap(pos):
                    if event.buttons() & Qt.LeftButton:
                        # 左击拖拽更新rect的第二个点
                        # 永远保持len(self.points) <= 2
                        if len(self.points) == 1:
                            self.points.addPoint(pos)
                        elif len(self.points) == 2:
                            self.points.popPoint()
                            self.points.addPoint(pos)
                        self.repaint()
                    self.prevPoint = QPointF()
                elif self.out_of_pixmap(pos):
                    # 这里需要增加一个points
                    self.overrideCursor(CURSOR_DEFAULT)  # 如果在图片外，回到默认手形
                    # print('self.points[-1]', self.points[-1])
            else:
                self.prevPoint = pos
            
            # 移动顶点 vertex
            # 移动rect shape
            if not self.out_of_pixmap(pos):
                if Qt.LeftButton & event.buttons():  # 实现左击+拖拽
                    if self.selected_vertex():  # if self.hVertex is not None:
                        self.bounded_move_vertex(pos)
                        self.shapeMoved.emit()
                        self.repaint()
                    # elif self.selectedShape and self.prevPoint:
                    #     print('self.selectedShape:', self.selectedShape)
                    #     self.overrideCursor(CURSOR_MOVE)
                    #     self.boundedMoveShape(self.selectedShape, pos)
                    #     # self.shapeMoved.emit()
                    #     self.repaint()
                    return
                
                self.setToolTip("图片")  # 在画布外围，工具提示值为Image
                
                # 顶点和图形高亮
                for shape in reversed([s for s in self.shapes if self.isVisible(s)]):  # reversed()之后只在第一次遍历时返回值
                    # 寻找一个附近的顶点以突出高亮；
                    # 如果失败了，检查我们是否在形状的里面
                    index = shape.nearestVertex(pos, self.epsilon)  # self.epsilon == 11.0
                    if index is not None:  # 存在最近点
                        if self.selectedVertex():  # if self.hVertex is not None  移动顶点
                            self.hShape.highlightClear()  # 清除高亮
                        self.hVertex, self.hShape = index, shape
                        shape.highlightVertex(index, shape.MOVE_VERTEX)  # 顶点高亮, nidex：顶点的序列号
                        self.overrideCursor(CURSOR_POINT)  # 鼠标手型变为CURSOR_POINT
                        self.setToolTip("单击并拖动可以移动顶点(*￣︶￣)")  # 展示提示信息
                        self.setStatusTip(self.toolTip())
                        self.update()
                        break
                    # elif shape.containsPoint(pos):
                    #     if self.selectedVertex():
                    #         self.hShape.highlightClear()
                    #     self.hVertex, self.hShape = None, shape
                    #     self.setToolTip(
                    #         "单击并拖动可以移动这个矩形框 '%s'" % shape.label)
                    #     self.setStatusTip(self.toolTip())
                    #     self.overrideCursor(CURSOR_GRAB)
                    #     self.update()
                    #     break
                else:  # Nothing found, clear highlights, reset state.
                    if self.hShape:
                        self.hShape.highlightClear()
                        self.update()
                    self.hVertex, self.hShape = None, None
                    if self.currentCursor() == 2:
                        pass
                    else:
                        self.overrideCursor(CURSOR_DEFAULT)
        except Exception as e:
            print('Error in mouseMoveEvent:', e)
    
    def mousePressEvent(self, event):
        # 在打开本软件时，不能直接进入mouseMove功能，这个点还是需要修改的。
        try:
            pos = event.pos()
            self.start_point = self.transformPos(pos)
            
            if event.button() == Qt.LeftButton:
                if not self.out_of_pixmap(self.start_point):
                    if self.creating():
                        self.points.addPoint(self.start_point)
                    else:
                        self.selectShapePoint(pos)
                        self.prevPoint = pos
                        self.repaint()
                else:
                    QMessageBox.warning(self, 'WARNING',
                                        '不可以在图片外创建！！！',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        except Exception as e:
            print('Error in mousePressEvent:', e)
    
    def deSelectShape(self):
        if self.selectedShape:
            self.selectedShape.selected = False
            self.selectedShape = None
            self.setHiding(False)
            self.selectionChanged.emit(False)
            self.update()
    
    def selectShapePoint(self, point):
        """Select the first shape created which contains this point."""
        self.deSelectShape()
        if self.selectedVertex():  # A vertex is marked for selection.
            index, shape = self.hVertex, self.hShape
            shape.highlightVertex(index, shape.MOVE_VERTEX)
            self.selectShape(shape)
            return
        for shape in reversed(self.shapes):
            if self.isVisible(shape) and shape.containsPoint(point):
                self.selectShape(shape)
                self.calculateOffsets(shape, point)
                return
    
    def calculateOffsets(self, shape, point):
        rect = shape.boundingRect()
        x1 = rect.x() - point.x()
        y1 = rect.y() - point.y()
        x2 = (rect.x() + rect.width()) - point.x()
        y2 = (rect.y() + rect.height()) - point.y()
        self.offsets = QPointF(x1, y1), QPointF(x2, y2)
    
    def selectShape(self, shape):
        self.deSelectShape()  # re
        shape.selected = True
        self.selectedShape = shape
        self.setHiding()
        self.selectionChanged.emit(True)
        self.update()
    
    def setHiding(self, enable=True):
        self._hideBackround = self.hideBackround if enable else False
    
    def boundedMoveShape(self, shape, pos):
        # ？？？
        if self.out_of_pixmap(pos):
            return False  # No need to move
        o1 = pos + self.offsets[0]
        if self.out_of_pixmap(o1):
            pos -= QPointF(min(0, o1.x()), min(0, o1.y()))
        o2 = pos + self.offsets[1]
        if self.out_of_pixmap(o2):
            pos += QPointF(min(0, self.pixmap.width() - o2.x()),
                           min(0, self.pixmap.height() - o2.y()))
        # The next line tracks the new position of the cursor
        # relative to the shape, but also results in making it
        # a bit "shaky" when nearing the border and allows it to
        # go outside of the shape's area for some reason. XXX
        # self.calculateOffsets(self.selectedShape, pos)
        dp = pos - self.prevPoint
        if dp:
            shape.moveBy(dp)
            self.prevPoint = pos
            return True
        return False
    
    def mouseReleaseEvent(self, event):
        try:
            self.end_point = self.transformPos(event.pos())
            if not self.out_of_pixmap(self.end_point):
                if self.creating():
                    self.points.popPoint()
                    self.points.addPoint(self.end_point)
                    # print('self.points:', self.points)  # 一个shape
                    # print('self.points.points:', self.points.points)  # shape的2个point
                    import copy
                    self.point_four.points = self.points_to_point_four(copy.deepcopy(self.points))
                    # self.points: <AAA_labelImg_copy.shape.Shape object at 0x000002D5E3726708>
                    # self.points.points: [PyQt5.QtCore.QPoint(99, 195), PyQt5.QtCore.QPoint(384, 389)]
                    # print('self.point_four:', self.point_four)
                    # print('self.point_four.points:', self.point_four.points)
                    self.point_four.close()  # 最后一条线闭合
                    self.shapes.append(self.point_four)  # rect的信息就存储在self.shapes中
                    # print(self.shapes)
                    # 输出为2个对象时：
                    #  [<AAA_labelImg_copy.shape.Shape object at 0x000002403CA45508>,
                    # <AAA_labelImg_copy.shape.Shape object at 0x0000024043553FC8>]
                    
                    self.overrideCursor(CURSOR_DEFAULT)
                    # re self.point and self.point_four
                    # self.point self.point_four 作为中间件bottle存在
                    self.restart_status()
                    self.repaint()
                    
                    # 当以左键结束时，调用newShape
                    # 也就是在你结束框选时，会自动的出现一个labelDialog
                    # 这极大的丰富了交互
                    if event.button() == Qt.LeftButton:
                        self.newShape.emit()  # 信号发射
                else:
                    self.overrideCursor(CURSOR_DEFAULT)
                
                # 每一次新建rect完成之后，都会自动的将模式转换为edit
                self.mode_to_edit()
        except Exception as e:
            print('Error in mouseReleaseEvent:', e)
    
    def deleteSelected(self):
        # 删除选中的shape
        if self.selectedShape:
            shape = self.selectedShape
            self.shapes.remove(self.selectedShape)
            self.selectedShape = None
            self.update()
            return shape
    
    @staticmethod
    def points_to_point_four(points):
        # rect的2个顶点变成4个
        points_to_four = [QPointF(points[0].x(), points[0].y()), QPointF(points[1].x(), points[0].y()),
                          QPointF(points[1].x(), points[1].y()), QPointF(points[0].x(), points[1].y())]
        return points_to_four
    
    def restart_status(self):
        self.points = Shape(line_color=self.drawingLineColor)
        self.point_four = Shape(line_color=self.drawingLineColor)
    
    def load_pixmap(self, pixmap):
        # 加入pixmap(图)
        self.pixmap = pixmap
        self.repaint()
    
    def set_last_label(self):
        pass
    
    def transformPos(self, point):
        """Convert from widget-logical coordinates to painter-logical coordinates."""
        return point / self.scale - self.offsetToCenter()
    
    def offsetToCenter(self):
        s = self.scale
        area = super(Canvas, self).size()
        # print('area:', area)
        w, h = self.pixmap.width() * s, self.pixmap.height() * s
        aw, ah = area.width(), area.height()
        x = (aw - w) / (2 * s) if aw > w else 0
        y = (ah - h) / (2 * s) if ah > h else 0
        return QPointF(x, y)
    
    def paintEvent(self, event):
        if not self.pixmap:
            return super(Canvas, self).paintEvent(event)
        
        p = self.painter
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setRenderHint(QPainter.HighQualityAntialiasing)
        p.setRenderHint(QPainter.SmoothPixmapTransform)
        
        # 调整位置和大小
        p.scale(self.scale, self.scale)
        p.translate(self.offsetToCenter())
        
        # 图
        p.drawPixmap(0, 0, self.pixmap)  # 从(0, 0)开始到自己的大小结束。为了标记
        Shape.scale = self.scale
        
        # 成品之后
        # 让已经创建的rect一直显示在canvas上
        # 从第一个rect开始起作用
        for shape in self.shapes:
            # print('self.shapes:', self.shapes)
            # print('shape:', shape)
            if shape:
                shape.paint(p)
        
        # 成品之前
        # 顶点
        if self.points:
            self.points.paint(p)
        # rect
        if self.point_four:
            self.point_four.paint(p)
        # Paint rect
        if (
                len(self.points) == 2
                and self.creating()
        ):  # len(self.line) == 2 存放的是两个点
            leftTop = self.points[0]
            rightBottom = self.points[1]
            rectWidth = rightBottom.x() - leftTop.x()
            rectHeight = rightBottom.y() - leftTop.y()
            p.setPen(QColor(0, 0, 255))
            # 填充阴影效果
            brush = QBrush(Qt.BDiagPattern)
            p.setBrush(brush)
            # 实时的画出矩形
            p.drawRect(leftTop.x(), leftTop.y(), rectWidth, rectHeight)
        # 画出点的十字架
        # 未实现，可有可无的功能
        # if (
        #     self.creating()
        #     and not self.ten_bottle.isNull()
        #     and not self.outOfPixmap(self.ten_bottle)
        # ):
        #     print('1')
        #     p.setPen(QColor(0, 0, 0))
        #     p.drawLine(self.ten_bottle.x(), 0, self.ten_bottle.x(), self.pixmap.height())
        #     p.drawLine(0, self.ten_bottle.y(), self.pixmap.width(), self.ten_bottle.y())
        
        p.end()
    
    def setDrawingShapeToSquare(self, status):
        self.drawSquare = status
    
    def sizeHint(self):
        return self.minimumSizeHint()
    
    def minimumSizeHint(self):
        if self.pixmap:
            return self.scale * self.pixmap.size()
        return super(Canvas, self).minimumSizeHint()
