from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QRoundProgressBar(QWidget):
    def __init__(self, widget):
        super(QRoundProgressBar, self).__init__()

        self.mainFrame = QFrame(widget)
        self.mainFrame.setFixedSize(200, 200)
        self.mainFrame.setStyleSheet("""background-color: rgb(100, 100, 100);
        border-radius: 10px;""")
        self.mainFrame.setObjectName('frame')
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
        self.lRoundProgressBar.setStyleSheet("""border-radius: 70px""")
        self.lRoundProgressBar.setObjectName('lRoundProgressBar')

        self.mainFrameGrid.addWidget(self.lRoundProgressBar, 0, 0, 1, 1)

    def setValue(self, value):
        self.lRoundProgressBar.setText(f"CPU: {value*100:.2f}%")

        if value == 1.0:
            stop1 = "1.0"
            stop2 = "1.0"
        else:
            value = 1.0-value
            stop1 = str(round(value-0.001, 3))
            stop2 = str(round(value, 3))

        style = """border-radius: 95px;
        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:-90,
        stop: {stop1} rgba(0, 255, 0, 100), stop: {stop2} rgba(0, 255, 0, 255));"""
        style = style.replace("{stop1}", stop1).replace("{stop2}", stop2)
        self.roundProgressBar.setStyleSheet(style)

