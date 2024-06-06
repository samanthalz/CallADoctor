# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgetpasswordasXsiq.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class ForgotPwWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1942, 1128)
        MainWindow.setStyleSheet(u"#widget_2 {\n"
"                background-color: white;\n"
"            }\n"
"\n"
"#widget_3, #loginbutton {\n"
"                background-color: \"#B6D0E2\";\n"
"            }\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.bg = QFrame(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setMinimumSize(QSize(1920, 1080))
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.widget_2 = QWidget(self.bg)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, -30, 1350, 1080))
        self.widget_2.setMinimumSize(QSize(0, 1080))
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(500, 390, 531, 381))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"gridline-color: rgb(0, 126, 133);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(76, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 184, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        font = QFont()
        font.setFamily(u"Microsoft Sans Serif")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(21, 48, 96)")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(130, 130, 130);")

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(130, 130, 130);")

        self.verticalLayout_3.addWidget(self.label_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(21, 48, 96);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgb(182, 208, 226);")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout_4, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 184, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, -20, 291, 251))
        self.label_4.setPixmap(QPixmap(u"../../../../Downloads/Software Engineering/CAD/Figma icons/call a doctor.png"))
        self.label_4.setScaledContents(True)
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(500, 380, 531, 401))
        self.label_7.setStyleSheet(u"border: 2px solid green;\n"
"border-radius: 10px;")
        self.label_4.raise_()
        self.label_7.raise_()
        self.widget.raise_()
        self.widget_3 = QWidget(self.bg)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(1348, 0, 579, 1080))
        self.widget_3.setMinimumSize(QSize(0, 1080))
        self.frame = QFrame(self.bg)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(1040, 110, 641, 841))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)

        self.gridLayout_4.addWidget(self.bg, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1942, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Forgot Password", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter your email for the verification processes, we will send ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"4 digit codes to your email", None))
        self.label_6.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.label_4.setText("")
        self.label_7.setText("")
    # retranslateUi

