#-*- coding: utf-8 -*-
from New_MainWin import Ui_MainWindow
from dialog import Ui_about
from setting import Ui_setting
from image_window import Ui_Image_windows
from list_click_disp import Ui_list_click_disp
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,QThread,Qt,pyqtSlot,QSize,QRect
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QStyle,QGraphicsDropShadowEffect
from BarStack import ChartView
import configparser as cp


class MainDialog(QMainWindow,Ui_MainWindow):#Qwidget有最大最小化，Qdialog没有
    window_size_record={}
    def __init__(self, parent=None): #初始化
        super(MainDialog,self).__init__(parent)
        self.setupUi(self) #初始化页面
        self.resize(1280,800)
        self.initUI()


        self.background = QHBoxLayout()
        self.backlabel = QLabel("balabalabalaba")
        self.background.addWidget(self.backlabel)
        self.background.setGeometry(QRect(0,0,800,300))
        self.setLayout(self.background)
        self.workspace_lay = QHBoxLayout()
        self.workspace_lay.setContentsMargins(10,10,10,10)
        self.workspace.setLayout(self.workspace_lay)


    def initUI(self):
        self.init_title()
        self.init_menu()
        self.init_gif()
        self.init_chart()
        self.init_other()

    def init_title(self):  # 初始化自定义标题栏

        self.setWindowFlags(Qt.CustomizeWindowHint)
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 取消标题栏
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.maxwin.setIcon(QIcon(QPixmap('./Resource/maxwin.ico')))
        self.maxwin.setIconSize(QSize(20, 20))
        self.minwin.setIcon(QIcon(QPixmap('./Resource/min.ico')))
        self.minwin.setIconSize(QSize(20, 20))
        self.exit.setIcon(QIcon(QPixmap('./Resource/exit.ico')))  # 设定最大最小关闭按钮图标
        self.exit.setIconSize(QSize(20, 20))
        self.pix = QPixmap("./Resource/Logo.png")  # 设定logo图标
        self.logo.setPixmap(self.pix)
        self.logo.setScaledContents(True)
        self.exit.clicked.connect(lambda:on_exit_clicked(self))  # 自定义标题栏功能
        self.minwin.clicked.connect(lambda:on_minwin_clicked(self))
        self.maxwin.clicked.connect(lambda:on_maxwin_clicked(self))

        # aniButton = AnimationShadowEffect(Qt.blue, self.label_2_title)
        # self.label_2_title.setGraphicsEffect(aniButton)
        # aniButton.start()

        def on_minwin_clicked(self):
            # 最小化
            self.showMinimized()

        def on_maxwin_clicked(self):
            # 最大化与复原
            if self.isMaximized():
                self.showNormal()
                self.maxwin.setIcon(QIcon(QPixmap('./Resource/maxwin.ico')))
                self.maxwin.setIconSize(QSize(20,20))
                # self.maxwin.setText('□')  # 切换放大按钮图标字体
                self.maxwin.setToolTip("<html><head/><body><p>最大化</p></body></html>")
            else:
                self.showMaximized()
                self.maxwin.setIcon(QIcon(QPixmap('./Resource/minwin.ico')))
                self.maxwin.setIconSize(QSize(20,20))
                # self.maxwin.setText('◎')
                self.maxwin.setToolTip("<html><head/><body><p>恢复</p></body></html>")

        def on_exit_clicked(self):
            self.close()

    def init_menu(self):
        self.menu1 = QMenu()  # 第一个按钮菜单
        self.menu1.setObjectName("menu1")

        self.action_openfile = QAction("打开图片",self.menu1)
        self.menu1.addAction(self.action_openfile)
        # self.action_openfile.triggered.connect(lambda:print("打开图片"))
        self.action_opendir = QAction("打开目录",self.menu1)
        self.menu1.addAction(self.action_opendir)
        # self.action_opendir.triggered.connect(lambda: print("打开目录"))
        self.action_openvideo=QAction("载入视频",self.menu1)
        self.menu1.addAction(self.action_openvideo)
        self.action_opendata=QAction("载入数据",self.menu1)
        self.menu1.addAction(self.action_opendata)
        self.action_opendata.triggered.connect(lambda: print("载入数据"))

        self.action_save = QAction("保存",self.menu1)
        self.menu1.addAction(self.action_save)

        self.action_restart=QAction("重新开始",self.menu1)
        self.menu1.addAction(self.action_restart)
        # self.action_restart.triggered.connect(lambda: print("重新开始"))
        self.menu_button1.setMenu(self.menu1)
        self.action_exit=QAction("退出",self.menu1)
        self.menu1.addAction(self.action_exit)
        self.action_exit.triggered.connect(self.close)


        self.menu2 = QMenu()  # 第二个按钮菜单
        self.action_view1 = QAction("变化检测", self.menu2)
        self.menu2.addAction(self.action_view1)
        # self.action_view1.triggered.connect(lambda: print("选项1"))
        self.action_view2 = QAction("目标检测", self.menu2)
        self.menu2.addAction(self.action_view2)
        # self.action_view2.triggered.connect(lambda: print("选项2"))
        self.menu_button2.setMenu(self.menu2)
        self.action_view1.setIcon(QIcon(QPixmap('./Resource/check_mark.ico')))
        self.action_view2.setIcon(QIcon(QPixmap('./Resource/check_mark.ico')))

        self.menu3 = QMenu()  # 第三个按钮菜单
        self.action_setting = QAction("设置", self.menu3)
        self.menu3.addAction(self.action_setting)
        self.action_setting.triggered.connect(lambda: print("设置"))
        self.action_setting2 = QAction("待定", self.menu3)
        self.menu3.addAction(self.action_setting2)
        self.action_setting2.triggered.connect(lambda: print("待定"))
        self.menu_button3.setMenu(self.menu3)

        self.menu4 = QMenu()  # 第四个按钮菜单
        self.action_help = QAction("帮助", self.menu4)
        self.menu4.addAction(self.action_help)
        self.action_help.triggered.connect(lambda: print("帮助"))
        self.action_about = QAction("关于...", self.menu4)
        self.menu4.addAction(self.action_about)
        # self.action_about.triggered.connect(self.about_window.show)
        self.menu_button4.setMenu(self.menu4)

        self.menu1.setObjectName("menu1")
        self.menu2.setObjectName("menu2")
        self.menu3.setObjectName("menu3")
        self.menu4.setObjectName("menu4")
        self.menu1.setAttribute(Qt.WA_TranslucentBackground)
        self.menu1.setWindowFlags(self.menu1.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.menu2.setAttribute(Qt.WA_TranslucentBackground)
        self.menu2.setWindowFlags(self.menu1.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.menu3.setAttribute(Qt.WA_TranslucentBackground)
        self.menu3.setWindowFlags(self.menu1.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.menu4.setAttribute(Qt.WA_TranslucentBackground)
        self.menu4.setWindowFlags(self.menu1.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)

        self.menu1.setStyleSheet("QMenu{background:rgba(38,156,211,100);}"  # 选项背景颜色
                           "QMenu{border:1px solid lightgray;}"  # 设置整个菜单框的边界高亮厚度
                           "QMenu{border-color:rgba(255,255,255,100);}"  # 整个边框的颜色
                           "QMenu{width:150px;}"  # 整个边框的颜色
                           "QMenu::item{padding:0px 50px 0px 25px;}"  # 以文字为标准，右边距文字40像素，左边同理
                           "QMenu::item{height:30px;}"  # 显示菜单选项高度
                           "QMenu::item{width:150px;}"  # 显示菜单选项高度
                           "QMenu::item{color:white;}"  # 选项文字颜色
                           "QMenu::item{background:transparent;}"  # 选项背景
                           "QMenu::item{margin:1px 1px 1px 1px;}"  # 每个选项四边的边界厚度，上，右，下，左


                           "QMenu::item:selected:enabled{background:rgb(243,152,0);}"
                           "QMenu::item:selected:enabled{color:white;}"  # 鼠标在选项上面时，文字的颜色
                                 )
        self.menu2.setStyleSheet("QMenu{background:rgba(38,156,211,100);}"  # 选项背景颜色
                           "QMenu{border:1px solid lightgray;}"  # 设置整个菜单框的边界高亮厚度
                           "QMenu{border-color:rgba(255,255,255,100);}"  # 整个边框的颜色
                           "QMenu{width:150px;}"  # 整个边框的颜色
                           "QMenu::item{padding:0px 50px 0px 15px;}"  # 以文字为标准，右边距文字40像素，左边同理
                           "QMenu::item{height:30px;}"  # 显示菜单选项高度
                           "QMenu::item{width:150px;}"  # 显示菜单选项高度
                           "QMenu::item{color:white;}"  # 选项文字颜色
                           "QMenu::item{background:transparent;}"  # 选项背景
                           "QMenu::item{margin:1px 1px 1px 1px;}"  # 每个选项四边的边界厚度，上，右，下，左


                           "QMenu::item:selected:enabled{background:rgb(243,152,0);}"
                           "QMenu::item:selected:enabled{color:white;}"  # 鼠标在选项上面时，文字的颜色
                                 )
        self.menu3.setStyleSheet("QMenu{background:rgba(38,156,211,100);}"  # 选项背景颜色
                           "QMenu{border:1px solid lightgray;}"  # 设置整个菜单框的边界高亮厚度
                           "QMenu{border-color:rgba(255,255,255,100);}"  # 整个边框的颜色
                           "QMenu{width:150px;}"  # 整个边框的颜色
                           "QMenu::item{padding:0px 50px 0px 25px;}"  # 以文字为标准，右边距文字40像素，左边同理
                           "QMenu::item{height:30px;}"  # 显示菜单选项高度
                           "QMenu::item{width:150px;}"  # 显示菜单选项高度
                           "QMenu::item{color:white;}"  # 选项文字颜色
                           "QMenu::item{background:transparent;}"  # 选项背景
                           "QMenu::item{margin:1px 1px 1px 1px;}"  # 每个选项四边的边界厚度，上，右，下，左
                           "QMenu::item:selected:enabled{background:rgb(243,152,0);}"
                           "QMenu::item:selected:enabled{color:white;}"  # 鼠标在选项上面时，文字的颜色
                                 )
        self.menu4.setStyleSheet("QMenu{background:rgba(38,156,211,100);}"  # 选项背景颜色
                           "QMenu{border:1px solid lightgray;}"  # 设置整个菜单框的边界高亮厚度
                           "QMenu{border-color:rgba(255,255,255,100);}"  # 整个边框的颜色
                           "QMenu{width:150px;}"  # 整个边框的颜色
                           "QMenu::item{padding:0px 50px 0px 25px;}"  # 以文字为标准，右边距文字40像素，左边同理
                           "QMenu::item{height:30px;}"  # 显示菜单选项高度
                           "QMenu::item{width:150px;}"  # 显示菜单选项高度
                           "QMenu::item{color:white;}"  # 选项文字颜色
                           "QMenu::item{background:transparent;}"  # 选项背景
                           "QMenu::item{margin:1px 1px 1px 1px;}"  # 每个选项四边的边界厚度，上，右，下，左
                           "QMenu::item:selected:enabled{background:rgb(243,152,0);}"
                           "QMenu::item:selected:enabled{color:white;}"  # 鼠标在选项上面时，文字的颜色
                                 )


        # self.menu1.setStyleSheet("background-color:rgba(38,156,211,100);color:rgb(255,255,255);border:1px solid lightgray")
        # self.menu2.setStyleSheet("background-color:rgba(0,170,255,100);color:rgb(255,255,255)")
        # self.menu3.setStyleSheet("background-color:rgba(0,170,255,100);color:rgb(255,255,255)")
        # self.menu4.setStyleSheet("background-color:rgba(0,170,255,100);color:rgb(255,255,255)")

    def init_gif(self):
        self.background_movie = QtGui.QMovie()
        self.background_movie.setFileName('./Resource/dynamic_bg.gif')
        self.background.setMovie(self.background_movie)
        self.background_movie.setSpeed(200)
        # self.background_movie.start()  # 是否需要动态背景

    def init_chart(self):
        self.chart = ChartView(self.label_2)
        self.chart.setObjectName("chart")
        self.chart.resize(300,184)

    def init_other(self):
        pass

    # *********关于选项**************
    # def open_about(self):
    #     about_win = Ui_about()
    #     about_win.setupUi()
    #     about_win.open()

    # *********事件部分重写************
    def closeEvent(self,event ) : #重新实现关闭事件
        reply = QtWidgets.QMessageBox.question(self,'关闭确认','是否关闭？',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()#接受退出指令
        else:
            event.ignore()#忽略该指令




class About_Window(QDialog,Ui_about):  # 关于对话框
    def __init__(self):
        super(About_Window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("关于")


class Setting_Window(QWidget,Ui_setting):  # 设置对话框
    def __init__(self):

        super(Setting_Window,self).__init__()
        self.setupUi(self)
        self.conf = cp.ConfigParser()
        self.readConfigFile()
        self.setWindowModality(Qt.ApplicationModal)  # 打开设置后不允许与主窗口交互
        self.setWindowTitle("设置")
        self.setting_apply.setEnabled(True)

        # self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 置顶

    def readConfigFile(self):  # 载入配置文件
        self.conf.read('Configuration.ini',encoding='utf-8')
        # 根据配置文件将设置窗口初始化
        self.Fullscreen.setChecked(eval(self.conf.get('setting','Fullscreen')))
        self.history_dir_edit.setText(self.conf.get('setting','History_cmp_dir'))
        self.dir_gps.setText(self.conf.get('setting','Gps_dir'))

        # self.cfg['save_dir']=json_str['Save_dir']

class Image_Window(QWidget,Ui_Image_windows):
    sp = 1
    def __init__(self):
        super(Image_Window,self).__init__()
        self.setupUi(self)
        self.setStyle(QStyleFactory.create('WindowsVista'))
        self.image_view.setStyleSheet("background: transparent;border:0px")
        # self.image_left.setIcon(QIcon(QPixmap('./Resource/image_left.png')))
        # self.image_left.setIconSize(QSize(50, 50))
        # self.image_right.setIcon(QIcon(QPixmap('./Resource/image_right.png')))
        # self.image_right.setIconSize(QSize(50, 50))
        self.sp = 1
        self.image_start_detect.setIcon(QIcon(QPixmap('./Resource/image_start.png')))
        self.image_stop_detect.setIcon(QIcon(QPixmap('./Resource/image_stop.png')))
        self.image_start_detect.setIconSize(QSize(50, 50))
        self.image_stop_detect.setIconSize(QSize(50, 50))
        self.image_close.setIcon(QIcon(QPixmap('./Resource/exit.ico')))
        # self.image_close.setIconSize(QSize(50,50))
        self.image_left.setHidden(False)
        self.image_right.setHidden(False)
        self.image_right.raise_()
        self.image_left.raise_()


    def resizeEvent(self,event):
        # print("IMAGE_VIEW resize")
        self.image_close.setGeometry(self.width()-50,0,25,25)
        self.image_title.setGeometry(0,0,self.width(),25)
        self.image_left.setGeometry(0,25,50,self.height()-25-75)
        self.image_right.setGeometry(self.width()-40,25,50,self.height()-25-75)
        self.image_view.setGeometry(0,25,self.width(),self.height()-25-75)
        self.image_start_detect.setGeometry(self.width()/2-25,self.height()-50-4-20,50,50)
        self.image_stop_detect.setGeometry(self.width()/2+25+20,self.height()-50-4-20,50,50)
        self.image_change_detect.setGeometry(self.width()/2-200,self.height()-25-20,87,19)
        self.image_obj_detect.setGeometry(self.width() / 2 - 200, self.height() - 50-20, 87, 19)
        self.image_line.setGeometry(self.width()/2-200,self.height()-20,97,19)

    def switch_play_icon(self,flag):
        if flag=='p':
            self.image_start_detect.setIcon(QIcon(QPixmap('./Resource/image_pause.png')))
            self.image_start_detect.setIconSize(QSize(50, 50))
            self.update()
            QApplication.processEvents()
        elif(flag=='s'):
            self.image_start_detect.setIcon(QIcon(QPixmap('./Resource/image_start.png')))
            self.image_start_detect.setIconSize(QSize(50, 50))
            self.update()
            QApplication.processEvents()
        else:
            pass



class List_disp(QDialog,Ui_list_click_disp):
    def __init__(self):
        super(List_disp,self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        self.ok.clicked.connect(self.close)

class PercentProgressBar(QWidget):

    MinValue = 0
    MaxValue = 100
    Value = 0
    BorderWidth = 10
    Clockwise = True  # 顺时针还是逆时针
    ShowPercent = True  # 是否显示百分比
    ShowFreeArea = False  # 显示背后剩余
    ShowSmallCircle = True  # 显示带头的小圆圈
    TextColor = QColor(255, 255, 255)  # 文字颜色
    BorderColor = QColor(24, 189, 155)  # 边框圆圈颜色
    BackgroundColor = QColor(70, 70, 70)  # 背景颜色

    def __init__(self, *args, value=0, minValue=0, maxValue=100,
                 borderWidth=8, clockwise=True, showPercent=True,
                 showFreeArea=False, showSmallCircle=False,
                 textColor=QColor(255, 255, 255),
                 borderColor=QColor(0, 170, 255),
                 backgroundColor=QColor(70, 70, 70), **kwargs):
        super(PercentProgressBar, self).__init__(*args, **kwargs)
        self.Value = value
        self.MinValue = minValue
        self.MaxValue = maxValue
        self.BorderWidth = borderWidth
        self.Clockwise = clockwise
        self.ShowPercent = showPercent
        self.ShowFreeArea = showFreeArea
        self.ShowSmallCircle = showSmallCircle
        self.TextColor = textColor
        self.BorderColor = borderColor
        self.BackgroundColor = backgroundColor


    def setRange(self, minValue: int, maxValue: int):
        if minValue >= maxValue:  # 最小值>=最大值
            return
        self.MinValue = minValue
        self.MaxValue = maxValue
        self.update()

    def paintEvent(self, event):
        super(PercentProgressBar, self).paintEvent(event)
        width = self.width()
        height = self.height()
        side = min(width, height)

        painter = QPainter(self)
        # 反锯齿
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.TextAntialiasing)
        # 坐标中心为中间点
        painter.translate(width / 2, height / 2)
        # 按照100x100缩放
        painter.scale(side / 100.0, side / 100.0)

        # 绘制中心园
        self._drawCircle(painter, 50)
        # 绘制圆弧
        self._drawArc(painter, 50 - self.BorderWidth / 2)
        # 绘制文字
        self._drawText(painter, 50)
        self._drawText_tip(painter, 50)

    def _drawCircle(self, painter: QPainter, radius: int):
        # 绘制中心园
        radius = radius - self.BorderWidth
        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.BackgroundColor)
        painter.drawEllipse(QRectF(-radius, -radius, radius * 2, radius * 2))
        painter.restore()

    def _drawArc(self, painter: QPainter, radius: int):
        # 绘制圆弧
        painter.save()
        painter.setBrush(Qt.NoBrush)
        # 修改画笔
        pen = painter.pen()
        pen.setWidthF(self.BorderWidth)
        pen.setCapStyle(Qt.RoundCap)

        arcLength = 360.0 / (self.MaxValue - self.MinValue) * self.Value
        rect = QRectF(-radius, -radius, radius * 2, radius * 2)

        if not self.Clockwise:
            # 逆时针
            arcLength = -arcLength

        # 绘制剩余进度圆弧
        if self.ShowFreeArea:
            acolor = self.BorderColor.toRgb()
            acolor.setAlphaF(0.2)
            pen.setColor(acolor)
            painter.setPen(pen)
            painter.drawArc(rect, (0 - arcLength) *
                            16, -(360 - arcLength) * 16)

        # 绘制当前进度圆弧
        pen.setColor(self.BorderColor)
        painter.setPen(pen)
        painter.drawArc(rect, 0, -arcLength * 16)

        # 绘制进度圆弧前面的小圆
        if self.ShowSmallCircle:
            offset = radius - self.BorderWidth + 1
            radius = self.BorderWidth / 2 - 1
            painter.rotate(-90)
            circleRect = QRectF(-radius, radius + offset,
                                radius * 2, radius * 2)
            painter.rotate(arcLength)
            painter.drawEllipse(circleRect)

        painter.restore()

    def _drawText(self, painter: QPainter, radius: int):
        # 绘制文字
        painter.save()
        painter.setPen(self.TextColor)
        painter.setFont(QFont('Arial', 25))
        strValue = '{}%'.format(int(self.Value / (self.MaxValue - self.MinValue)
                                    * 100)) if self.ShowPercent else str(self.Value)
        painter.drawText(QRectF(-radius, -radius, radius * 2,
                                radius * 2), Qt.AlignCenter, strValue)
        painter.restore()

    def _drawText_tip(self, painter: QPainter, radius: int):
        # 绘制文字
        painter.save()
        painter.setPen(self.TextColor)
        painter.setFont(QFont('Arial', 8))
        strValue = 'ESC 取消'
        painter.drawText(QRectF(-radius, -0.5*radius, radius * 2,
                                radius * 2), Qt.AlignCenter, strValue)
        painter.restore()

    @pyqtProperty(int)
    def minValue(self) -> int:
        return self.MinValue

    @minValue.setter
    def minValue(self, minValue: int):
        if self.MinValue != minValue:
            self.MinValue = minValue
            self.update()

    @pyqtProperty(int)
    def maxValue(self) -> int:
        return self.MaxValue

    @maxValue.setter
    def maxValue(self, maxValue: int):
        if self.MaxValue != maxValue:
            self.MaxValue = maxValue
            self.update()

    @pyqtProperty(int)
    def value(self) -> int:
        return self.Value

    @value.setter
    def value(self, value: int):
        if self.Value != value:
            self.Value = value
            self.update()

    @pyqtProperty(float)
    def borderWidth(self) -> float:
        return self.BorderWidth

    @borderWidth.setter
    def borderWidth(self, borderWidth: float):
        if self.BorderWidth != borderWidth:
            self.BorderWidth = borderWidth
            self.update()

    @pyqtProperty(bool)
    def clockwise(self) -> bool:
        return self.Clockwise

    @clockwise.setter
    def clockwise(self, clockwise: bool):
        if self.Clockwise != clockwise:
            self.Clockwise = clockwise
            self.update()

    @pyqtProperty(bool)
    def showPercent(self) -> bool:
        return self.ShowPercent

    @showPercent.setter
    def showPercent(self, showPercent: bool):
        if self.ShowPercent != showPercent:
            self.ShowPercent = showPercent
            self.update()

    @pyqtProperty(bool)
    def showFreeArea(self) -> bool:
        return self.ShowFreeArea

    @showFreeArea.setter
    def showFreeArea(self, showFreeArea: bool):
        if self.ShowFreeArea != showFreeArea:
            self.ShowFreeArea = showFreeArea
            self.update()

    @pyqtProperty(bool)
    def showSmallCircle(self) -> bool:
        return self.ShowSmallCircle

    @showSmallCircle.setter
    def showSmallCircle(self, showSmallCircle: bool):
        if self.ShowSmallCircle != showSmallCircle:
            self.ShowSmallCircle = showSmallCircle
            self.update()

    @pyqtProperty(QColor)
    def textColor(self) -> QColor:
        return self.TextColor

    @textColor.setter
    def textColor(self, textColor: QColor):
        if self.TextColor != textColor:
            self.TextColor = textColor
            self.update()

    @pyqtProperty(QColor)
    def borderColor(self) -> QColor:
        return self.BorderColor

    @borderColor.setter
    def borderColor(self, borderColor: QColor):
        if self.BorderColor != borderColor:
            self.BorderColor = borderColor
            self.update()

    @pyqtProperty(QColor)
    def backgroundColor(self) -> QColor:
        return self.BackgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: QColor):
        if self.BackgroundColor != backgroundColor:
            self.BackgroundColor = backgroundColor
            self.update()

    def setValue(self, value):
        self.value = value

    def sizeHint(self) -> QSize:
        return QSize(100, 100)

class CircleProgressBar(QWidget):

    Color = QColor(24, 189, 155)  # 圆圈颜色
    Clockwise = True  # 顺时针还是逆时针
    Delta = 36

    def __init__(self, *args, color=None, clockwise=True, **kwargs):
        super(CircleProgressBar, self).__init__(*args, **kwargs)
        self.angle = 0
        self.Clockwise = clockwise
        if color:
            self.Color = color
        self._timer = QTimer(self, timeout=self.update)
        self._timer.start(100)

    def paintEvent(self, event):
        super(CircleProgressBar, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        side = min(self.width(), self.height())
        painter.scale(side / 100.0, side / 100.0)
        painter.rotate(self.angle)
        painter.save()
        painter.setPen(Qt.NoPen)
        color = self.Color.toRgb()
        for i in range(11):
            color.setAlphaF(1.0 * i / 10)
            painter.setBrush(color)
            painter.drawEllipse(30, -10, 20, 20)
            painter.rotate(36)
        painter.restore()
        self.angle += self.Delta if self.Clockwise else -self.Delta
        self.angle %= 360

    @pyqtProperty(QColor)
    def color(self) -> QColor:
        return self.Color

    @color.setter
    def color(self, color: QColor):
        if self.Color != color:
            self.Color = color
            self.update()

    @pyqtProperty(bool)
    def clockwise(self) -> bool:
        return self.Clockwise

    @clockwise.setter
    def clockwise(self, clockwise: bool):
        if self.Clockwise != clockwise:
            self.Clockwise = clockwise
            self.update()

    @pyqtProperty(int)
    def delta(self) -> int:
        return self.Delta

    @delta.setter
    def delta(self, delta: int):
        if self.delta != delta:
            self.delta = delta
            self.update()

    def sizeHint(self) -> QSize:
        return QSize(100, 100)