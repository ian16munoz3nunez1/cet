from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qroundprogressbar import QRoundProgressBar

class Ui_Running(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName('MainWindow')

        MainWindow.resize(500, 250)
        qRect = MainWindow.frameGeometry()
        centerPoint = QDektopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        MainWindow.move(qRect.topLeft())
        MainWindow.setWindowTitle(u"Running")

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName('centralwidget')
        self.gridlayout = QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName('gridlayout')
        self.centralwidget.setLayout(self.gridlayout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setFixedSize(200, 200)
        self.widget.setObjectName('widget')
        self.widgetGrid = QGridLayout(self.widget)
        self.widgetGrid.setObjectName('widgetGrid')
        self.widget.setLayout(self.widgetGrid)

        self.roundProgressBar = QRoundProgressBar(self.widget)
        self.widgetGrid.addWidget(self.roundProgressBar, 0, 0, 1, 1)

        self.rebootLabel = QLabel(self.centralwidget)
        self.rebootLabel.setAlignment(Qt.AlignCenter)
        self.rebootLabel.setObjectName('rebootLabel')

        self.label = QLabel(self.centralwidget)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName('label')

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setText(u"Cancelar")
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.pushButton.setObjectName('pushButton')

        self.gridlayout.addWidget(self.widget, 0, 0, 3, 1)
        self.gridlayout.addWidget(self.rebootLabel, 0, 1, 1, 1)
        self.gridlayout.addWidget(self.label, 1, 1, 1, 1)
        self.gridlayout.addWidget(self.pushButton, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName('menubar')
        self.statusbar = QStatusBar()
        self.statusbar.setObjectName('statusbar')

        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)

