from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class RegisterWidget(QWidget):
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
        self.widget_2.setStyleSheet(u"background-color: white;")
        self.loginwidget = QWidget(self.widget_2)
        self.loginwidget.setObjectName(u"loginwidget")
        self.loginwidget.setGeometry(QRect(170, 40, 671, 991))
        self.loginbutton_2 = QPushButton(self.loginwidget)
        self.loginbutton_2.setObjectName(u"loginbutton_2")
        self.loginbutton_2.setGeometry(QRect(190, 910, 331, 28))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(10)
        self.loginbutton_2.setFont(font)
        self.loginbutton_2.setStyleSheet(u"border: none")
        self.widget = QWidget(self.loginwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 73, 504, 799))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logintext = QLabel(self.widget)
        self.logintext.setObjectName(u"logintext")
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(36)
        font1.setBold(True)
        font1.setWeight(75)
        self.logintext.setFont(font1)
        self.logintext.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.logintext)

        self.verticalSpacer_13 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_13)

        self.name_layout = QVBoxLayout()
        self.name_layout.setSpacing(10)
        self.name_layout.setObjectName(u"name_layout")
        self.name = QLabel(self.widget)
        self.name.setObjectName(u"name")
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(12)
        self.name.setFont(font2)

        self.name_layout.addWidget(self.name)

        self.name_input = QLineEdit(self.widget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMinimumSize(QSize(500, 40))
        self.name_input.setBaseSize(QSize(0, 0))

        self.name_layout.addWidget(self.name_input)


        self.verticalLayout.addLayout(self.name_layout)

        self.ic_layout = QVBoxLayout()
        self.ic_layout.setObjectName(u"ic_layout")
        self.ic = QLabel(self.widget)
        self.ic.setObjectName(u"ic")
        self.ic.setFont(font2)

        self.ic_layout.addWidget(self.ic)

        self.ic_input = QLineEdit(self.widget)
        self.ic_input.setObjectName(u"ic_input")
        self.ic_input.setMinimumSize(QSize(0, 40))

        self.ic_layout.addWidget(self.ic_input)


        self.verticalLayout.addLayout(self.ic_layout)

        self.phone_layout = QVBoxLayout()
        self.phone_layout.setObjectName(u"phone_layout")
        self.phonenum = QLabel(self.widget)
        self.phonenum.setObjectName(u"phonenum")
        self.phonenum.setFont(font2)

        self.phone_layout.addWidget(self.phonenum)

        self.phone_input = QLineEdit(self.widget)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setMinimumSize(QSize(0, 40))

        self.phone_layout.addWidget(self.phone_input)


        self.verticalLayout.addLayout(self.phone_layout)

        self.email_layout = QVBoxLayout()
        self.email_layout.setObjectName(u"email_layout")
        self.email = QLabel(self.widget)
        self.email.setObjectName(u"email")
        self.email.setFont(font2)

        self.email_layout.addWidget(self.email)

        self.email_input = QLineEdit(self.widget)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setMinimumSize(QSize(0, 40))

        self.email_layout.addWidget(self.email_input)


        self.verticalLayout.addLayout(self.email_layout)

        self.username_layout = QVBoxLayout()
        self.username_layout.setObjectName(u"username_layout")
        self.username = QLabel(self.widget)
        self.username.setObjectName(u"username")
        self.username.setFont(font2)

        self.username_layout.addWidget(self.username)

        self.username_input = QLineEdit(self.widget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(0, 40))

        self.username_layout.addWidget(self.username_input)


        self.verticalLayout.addLayout(self.username_layout)

        self.password_layout = QVBoxLayout()
        self.password_layout.setObjectName(u"password_layout")
        self.password = QLabel(self.widget)
        self.password.setObjectName(u"password")
        self.password.setFont(font2)

        self.password_layout.addWidget(self.password)

        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(0, 40))

        self.password_layout.addWidget(self.password_input)


        self.verticalLayout.addLayout(self.password_layout)

        self.confirmpass = QVBoxLayout()
        self.confirmpass.setObjectName(u"confirmpass")
        self.confirmpass_2 = QLabel(self.widget)
        self.confirmpass_2.setObjectName(u"confirmpass_2")
        self.confirmpass_2.setFont(font2)

        self.confirmpass.addWidget(self.confirmpass_2)

        self.confirmpass_input = QLineEdit(self.widget)
        self.confirmpass_input.setObjectName(u"confirmpass_input")
        self.confirmpass_input.setMinimumSize(QSize(0, 40))

        self.confirmpass.addWidget(self.confirmpass_input)


        self.verticalLayout.addLayout(self.confirmpass)

        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.registerbutton = QPushButton(self.widget)
        self.registerbutton.setObjectName(u"registerbutton")
        self.registerbutton.setMinimumSize(QSize(0, 60))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(14)
        self.registerbutton.setFont(font3)
        self.registerbutton.setStyleSheet(u"border-radius: 15px; color: white; background-color: \"#B6D0E2\";")

        self.verticalLayout.addWidget(self.registerbutton)

        self.widget_3 = QWidget(self.bg)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(1348, 0, 579, 1080))
        self.widget_3.setMinimumSize(QSize(0, 1080))
        self.widget_3.setStyleSheet(u"background-color: \"#B6D0E2\";")
        self.imageframe = QFrame(self.bg)
        self.imageframe.setObjectName(u"imageframe")
        self.imageframe.setGeometry(QRect(1040, 110, 641, 841))
        self.imageframe.setFrameShape(QFrame.StyledPanel)
        self.imageframe.setFrameShadow(QFrame.Raised)
        self.imageframe.setLineWidth(0)
        self.image = QLabel(self.imageframe)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(0, 0, 641, 891))
        self.image.setPixmap(QPixmap(u"CAD/Images/Stethoscope.jpg"))
        self.image.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.loginbutton_2.setText(QCoreApplication.translate("Form", u"Already have an account? Login here.", None))
        self.logintext.setText(QCoreApplication.translate("Form", u"Register", None))
        self.name.setText(QCoreApplication.translate("Form", u"Name", None))
        self.ic.setText(QCoreApplication.translate("Form", u"IC Number", None))
        self.phonenum.setText(QCoreApplication.translate("Form", u"Phone Number (eg. 601XXXXXXXXX)", None))
        self.email.setText(QCoreApplication.translate("Form", u"Email Address", None))
        self.username.setText(QCoreApplication.translate("Form", u"Username", None))
        self.password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.confirmpass_2.setText(QCoreApplication.translate("Form", u"Confirm Password", None))
#if QT_CONFIG(tooltip)
        self.registerbutton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.registerbutton.setText(QCoreApplication.translate("Form", u"Register", None))
        self.image.setText("")
    # retranslateUi

