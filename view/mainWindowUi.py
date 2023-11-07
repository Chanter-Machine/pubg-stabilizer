# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowUi.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 350)
        self.actionSaveConfig = QAction(MainWindow)
        self.actionSaveConfig.setObjectName(u"actionSaveConfig")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 481, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.label_run_title = QLabel(self.verticalLayoutWidget)
        self.label_run_title.setObjectName(u"label_run_title")
        self.label_run_title.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_1.addWidget(self.label_run_title)

        self.label_run = QLabel(self.verticalLayoutWidget)
        self.label_run.setObjectName(u"label_run")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_run.sizePolicy().hasHeightForWidth())
        self.label_run.setSizePolicy(sizePolicy)

        self.horizontalLayout_1.addWidget(self.label_run)


        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_use_gun_title = QLabel(self.verticalLayoutWidget)
        self.label_use_gun_title.setObjectName(u"label_use_gun_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_use_gun_title.sizePolicy().hasHeightForWidth())
        self.label_use_gun_title.setSizePolicy(sizePolicy1)
        self.label_use_gun_title.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.label_use_gun_title)

        self.label_use_gun = QLabel(self.verticalLayoutWidget)
        self.label_use_gun.setObjectName(u"label_use_gun")
        sizePolicy.setHeightForWidth(self.label_use_gun.sizePolicy().hasHeightForWidth())
        self.label_use_gun.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_use_gun)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_gun_1_title = QLabel(self.verticalLayoutWidget)
        self.label_gun_1_title.setObjectName(u"label_gun_1_title")

        self.horizontalLayout_3.addWidget(self.label_gun_1_title)

        self.label_gun_1 = QLabel(self.verticalLayoutWidget)
        self.label_gun_1.setObjectName(u"label_gun_1")
        sizePolicy.setHeightForWidth(self.label_gun_1.sizePolicy().hasHeightForWidth())
        self.label_gun_1.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_gun_1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_3_1 = QHBoxLayout()
        self.horizontalLayout_3_1.setObjectName(u"horizontalLayout_3_1")
        self.gun1_edit_label = QLabel(self.verticalLayoutWidget)
        self.gun1_edit_label.setObjectName(u"gun1_edit_label")

        self.horizontalLayout_3_1.addWidget(self.gun1_edit_label)

        self.gun1_textEdit = QTextEdit(self.verticalLayoutWidget)
        self.gun1_textEdit.setObjectName(u"gun1_textEdit")
        self.gun1_textEdit.setEnabled(False)
        self.gun1_textEdit.setReadOnly(False)

        self.horizontalLayout_3_1.addWidget(self.gun1_textEdit)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_edit1 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_edit1.setObjectName(u"pushButton_edit1")

        self.verticalLayout_3.addWidget(self.pushButton_edit1)

        self.pushButton_save1 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_save1.setObjectName(u"pushButton_save1")

        self.verticalLayout_3.addWidget(self.pushButton_save1)


        self.horizontalLayout_3_1.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3_1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_gun_2_title = QLabel(self.verticalLayoutWidget)
        self.label_gun_2_title.setObjectName(u"label_gun_2_title")

        self.horizontalLayout_4.addWidget(self.label_gun_2_title)

        self.label_gun_2 = QLabel(self.verticalLayoutWidget)
        self.label_gun_2.setObjectName(u"label_gun_2")
        sizePolicy.setHeightForWidth(self.label_gun_2.sizePolicy().hasHeightForWidth())
        self.label_gun_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_gun_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_4_1 = QHBoxLayout()
        self.horizontalLayout_4_1.setObjectName(u"horizontalLayout_4_1")
        self.gun1_edit_label_2 = QLabel(self.verticalLayoutWidget)
        self.gun1_edit_label_2.setObjectName(u"gun1_edit_label_2")

        self.horizontalLayout_4_1.addWidget(self.gun1_edit_label_2)

        self.gun2_textEdit = QTextEdit(self.verticalLayoutWidget)
        self.gun2_textEdit.setObjectName(u"gun2_textEdit")
        self.gun2_textEdit.setEnabled(False)
        self.gun2_textEdit.setReadOnly(False)

        self.horizontalLayout_4_1.addWidget(self.gun2_textEdit)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_edit2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_edit2.setObjectName(u"pushButton_edit2")

        self.verticalLayout_4.addWidget(self.pushButton_edit2)

        self.pushButton_save2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_save2.setObjectName(u"pushButton_save2")

        self.verticalLayout_4.addWidget(self.pushButton_save2)


        self.horizontalLayout_4_1.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4_1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSaveConfig)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PUBG-Stabilizer", None))
        self.actionSaveConfig.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.label_run_title.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u72b6\u6001", None))
        self.label_run.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u4e2d", None))
        self.label_use_gun_title.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6b66\u5668", None))
        self.label_use_gun.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.label_gun_1_title.setText(QCoreApplication.translate("MainWindow", u"\u6b66\u56681\u53f7\u4f4d", None))
        self.label_gun_1.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.gun1_edit_label.setText(QCoreApplication.translate("MainWindow", u"\u6b66\u56681\u53f7\u4fee\u6539", None))
        self.pushButton_edit1.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.pushButton_save1.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label_gun_2_title.setText(QCoreApplication.translate("MainWindow", u"\u6b66\u56682\u53f7\u4f4d", None))
        self.label_gun_2.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.gun1_edit_label_2.setText(QCoreApplication.translate("MainWindow", u"\u6b66\u56682\u53f7\u4fee\u6539", None))
        self.pushButton_edit2.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.pushButton_save2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

