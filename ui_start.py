from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qroundprogressbar import QRoundProgressBar

class Ui_Start(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName('MainWindow')

        MainWindow.setGeometry(400, 200, 300, 200)
        MainWindow.setWindowTitle(u"Start")

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName('centralwidget')
        self.gridlayout = QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName('gridlayout')
        self.centralwidget.setLayout(self.gridlayout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setFixedSize(210, 210)
        self.widget.setObjectName('widget')
        self.widgetGrid = QGridLayout(self.widget)
        self.widgetGrid.setObjectName('widgetGrid')
        self.widget.setLayout(self.widgetGrid)

        self.roundProgressBar = QRoundProgressBar(self.widget)
        self.roundProgressBar.setValue(u"75%")
        self.widgetGrid.addWidget(self.roundProgressBar, 0, 0, 1, 1)

        self.rebootLabel = QLabel(self.centralwidget)
        self.rebootLabel.setAlignment(Qt.AlignCenter)
        self.rebootLabel.hide()
        self.rebootLabel.setObjectName('rebootLabel')

        self.label = QLabel(self.centralwidget)
        self.label.setText(u"Ingresa el numero de reinicios:")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName('label')

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setValue(1)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setAccelerated(True)
        self.spinBox.setObjectName('spinBox')

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setText(u"Iniciar proceso")
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.pushButton.setObjectName('pushButton')

        self.gridlayout.addWidget(self.widget, 0, 0, 2, 1)
        self.gridlayout.addWidget(self.label, 0, 1, 1, 1)
        self.gridlayout.addWidget(self.spinBox, 0, 2, 1, 1)
        self.gridlayout.addWidget(self.pushButton, 1, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName('menubar')
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')

        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)

