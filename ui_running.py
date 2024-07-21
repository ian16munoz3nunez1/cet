from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qroundprogressbar import QRoundProgressBar

class Ui_Running(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName('MainWindow')

        MainWindow.setGeometry(400, 200, 300, 200)
        MainWindow.setWindowTitle(u"Running")

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName('centralwidget')
        self.gridlayout = QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName('gridlayout')
        self.centralwidget.setLayout(self.gridlayout)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setFixedSize(200, 200)
        self.mainFrame.setStyleSheet("""border-radius: 10px;
        background-color: rgb(100, 100, 100);""")
        self.mainFrame.setObjectName('mainFrame')
        self.mainFrameGrid = QGridLayout(self.mainFrame)
        self.mainFrameGrid.setObjectName('mainFrameGrid')
        self.mainFrame.setLayout(self.mainFrameGrid)

        self.roundProgressBar = QFrame(self.mainFrame)
        self.roundProgressBar.setGeometry(QRect(5, 5, 190, 190))
        self.roundProgressBar.setStyleSheet("""border-radius: 95px;
        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:-90,
        stop: 0.999 rgba(0, 255, 0, 100), stop: 1.0 rgba(0, 255, 0, 255));""")
        self.roundProgressBar.setObjectName('roundProgressBar')

        self.backFrame = QFrame(self.mainFrame)
        self.backFrame.setGeometry(QRect(20, 20, 160, 160))
        self.backFrame.setStyleSheet("""border-radius: 80px;
        background-color: rgb(100, 100, 100);""")
        self.backFrame.setObjectName('backFrame')

        self.lRoundProgressBar = QLabel(self.mainFrame)
        self.lRoundProgressBar.setFixedSize(140, 140)
        self.lRoundProgressBar.setAlignment(Qt.AlignCenter)
        self.lRoundProgressBar.setStyleSheet("""border-radius: 70px;""")
        self.lRoundProgressBar.setObjectName('roundProgressBar')

        self.mainFrameGrid.addWidget(self.lRoundProgressBar, 0, 0, 1, 1)

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

        self.gridlayout.addWidget(self.mainFrame, 0, 0, 3, 1)
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

