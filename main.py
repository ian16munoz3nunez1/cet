#!/bin/python3

import sys
import os
import getpass
from PyQt5.QtWidgets import QApplication
from start import Start
from running import Running

app = QApplication(sys.argv)
style = """
QMainWindow {
    background-color: rgb(100, 100, 100);
}

QLabel {
    color: rgb(255, 255, 255);
    font: 12pt 'monospace';
}

QSpinBox {
    color: rgb(255, 255, 255);
    font: 12pt 'monospace';
    background-color: rgb(100, 100, 100);
}

QPushButton {
    color: rgb(255, 255, 255);
    font: 12pt 'monospace';
}
"""
app.setStyleSheet(style)

username = getpass.getuser()
filename = 'reboot.txt'
# filename = f'C:\\Users\\{username}\\Desktop\\reboot.txt'

if not os.path.exists(filename):
    start = Start()
    start.show()
else:
    with open(filename, 'r') as file:
        content = file.readline().split('-')
        if int(content[0]) == int(content[1]):
            print("Fin de la prueba")
            sys.exit(1)
    file.close()

    running = Running()
    running.show()

sys.exit(app.exec_())

