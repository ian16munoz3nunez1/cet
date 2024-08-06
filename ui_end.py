from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_End(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName('MainWindow')

        MainWindow.resize(200, 150)
        qRect = MainWindow.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        MainWindow.move(qRect.topLeft())
        MainWindow.setWindowTitle(u"Test complete")

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName('centralwidget')
        self.gridlayout = QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName('gridlayout')
        self.centralwidget.setLayout(self.gridlayout)

        self.label = QLabel(self.centralwidget)
        self.label.setText(u"Test completed successfully")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName('label')

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setText(u"OK")
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.pushButton.setStyleSheet("""QPushButton {
            min-height: 30px;
            background-color: rgb(40, 40, 40);
            border: 1px;
            border-style: solid;
            border-color: rgb(0, 160, 0);
            border-radius: 15px;
        }

        QPushButton:hover {
            background: rgb(0, 200, 0);
        }
        QPushButton:pressed {
            background: rgb(0, 180, 0);
        }""")
        self.pushButton.setObjectName('pushButton')

        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.pushButton, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName('menubar')
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')

        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)

