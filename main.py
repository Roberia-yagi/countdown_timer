import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtWidgets, uic
import time
import os

DURATION_INT = 3


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.window_setting()
        self.tray_setting()
        self.background_setting()

        # setting for timer
        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        self.pages_qsw = QtWidgets.QStackedWidget()
        vbox.addWidget(self.pages_qsw)
        self.time_passed_qll = QtWidgets.QLabel()
        vbox.addWidget(self.time_passed_qll)

        self.widget_one = QtWidgets.QLabel("This is widget one")
        self.pages_qsw.addWidget(self.widget_one)
        self.widget_two = QtWidgets.QLabel("This is widget two")
        self.pages_qsw.addWidget(self.widget_two)
        self.widget_three = QtWidgets.QLabel("This is widget three")
        self.pages_qsw.addWidget(self.widget_three)
        self.widget_four = QtWidgets.QLabel("This is widget four")
        self.pages_qsw.addWidget(self.widget_four)

    def window_setting(self):
        # setting for main window
        self.w_width = 200
        self.w_height = 200
        self.setGeometry(100, 100, self.w_width, self.w_height)
        self.qtRectangle = self.frameGeometry()
        self.point = QDesktopWidget().availableGeometry().topRight()
        self.qtRectangle.moveTopRight(self.point)
        self.move(self.qtRectangle.topLeft())
        self.setWindowOpacity(0.5)
        # Stay on top
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        # Hide Title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Click-through window
        self.setWindowFlag(Qt.WindowTransparentForInput)

    def tray_setting(self):
        # setting for tray
        icon = QIcon(resource_path('./images/image2_small.png'))
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setVisible(True)

        # To quit the app
        self.menu = QMenu()
        self.quit = QAction("Quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)

        # Adding options to the System Tray
        self.tray.setContextMenu(self.menu)

    def background_setting(self):
        # setting for background image
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.w_width, self.w_height)
        self.pixmap = QPixmap(resource_path('./images/image2.png'))
        self.pixmap_resized = self.pixmap.scaledToWidth(self.w_width)
        self.label.setPixmap(self.pixmap_resized)
        self.show()

    def timer_start(self):
        self.time_left_int = DURATION_INT

        self.my_qtimer = QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)

        self.update_gui()

    def timer_timeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:
            self.widget_counter_int = (self.widget_counter_int + 1) % 4
            self.pages_qsw.setCurrentIndex(self.widget_counter_int)
            self.time_left_int = DURATION_INT

        self.update_gui()

    def update_gui(self):
        self.time_passed_qll.setText(str(self.time_left_int))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_icon = QIcon((resource_path('./images/image2_256.png')))
    app.setWindowIcon(app_icon)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
