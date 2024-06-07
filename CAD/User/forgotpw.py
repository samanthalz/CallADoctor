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
        self.widget.setGeometry(QRect(580, 280, 621, 511))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(76, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 184, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(182, 208, 226);")

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(28)
        self.label.setFont(font1)
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
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(130, 130, 130);")

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_5.setFont(font3)
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
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(21, 48, 96);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 180, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, -50, 281, 261))
        self.label_4.setPixmap(QPixmap(u"CAD/Images/call a doctor.png"))
        self.label_4.setScaledContents(True)
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(540, 270, 681, 531))
        self.label_7.setStyleSheet(u"border: 2px solid green;\n"
                                    "border-radius: 10px;")
        self.label_4.raise_()
        self.label_7.raise_()
        self.widget.raise_()
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
        self.pushButton.setText(QCoreApplication.translate("Form", u"Continue", None))
        self.label.setText(QCoreApplication.translate("Form", u"Forgot Password", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Enter your email for the verification processes, we will send ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"4 digit codes to your email", None))
        self.label_6.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_4.setText("")
        self.label_7.setText("")
    # retranslateUi


