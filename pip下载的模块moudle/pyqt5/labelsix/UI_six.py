# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_six.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1804, 1050)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1506, 945))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.label_dirName = QtWidgets.QLabel(self.centralwidget)
        self.label_dirName.setObjectName("label_dirName")
        self.gridLayout.addWidget(self.label_dirName, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolBar.setToolTip("")
        self.toolBar.setToolTipDuration(-1)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1804, 23))
        self.menubar.setObjectName("menubar")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidget_4 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_4.setMouseTracking(False)
        self.dockWidget_4.setAutoFillBackground(False)
        self.dockWidget_4.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_backlight_yes = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_backlight_yes.setObjectName("pushButton_backlight_yes")
        self.horizontalLayout_8.addWidget(self.pushButton_backlight_yes)
        self.pushButton_backlight_no = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_backlight_no.setObjectName("pushButton_backlight_no")
        self.horizontalLayout_8.addWidget(self.pushButton_backlight_no)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_hasGlove_yes = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_hasGlove_yes.setObjectName("pushButton_hasGlove_yes")
        self.horizontalLayout_7.addWidget(self.pushButton_hasGlove_yes)
        self.pushButton_hasGlove_no = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_hasGlove_no.setObjectName("pushButton_hasGlove_no")
        self.horizontalLayout_7.addWidget(self.pushButton_hasGlove_no)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.label_7 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_resolution_clear = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_resolution_clear.setObjectName("pushButton_resolution_clear")
        self.horizontalLayout_2.addWidget(self.pushButton_resolution_clear)
        self.pushButton_resolution_blur = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_resolution_blur.setObjectName("pushButton_resolution_blur")
        self.horizontalLayout_2.addWidget(self.pushButton_resolution_blur)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_resolution_dark = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_resolution_dark.setObjectName("pushButton_resolution_dark")
        self.horizontalLayout_3.addWidget(self.pushButton_resolution_dark)
        self.pushButton_resolution_invisible = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_resolution_invisible.setObjectName("pushButton_resolution_invisible")
        self.horizontalLayout_3.addWidget(self.pushButton_resolution_invisible)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_8 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_immerse_yes = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_immerse_yes.setObjectName("pushButton_immerse_yes")
        self.horizontalLayout_9.addWidget(self.pushButton_immerse_yes)
        self.pushButton_immerse_no = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_immerse_no.setObjectName("pushButton_immerse_no")
        self.horizontalLayout_9.addWidget(self.pushButton_immerse_no)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.label_9 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_lightOn_on = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_lightOn_on.setObjectName("pushButton_lightOn_on")
        self.horizontalLayout_10.addWidget(self.pushButton_lightOn_on)
        self.pushButton_lightOn_off = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_lightOn_off.setObjectName("pushButton_lightOn_off")
        self.horizontalLayout_10.addWidget(self.pushButton_lightOn_off)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.label_11 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_integrity_full = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_integrity_full.setObjectName("pushButton_integrity_full")
        self.horizontalLayout_4.addWidget(self.pushButton_integrity_full)
        self.pushButton_integrity_complete = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_integrity_complete.setObjectName("pushButton_integrity_complete")
        self.horizontalLayout_4.addWidget(self.pushButton_integrity_complete)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_integrity_incomplete = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_integrity_incomplete.setObjectName("pushButton_integrity_incomplete")
        self.horizontalLayout_5.addWidget(self.pushButton_integrity_incomplete)
        self.pushButton_integrity_nodevice = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_integrity_nodevice.setObjectName("pushButton_integrity_nodevice")
        self.horizontalLayout_5.addWidget(self.pushButton_integrity_nodevice)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label_12 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_angle_front = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_angle_front.setObjectName("pushButton_angle_front")
        self.horizontalLayout_6.addWidget(self.pushButton_angle_front)
        self.pushButton_angle_side = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.pushButton_angle_side.setObjectName("pushButton_angle_side")
        self.horizontalLayout_6.addWidget(self.pushButton_angle_side)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_4)
        self.dockWidget_5 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_5.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_5.setObjectName("dockWidget_5")
        self.dockWidgetContents_6 = QtWidgets.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_one = QtWidgets.QLabel(self.dockWidgetContents_6)
        self.label_one.setObjectName("label_one")
        self.horizontalLayout.addWidget(self.label_one)
        self.label_all = QtWidgets.QLabel(self.dockWidgetContents_6)
        self.label_all.setObjectName("label_all")
        self.horizontalLayout.addWidget(self.label_all)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents_6)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.dockWidget_5.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_5)
        self.action_root = QtWidgets.QAction(MainWindow)
        self.action_root.setChecked(False)
        self.action_root.setPriority(QtWidgets.QAction.NormalPriority)
        self.action_root.setObjectName("action_root")
        self.action_pre = QtWidgets.QAction(MainWindow)
        self.action_pre.setObjectName("action_pre")
        self.action_next = QtWidgets.QAction(MainWindow)
        self.action_next.setObjectName("action_next")
        self.action_rect = QtWidgets.QAction(MainWindow)
        self.action_rect.setObjectName("action_rect")
        self.action_edit = QtWidgets.QAction(MainWindow)
        self.action_edit.setObjectName("action_edit")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_delete = QtWidgets.QAction(MainWindow)
        self.action_delete.setObjectName("action_delete")
        self.action_autosave = QtWidgets.QAction(MainWindow)
        self.action_autosave.setObjectName("action_autosave")
        self.action_copy = QtWidgets.QAction(MainWindow)
        self.action_copy.setObjectName("action_copy")
        self.dockWidget_5.raise_()
        self.dockWidget_4.raise_()
        self.toolBar.addAction(self.action_root)
        self.toolBar.addAction(self.action_pre)
        self.toolBar.addAction(self.action_next)
        self.toolBar.addAction(self.action_save)
        self.toolBar.addAction(self.action_rect)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_edit)
        self.toolBar.addAction(self.action_delete)
        self.toolBar.addAction(self.action_copy)
        self.menu_5.addAction(self.action_root)
        self.menu_5.addAction(self.action_pre)
        self.menu_5.addAction(self.action_next)
        self.menu_5.addAction(self.action_save)
        self.menu_5.addAction(self.action_rect)
        self.menu_5.addAction(self.action_edit)
        self.menu_5.addAction(self.action_delete)
        self.menu_5.addAction(self.action_autosave)
        self.menu.addAction(self.action_autosave)
        self.menu.addAction(self.action_delete)
        self.menu.addAction(self.action_copy)
        self.menu_2.addAction(self.action_root)
        self.menu_2.addAction(self.action_save)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        self.action_root.triggered.connect(MainWindow.select_root_dir)
        self.action_next.triggered.connect(MainWindow.next_dir)
        self.action_pre.triggered.connect(MainWindow.last_dir)
        self.action_rect.triggered.connect(MainWindow.mode_to_create)
        self.action_edit.triggered.connect(MainWindow.mode_to_edit)
        self.action_save.triggered.connect(MainWindow.save_current_json)
        self.pushButton_backlight_yes.clicked.connect(MainWindow.backlight_yes)
        self.pushButton_backlight_no.clicked.connect(MainWindow.backlight_no)
        self.pushButton_hasGlove_yes.clicked.connect(MainWindow.hasGlove_yes)
        self.pushButton_hasGlove_no.clicked.connect(MainWindow.hasGlove_no)
        self.pushButton_resolution_clear.clicked.connect(MainWindow.resolution_clear)
        self.pushButton_resolution_blur.clicked.connect(MainWindow.resolution_blur)
        self.pushButton_resolution_dark.clicked.connect(MainWindow.resolution_dark)
        self.pushButton_resolution_invisible.clicked.connect(MainWindow.resolution_invisible)
        self.pushButton_immerse_yes.clicked.connect(MainWindow.immerse_yes)
        self.pushButton_immerse_no.clicked.connect(MainWindow.immerse_no)
        self.pushButton_lightOn_on.clicked.connect(MainWindow.lightOn_on)
        self.pushButton_lightOn_off.clicked.connect(MainWindow.lightOn_off)
        self.pushButton_integrity_complete.clicked.connect(MainWindow.integrity_complete)
        self.pushButton_integrity_incomplete.clicked.connect(MainWindow.integrity_incomplete)
        self.pushButton_integrity_nodevice.clicked.connect(MainWindow.integrity_nodevice)
        self.action_delete.triggered.connect(MainWindow.deleteSelectedShape)
        self.action_copy.triggered.connect(MainWindow.copySelectedShape)
        self.pushButton_integrity_full.clicked.connect(MainWindow.integrity_full)
        self.pushButton_angle_front.clicked.connect(MainWindow.angle_front)
        self.pushButton_angle_side.clicked.connect(MainWindow.angle_side)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "双图标记工具V1.0"))
        self.label_dirName.setText(_translate("MainWindow", "当前图片处理路径"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menu_5.setTitle(_translate("MainWindow", "快捷键总览"))
        self.menu.setTitle(_translate("MainWindow", "视图"))
        self.menu_2.setTitle(_translate("MainWindow", "文件"))
        self.dockWidget_4.setWindowTitle(_translate("MainWindow", "标注属性"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#aa0000;\">*逆光：</span></p></body></html>"))
        self.pushButton_backlight_yes.setText(_translate("MainWindow", "逆光"))
        self.pushButton_backlight_no.setText(_translate("MainWindow", "不逆光"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#aa0000;\">*手持时是否带手套：</span></p></body></html>"))
        self.pushButton_hasGlove_yes.setText(_translate("MainWindow", "带"))
        self.pushButton_hasGlove_no.setText(_translate("MainWindow", "不带"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#aa0000;\">*设备清晰度:</span></p></body></html>"))
        self.pushButton_resolution_clear.setText(_translate("MainWindow", "清晰"))
        self.pushButton_resolution_blur.setText(_translate("MainWindow", "模糊"))
        self.pushButton_resolution_dark.setText(_translate("MainWindow", "偏暗"))
        self.pushButton_resolution_invisible.setText(_translate("MainWindow", "看不清"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#aa0000;\">*是否和背景融为一体:</span></p></body></html>"))
        self.pushButton_immerse_yes.setText(_translate("MainWindow", "是"))
        self.pushButton_immerse_no.setText(_translate("MainWindow", "否"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#aa0000;\">*扫码枪是否亮灯:</span></p></body></html>"))
        self.pushButton_lightOn_on.setText(_translate("MainWindow", "亮灯"))
        self.pushButton_lightOn_off.setText(_translate("MainWindow", "不亮灯"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#aa0000;\">*扫码窗口露出比例:</span></p></body></html>"))
        self.pushButton_integrity_full.setText(_translate("MainWindow", "完整"))
        self.pushButton_integrity_complete.setText(_translate("MainWindow", "超过80%"))
        self.pushButton_integrity_incomplete.setText(_translate("MainWindow", "不到80%"))
        self.pushButton_integrity_nodevice.setText(_translate("MainWindow", "无支付设备"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#aa0000;\">*设备:</span></p></body></html>"))
        self.pushButton_angle_front.setText(_translate("MainWindow", "正面"))
        self.pushButton_angle_side.setText(_translate("MainWindow", "侧面"))
        self.dockWidget_5.setWindowTitle(_translate("MainWindow", "文件列表"))
        self.label_one.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">当前数量</p></body></html>"))
        self.label_all.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">/ 总数</span></p></body></html>"))
        self.action_root.setText(_translate("MainWindow", "打开"))
        self.action_root.setToolTip(_translate("MainWindow", "打开需要标注的文件夹"))
        self.action_root.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_pre.setText(_translate("MainWindow", "上一张"))
        self.action_pre.setShortcut(_translate("MainWindow", "A"))
        self.action_next.setText(_translate("MainWindow", "下一张"))
        self.action_next.setShortcut(_translate("MainWindow", "D"))
        self.action_rect.setText(_translate("MainWindow", "创建模式"))
        self.action_rect.setShortcut(_translate("MainWindow", "W"))
        self.action_edit.setText(_translate("MainWindow", "编辑模式"))
        self.action_edit.setShortcut(_translate("MainWindow", "S"))
        self.action_save.setText(_translate("MainWindow", "保存"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_delete.setText(_translate("MainWindow", "删除框图"))
        self.action_delete.setToolTip(_translate("MainWindow", "删除一个指定框图"))
        self.action_delete.setShortcut(_translate("MainWindow", "Del"))
        self.action_autosave.setText(_translate("MainWindow", "自动保存"))
        self.action_autosave.setToolTip(_translate("MainWindow", "自动保存"))
        self.action_autosave.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action_copy.setText(_translate("MainWindow", "复制框图"))
        self.action_copy.setToolTip(_translate("MainWindow", "右击复制框选的图"))
        self.action_copy.setShortcut(_translate("MainWindow", "Ctrl+D"))
