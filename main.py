import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic
import datetime
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_h_m_s(td):
    m, s = divmod(int(td.total_seconds()), 60)
    h, m = divmod(m, 60)
    return h, m, s


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.window_setting()
        self.tray_setting()
        self.background_setting()
        self.timer_setting()
        self.timer_start()
        self.show()

    def window_setting(self):
        # setting for main window
        # hide from taskbar
        self.setWindowFlags(Qt.Tool)
        self.w_width = 200
        self.w_height = 200
        self.setGeometry(100, 100, self.w_width, self.w_height)
        self.qtRectangle = self.frameGeometry()
        self.point = QDesktopWidget().availableGeometry().topRight()
        self.qtRectangle.moveTopRight(self.point)
        self.move(self.qtRectangle.topLeft())
        # Stay on top
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        # Hide Title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Click-through window
        self.setWindowFlag(Qt.WindowTransparentForInput)

        # opacity
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def tray_setting(self):
        # setting for tray
        icon = QIcon(resource_path('./images/image2_small.png'))
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setVisible(True)

        # To add menus
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
        self.new_pix = QPixmap(self.pixmap_resized.size())
        self.new_pix.fill(Qt.transparent)
        self.painter = QPainter(self.new_pix)
        self.painter.setOpacity(0.5)
        self.painter.drawPixmap(QPoint(), self.pixmap_resized)
        self.painter.end()
        self.label.setPixmap(self.new_pix)

    def create_text(self):
        new_label = QtWidgets.QLabel()
        # new_label.setStyleSheet("background-color: black;")
        new_label.setStyleSheet("color: white;")
        return new_label

    def timer_setting(self):
        # setting vbox
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(40, 40, 40, 20)
        self.central_widget.setLayout(self.vbox)
        self.vbox_days = QtWidgets.QVBoxLayout()
        self.vbox_days.setSpacing(0)
        self.vbox_days.setContentsMargins(0, 0, 0, 0)
        self.hbox_hours = QtWidgets.QHBoxLayout()
        self.hbox_hours.setSpacing(0)
        self.hbox_hours.setContentsMargins(0, 0, 0, 0)
        self.vbox.addLayout(self.vbox_days, 2)
        self.vbox.addLayout(self.hbox_hours, 1)

        # setting days_label
        self.days_label = self.create_text()
        self.days_label.setFont(QFont('851tegakizatsu', 60))
        self.days_left = self.create_text()
        self.days_left.setFont(QFont('851tegakizatsu', 15))
        self.days_left.setText('days left')
        self.vbox_days.addWidget(self.days_label, alignment=(
            Qt.AlignBottom | Qt.AlignCenter))
        self.vbox_days.addWidget(
            self.days_left, alignment=(Qt.AlignTop | Qt.AlignCenter))

        # setting hours_label
        self.hours_label = self.create_text()
        self.hours_label.setFont(QFont('851tegakizatsu', 20))
        self.hours_left = self.create_text()
        self.hours_left.setFont(QFont('851tegakizatsu', 10))
        self.hours_left.setText('hours left')
        self.hbox_hours.addWidget(self.hours_label, alignment=(
            Qt.AlignBottom | Qt.AlignCenter))
        self.hbox_hours.addWidget(
            self.hours_left, alignment=(Qt.AlignBottom | Qt.AlignCenter))

        self.time_goal = datetime.datetime(
            year=2022, month=12, day=31, hour=23, minute=59)

    def update_time(self):
        self.time_now = datetime.datetime.now()
        self.td = self.time_goal - self.time_now
        self.hours, self.minutes, self.seconds = get_h_m_s(self.td)

    def timer_start(self):
        self.update_time()
        self.my_qtimer = QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)

        self.update_gui()

    def timer_timeout(self):
        self.update_time()
        self.update_gui()

    def update_gui(self):
        self.days_label.setText(str(self.td.days))
        self.hours_label.setText(str(self.hours))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    main_window = MainWindow(widget)
    main_window.show()
    sys.exit(app.exec_())
