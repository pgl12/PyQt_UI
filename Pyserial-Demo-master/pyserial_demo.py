import sys
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from ui_demo_1 import Ui_Form
import pyqtgraph as pg
import numpy as np
import re
import xlwt
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import _thread
import threading


def_serial_rx_mode=0



class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    data_dict = {}  # 存放所有收到的数据
    data_time=[]
    Max_count = 7200  # 页面最多显示的数据个数
    p1={}
    temperature=24.5
    rx_num_last=0
    rx_num=0
    rx_timeOut=0
    rx_data=bytes()
    rx_OK_Flag=0
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("hcd-CT1-test")
        self.ser = serial.Serial()
        self.port_check()

        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        self.lineEdit_4.setText(str(self.temperature))

        self.pushButton_4.clicked.connect(self.temperature_add)
        self.pushButton_5.clicked.connect(self.temperature_reduce)

        win = pg.GraphicsWindow()
        win.setWindowTitle(u'波形显示')
        self.verticalLayout_3.addWidget(win)
        self.p1 = win.addPlot()  # win.addPlot()添加一个波形窗口，多次调用会将窗口分成多个界面
        self.p1.addLegend()  # 不添加就显示不了图例 ，一定要放在plot前调用

        # timer1 = pg.QtCore.QTimer()
        #         # timer1.timeout.connect(self.addToDisplay)  # 定时刷新数据显示
        #         # timer1.start(1)
        self.DisplayConfig()
        #_thread.start_new_thread(self.data_receive,None)
        #self.rx_thread = threading.Thread(target=self.data_receive)
        #self.rx_thread.start()
        pass

    def addToDisplay(self):

        for i in self.data_dict.items():
            data = i[1][1]  # 数据部分
            curve = i[1][0]  # 当前的线
            # if(len(data) > 1000):#一个界面都数据控制在1000个
            #     data=data[-1000:]
            # else:
            #     data = data[:]
            curve.setData(data)  # 添加数据显示
            pass
    # 配置波形显示信息
    def DisplayConfig(self):
        self.p1.showGrid(x=True, y=True, alpha=0.5)
        self.p1.setLabels(left='y/Value', bottom='x/point', title='iGtable')  # left纵坐标名 bottom横坐标名

        #label = pg.TextItem()
        #self.p1.addItem(label)

    # 将串口收到的数据添加到字典
    # 数据格式 “name1,float;name2,flaot\n”
    def AddDataToDict(self,rxData):
        rxData = rxData.split("\\n")  # 目的是去除最后的\n换行，别的方式还没用明白
        str_arr = rxData[0].split(';')  # 因为上边分割了一下，所以是数组
        color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']  # 颜色表，这些应该够了，最多8条线，在添加颜色可以用(r,g,b)表示
        getFlag=0
        for a in str_arr:  # 遍历获取单个变量 如“a,1;b,2;c,3”中的"a,1"
            s = a.split(',')  # 提取名称和数据部分
            if (len(s) != 2):  # 不等于2字符串可能错了，正确的只有名称和数据两个字符串
                print("len-error")
                print("rxData%s" %rxData)
                print(str_arr)
                return
            name = s[0]
            val_str = re.findall(r"^[-+]?([0-9]+(\.[0-9]*)?|\.[0-9]+)([eE][-+]?[0-9]+)?$", s[1])[0]  # 用正则表达式提取数字部分
            print(val_str)
            print(name)
            if (len(val_str) > 0):  # 再判断下是否匹配到了数字
                val = float(val_str[0])  # 转成浮点型数字
                if (self.data_dict.get(name) == None):  # 判断是否存在添加当前键值，None则需要添加键值
                    # curve = p.plot(pen = color[len(data_dict)],name=name,symbolBrush=color[len(data_dict)])#为新的变量添加新的曲线,显示数据点
                    curve = self.p1.plot(pen=color[len(self.data_dict)], name=name)  # 为新的变量添加新的曲线
                    self.data_dict[name] = [curve]  # 在字典中添加当前键值，并赋值曲线，字典数据格式{key:[curve,[dadta1,data2,...]]}
                    self.data_dict[name].append([val])  # 将当前数据已列表的形式添加到字典对象中
                    getFlag +=1
                else:  # 键值存在直接添加到对应的数据部分
                    if (len(self.data_dict[s[0]][1]) == self.Max_count):  # 限制一下页面数据个数
                        self.data_dict[s[0]][1] = self.data_dict[s[0]][1][1:-1]
                        self.data_dict[s[0]][1][-1] = float(s[1])
                        getFlag +=1
                    else:
                        self.data_dict[s[0]][1].append(val)
                        getFlag +=1

            else:  # 接收错误
                print("error:" + a)

                return
        time_now=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(time_now)
        if getFlag >0:
            self.data_time.append(time_now)

        #print("self.data_time['time']:%s" % self.data_time)

    def init(self):
        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)

        # 串口信息显示
        self.s1__box_2.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.close_button.clicked.connect(self.port_close)

        # 发送数据按钮
        self.s3__send_button.clicked.connect(self.data_send)

        # 定时发送数据
        self.timer_send = QTimer()
        self.timer_send.timeout.connect(self.data_send)
        self.timer_send_cb.stateChanged.connect(self.data_send_timer)

        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

        # 清除发送窗口
        self.s3__clear_button.clicked.connect(self.send_data_clear)

        # 清除接收窗口
        self.s2__clear_button.clicked.connect(self.receive_data_clear)

        # 保存曲线按钮
        self.pushButton_3.clicked.connect(self.save_cure)

    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        self.s1__box_2.clear()
        for port in port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.s1__box_2.addItem(port[0])
        if len(self.Com_Dict) == 0:
            self.state_label.setText(" 无串口")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.s1__box_2.currentText()
        if imf_s != "":
            self.state_label.setText(self.Com_Dict[self.s1__box_2.currentText()])

    # 打开串口
    def port_open(self):
        self.ser.port = self.s1__box_2.currentText()
        self.ser.baudrate = int(self.s1__box_3.currentText())
        self.ser.bytesize = int(self.s1__box_4.currentText())
        self.ser.stopbits = int(self.s1__box_6.currentText())
        self.ser.parity = self.s1__box_5.currentText()

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        # 打开串口接收定时器，周期为2ms
        self.timer.start(10)

        if self.ser.isOpen():
            self.open_button.setEnabled(False)
            self.close_button.setEnabled(True)
            self.formGroupBox1.setTitle("串口状态（已开启）")

    # 关闭串口
    def port_close(self):
        self.timer.stop()
        self.timer_send.stop()
        try:
            self.ser.close()
        except:
            pass
        self.open_button.setEnabled(True)
        self.close_button.setEnabled(False)
        self.lineEdit_3.setEnabled(True)
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        self.formGroupBox1.setTitle("串口状态（已关闭）")

    # 发送数据
    def data_send(self):
        if self.ser.isOpen():
            input_s = self.s3__send_text.toPlainText()
            if input_s != "":
                # 非空字符串
                if self.hex_send.isChecked():
                    # hex发送
                    input_s = input_s.strip()
                    send_list = []
                    while input_s != '':
                        try:
                            num = int(input_s[0:2], 16)
                        except ValueError:
                            QMessageBox.critical(self, 'wrong data', '请输入十六进制数据，以空格分开!')
                            return None
                        input_s = input_s[2:].strip()
                        send_list.append(num)
                    input_s = bytes(send_list)
                else:
                    # ascii发送
                    input_s = (input_s + '\r\n').encode('utf-8')

                num = self.ser.write(input_s)
                self.data_num_sended += num
                self.lineEdit_2.setText(str(self.data_num_sended))
        else:
            pass

    # 接收数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if def_serial_rx_mode == 1:
            if num > 0:
                self.rx_data = self.rx_data+self.ser.read(num)
                self.rx_num_last = len(self.rx_data)
                print("rx_len:%d" %self.rx_num_last)
                pass
            if self.rx_num_last > 0 and num == 0:
                self.rx_timeOut += 1
                if self.rx_timeOut >= 20:
                    self.rx_OK_Flag = 1
                pass
            else:
                self.rx_OK_Flag = 0
                pass

        else:
            self.rx_OK_Flag = 0

        if self.rx_OK_Flag > 0 or num > 0:

            if def_serial_rx_mode == 1:
                data = self.rx_data
                print(data)
                num = len(self.rx_data)
                self.rx_num_last = 0
                self.rx_data = bytes()
                self.rx_OK_Flag = 0
            else:
                data = self.ser.read(num)
                num = len(data)
                print(data)
                print("rx_len:%d" % num)


            rxData=data.decode()
            #print(rxData)
            self.AddDataToDict(rxData)
            self.addToDisplay()

            #hex显示
            if self.hex_receive.checkState():
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                self.s2__receive_text.insertPlainText(out_s)
            else:
                # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                self.s2__receive_text.insertPlainText(data.decode('iso-8859-1'))



            # 统计接收字符的数量
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))

            # 获取到text光标
            textCursor = self.s2__receive_text.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.s2__receive_text.setTextCursor(textCursor)
        else:
            pass


    # 定时发送数据
    def data_send_timer(self):
        if self.timer_send_cb.isChecked():
            self.timer_send.start(int(self.lineEdit_3.text()))
            self.lineEdit_3.setEnabled(False)
        else:
            self.timer_send.stop()
            self.lineEdit_3.setEnabled(True)

    # 清除显示
    def send_data_clear(self):
        self.s3__send_text.setText("")

    def receive_data_clear(self):
        self.s2__receive_text.setText("")

    def save_cure(self):
        wb = xlwt.Workbook(encoding='ascii')  # 创建新的Excel（新的workbook），建议还是用ascii编码
        ws = wb.add_sheet('table')  # 创建新的表单weng
        #print(self.data_dict)
        ws.write(0, 0, label='time')
        y=1
        for savetime in self.data_time:
            ws.write(y, 0, label=savetime)
            y=y+1
            pass
        i=1
        print("savetime")
        for key in self.data_dict.keys():
            ws.write(0, i, label=format(key))  # 在（0,0）加入hello
            y=1
            #print(self.data_dict[key])
            for key_value in self.data_dict[key][1]:
                ws.write(y, i, label=key_value)
                #print('key_value',key_value)
                y=y+1
                pass
            #print('key = {}'.format(key))
            i = i + 1
            pass
        getTime=time.strftime("%y%m%d %H_%M_%S.xls", time.localtime())
        #getTime=getTime+'.xls'
        print(getTime)
        wb.save(getTime)  # 保存为weng.xls文件
        QMessageBox.about(self,"提示","保存ok，文件在应用程序目录下")
        pass
    def temperature_add(self):
        self.temperature = round(self.temperature+0.2,2)
        self.lineEdit_4.setText(str(self.temperature))
        self.temperature_send()
        pass
    def temperature_reduce(self):
        self.temperature = round(self.temperature-0.2,2)
        self.lineEdit_4.setText(str(self.temperature))
        self.temperature_send()
        pass
    def temperature_send(self):
        sendBuff="set_roomtemp="+str(self.temperature)
        if self.ser.isOpen():
            self.ser.write(sendBuff.encode('utf-8'))
        print(sendBuff)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())
