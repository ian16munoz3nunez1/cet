from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
import threading
import psutil
import numpy as np
import os
from time import sleep
from ui_running import Ui_Running

class Running(QMainWindow):
    def __init__(self):
        super(Running, self).__init__()
        self.ui = Ui_Running()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.runningProcess)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setBlurRadius(20)
        self.shadow.setColor(QColor(255, 0, 0, 255))
        self.ui.pushButton.setGraphicsEffect(self.shadow)
        self.ui.pushButton.installEventFilter(self)

        self.__currentReboot = 0
        self.__reboots = 0

        self.__running = False
        self.__cancel = False
        self.__end = False

        self.__sec = 10
        self.__i = self.__sec
        self.__cpu = 0

        runCPU = threading.Thread(target=self.runCPU)
        showCPU = threading.Thread(target=self.showCPU)
        runCPU.start()
        showCPU.start()

        self.runningProcess()

    def closeEvent(self, event):
        self.__cancel = True
        self.__end = True

    def eventFilter(self, object, event):
        if object == self.ui.pushButton and event.type() == QEvent.Enter:
            self.shadow.setBlurRadius(50)
            self.ui.pushButton.setGraphicsEffect(self.shadow)
        if object == self.ui.pushButton and event.type() == QEvent.Leave:
            self.shadow.setBlurRadius(20)
            self.ui.pushButton.setGraphicsEffect(self.shadow)

        return False

    def runningProcess(self):
        if self.__running == False:
            self.__running = True

            with open('reboot.txt', 'r') as file:
                content = file.read().split('-')
                self.__currentReboot = int(content[0])
                self.__reboots = int(content[1])
            file.close()

            self.ui.rebootLabel.setText(f"Reinicio {self.__currentReboot+1} de {self.__reboots}")

            t1 = threading.Thread(target=self.runProc)
            t2 = threading.Thread(target=self.showProc)

            t1.start()
            t2.start()

        else:
            self.__cancel = True
            self.__end = True

    def runCPU(self):
        while True:
            if self.__cancel or self.__end:
                break

            cpu = psutil.cpu_percent(interval=1, percpu=True)
            self.__cpu = np.mean(cpu)
            sleep(0.5)

    def showCPU(self):
        while True:
            if self.__cancel or self.__end:
                break

            value = round(self.__cpu/100, 3)
            self.ui.roundProgressBar.setValue(value)
            sleep(0.5)

    def runProc(self):
        while True:
            if self.__i == 0 or self.__cancel:
                break

            self.__i -= 1
            sleep(1)

        self.__end = True
        if self.__i == 0:
            with open('reboot.txt', 'w') as file:
                file.write(f"{self.__currentReboot+1}-{self.__reboots}")
            file.close()
            os.system("shutdown /r /t 1")
        self.close()

    def showProc(self):
        while True:
            if self.__i == 0 or self.__cancel or self.__end:
                break
            self.ui.label.setText(f"Reiniciando en {self.__i} segundos")

