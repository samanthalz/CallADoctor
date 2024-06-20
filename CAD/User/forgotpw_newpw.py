from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class ForgotPw_newpwWidget(QWidget):
    update_successful = pyqtSignal()

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
        self.widget.setGeometry(QRect(550, 280, 658, 511))
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(638, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.New_pw = QLabel(self.widget)
        self.New_pw.setObjectName(u"New_pw")
        self.New_pw.setEnabled(True)
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.New_pw.setFont(font)
        self.New_pw.setStyleSheet(u"color:rgb(21, 48, 96)")
        self.New_pw.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.New_pw)

        self.verticalSpacer_3 = QSpacerItem(640, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(130, 130, 130);")

        self.verticalLayout.addWidget(self.label_2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(130, 130, 130);")

        self.verticalLayout.addWidget(self.label_5)

        self.verticalSpacer_4 = QSpacerItem(14, 43, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_ = QLabel(self.widget)
        self.label_.setObjectName(u"label_")
        self.label_.setFont(font1)
        self.label_.setStyleSheet(u"color: rgb(21, 48, 96);")

        self.verticalLayout.addWidget(self.label_)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.lineEdit)

        self.verticalSpacer_5 = QSpacerItem(14, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"color: rgb(21, 48, 96);")

        self.verticalLayout.addWidget(self.label_1)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.verticalSpacer_6 = QSpacerItem(17, 6, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.updatepw = QPushButton(self.widget)
        self.updatepw.setObjectName(u"updatepw")
        self.updatepw.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(10)
        self.updatepw.setFont(font2)
        self.updatepw.setStyleSheet(u"background-color: rgb(182, 208, 226);\n"
"border-radius: 10px;\n"
"border: none")
    
        self.updatepw.clicked.connect(self.emitUpdate)

        self.verticalLayout.addWidget(self.updatepw)

        self.logo = QLabel(self.widget_2)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, -50, 281, 261))
        self.logo.setPixmap(QPixmap(u"../Images/call a doctor.png"))
        self.logo.setScaledContents(True)
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(540, 270, 681, 531))
        self.label_7.setStyleSheet(u"border: 2px solid #B6D0E2;\n"
"border-radius: 10px;")
        self.logo.raise_()
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
        self.New_pw.setText(QCoreApplication.translate("Form", u"New Password", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Set the new password for your account so you can login", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"and access all features.", None))
        self.label_.setText(QCoreApplication.translate("Form", u"Enter new password", None))
        self.lineEdit.setText("")
        self.label_1.setText(QCoreApplication.translate("Form", u"Confirm password", None))
        self.lineEdit_2.setText("")
        self.updatepw.setText(QCoreApplication.translate("Form", u"Update Password", None))
        self.logo.setText("")
        self.label_7.setText("")
    # retranslateUi

    @pyqtSlot()
    def emitUpdate(self):
        self.update_successful.emit()