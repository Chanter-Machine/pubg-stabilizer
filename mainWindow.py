# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
                               QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
                               QVBoxLayout, QWidget)

global_main_window = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(200, 355)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 191, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.label_run_title = QLabel(self.verticalLayoutWidget)
        self.label_run_title.setObjectName(u"label_run_title")

        self.horizontalLayout_1.addWidget(self.label_run_title)

        self.label_run = QLabel(self.verticalLayoutWidget)
        self.label_run.setObjectName(u"label_run")

        self.horizontalLayout_1.addWidget(self.label_run)

        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_use_gun_title = QLabel(self.verticalLayoutWidget)
        self.label_use_gun_title.setObjectName(u"label_use_gun_title")

        self.horizontalLayout_2.addWidget(self.label_use_gun_title)

        self.label_use_gun = QLabel(self.verticalLayoutWidget)
        self.label_use_gun.setObjectName(u"label_use_gun")

        self.horizontalLayout_2.addWidget(self.label_use_gun)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_gun_1_title = QLabel(self.verticalLayoutWidget)
        self.label_gun_1_title.setObjectName(u"label_gun_1_title")

        self.horizontalLayout_3.addWidget(self.label_gun_1_title)

        self.label_gun_1 = QLabel(self.verticalLayoutWidget)
        self.label_gun_1.setObjectName(u"label_gun_1")

        self.horizontalLayout_3.addWidget(self.label_gun_1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_gun_2_title = QLabel(self.verticalLayoutWidget)
        self.label_gun_2_title.setObjectName(u"label_gun_2_title")

        self.horizontalLayout_4.addWidget(self.label_gun_2_title)

        self.label_gun_2 = QLabel(self.verticalLayoutWidget)
        self.label_gun_2.setObjectName(u"label_gun_2")

        self.horizontalLayout_4.addWidget(self.label_gun_2)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 200, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PUBG-Stabilizer", None))
        self.label_run_title.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u72b6\u6001", None))
        self.label_run.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.label_use_gun_title.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u67aa\u652f", None))
        self.label_use_gun.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.label_gun_1_title.setText(QCoreApplication.translate("MainWindow", u"\u67aa\u652f1\u53f7\u4f4d", None))
        self.label_gun_1.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.label_gun_2_title.setText(QCoreApplication.translate("MainWindow", u"\u67aa\u652f2\u53f7\u4f4d", None))
        self.label_gun_2.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))

    # retranslateUi

    def setLabelRun(self, text):
        self.label_run.setText(text)

    def setLabelUseGun(self, text):
        self.label_use_gun.setText(text)

    def setLabelGun1(self, text):
        self.label_gun_1.setText(text)

    def setLabelGun2(self, text):
        self.label_gun_2.setText(text)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.label_run = self.ui.label_run
        self.label_use_gun = self.ui.label_use_gun
        self.label_gun_1 = self.ui.label_gun_1
        self.label_gun_2 = self.ui.label_gun_2

def run_main_window():
    app = QApplication(sys.argv)
    global_main_window = MainWindow()
    global_main_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    run_main_window()
