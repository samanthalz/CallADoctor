from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class ForgotPwWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        self.bg = QFrame(Form)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(0, 0, 1920, 1080))
        self.bg.setMinimumSize(QSize(1920, 1080))
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.widget_2 = QWidget(self.bg)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 1350, 1080))
        self.widget_2.setMinimumSize(QSize(0, 1080))
        self.widget_2.setStyleSheet(u"background-color: \"white\";")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(550, 290, 661, 471))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(638, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(21, 48, 96)")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(640, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(130, 130, 130);")

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(130, 130, 130);")

        self.verticalLayout_4.addWidget(self.label_5)

        self.verticalSpacer_4 = QSpacerItem(14, 43, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.label_ = QLabel(self.widget)
        self.label_.setObjectName(u"label_")
        self.label_.setFont(font1)
        self.label_.setStyleSheet(u"color: rgb(21, 48, 96);")

        self.verticalLayout_4.addWidget(self.label_)

        self.email = QLineEdit(self.widget)
        self.email.setObjectName(u"email")
        self.email.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        self.email.setFont(font2)
        self.email.setStyleSheet(u"")
        self.email.setFrame(True)
        self.email.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_4.addWidget(self.email)

        self.verticalSpacer_5 = QSpacerItem(14, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.Continue = QPushButton(self.widget)
        self.Continue.setObjectName(u"Continue")
        self.Continue.setMinimumSize(QSize(0, 40))
        self.Continue.setFont(font1)
        self.Continue.setStyleSheet(u"background-color: rgb(182, 208, 226);\n"
"border-radius: 10px;\n"
"border: none\n"
"")

        self.verticalLayout_4.addWidget(self.Continue)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(540, 270, 681, 531))
        self.label_7.setStyleSheet(u"border: 2px solid rgb(182, 208, 226);\n"
"border-radius: 10px;")
        self.back_button = QPushButton(self.widget_2)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setEnabled(True)
        self.back_button.setGeometry(QRect(20, 30, 181, 61))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setWeight(75)
        self.back_button.setFont(font3)
        self.back_button.setAutoFillBackground(False)
        self.back_button.setStyleSheet(u"background-color: rgba(182, 208, 226,0.8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.back_button.setIconSize(QSize(70, 70))
        self.label_7.raise_()
        self.widget.raise_()
        self.back_button.raise_()
        self.widget_3 = QWidget(self.bg)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(1348, 0, 579, 1080))
        self.widget_3.setMinimumSize(QSize(0, 1080))
        self.widget_3.setStyleSheet(u"background-color: \"#B6D0E2\";")
        self.widget_3.raise_()
        self.widget_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Forgot Password", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Enter your email for the verification processes, we will ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"send 4 digit codes to your email", None))
        self.label_.setText(QCoreApplication.translate("Form", u"Email", None))
        self.Continue.setText(QCoreApplication.translate("Form", u"Continue", None))
        self.label_7.setText("")
        self.back_button.setText(QCoreApplication.translate("Form", u"< Back", None))
    # retranslateUi



