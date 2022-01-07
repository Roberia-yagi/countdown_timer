import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
import time

DURATION_INT = 3


stylesheet = """
    MainWindow {
        background-image: url("./image.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        uic.loadUi('mainWindow.ui', self)
        self.setWindowTitle('QCheckBox')
        self.setWindowOpacity(0.5)
        self.label_1 = QLabel("transparent ", self)
        self.label_1.move(100, 100)
        self.label_1.adjustSize()
        self.show()

        # # Stay on top
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)
        # # Hide Title bar
        # self.setWindowFlag(Qt.FramelessWindowHint)

    #     self.time_left_int = DURATION_INT
    #     self.widget_counter_int = 0

    #     central_widget = QtWidgets.QWidget()
    #     self.setCentralWidget(central_widget)
    #     vbox = QtWidgets.QVBoxLayout()
    #     central_widget.setLayout(vbox)

    #     self.pages_qsw = QtWidgets.QStackedWidget()
    #     vbox.addWidget(self.pages_qsw)
    #     self.time_passed_qll = QtWidgets.QLabel()
    #     vbox.addWidget(self.time_passed_qll)

    #     self.widget_one = QtWidgets.QLabel("This is widget one")
    #     self.pages_qsw.addWidget(self.widget_one)
    #     self.widget_two = QtWidgets.QLabel("This is widget two")
    #     self.pages_qsw.addWidget(self.widget_two)
    #     self.widget_three = QtWidgets.QLabel("This is widget three")
    #     self.pages_qsw.addWidget(self.widget_three)
    #     self.widget_four = QtWidgets.QLabel("This is widget four")
    #     self.pages_qsw.addWidget(self.widget_four)


    # def timer_start(self):
    #     self.time_left_int = DURATION_INT

    #     self.my_qtimer = QTimer(self)
    #     self.my_qtimer.timeout.connect(self.timer_timeout)
    #     self.my_qtimer.start(1000)

    #     self.update_gui()

    # def timer_timeout(self):
    #     self.time_left_int -= 1

    #     if self.time_left_int == 0:
    #         self.widget_counter_int = (self.widget_counter_int + 1) % 4
    #         self.pages_qsw.setCurrentIndex(self.widget_counter_int)
    #         self.time_left_int = DURATION_INT

    #     self.update_gui()

    # def update_gui(self):
    #     self.time_passed_qll.setText(str(self.time_left_int))

    # def contextMenuEvent(self, event):
    #     contextMenu = QMenu(self)
    #     newAct = contextMenu.addAction("Set a timer")
    #     openAct = contextMenu.addAction("Set a backgroun image")
    #     quitAct = contextMenu.addAction("Quit")
    #     action = contextMenu.exec_(self.mapToGlobal(event.pos()))
    #     if action == quitAct:
    #         self.close()
    #     # if action == newAct:
    #     #     self.timer_start()
    #     # if action == openAct:
    #     #     self.update_gui()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    # main_window.setStyleSheet(stylesheet)
    main_window.show()
    sys.exit(app.exec_())
