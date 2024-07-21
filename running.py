from PyQt5.QtWidgets import QMainWindow
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
            self.setRoundProgressBarValue(value)
            sleep(0.5)

    def setRoundProgressBarValue(self, value):
        self.ui.lRoundProgressBar.setText(f"CPU: {value*100:.2f}%")

        value = 1.0-value
        stop1 = round(value-0.001, 3)
        stop2 = round(value, 3)

        self.ui.roundProgressBar.setStyleSheet(f"""border-radius: 95px;
        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:-90,
        stop: {stop1} rgba(0, 255, 0, 100), stop: {stop2} rgba(0, 255, 0, 255));""")

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
            if self.__i == 0 or self.__cancel:
                break
            self.ui.label.setText(f"Reiniciando en {self.__i} segundos")
