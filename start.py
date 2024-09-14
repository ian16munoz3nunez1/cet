from PyQt5.QtCore import Qt, QEvent, QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QGraphicsDropShadowEffect
import threading
import psutil
import os
import getpass
from time import sleep
from ui_start import Ui_Start

class Start(QMainWindow):
    def __init__(self):
        super(Start, self).__init__()
        self.ui = Ui_Start()
        self.ui.setupUi(self)
        self.ui.actionSalir.triggered.connect(self.close) # Accion para cerrar la ventana
        self.ui.pushButton.clicked.connect(self.startingProcess) # Boton para iniciar o cancelar el proceso

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(20)
        self.shadow.setColor(QColor(0, 255, 0, 255))
        self.ui.pushButton.setGraphicsEffect(self.shadow)
        self.ui.pushButton.installEventFilter(self)

        self.__running = False # Indica que inicio el proceso
        self.__stop = False # Para pausar el conteo de segundos
        self.__cancel = False # Cancela el proceso
        self.__end = False # Indica el final del proceso de conteo

        self.__reboots = 1
        self.__sec = 10 # Numero de segundos de espera
        self.__i = self.__sec
        self.__username = getpass.getuser() # Nombre de usuario
        self.__filename = f'C:\\Users\\{self.__username}\\Desktop\\reboot.txt'

        self.timer = QTimer()
        self.timer.timeout.connect(self.showCPU)
        self.timer.start(500)

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

    def startingProcess(self):
        if self.__running == False:
            self.__running = True

            self.__reboots = self.ui.spinBox.value() # Se lee el numero de reinicios deseados

            self.ui.spinBox.hide() # Se oculta el SpinBox
            self.shadow.setColor(QColor(255, 0, 0, 255)) # Se cambia el color de la sombra de verde a rojo
            self.ui.pushButton.setText(u"Cancel") # Se cambia el texto del boton
            # Estilo del boton
            self.ui.pushButton.setStyleSheet("""QPushButton {
            min-height: 30px;
            background-color: rgb(40, 40, 40);
            border: 1px;
            border-style: solid;
            border-color: rgb(160, 0, 0);
            border-radius: 15px;
            }
            QPushButton:hover {
            background: rgb(200, 0, 0);
            }
            QPushButton:pressed {
            background: rgb(180, 0, 0);
            }""")
            # Se agrega un Label para mostrar el numero de reinicios
            self.ui.rebootLabel.show()
            self.ui.rebootLabel.setText(f"Reboot 1 of {self.__reboots}")
            # Se modifica la cuadricula de la ventana
            self.ui.gridlayout.addWidget(self.ui.widget, 0, 0, 3, 1)
            self.ui.gridlayout.addWidget(self.ui.rebootLabel, 0, 1, 1, 1)
            self.ui.gridlayout.addWidget(self.ui.label, 1, 1, 1, 1)
            self.ui.gridlayout.addWidget(self.ui.pushButton, 2, 1, 1, 1)

            t1 = threading.Thread(target=self.runProc) # Primer hilo a funcion runProc
            t2 = threading.Thread(target=self.showProc) # Segundo hilo a funcion showProc

            # Inicio de los hilos
            t1.start()
            t2.start()

        else:
            self.__stop = True # Detiene el conteo de segundos

            # Pregunta al usuario si quiere cancelar el proceso
            ans = QMessageBox.warning(
                self,
                "Canceling test",
                "Are you sure you want to cancel the test?...",
                buttons=QMessageBox.Yes | QMessageBox.No,
                defaultButton=QMessageBox.No
            )

            if ans == QMessageBox.Yes: # Se cancela el proceso
                self.hide()
                QMessageBox.critical(
                    self,
                    "Test canceled",
                    f"0 reboots of {self.__reboots}"
                )

                self.__cancel = True
                self.__end = True
            else: # Se reanuda el proceso
                self.__stop = False

    # Funcion para mostar el estado del CPU
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
        if self.__i == 0:
            with open(self.__filename, 'w') as file: # Se crea un archivo de conteo
                file.write(f"1-{self.__reboots}") # Se guarda el estado de los reinicios
            file.close()
            os.system("shutdown /r /t 1") # Reinicia el sistema en Windows
        self.close() # Cierra la ventana

    # Funcion para mostrar los segundos restantes (Hilo 2)
    def showProc(self):
        while True:
            if self.__i == 0 or self.__cancel or self.__end:
                break
            self.ui.label.setText(f"Rebooting in {self.__i} seconds")

