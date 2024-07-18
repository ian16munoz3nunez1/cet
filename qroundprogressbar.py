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

        self.backFrame = QFrame(self.mainFrame)
        self.backFrame.setStyleSheet("""border-radius: 90px;
        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:-90,
        stop: 0.099 rgba(0, 255, 0, 100), stop: 0.100 rgba(0, 255, 0, 255));""")
        self.backFrame.setObjectName('backFrame')
        self.backFrameGrid = QGridLayout(self.backFrame)
        self.backFrameGrid.setObjectName('backFrameGrid')
        self.backFrame.setLayout(self.backFrameGrid)

        self.roundFrame = QFrame(self.backFrame)
        self.roundFrame.setStyleSheet("""background-color: rgb(100, 100, 100);
        border-radius: 80px;""")
        self.roundFrame.setObjectName('roundFrame')
        self.roundFrameGrid = QGridLayout(self.roundFrame)
        self.roundFrameGrid.setObjectName('roundFrameGrid')
        self.roundFrame.setLayout(self.roundFrameGrid)

        self.progress = QLabel(self.roundFrame)
        self.progress.setAlignment(Qt.AlignCenter)
        self.progress.setStyleSheet("""border-radius: 70px;""")
        self.progress.setObjectName('progress')

        self.mainFrameGrid.addWidget(self.backFrame, 0, 0, 1, 1)
        self.backFrameGrid.addWidget(self.roundFrame, 0, 0, 1, 1)
        self.roundFrameGrid.addWidget(self.progress, 0, 0, 1, 1)

    def setValue(self, value:str):
        # self.backFrame.setStyleSheet(
        self.progress.setText(f"{value}")

