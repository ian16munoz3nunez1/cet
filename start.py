from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
import threading
import os
from time import sleep
from ui_start import Ui_Start

class Start(QMainWindow):
    def __init__(self):
        super(Start, self).__init__()
        self.ui = Ui_Start()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startingProcess)

        self.__running = False
        self.__cancel = False
        self.__reboots = 1
        self.__sec = 10
        self.__i = self.__sec

    def startingProcess(self):
        if self.__running == False:
            self.__running = True

            self.__reboots = self.ui.spinBox.value()

            self.ui.spinBox.hide()
            self.ui.pushButton.setText(u"Cancelar")
            self.ui.rebootLabel.show()
            self.ui.rebootLabel.setText(f"Reinicio 1 de {self.__reboots}")
            self.ui.gridlayout.addWidget(self.ui.widget, 0, 0, 3, 1)
            self.ui.gridlayout.addWidget(self.ui.rebootLabel, 0, 1, 1, 1)
            self.ui.gridlayout.addWidget(self.ui.label, 1, 1, 1, 1)
            self.ui.gridlayout.addWidget(self.ui.pushButton, 2, 1, 1, 1)
            
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
                file.write(f"1-{self.__reboots}")
            file.close()
            os.system("shutdown /r /t 1")
        self.close()

    def showProc(self):
        while True:
            if self.__i == 0 or self.__cancel:
                break
            self.ui.label.setText(f"Reiniciando en {self.__i} segundos")

