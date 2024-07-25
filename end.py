from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
from ui_end import Ui_End

class End(QMainWindow):
    def __init__(self):
        super(End, self).__init__()
        self.ui = Ui_End()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(20)
        self.shadow.setColor(QColor(0, 255, 0, 255))
        self.ui.pushButton.setGraphicsEffect(self.shadow)
        self.ui.pushButton.installEventFilter(self)

    def eventFilter(self, object, event):
        if object == self.ui.pushButton and event.type() == QEvent.Enter:
            self.shadow.setBlurRadius(50)
            self.ui.pushButton.setGraphicsEffect(self.shadow)
        if object == self.ui.pushButton and event.type() == QEvent.Leave:
            self.shadow.setBlurRadius(20)
            self.ui.pushButton.setGraphicsEffect(self.shadow)

        return False

