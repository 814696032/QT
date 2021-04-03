# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_click_disp.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_list_click_disp(object):
    def setupUi(self, list_click_disp):
        list_click_disp.setObjectName("list_click_disp")
        list_click_disp.resize(798, 590)
        self.horizontalLayout = QtWidgets.QHBoxLayout(list_click_disp)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.img = QtWidgets.QLabel(list_click_disp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy)
        self.img.setText("")
        self.img.setObjectName("img")
        self.verticalLayout.addWidget(self.img)
        self.ok = QtWidgets.QPushButton(list_click_disp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ok.setCheckable(False)
        self.ok.setObjectName("ok")
        self.verticalLayout.addWidget(self.ok)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(list_click_disp)
        QtCore.QMetaObject.connectSlotsByName(list_click_disp)

    def retranslateUi(self, list_click_disp):
        _translate = QtCore.QCoreApplication.translate
        list_click_disp.setWindowTitle(_translate("list_click_disp", "Dialog"))
        self.ok.setText(_translate("list_click_disp", "确定"))


