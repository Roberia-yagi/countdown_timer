import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
 
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
 
        uic.loadUi('test.ui', self)
        self.setGeometry(300, 50, 400, 350)
        self.setWindowTitle('QCheckBox')
        # Stay on top
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        # Hide Title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())