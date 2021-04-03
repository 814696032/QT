# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 800))
        MainWindow.setBaseSize(QtCore.QSize(600, 800))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.layout = QtWidgets.QFrame(self.centralwidget)
        self.layout.setMinimumSize(QtCore.QSize(1280, 800))
        self.layout.setMouseTracking(True)
        self.layout.setFrameShape(QtWidgets.QFrame.Box)
        self.layout.setObjectName("layout")
        self.mainlayout = QtWidgets.QVBoxLayout(self.layout)
        self.mainlayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.mainlayout.setSpacing(0)
        self.mainlayout.setObjectName("mainlayout")
        self.menubar = QtWidgets.QFrame(self.layout)
        self.menubar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMinimumSize(QtCore.QSize(0, 40))
        self.menubar.setMouseTracking(True)
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menubar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.menubar.setLineWidth(0)
        self.menubar.setMidLineWidth(0)
        self.menubar.setObjectName("menubar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.menubar)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo = QtWidgets.QLabel(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(200, 30))
        self.logo.setMaximumSize(QtCore.QSize(200, 30))
        self.logo.setSizeIncrement(QtCore.QSize(0, 0))
        self.logo.setBaseSize(QtCore.QSize(0, 0))
        self.logo.setMouseTracking(True)
        self.logo.setStyleSheet("")
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.spacer_label1 = QtWidgets.QLabel(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer_label1.sizePolicy().hasHeightForWidth())
        self.spacer_label1.setSizePolicy(sizePolicy)
        self.spacer_label1.setMinimumSize(QtCore.QSize(50, 40))
        self.spacer_label1.setMaximumSize(QtCore.QSize(50, 40))
        self.spacer_label1.setText("")
        self.spacer_label1.setObjectName("spacer_label1")
        self.horizontalLayout_2.addWidget(self.spacer_label1)
        self.menu_button1 = QtWidgets.QPushButton(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_button1.sizePolicy().hasHeightForWidth())
        self.menu_button1.setSizePolicy(sizePolicy)
        self.menu_button1.setMinimumSize(QtCore.QSize(150, 40))
        self.menu_button1.setMaximumSize(QtCore.QSize(150, 40))
        self.menu_button1.setBaseSize(QtCore.QSize(70, 0))
        self.menu_button1.setMouseTracking(True)
        self.menu_button1.setFlat(True)
        self.menu_button1.setObjectName("menu_button1")
        self.horizontalLayout_2.addWidget(self.menu_button1)
        self.menu_button2 = QtWidgets.QPushButton(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_button2.sizePolicy().hasHeightForWidth())
        self.menu_button2.setSizePolicy(sizePolicy)
        self.menu_button2.setMinimumSize(QtCore.QSize(150, 40))
        self.menu_button2.setMaximumSize(QtCore.QSize(150, 40))
        self.menu_button2.setBaseSize(QtCore.QSize(70, 0))
        self.menu_button2.setMouseTracking(True)
        self.menu_button2.setFlat(True)
        self.menu_button2.setObjectName("menu_button2")
        self.horizontalLayout_2.addWidget(self.menu_button2)
        self.menu_button3 = QtWidgets.QPushButton(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_button3.sizePolicy().hasHeightForWidth())
        self.menu_button3.setSizePolicy(sizePolicy)
        self.menu_button3.setMinimumSize(QtCore.QSize(150, 40))
        self.menu_button3.setMaximumSize(QtCore.QSize(150, 40))
        self.menu_button3.setBaseSize(QtCore.QSize(70, 0))
        self.menu_button3.setMouseTracking(True)
        self.menu_button3.setFlat(True)
        self.menu_button3.setObjectName("menu_button3")
        self.horizontalLayout_2.addWidget(self.menu_button3)
        self.menu_button4 = QtWidgets.QPushButton(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_button4.sizePolicy().hasHeightForWidth())
        self.menu_button4.setSizePolicy(sizePolicy)
        self.menu_button4.setMinimumSize(QtCore.QSize(150, 40))
        self.menu_button4.setMaximumSize(QtCore.QSize(150, 40))
        self.menu_button4.setBaseSize(QtCore.QSize(70, 0))
        self.menu_button4.setMouseTracking(True)
        self.menu_button4.setFlat(True)
        self.menu_button4.setObjectName("menu_button4")
        self.horizontalLayout_2.addWidget(self.menu_button4)
        self.spacer_label2 = QtWidgets.QLabel(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer_label2.sizePolicy().hasHeightForWidth())
        self.spacer_label2.setSizePolicy(sizePolicy)
        self.spacer_label2.setMinimumSize(QtCore.QSize(50, 40))
        self.spacer_label2.setMaximumSize(QtCore.QSize(50, 40))
        self.spacer_label2.setText("")
        self.spacer_label2.setObjectName("spacer_label2")
        self.horizontalLayout_2.addWidget(self.spacer_label2)
        spacerItem1 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.minwin = QtWidgets.QPushButton(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minwin.sizePolicy().hasHeightForWidth())
        self.minwin.setSizePolicy(sizePolicy)
        self.minwin.setMinimumSize(QtCore.QSize(30, 40))
        self.minwin.setMaximumSize(QtCore.QSize(30, 40))
        self.minwin.setMouseTracking(True)
        self.minwin.setText("")
        self.minwin.setIconSize(QtCore.QSize(40, 40))
        self.minwin.setFlat(True)
        self.minwin.setObjectName("minwin")
        self.horizontalLayout_2.addWidget(self.minwin)
        self.maxwin = QtWidgets.QPushButton(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxwin.sizePolicy().hasHeightForWidth())
        self.maxwin.setSizePolicy(sizePolicy)
        self.maxwin.setMinimumSize(QtCore.QSize(30, 40))
        self.maxwin.setMaximumSize(QtCore.QSize(30, 40))
        self.maxwin.setMouseTracking(True)
        self.maxwin.setText("")
        self.maxwin.setIconSize(QtCore.QSize(40, 40))
        self.maxwin.setFlat(True)
        self.maxwin.setObjectName("maxwin")
        self.horizontalLayout_2.addWidget(self.maxwin)
        self.exit = QtWidgets.QPushButton(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QtCore.QSize(30, 40))
        self.exit.setMaximumSize(QtCore.QSize(30, 40))
        self.exit.setMouseTracking(True)
        self.exit.setText("")
        self.exit.setIconSize(QtCore.QSize(40, 40))
        self.exit.setFlat(True)
        self.exit.setObjectName("exit")
        self.horizontalLayout_2.addWidget(self.exit)
        self.horizontalLayout_2.setStretch(0, 5)
        self.mainlayout.addWidget(self.menubar)
        self.content = QtWidgets.QWidget(self.layout)
        self.content.setEnabled(True)
        self.content.setMouseTracking(True)
        self.content.setAutoFillBackground(False)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftwindow = QtWidgets.QWidget(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftwindow.sizePolicy().hasHeightForWidth())
        self.leftwindow.setSizePolicy(sizePolicy)
        self.leftwindow.setMinimumSize(QtCore.QSize(300, 0))
        self.leftwindow.setMaximumSize(QtCore.QSize(300, 16777215))
        self.leftwindow.setMouseTracking(True)
        self.leftwindow.setObjectName("leftwindow")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftwindow)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.leftwindow)
        self.widget.setMouseTracking(True)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_title = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMinimumSize(QtCore.QSize(300, 25))
        self.label_title.setMaximumSize(QtCore.QSize(300, 25))
        self.label_title.setMouseTracking(True)
        self.label_title.setStyleSheet("")
        self.label_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_title.setLineWidth(0)
        self.label_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_4.addWidget(self.label_title)
        self.label = QtWidgets.QTextBrowser(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_bottom = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_bottom.sizePolicy().hasHeightForWidth())
        self.label_bottom.setSizePolicy(sizePolicy)
        self.label_bottom.setMinimumSize(QtCore.QSize(0, 25))
        self.label_bottom.setText("")
        self.label_bottom.setObjectName("label_bottom")
        self.verticalLayout_4.addWidget(self.label_bottom)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.leftwindow)
        self.widget_2.setMouseTracking(True)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2_title = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2_title.sizePolicy().hasHeightForWidth())
        self.label_2_title.setSizePolicy(sizePolicy)
        self.label_2_title.setMinimumSize(QtCore.QSize(300, 25))
        self.label_2_title.setMaximumSize(QtCore.QSize(300, 25))
        self.label_2_title.setMouseTracking(True)
        self.label_2_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_2_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2_title.setObjectName("label_2_title")
        self.verticalLayout_5.addWidget(self.label_2_title)
        self.label_2 = QtWidgets.QFrame(self.widget_2)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.label_2_bottom = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2_bottom.sizePolicy().hasHeightForWidth())
        self.label_2_bottom.setSizePolicy(sizePolicy)
        self.label_2_bottom.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2_bottom.setText("")
        self.label_2_bottom.setObjectName("label_2_bottom")
        self.verticalLayout_5.addWidget(self.label_2_bottom)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.leftwindow)
        self.widget_3.setMouseTracking(True)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem4)
        self.label_3_title = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3_title.sizePolicy().hasHeightForWidth())
        self.label_3_title.setSizePolicy(sizePolicy)
        self.label_3_title.setMinimumSize(QtCore.QSize(300, 25))
        self.label_3_title.setMaximumSize(QtCore.QSize(300, 25))
        self.label_3_title.setMouseTracking(True)
        self.label_3_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3_title.setObjectName("label_3_title")
        self.verticalLayout_6.addWidget(self.label_3_title)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_6.addWidget(self.textBrowser)
        self.label_3_bottom = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3_bottom.sizePolicy().hasHeightForWidth())
        self.label_3_bottom.setSizePolicy(sizePolicy)
        self.label_3_bottom.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3_bottom.setText("")
        self.label_3_bottom.setObjectName("label_3_bottom")
        self.verticalLayout_6.addWidget(self.label_3_bottom)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.leftwindow)
        self.workspace = QtWidgets.QFrame(self.content)
        self.workspace.setObjectName("workspace")
        self.horizontalLayout.addWidget(self.workspace)
        self.rightwindow = QtWidgets.QWidget(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightwindow.sizePolicy().hasHeightForWidth())
        self.rightwindow.setSizePolicy(sizePolicy)
        self.rightwindow.setMinimumSize(QtCore.QSize(300, 0))
        self.rightwindow.setMaximumSize(QtCore.QSize(300, 16777215))
        self.rightwindow.setMouseTracking(True)
        self.rightwindow.setObjectName("rightwindow")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rightwindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_info_title = QtWidgets.QLabel(self.rightwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_info_title.sizePolicy().hasHeightForWidth())
        self.list_info_title.setSizePolicy(sizePolicy)
        self.list_info_title.setMinimumSize(QtCore.QSize(300, 25))
        self.list_info_title.setMaximumSize(QtCore.QSize(300, 25))
        self.list_info_title.setMouseTracking(True)
        self.list_info_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.list_info_title.setObjectName("list_info_title")
        self.verticalLayout.addWidget(self.list_info_title)
        self.list_info = QtWidgets.QLabel(self.rightwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_info.sizePolicy().hasHeightForWidth())
        self.list_info.setSizePolicy(sizePolicy)
        self.list_info.setMinimumSize(QtCore.QSize(0, 300))
        self.list_info.setMaximumSize(QtCore.QSize(16777215, 300))
        self.list_info.setAlignment(QtCore.Qt.AlignCenter)
        self.list_info.setObjectName("list_info")
        self.verticalLayout.addWidget(self.list_info)
        self.list_bottom = QtWidgets.QLabel(self.rightwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_bottom.sizePolicy().hasHeightForWidth())
        self.list_bottom.setSizePolicy(sizePolicy)
        self.list_bottom.setMinimumSize(QtCore.QSize(0, 25))
        self.list_bottom.setText("")
        self.list_bottom.setObjectName("list_bottom")
        self.verticalLayout.addWidget(self.list_bottom)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.tabWidget_title = QtWidgets.QLabel(self.rightwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_title.sizePolicy().hasHeightForWidth())
        self.tabWidget_title.setSizePolicy(sizePolicy)
        self.tabWidget_title.setMinimumSize(QtCore.QSize(300, 25))
        self.tabWidget_title.setMaximumSize(QtCore.QSize(300, 25))
        self.tabWidget_title.setMouseTracking(True)
        self.tabWidget_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.tabWidget_title.setObjectName("tabWidget_title")
        self.verticalLayout.addWidget(self.tabWidget_title)
        self.tabWidget = QtWidgets.QTabWidget(self.rightwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 40))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.changelist = QtWidgets.QWidget()
        self.changelist.setObjectName("changelist")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.changelist)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.list1 = QtWidgets.QListWidget(self.changelist)
        self.list1.setObjectName("list1")
        self.horizontalLayout_5.addWidget(self.list1)
        self.tabWidget.addTab(self.changelist, "")
        self.objlist = QtWidgets.QWidget()
        self.objlist.setObjectName("objlist")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.objlist)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.list2 = QtWidgets.QListWidget(self.objlist)
        self.list2.setObjectName("list2")
        self.horizontalLayout_6.addWidget(self.list2)
        self.tabWidget.addTab(self.objlist, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.rightwindow)
        self.mainlayout.addWidget(self.content)
        self.gridLayout.addWidget(self.layout, 0, 0, 1, 1)
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setObjectName("background")
        self.gridLayout.addWidget(self.background, 0, 0, 1, 1)
        self.background.raise_()
        self.layout.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo.setText(_translate("MainWindow", "logo"))
        self.menu_button1.setText(_translate("MainWindow", "文件"))
        self.menu_button2.setText(_translate("MainWindow", "视图"))
        self.menu_button3.setText(_translate("MainWindow", "设置"))
        self.menu_button4.setText(_translate("MainWindow", "关于"))
        self.label_title.setText(_translate("MainWindow", "检测结果"))
        self.label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">占位</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">这里保存当前图片检测结果</p></body></html>"))
        self.label_2_title.setText(_translate("MainWindow", "目标检测统计"))
        self.label_3_title.setText(_translate("MainWindow", "输出日志"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">欢迎使用！</p></body></html>"))
        self.list_info_title.setText(_translate("MainWindow", "预览窗口"))
        self.list_info.setText(_translate("MainWindow", "未选择项目"))
        self.tabWidget_title.setText(_translate("MainWindow", "窗体右二"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.changelist), _translate("MainWindow", "变化检测"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.objlist), _translate("MainWindow", "目标检测"))
        self.background.setText(_translate("MainWindow", "背景"))
