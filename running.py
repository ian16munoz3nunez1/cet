from PyQt5.QtCore import Qt, QEvent, QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QGraphicsDropShadowEffect
import threading
import psutil
import os
import getpass
from datetime import datetime
from time import sleep
from ui_running import Ui_Running

class Running(QMainWindow):
    def __init__(self):
        super(Running, self).__init__()
        self.ui = Ui_Running()
        self.ui.setupUi(self)
        self.ui.actionSalir.triggered.connect(self.close) # Accion para cerrar la ventana
        self.ui.pushButton.clicked.connect(self.runningProcess) # Boton para iniciar o cancelar el proceso

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(20)
        self.shadow.setColor(QColor(255, 0, 0, 255))
        self.ui.pushButton.setGraphicsEffect(self.shadow)
        self.ui.pushButton.installEventFilter(self)

        self.__currentReboot = 0 # Variable para asignar el reinicio actual
        self.__reboots = 0 # Variable para asignar los reinicios deseados

        self.__running = False # Indica el inicio del proceso
        self.__stop = False # Para pausar el conteo de segundos
        self.__cancel = False # Cancela el proceso
        self.__end = False # Indica el final del proceso de conteo

        self.__sec = 10 # Numero de segundos de espera
        self.__i = self.__sec
        self.__username = getpass.getuser() # Nombre de usuario
        self.__filename = f'C:\\Users\\{self.__username}\\Desktop\\reboot.txt'

        self.timer = QTimer()
        self.timer.timeout.connect(self.showCPU)
        self.timer.start(1000)

        self.runningProcess()

    # Funcion llamada cuando se cierra la ventana
    def closeEvent(self, event):
        self.__cancel = True
        self.__end = True

    # Funcion para iluminar los botones
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

            with open(self.__filename, 'r') as file:
                content = file.read().split('-') # Se lee el contenido del archivo
                self.__currentReboot = int(content[0]) # Se lee el reinicio actual
                self.__reboots = int(content[1]) # Se lee el numero de reinicios actuales
            file.close()

            # Se muestra el estado de reinicios al usuario
            self.ui.rebootLabel.setText(f"Reboot {self.__currentReboot+1} of {self.__reboots}")

            t1 = threading.Thread(target=self.runProc) # Primer hilo a funcion runProc
            t2 = threading.Thread(target=self.showProc) # Segundo hilo a funcion showProc

            # Se inician los hilos
            t1.start()
            t2.start()

        else:
            self.__stop = True # Se detiene el conteo de segundos

            # Pregunta al usuario si quiere cancelar el proceso
            msgBox = QMessageBox()
            msgBox.setWindowTitle(u"Canceling test")
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText(u"Are you sure you want to cancel the test?...")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.No)
            msgBox.setInformativeText(u"Progress will be lost")
            msgBox.setDetailedText(u"The progress of the test will be lost and you will need to start the test again")
            style = """
            QWidget {
                background-color: rgb(100, 100, 100);
            }
            QPushButton {
                min-height: 30px;
                min-width: 40px;
                background-color: rgb(40, 40, 40);
                border: 1px;
                border-style: solid;
                border-color: rgb(0, 0, 200);
                border-radius: 15px;
            }
            QPushButton:hover {
                background: rgb(0, 0, 200);
            }
            QPushButton:pressed {
                background: rgb(0, 0, 180);
            }
            """
            msgBox.setStyleSheet(style)
            msgBox.setObjectName('msgBox')

            ans = msgBox.exec_()

            if ans == QMessageBox.Yes: # Se cancela el proceso
                self.hide()
                os.remove(self.__filename)

                msgBox = QMessageBox()
                msgBox.setWindowTitle(u"Test canceled")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText(f"{self.__currentReboot} reboots of {self.__reboots}")
                now = datetime.now()
                date = now.strftime('%Y/%m/%d')
                time = now.strftime('%H:%M:%S')
                msgBox.setInformativeText(f"Test canceled at\n{date}\n{time}")
                style = """
                QWidget {
                    background-color: rgb(100, 100, 100);
                }
                QPushButton {
                    min-height: 30px;
                    min-width: 40px;
                    background-color: rgb(40, 40, 40);
                    border: 1px;
                    border-style: solid;
                    border-color: rgb(0, 0, 200);
                    border-radius: 15px;
                }
                QPushButton:hover {
                    background-color: rgb(0, 0, 200);
                }
                QPushButton:pressed {
                    background-color: rgb(0, 0, 180);
                }
                """
                msgBox.setStyleSheet(style)
                msgBox.exec_()

                self.__cancel = True
                self.__end = True

            else: # Se reanuda el proceso
                self.__stop = False

    # Funcion para mostrar el estado del CPU
    def showCPU(self):
        cpu = psutil.cpu_percent()
        value = round(cpu/100, 3)
        self.ui.roundProgressBar.setValue(value)

    # Funcion para llevar el conteo de segundos (Hilo 1)
    def runProc(self):
        while True:
            if self.__i == 0 or self.__cancel:
                break

            if self.__stop:
                self.__i = self.__i
            else:
                self.__i -= 1
            sleep(1)

        self.__end = True
        if self.__i == 0: # Se actualiza el estado del archivo de conteo
            with open(self.__filename, 'w') as file:
                file.write(f"{self.__currentReboot+1}-{self.__reboots}")
            file.close()
            os.system("shutdown /r /t 1") # Reinicia el sistema en Windows
        self.close() # Cierra la ventana

    # Funcion para mostrar los segundos restantes (Hilo 2)
    def showProc(self):
        while True:
            if self.__i == 0 or self.__cancel or self.__end:
                break
            self.ui.label.setText(f"Rebooting in {self.__i} seconds")

