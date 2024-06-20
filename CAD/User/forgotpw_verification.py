from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QSizePolicy, QSpacerItem, QFrame

class ForgotPw_verificationWidget(QWidget):
    continue_successful = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 1350, 1080))
        self.widget_2.setMinimumSize(QSize(0, 1080))
        self.widget_2.setStyleSheet(u"background-color: \"white\";")
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
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(550, 280, 658, 451))
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

        self.verification = QLabel(self.widget)
        self.verification.setObjectName(u"verification")
        self.verification.setEnabled(True)
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.verification.setFont(font)
        self.verification.setStyleSheet(u"color:rgb(21, 48, 96)")
        self.verification.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.verification)

        self.verticalSpacer_3 = QSpacerItem(640, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.text1 = QLabel(self.widget)
        self.text1.setObjectName(u"text1")
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(12)
        self.text1.setFont(font1)
        self.text1.setStyleSheet(u"color: rgb(130, 130, 130);")
        self.text1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.text1)

        self.verticalSpacer_4 = QSpacerItem(14, 43, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.noboxline = QWidget(self.widget)
        self.noboxline.setObjectName(u"noboxline")
        self.horizontalLayout_2 = QHBoxLayout(self.noboxline)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.no2 = QLineEdit(self.noboxline)
        self.no2.setObjectName(u"no2")
        self.no2.setMaxLength(1)
        self.no2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.no2)

        self.no3 = QLineEdit(self.noboxline)
        self.no3.setObjectName(u"no3")
        self.no3.setMaxLength(1)
        self.no3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.no3)

        self.no1 = QLineEdit(self.noboxline)
        self.no1.setObjectName(u"no1")
        self.no1.setMaxLength(1)
        self.no1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.no1)

        self.lineEdit_4 = QLineEdit(self.noboxline)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaxLength(1)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_4)


        self.verticalLayout.addWidget(self.noboxline)

        self.verticalSpacer_5 = QSpacerItem(14, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.Continuebutton = QPushButton(self.widget)
        self.Continuebutton.setObjectName(u"Continuebutton")
        self.Continuebutton.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(10)
        self.Continuebutton.setFont(font2)
        self.Continuebutton.setStyleSheet(u"background-color: rgb(182, 208, 226);\n"
"border-radius: 10px;\n"
"border: none")
        self.Continuebutton.clicked.connect(self.emitContinue)

        self.verticalLayout.addWidget(self.Continuebutton)

        self.verticalSpacer_6 = QSpacerItem(14, 23, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.text2 = QLabel(self.widget)
        self.text2.setObjectName(u"text2")
        self.text2.setFont(font2)
        self.text2.setStyleSheet(u"color: rgb(130, 130, 130);")
        self.text2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.text2)

        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(1348, 0, 579, 1080))
        self.widget_4.setMinimumSize(QSize(0, 1080))
        self.widget_4.setStyleSheet(u"background-color: \"#B6D0E2\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo.setText("")
        self.label_7.setText("")
        self.verification.setText(QCoreApplication.translate("Form", u"Verification", None))
        self.text1.setText(QCoreApplication.translate("Form", u"Enter your 4 digits code that you received on your email", None))
        self.no2.setInputMask(QCoreApplication.translate("Form", u"9", None))
        self.no3.setInputMask(QCoreApplication.translate("Form", u"9", None))
        self.no1.setInputMask(QCoreApplication.translate("Form", u"9", None))
        self.lineEdit_4.setInputMask(QCoreApplication.translate("Form", u"9", None))
        self.Continuebutton.setText(QCoreApplication.translate("Form", u"Continue", None))
        self.text2.setText(QCoreApplication.translate("Form", u"If you didn't receive a code ! Resend", None))
    # retranslateUi

    @pyqtSlot()
    def emitContinue(self):
        # Emit the custom signal
        self.continue_successful.emit()