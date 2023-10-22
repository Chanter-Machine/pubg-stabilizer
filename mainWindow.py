import sys
from mainWindowUi import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
import keyListen


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.label_run = self.ui.label_run
        self.label_use_gun = self.ui.label_use_gun
        self.label_gun_1 = self.ui.label_gun_1
        self.label_gun_2 = self.ui.label_gun_2
        keyListen.init_listener()
        self.keyboard_listener = keyListen.keyboard_listener
        self.mouse_listener = keyListen.mouse_listener
        self.keyboard_listener.start()
        self.mouse_listener.start()

    # 重写 closeEvent 方法
    def closeEvent(self, event):
        # 当窗口关闭时，停止键盘监听器
        self.keyboard_listener.stop()
        self.mouse_listener.stop()

global_main_window = None

def run_main_window():
    app = QApplication(sys.argv)
    global global_main_window
    global_main_window = MainWindow()
    global_main_window.show()
    sys.exit(app.exec())
