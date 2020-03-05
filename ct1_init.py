import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import pyqtgraph as pg
import numpy as np
import serial
import serial.tools.list_ports
from serial_ui import*
import GL   # GL.py 中存放了程序需要用到的全局变量







class ct1_windows_init(object):
    uiInfo = Ui_MainWindow()
    comport = 'COM7'
    baudrate = 9600
    serialName=list()
    serialFd=0
    def serial_init(self):
        plist = list(serial.tools.list_ports.comports())
        if len(plist) <= 0:
            print("没有发现端口!")
        else:
            plist_0 = list(plist[0])
            serialName = plist_0[0]
            serialFd = serial.Serial(serialName, 9600, timeout=60)
            print("可用端口名>>>", serialFd.name)
        pass
        self.uiInfo.comboBox_2=QtWidgets.QComboBox(self.serialName)


    pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ct1_windows=ct1_windows_init()
    ct1_windows.serial_init()
    ct1_windows.uiInfo.setupUi(MainWindow)
# ui = Ui_MainWindow()
#ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())