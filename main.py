#!/bin/python3

import sys
import os
from PyQt5.QtWidgets import QApplication
from start import Start
from running import Running

app = QApplication(sys.argv)

filename = 'reboot.txt'

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

