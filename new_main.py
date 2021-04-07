#-*- coding: utf-8 -*-
from UI_Init import MainDialog,About_Window,\
    Setting_Window,Image_Window,List_disp,\
    PercentProgressBar,CircleProgressBar
from Lib import External,QSSLoad,VideoCapture
from experiment.xml_test import GetItems,Xml_Tools
from dialog import Ui_about
from PyQt5.QtWidgets import *
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets,QtTest
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy as np
import shutil
import datetime
import configparser as cp
import win32con
import ctypes
import time
from win32process import SuspendThread, ResumeThread
from PyQt5 import QtMultimedia

#逻辑文件，业务文件
class AppDialog(MainDialog):
    # <editor-fold desc="属性">
    cur = 0  # 载入文件夹图片时，用于标定当前显示图片
    change_item_num = 0
    object_item_num = 0
    mode = -1  # 0 图片模式 1 文件夹模式  2视频模式 3数据模式 4正在播放 5正在暂停
    files = []  # 载入文件夹图片时，读入文件名
    dir_name = ''  # 目录名字
    ctrlPressed = False  # ctrl键是否被按下，用于实现ctrl+滚轮缩放图像
    # image = []  # 当前显示图片，用于刷新显示
    last_dir = ''  # 记录上次目录
    zoomscale = 1  # 记录图片的缩放比例
    new_image = []
    isShow = False
    isPlay = False
    window_size_record = {"pos_x": 0, "pox_y": 0, "width": -1, "height": -1, "INIT": 1}  # 记录屏幕尺寸，用于切换图片时不会重新调整大小
    window_state=1  # 记录全屏前的窗口状态，1代表正常大小，2代表最大化
    MousePressed=False
    MouseTmpPos=[]
    cfg={'position':'0,0','fullscreen':'False','history_cmp_dir':'','gps_dir':''}
    # </editor-fold>
    def __init__(self,parent=None):
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.conf = cp.ConfigParser()
        self.readConfigFile()  # 载入配置
        super(AppDialog, self).__init__(parent)
        MainDialog()
        if eval(self.cfg['fullscreen']):
            self.showFullScreen()
            self.maxwin.setHidden(True)
            self.minwin.setHidden(True)
            # self.maxwin.setEnabled(False)
            # self.minwin.setEnabled(False)
        if not eval(self.cfg['fullscreen']):
            self.setGeometry(eval(self.cfg['position'].split(',')[0]),eval(self.cfg['position'].split(',')[1]),self.width(),self.height())
        print(self.width(),self.height())
        self.about_window = About_Window()
        self.setting_window = Setting_Window()
        self.sublay = Image_Window()
        self.sublay.hide()

        self.list_disp = List_disp()
        self.desktop = QApplication.desktop()
        self.screen_rect = self.desktop.screenGeometry()
        try:
            shutil.rmtree('./temp/change_temp')
            shutil.rmtree('./temp/object_temp')
        except:
            pass
        os.mkdir('./temp/change_temp')
        os.mkdir('./temp/object_temp')
        self.progress_bar=PercentProgressBar()
        self.progress_bar.setGeometry(int(self.desktop.width()/2)-75,int(self.desktop.height()/2)-75,150,150)
        self.progress_bar.setAttribute(Qt.WA_TranslucentBackground,True)
        self.progress_bar.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool )
        self.progress_bar.setWindowModality(Qt.ApplicationModal )
        # self.progress_bar.setWindowModality(Qt.WindowModal)
        #self.progress_bar.show()
        self.progress_wait = CircleProgressBar()
        self.progress_wait.setGeometry(int(self.desktop.width()/2)-75,int(self.desktop.height()/2)-75,100,100)
        self.progress_wait.setAttribute(Qt.WA_TranslucentBackground,True)
        self.progress_wait.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool )
        self.progress_wait.setWindowModality(Qt.ApplicationModal )
        self.progress_bar.hide()
        self.progress_wait.hide()

        # 右侧列表点击显示
        self.list1.itemDoubleClicked.connect(self.list_disp.show)
        self.list2.itemDoubleClicked.connect(self.list_disp.show)  # 新建窗口
        self.list1.itemDoubleClicked.connect(lambda: self.list_show(self.list1))
        self.list2.itemDoubleClicked.connect(lambda: self.list_show(self.list2))  # 显示小图
        self.list1.itemClicked.connect(lambda: self.list_show_little(self.list1))
        self.list2.itemClicked.connect(lambda: self.list_show_little(self.list2))


    # *********菜单功能调用************
        # <editor-fold desc="菜单功能调用">
        self.action_openfile.triggered.connect(self.openfile)
        self.action_opendir.triggered.connect(self.opendir)
        self.action_openvideo.triggered.connect(self.openvideo)

        self.action_about.triggered.connect(self.about_window.show)
        self.action_view1.triggered.connect(self.click_view1)
        self.action_view2.triggered.connect(self.click_view2)
        self.action_setting.triggered.connect(self.setting_show)
        self.action_restart.triggered.connect(self.restart)
        self.action_save.triggered.connect(self.save_result)

        # </editor-fold>
    # *********设置功能调用************  TODO 这里还有个小bug：打开设置，改动后点击取消，窗口状态还是保持了，只是设置没应用，这里要修改
        # <editor-fold desc="设置功能调用">
        self.setting_window.setting_ok.clicked.connect(self.setting_ok_event)
        self.setting_window.setting_apply.clicked.connect(self.setting_apply_event)
        self.setting_window.setting_cancel.clicked.connect(self.setting_cancel_event)
        self.setting_window.history_dir_open.clicked.connect(self.open_history_cmp_dir)
        self.setting_window.history_dir_explorer.clicked.connect(self.open_history_cmp_dir_explorer)
        self.setting_window.history_dir_open_gps.clicked.connect(self.open_gps_dir)
        self.setting_window.history_dir_explorer_gps.clicked.connect(self.open_gps_dir_explorer)
        # </editor-fold>
    # ********显示功能调用**************
        self.sublay.image_left.clicked.connect(lambda: self.lastImage())
        self.sublay.image_right.clicked.connect(lambda: self.nextImage())
        self.sublay.image_start_detect.clicked.connect(self.play_auto)
        self.sublay.image_stop_detect.clicked.connect(self.play_stop)
        self.sublay.image_close.clicked.connect(self.restart)
        self.sublay.image_line.stateChanged.connect(self.line_check_event)
        self.sublay.image_change_detect.stateChanged.connect(self.change_check_event)
        self.sublay.image_obj_detect.stateChanged.connect(self.obj_check_event)
        self.workspace_lay.addWidget(self.sublay)
    # *********切换选项卡部分功能*******
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
    # *********事件部分重写************
    # <editor-fold desc="事件部分">
    def printf(self, mes):  # print日志到日志窗口
        now_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.textBrowser.append("["+now_time+"] " + mes)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

    def resizeEvent(self,event):
        self.background_movie.setScaledSize(QtCore.QSize(self.centralwidget.width(), self.centralwidget.height()))
        if self.isShow:
            self.freshImage()
            # self.sublay.update()
            # print("刷新图片")
        else:
            pass

    def title_double_click(self):  # 双击标题栏最大化复原
        if not self.isFullScreen():
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()
    def title_LMouseMove(self,event):  # 移动标题栏（只支持logo space 部分  按钮对此无效）
        if self.MousePressed==True and not self.isMaximized() and not self.isFullScreen():  # 最大化时无法移动
            self.move(self.x()+(event.globalX()-self.MouseTmpPos[0]),
                             self.y()+(event.globalY()-self.MouseTmpPos[1]))
            self.MouseTmpPos = [event.globalX(), event.globalY()]
        else:
            # print("normal title move")
            pass

    def eventFilter(self, obj, event): #重写事件过滤器 不同组件之间的互动 重要部分
        if obj==self.menubar:
            if event.type()==QMouseEvent.MouseMove:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.title_LMouseMove(event)
            if event.type()==QMouseEvent.MouseButtonDblClick:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.title_double_click()
                elif mouseEvent.button() == Qt.MidButton:
                    print("按下鼠标中键")
                elif mouseEvent.buttons() == Qt.RightButton:
                    print("按下了鼠标右键")
            if event.type()==QMouseEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.MousePressed = True
                    self.MouseTmpPos=[event.globalX(),event.globalY()]
                # print(self.MouseTmpPos)
            if event.type()==QMouseEvent.MouseButtonRelease:
                self.MousePressed=False
                self.MouseTmpPos=[]
                # print(self.MousePressed)
        return False

    def keyPressEvent(self, event): #监控按键事件  用于添加快捷键
        if (event.key() == QtCore.Qt.Key_A):  # A D实现同一目录下的显示图片切换
            self.lastImage()
        elif(event.key()==QtCore.Qt.Key_D):
            self.nextImage()
    # </editor-fold>
    #******************槽函数部分*********************
    def __show_warning_message_box(self, msg):
        QMessageBox.warning(self, "警告", msg, QMessageBox.Ok)
    def line_check_event(self,sig):
        if sig==0 and self.line_group is not None:
            self.line_group.hide()
        if (sig==2 or sig==1) and self.line_group is not None:
            self.line_group.show()
        # print("line_check_test")
        QApplication.processEvents()
    def change_check_event(self,sig):
        if sig==0 and self.cd_group is not None:
            self.cd_group.hide()
        if (sig==2 or sig==1) and self.cd_group is not None:
            self.cd_group.show()
        QApplication.processEvents()
    def obj_check_event(self,sig):
        if sig==0 and self.od_group is not None:
            self.od_group.hide()
        if (sig==2 or sig==1)and self.od_group is not None:
            self.od_group.show()
        QApplication.processEvents()
    #***************主菜单逻辑函数*****************
    # <editor-fold desc="主菜单逻辑函数">
    def readConfigFile(self):  # 载入配置文件
        self.conf.read('Configuration.ini',encoding="utf-8")
        self.cfg['position'] = self.conf.get('setting','Position')
        self.cfg['fullscreen']=self.conf.get('setting','Fullscreen')
        self.cfg['history_cmp_dir']=self.conf.get('setting','History_cmp_dir')
        self.cfg['gps_dir']=self.conf.get('setting','Gps_dir')
        print("配置文件加载成功！")

    def saveConfigFile(self):  # 保存配置文件
        # 载入和保存逻辑如下：载入后，更新self.cfg属性，窗口的变化实时与self.cfg挂钩，保存时，只保存self.cfg到json文件就好
        # 载入后，还要更新setting的窗口表现，还存在一点bug
        self.conf.set('setting','Position',self.cfg['position'])
        self.conf.set('setting', 'Fullscreen', self.cfg['fullscreen'])
        self.conf.set('setting', 'History_cmp_dir', self.cfg['history_cmp_dir'])
        self.conf.set('setting', 'Gps_dir', self.cfg['gps_dir'])
        self.conf.write(open('Configuration.ini', 'w'))
        self.printf("配置文件保存成功!")


    def openfile(self): #菜单中openfile 绑定的槽函数
        self.cur = 0
        self.files=[]
        # self.image=[]  # 清空文件和图片列表，防止多次打开出现bug
        if self.last_dir=="":  # 如果第一次打开  就进入程序目录； 后续打开 进入上一次的目录
            open_path = self.cwd
        else:
            open_path = self.last_dir
        openfile_name, openfile_type = QtWidgets.QFileDialog.getOpenFileName(None,"选择图片",open_path,
                                                                            "Img Files (*.jpg *.jpeg *.bmp);;All Files (*)")  # 起始路径
        print(openfile_name)
        if openfile_name == "": #取消选择
            self.__show_warning_message_box("未选择图片")
            return
        if self.isShow:  # 避免同时打开多个窗口
            self.restart()

        typelist = ['jpg', 'jpeg', 'bmp']
        if os.path.splitext(openfile_name)[-1][1:].lower() not in typelist:
            self.__show_warning_message_box("无法打开该格式的文件")
            return

        current_dir = os.path.dirname(openfile_name)  # 实现打开上次访问的目录
        if current_dir != open_path:
            self.last_dir = current_dir
        self.dir='' #避免bug  线程在用 且保留
        self.files.append(openfile_name)  # 打开图片和打开目录一样 只得到一个filelist
        xml_path = current_dir + "/" + os.path.split(openfile_name)[1].split('.')[0]+".xml"
        self.mode = 0
        self.show_window_build(xml_path)


    def opendir(self):#与opendir绑定
        self.cur = 0  # 默认从第一张开始显示
        self.files=[]
        # self.image=[] # 清空文件和图片列表，防止多次打开出现bug
        if self.last_dir=="":  # 如果第一次打开  就进入程序目录； 后续打开 进入上一次的目录
            open_path = self.cwd
        else:
            open_path = self.last_dir
        self.dir_name = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                                             "选择文件夹",
                                                                             open_path)  # 起始路径
        if self.isShow:  # 避免同时打开多个窗口
            self.restart()
        if self.dir_name == "": #取消选择
            self.__show_warning_message_box("未选择目录")
            return
        self.mode = 1
        if self.dir_name != open_path:  # 实现打开上一次访问的目录
            self.last_dir = self.dir_name
        typelist = ['jpg','jpeg','bmp']
        for root, dirs, filelist in os.walk(self.dir_name,topdown=True,followlinks=False): #读入时 需排除非图片部分
            # 读取图片文件  根据后缀名列表只筛选出图片文件
            for i in range(len(filelist)):
                suffix = os.path.splitext(filelist[i])[-1][1:].lower()  # lower防止大写后缀名出现bug
                if suffix in typelist:
                    self.files.append(root + "/" + filelist[i])
            break
        if len(self.files)==0:
            self.__show_warning_message_box("目录为空")
            return
        xml_path = self.dir_name+"/"+self.dir_name.split('/')[-1] +".xml"
        self.show_window_build(xml_path)

    def openvideo(self): #与openvideo绑定 载入视频
        # TODO 载入视频的过程需要等待  暂时不能取消 后续会加入
        self.files=[]  # 清理缓存
        self.cur = 0
        if self.last_dir=="":  # 如果第一次打开  就进入程序目录； 后续打开 进入上一次的目录
            open_path = self.cwd
        else:
            open_path = self.last_dir
        openfile_name, openfile_type = QtWidgets.QFileDialog.getOpenFileName(None,"选择视频",open_path,
                                                                             "Img Files (*.mp4 *.avi);;All Files (*)")  # 起始路径

        if openfile_name == "": #取消选择
            self.__show_warning_message_box("未选择视频")
            return
        if self.isShow:  # 避免同时打开多个窗口
            self.restart()
        typelist = ['mp4', 'avi']
        if os.path.splitext(openfile_name)[-1][1:].lower() not in typelist:
            self.__show_warning_message_box("无法打开该格式的文件")
            return

        file = openfile_name.split('/')[-1]
        current_dir = os.path.dirname(openfile_name)
        self.video_xml_path = current_dir + "/" + os.path.split(openfile_name)[1].split('.')[0]+".xml"
        if current_dir != open_path:
            self.last_dir = current_dir
        video_pic_path = current_dir + "/" + file
        self.vc = VideoCapture(openfile_name)
        self.vc.progress.connect(self.openvideo_slot)
        self.vc.info.connect(self.openvideo_info_slot)
        self.vc.f.connect(self.openvideo_addfile_slot)
        self.progress_bar.setValue(0)
        self.vc.start()
        self.progress_bar.show()

    def openvideo_slot(self,val):
        self.progress_bar.setValue(val)
        QtWidgets.QApplication.processEvents()
    def openvideo_info_slot(self,st):
        if st !="finish":
            self.printf(st)
        else:
            self.progress_bar.hide()
            self.mode = 2
            self.show_window_build(self.video_xml_path)
    def openvideo_addfile_slot(self,file):
        self.files.append(file)

    def show_window_build(self,xml_path = './current.xml'):
        self.op = Xml_Tools(xml_path)
        self.op.Init_xml(xml_path)
        self.bd = BackgroudDisp(self.files,self.op)
        self.bd.Finish.connect(self.printf)
        self.bd.start()
        # self.update_image_window_UI()
        # self.sublay.show()
        # self.sublay.image_title.setText(current_file_name)
        # 展示窗口标题栏需不需要动态变化还在商榷
        # 甚至可以试试 来一个进度条
        self.showImage2()

    def showImage2(self,mask1=None,mask2=None,mask3=None):
        self.isShow = True
        current_file_name = self.files[self.cur]
        img = cv2.imdecode(np.fromfile(current_file_name, dtype=np.uint8), -1)  # 读入中文目录 RGB格式
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # 转化为BGR格式
        # 在这里叠加mask
        # if mask1 is not None:
        #     img = merge_mask(img,mask1)
        #     # img = img + mask1  # 带画线的
        # if mask2 is not None:  # 带变化的
        #     change_item_temp_pic = merge_mask(img,mask2)
        #     # change_item_temp_pic = img + mask2
        #     self.list_add_item(self.list1,change_item_temp_pic)  # 将画线与变化存入item
        # if mask3 is not None:  # 带目标的
        #     object_item_temp_pic = merge_mask(img, mask3)
        #     # object_item_temp_pic = img + mask3
        #     self.list_add_item(self.list2, object_item_temp_pic)  # 将画线与目标存入item
        # if mask2 is not None:
        #     img = img + mask2
        # if mask3 is not None:
        #     img = img + mask3
        # 图片属性（先读入图片属性，再根据属性调整窗口和视野）
        height,width,depth = img.shape
        ratio = float(height / width)  # 高宽比

        # 使用graphicsView显示图片
        self.cvimg = QImage(img.data, width, height, width * depth, QImage.Format_RGB888)
        self.pix = QtGui.QPixmap.fromImage(self.cvimg)
        self.item = QtWidgets.QGraphicsPixmapItem(self.pix)  # 创建像素图元
        self.scene = QtWidgets.QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)

        while(1):
            # print("正在寻找",self.cur)
            flag,d = self.op.read(os.path.split(current_file_name)[1])
            if(flag):
                # print("已找到")
                break;
            self.progress_wait.show()
            QApplication.processEvents()
        self.progress_wait.hide()
        gi = GetItems(d)
        self.line_group, self.cd_group, self.od_group = gi.Disp()
        self.scene.addItem(self.line_group)
        self.scene.addItem(self.cd_group)
        self.scene.addItem(self.od_group)


        self.sublay.image_view.setScene(self.scene)
        self.sublay.image_view.setStyleSheet("padding: 0px; border: 0px;")  # view正好和图片一致时不会出现滑条
        self.sublay.image_view.fitInView(self.item, Qt.KeepAspectRatio)
        self.sublay.image_view.centerOn(self.item)
        # self.sublay.image_view.fitInView(self.item4, Qt.KeepAspectRatio)
        self.sublay.image_view.viewport().update()
        self.update_image_window_UI()
        self.sublay.show()

    # def showImage

    def update_image_window_UI(self):
        # 每次显示图片时，根据图片序号 修改显示的UI
        # 左右切换的按钮开关
        if self.mode == 4:# 正在播放
            self.sublay.image_left.setHidden(True)
            self.sublay.image_right.setHidden(True)
            self.sublay.image_stop_detect.setEnabled(True)
            self.sublay.switch_play_icon('p')
        elif self.mode == 5:
            self.sublay.image_left.setHidden(True)
            self.sublay.image_right.setHidden(True)
            self.sublay.image_stop_detect.setEnabled(True)
            self.sublay.switch_play_icon('s')
        else:
            self.sublay.image_left.setHidden(False)
            self.sublay.image_right.setHidden(False)
            self.sublay.switch_play_icon('s')
            self.sublay.image_stop_detect.setEnabled(False)
            num = len(self.files)
            if(num==1):
                self.sublay.image_left.setEnabled(False)
                self.sublay.image_right.setEnabled(False)
            else:
                if self.cur==0:
                    self.sublay.image_left.setEnabled(False)
                    self.sublay.image_right.setEnabled(True)
                elif self.cur==num-1:
                    self.sublay.image_left.setEnabled(True)
                    self.sublay.image_right.setEnabled(False)
                else:
                    self.sublay.image_right.setEnabled(True)
                    self.sublay.image_left.setEnabled(True)
        QApplication.processEvents()


    def restart(self):  # 清除缓存，清除窗口
        reply = QtWidgets.QMessageBox.question(self, '保存确认', '是否保存现有检测结果？',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No |
                                               QtWidgets.QMessageBox.Cancel)
        if reply == QtWidgets.QMessageBox.Yes:
            self.save_result()  # 保存当前工作
        if reply == QtWidgets.QMessageBox.Cancel:
            return

        # 结束进程
        self.bd.is_running = False

        try:

            self.thread.stop()
            print("已终止线程") # 暂时有问题
        except:
            print("线程未开启")
        if self.isShow:
            self.sublay.hide()
            self.files = []
            self.cur = 0
            self.sublay.image_left.setEnabled(True)
            self.sublay.image_right.setEnabled(True)
            self.isShow = False
        if self.list1.count():
            self.list_info.setText("None")
            self.list1.clear()
            shutil.rmtree('./temp/change_temp')
            os.mkdir('./temp/change_temp')
        if self.list2.count():
            self.list_info.setText("None")
            self.list2.clear()
        self.textBrowser.clear()
        self.printf("重置程序")

    def save_result(self):
        save_path = self.cwd
        self.res_save_dir_name = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                                             "选择保存文件夹",
                                                                             save_path)  # 保存路径
        if self.res_save_dir_name == "":
            return
        today = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        print(self.res_save_dir_name + '/' + today)
        self.progress_bar.show()
        calc = External()
        calc.countChanged.connect(self.onCountChanged)
        calc.start()

        shutil.copytree('./temp', self.res_save_dir_name+'/'+today, ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
        try:
            StrText = self.textBrowser.toPlainText()
            qS = str(StrText)
            f = open(self.res_save_dir_name+'/'+today+"/log.txt", 'w')
            print(f.write('{}'.format(qS)))
            f.close()
        except Exception as e:
            print(e)

        self.progress_bar.setValue(100)
        QtTest.QTest.qWait(500)
        self.progress_bar.hide()
        self.printf("保存检测结果至"+self.res_save_dir_name+'/'+today)

    def onCountChanged(self,val):
        self.progress_bar.setValue(val)
    #***************界面部分逻辑函数******************

    def close_tab(self,index):
        # TODO 这里要保存下这个tab的状态和数据  设置为隐藏的话 可能不需要保存 还存在问题
        self.printf("关闭选项卡")
        self.tabWidget.setTabEnabled(index,False)
        self.tabWidget.setStyleSheet("QTabBar::tab:disabled {width: 0;color:transparent;}")
        # self.tabWidget.removeTab(index)
        if index==0:
            self.action_view1.setIconVisibleInMenu(False)
        if index==1:
            self.action_view2.setIconVisibleInMenu(False)

    def click_view1(self):
        if self.action_view1.isIconVisibleInMenu():#说明选项卡已经打开了
            self.tabWidget.setTabEnabled(0, False)
            self.tabWidget.setStyleSheet("QTabBar::tab:disabled{width: 0;color:transparent;}")
            self.action_view1.setIconVisibleInMenu(False)
            return
        # tab_change = QWidget()
        # tab_change.setObjectName("changelist")
        # self.tabWidget.addTab(tab_change,"变化检测")
        self.tabWidget.setTabEnabled(0,True)
        self.tabWidget.setTabEnabled(1,True)
        self.tabWidget.setStyleSheet("QTabBar::tab:first{width: 120;color:rgb(255,255,255);}")
        self.action_view1.setIconVisibleInMenu(True)
        self.action_view2.setIconVisibleInMenu(True)
    def click_view2(self):
        if self.action_view2.isIconVisibleInMenu():#说明选项卡已经打开了
            self.tabWidget.setTabEnabled(1, False)
            self.tabWidget.setStyleSheet("QTabBar::tab:disabled{width: 0;color:transparent;}")
            self.action_view2.setIconVisibleInMenu(False)
            return
        # tab_objlist = QWidget()
        # tab_objlist.setObjectName("objlist")
        # self.tabWidget.addTab(tab_objlist,"目标检测")
        self.tabWidget.setTabEnabled(1,True)
        self.tabWidget.setTabEnabled(0, True)
        self.tabWidget.setStyleSheet("QTabBar::tab:last{width: 120;color:rgb(255,255,255);}")
        self.action_view2.setIconVisibleInMenu(True)
        self.action_view1.setIconVisibleInMenu(True)
        # TODO 实现不同选项卡不同样式，以保证单独显示

    def nextImage(self):  # next image
        if self.cur==len(self.files)-1:
            return
        self.cur = self.cur + 1
        self.showImage2()

    def lastImage(self):  # previous image
        if self.cur==0:
            return
        self.cur = self.cur - 1
        self.showImage2()
    # </editor-fold>
    #------------------设置窗口的逻辑函数--------------------#
    # <editor-fold desc="设置窗口逻辑函数">
    #cfg={'Fullscreen':'False','history_cmp_dir':'','save_dir':''}#
    def setting_show(self):
        self.setting_window.setting_apply.setEnabled(True)
        self.setting_window.show()

    def setting_ok_event(self):  # 设置窗口的确定按钮功能
        # TODO 设置ok后需要重新加载一次设置，以实现应用
        # 直接按确定相当于先应用后退出
        self.setting_apply_event()
        self.setting_window.close()

    def setting_apply_event(self):  # 设置窗口的应用按钮功能
        # TODO 设置应用后重新加载一次设置，实现应用
        if self.setting_window.Fullscreen.isChecked():
            if self.isMaximized():
                self.window_state = 2
            else:
                self.window_state = 1
            self.showFullScreen()
            self.cfg['fullscreen']='True'
            # self.minwin.setEnabled(False)
            # self.maxwin.setEnabled(False)  # 全屏后要屏蔽最大化和最小化按钮 避免bug
            self.maxwin.setHidden(True)
            self.minwin.setHidden(True)  # 选择隐藏的方式或者直接禁用按钮的方式
        else:
            # self.minwin.setEnabled(True)  # 非全屏恢复最大化最小化按钮
            # self.maxwin.setEnabled(True)
            self.maxwin.setHidden(False)
            self.minwin.setHidden(False)
            if self.window_state == 2:
                self.showMaximized()
            else:
                self.showNormal()
            self.cfg['fullscreen'] = 'False'
        self.cfg['history_cmp_dir'] = self.setting_window.history_dir_edit.text()
        self.saveConfigFile()
        self.setting_window.setting_apply.setEnabled(False)

    def setting_cancel_event(self):  # 设置窗口的取消按钮功能
        self.setting_window.close()

    def open_history_cmp_dir(self):  # 这个是设置窗口里的选择文件夹按钮功能
        if self.cfg['history_cmp_dir']=="":  # 打开进入当前历史影像文件夹的目录
            open_path = self.cwd
        else:
            open_path = self.cfg['history_cmp_dir']
        self.cmp_dir_name = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                                             "选择历史影像文件夹",
                                                                             open_path)  # 起始路径
        if self.cmp_dir_name == "":
            return
        self.cfg['history_cmp_dir']=self.cmp_dir_name
        self.setting_window.history_dir_edit.setText(self.cfg["history_cmp_dir"])

    def open_history_cmp_dir_explorer(self):  # 设置窗口的打开文件夹按钮功能，在资源管理器中直接打开
        try:
            os.startfile(self.setting_window.history_dir_edit.text())
            # TODO 这里是通过直接读取当前的text 没有经过cfg 考虑后续会改进
        except:
            self.__show_warning_message_box("路径不存在！")

    def open_gps_dir(self):
        if self.cfg['gps_dir']=="":  # 打开进入当前历史影像文件夹的目录
            open_path = self.cwd
        else:
            open_path = self.cfg['gps_dir']
        self.gps_dir_name = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                                             "选择GPS文件夹",
                                                                             open_path)  # 起始路径
        if self.gps_dir_name == "":
            return
        self.cfg['gps_dir']=self.gps_dir_name
        self.setting_window.dir_gps.setText(self.cfg["gps_dir"])
    def open_gps_dir_explorer(self):  # 设置窗口的打开文件夹按钮功能，在资源管理器中直接打开
        try:
            os.startfile(self.setting_window.dir_gps.text())
            # TODO 这里是通过直接读取当前的text 没有经过cfg 考虑后续会改进
        except:
            self.__show_warning_message_box("路径不存在！")
    # </editor-fold>
    #-----------------主窗口逻辑函数-----------------
    # <editor-folder desc="主窗口逻辑函数">
    def list_show(self,list_widget):
        item = list_widget.selectedItems()[0]
        self.list_disp.setWindowTitle(item.text())
        self.list_disp.img.setScaledContents(True)
        if list_widget.objectName()=='list1':
            pix = QPixmap(QImage('./temp/change_temp/%s_%s.jpg'%(list_widget.objectName(),item.text())))
        else:
            pix = QPixmap(QImage('./temp/object_temp/%s_%s.jpg' % (list_widget.objectName(), item.text())))
        pix.scaled(self.list_disp.img.width(),self.list_disp.img.height(),Qt.KeepAspectRatioByExpanding)
        self.list_disp.img.setPixmap(pix)

    def list_show_little(self,list_widget):
        item = list_widget.selectedItems()[0]
        if list_widget.objectName()=='list1':
            pix = QPixmap(QImage('./temp/change_temp/%s_%s.jpg'%(list_widget.objectName(),item.text())))
        else:
            pix = QPixmap(QImage('./temp/object_temp/%s_%s.jpg'%(list_widget.objectName(),item.text())))
        pix.scaled(self.list_info.size(),Qt.KeepAspectRatio)
        self.list_info.setPixmap(pix)
        self.list_info.setScaledContents(True)

    def list_add_item(self,list,mask):
        mask = cv2.cvtColor(mask, cv2.COLOR_RGB2BGR)
        if list==self.list1:
            cv2.imwrite("./temp/change_temp/list1_%s.jpg" % self.change_item_num, mask)
            self.printf("检测到变化")
            self.list1.addItem('%s' % self.change_item_num)
            self.change_item_num += 1
        if list==self.list2:
            self.printf("检测到目标")
            cv2.imwrite("./temp/object_temp/list2_%s.jpg" % self.object_item_num, mask)
            self.list2.addItem('%s' % self.object_item_num)
            self.object_item_num += 1

    def freshImage(self):
        self.sublay.image_view.fitInView(self.item,Qt.KeepAspectRatio)

    def play_auto(self):
        if(self.mode!=4 and self.mode!=5): # 第一次启动
            self.mode = 4
            self.update_image_window_UI()
            self.play_thread = Play()
            self.play_thread.next_signal.connect(self.play_slot)
            self.play_thread.start()  # 启动线程
        elif(self.mode==4):  # 要暂停
            if self.play_thread.handle == -1:
                return print('handle is wrong')
            ret = SuspendThread(self.play_thread.handle)
            print('挂起线程', self.play_thread.handle, ret)

            self.mode = 5
            self.update_image_window_UI()
        else:  # 要恢复
            if self.play_thread.handle == -1:
                return print('handle is wrong')
            ret = ResumeThread(self.play_thread.handle)
            print('恢复线程', self.play_thread.handle, ret)

            self.mode = 4
            self.update_image_window_UI()

    def play_stop(self):
        ret = ctypes.windll.kernel32.TerminateThread(  # @UndefinedVariable
            self.play_thread.handle, 0)
        print('终止线程', self.play_thread.handle, ret)
        self.mode = 2
        self.update_image_window_UI()



    def play_slot(self): # i 为 1 时  说明产生变化  添加列表项
        if(self.cur==len(self.files)-1):
            self.play_thread.play_is_running = False
            self.play_stop()
        else:
            self.nextImage()


from experiment.box_factory import BoxFactory
class BackgroudDisp(QThread):
    Finish = pyqtSignal(str)
    is_running = True
    def __init__(self,path_list,op):
        super(BackgroudDisp,self).__init__()
        self.path_list = path_list
        self.op = op
        self.size = len(path_list)
        self.cur = 0
        self.width = 1920
        self.height = 1080
        self.depth = 3
        self.factory = BoxFactory(self.width,self.height)
        self.is_running = True

    def run(self):
        import time
        while(self.cur<=self.size-1 and self.is_running):
            path = self.path_list[self.cur]
            size_info = [self.width,self.height,self.depth]
            line_info = self.factory.line()
            time.sleep(0.1)
            cd_info = self.factory.cd_box()
            time.sleep(0.5)
            od_info = self.factory.od_box()
            time.sleep(0.2)
            self.op.write(path,size_info,line_info,cd_info,od_info)
            self.cur+=1
        if self.is_running:
            self.Finish.emit("后台处理完成！")
        else:
            self.Finish.emit("中断后台处理")


class Play(QThread):  # 播放图片的线程
    next_signal =pyqtSignal()
    handle = -1
    is_running = True
    def __init__(self):
        super().__init__()
        self.is_running = True

    def run(self):
        try:
            self.handle = ctypes.windll.kernel32.OpenThread(  # @UndefinedVariable
                win32con.PROCESS_ALL_ACCESS, False, int(QThread.currentThreadId()))
        except Exception as e:
            print('get thread handle failed', e)
        print('thread id', int(QThread.currentThreadId()))
        while self.is_running:
            time.sleep(1)
            self.next_signal.emit()
        print('播放进程结束')


if __name__=='__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    myapp = QApplication(sys.argv)

    # 启动画面
    splash = QSplashScreen(QPixmap("./Resource/welcome.jpg"))  #启动界面图片地址
    splash.show()  # 展示启动图片
    myapp.processEvents() #防止进程卡死
    # 加载设置
    try:
        cfg_file = open("./Configuration.ini", "r+", encoding='UTF-8')
    except:

        dia = QDialog()
        QMessageBox.warning(dia,"配置文件缺失", "未找到 Configuration.ini 文件", QMessageBox.Ok)
        splash.close()
        sys.exit()
    #创建对象
    myDlg = AppDialog()
    # 加载样式
    qssFileName = "./Resource/main.qss"  # 样式文件路径
    qssFile = QSSLoad.readQssFile(qssFileName)

    # 显示主窗口
    myDlg.setStyleSheet(qssFile)
    myDlg.show()
    myapp.installEventFilter(myDlg) #安装重写的eventFilter捕获应用事件的方法
    # 进入改程序的主循环
    splash.finish(myDlg)   #关闭启动界面
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(myapp.exec_()) #exit 确保程序完整地结束  为了保持python2兼容  exec()