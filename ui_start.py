from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qroundprogressbar import QRoundProgressBar

class Ui_Start(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName('MainWindow')

        MainWindow.resize(650, 250)
        qRect = MainWindow.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        MainWindow.move(qRect.topLeft())
        MainWindow.setWindowTitle(u"Start")

        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setText(u"Quit")
        self.actionSalir.setShortcut("Ctrl+Q")
        self.actionSalir.setObjectName('actionSalir')

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
        self.rebootLabel.hide()
        self.rebootLabel.setObjectName('rebootLabel')

        self.label = QLabel(self.centralwidget)
        self.label.setText(u"Enter the number of reboots:")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName('label')

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setValue(1)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setAccelerated(True)
        self.spinBox.setObjectName('spinBox')

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setText(u"Start test")
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

        self.gridlayout.addWidget(self.widget, 0, 0, 2, 1)
        self.gridlayout.addWidget(self.label, 0, 1, 1, 1)
        self.gridlayout.addWidget(self.spinBox, 0, 2, 1, 1)
        self.gridlayout.addWidget(self.pushButton, 1, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName('menubar')
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')

        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setTitle(u"File")
        self.menuArchivo.setObjectName('menuArchivo')
        self.menuArchivo.addAction(self.actionSalir)

        self.menubar.addAction(self.menuArchivo.menuAction())

        MainWindow.setMenuBar(self.menubar)
        MainWindow.setStatusBar(self.statusbar)

