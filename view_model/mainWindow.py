import datetime
import sys

from PySide6.QtCore import QMetaObject, Qt, Q_ARG

from model.secret import parse_activate
from view.mainWindowUi import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import model.keyListen
from model.tts import text2voice_list, text2voice
from model.contants import c_contants
from model.equipment import c_equipment
from model.mouse import c_mouse
import json


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionSaveConfig.triggered.connect(self.save_json_config)

        self.ui.pushButton_edit1.clicked.connect(self.on_pushButton_edit1_keyPressEvent)
        self.ui.pushButton_edit2.clicked.connect(self.on_pushButton_edit2_keyPressEvent)
        self.ui.pushButton_save1.clicked.connect(self.on_pushButton_save1_keyPressEvent)
        self.ui.pushButton_save2.clicked.connect(self.on_pushButton_save2_keyPressEvent)

        model.keyListen.init_listener()
        self.keyboard_listener = c_contants.keyboard_listener
        self.mouse_listener = c_contants.mouse_listener
        self.keyboard_listener.start()
        self.mouse_listener.start()

    # 重写 closeEvent 方法
    def closeEvent(self, event):
        # 当窗口关闭时，停止键盘监听器
        self.keyboard_listener.stop()
        self.mouse_listener.stop()

    def on_pushButton_edit1_keyPressEvent(self, event):
        self.ui.gun1_textEdit.setEnabled(True)

    def on_pushButton_edit2_keyPressEvent(self, event):
        self.ui.gun2_textEdit.setEnabled(True)

    def on_pushButton_save1_keyPressEvent(self, event):
        self.ui.gun1_textEdit.setEnabled(False)
        new_basic_config_string = self.ui.gun1_textEdit.toPlainText()
        try:
            new_basic_config = json.loads(new_basic_config_string)
            c_contants.guns[c_equipment.wepone1.name]["basic"] = new_basic_config
            c_equipment.wepone1.basic = new_basic_config
        except:
            QMessageBox.information(None, "Error", "保存配置失败")

    def on_pushButton_save2_keyPressEvent(self, event):
        self.ui.gun2_textEdit.setEnabled(False)
        new_basic_config_string = self.ui.gun2_textEdit.toPlainText()
        try:
            new_basic_config = json.loads(new_basic_config_string)
            c_contants.guns[c_equipment.wepone2.name]["basic"] = new_basic_config
            c_equipment.wepone2.basic = new_basic_config
        except:
            QMessageBox.information(None, "Error", "保存配置失败")

    def update_use_gun(self, gun_name):
        self.ui.label_use_gun.setText(gun_name)

    def update_equipment(self):
        self.ui.label_gun_1.setText(c_equipment.wepone1.name)
        self.ui.label_gun_2.setText(c_equipment.wepone2.name)
        wepone1_basic_json = json.dumps(c_equipment.wepone1.basic)
        QMetaObject.invokeMethod(self.ui.gun1_textEdit, "setText", Qt.QueuedConnection, Q_ARG(str, wepone1_basic_json))
        wepone2_basic_json = json.dumps(c_equipment.wepone2.basic)
        QMetaObject.invokeMethod(self.ui.gun2_textEdit, "setText", Qt.QueuedConnection, Q_ARG(str, wepone2_basic_json))
        text2voice_list(["武器1", c_equipment.wepone1.name, "武器2", c_equipment.wepone2.name])

    def update_mouse_control_status(self):
        if c_mouse.openFlag:
            self.ui.label_run.setText("运行中")
            text2voice("运行中")
        else:
            self.ui.label_run.setText("已停止")
            text2voice("已停止")

    def save_json_config(self):
        json.dump(c_contants.guns, open("./resource/config.json", "w", encoding="utf-8"), indent=4, ensure_ascii=False)
        QMessageBox.information(None, "Message", "已保存配置")


global_main_window = None


def run_main_window():
    app = QApplication(sys.argv)
    global global_main_window
    global_main_window = MainWindow()
    date = parse_activate("./resource/secrets/activate")
    c_contants.isAuthorized = str(datetime.datetime.now()) <= date
    if not c_contants.isAuthorized:
        QMessageBox.information(None, "DFrank Warning",
                                "DDDDDFRANK       Push GITHUB!!!   \n    \n OR \n\n \nWatch out your ASS HOLE      ")
        sys.exit()

    global_main_window.show()
    sys.exit(app.exec())
