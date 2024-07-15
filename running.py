from PyQt5.QtWidgets import QMainWindow
import threading
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
        self.__sec = 10
        self.__i = self.__sec
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

    def runProc(self):
        while True:
            if self.__i == 0 or self.__cancel:
                break

            self.__i -= 1
            sleep(1)

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

