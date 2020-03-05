# -*- coding: utf-8 -*-
1
# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(354, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_rx = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_rx.setMinimumSize(QtCore.QSize(100, 100))
        self.textBrowser_rx.setObjectName("textBrowser_rx")
        self.gridLayout_2.addWidget(self.textBrowser_rx, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setMaximumSize(QtCore.QSize(300, 300))
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.pushButton_reflash = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reflash.setMaximumSize(QtCore.QSize(300, 300))
        self.pushButton_reflash.setObjectName("pushButton_reflash")
        self.verticalLayout.addWidget(self.pushButton_reflash)
        self.pushButton_portEnable = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_portEnable.setMaximumSize(QtCore.QSize(300, 300))
        self.pushButton_portEnable.setObjectName("pushButton_portEnable")
        self.verticalLayout.addWidget(self.pushButton_portEnable)
        self.comboBox_sPort = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_sPort.setMaximumSize(QtCore.QSize(300, 300))
        self.comboBox_sPort.setObjectName("comboBox_sPort")
        self.verticalLayout.addWidget(self.comboBox_sPort)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 100))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.textBrowser_tx = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_tx.setObjectName("textBrowser_tx")
        self.verticalLayout_2.addWidget(self.textBrowser_tx)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 2, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout_2.addWidget(self.verticalScrollBar, 1, 2, 2, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 354, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_reflash.setText(_translate("MainWindow", "刷新串口"))
        self.pushButton_portEnable.setText(_translate("MainWindow", "打开端口"))
        self.label.setText(_translate("MainWindow", "ms/次"))
        self.checkBox_2.setText(_translate("MainWindow", "定时发送"))
        self.checkBox.setText(_translate("MainWindow", "hex"))
        self.pushButton_3.setText(_translate("MainWindow", "hold"))
        self.pushButton_2.setText(_translate("MainWindow", "关机"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
