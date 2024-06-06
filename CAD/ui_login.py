from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt )
from PyQt5 import QtCore
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class LoginWindow(QMainWindow):
    
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1938, 1124)
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
        self.widget_2.setGeometry(QRect(-2, 0, 1350, 1080))
        self.widget_2.setMinimumSize(QSize(0, 1080))
        self.loginwidget = QWidget(self.widget_2)
        self.loginwidget.setObjectName(u"loginwidget")
        self.loginwidget.setGeometry(QRect(160, 200, 701, 721))
        self.widget = QWidget(self.loginwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(102, 72, 506, 428))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logintext = QLabel(self.widget)
        self.logintext.setObjectName(u"logintext")
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.logintext.setFont(font)
        self.logintext.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.logintext)

        self.verticalSpacer_13 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.user_layout = QVBoxLayout()
        self.user_layout.setSpacing(10)
        self.user_layout.setObjectName(u"user_layout")
        self.username = QLabel(self.widget)
        self.username.setObjectName(u"username")
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(12)
        self.username.setFont(font1)

        self.user_layout.addWidget(self.username)

        self.username_input = QLineEdit(self.widget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(500, 40))
        self.username_input.setBaseSize(QSize(0, 0))

        self.user_layout.addWidget(self.username_input)


        self.verticalLayout_14.addLayout(self.user_layout)

        self.password_layout = QVBoxLayout()
        self.password_layout.setObjectName(u"password_layout")
        self.password = QLabel(self.widget)
        self.password.setObjectName(u"password")
        self.password.setFont(font1)

        self.password_layout.addWidget(self.password)

        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(0, 40))

        self.password_layout.addWidget(self.password_input)


        self.verticalLayout_14.addLayout(self.password_layout)


        self.verticalLayout.addLayout(self.verticalLayout_14)

        self.forgetpassword = QHBoxLayout()
        self.forgetpassword.setObjectName(u"forgetpassword")
        self.horizontalSpacer_9 = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.forgetpassword.addItem(self.horizontalSpacer_9)

        self.forgetpassbutton = QPushButton(self.widget)
        self.forgetpassbutton.setObjectName(u"forgetpassbutton")
        font2 = QFont()
        font2.setFamily(u"Consolas")
        self.forgetpassbutton.setFont(font2)
        self.forgetpassbutton.setStyleSheet(u"QPushButton { border: none; }")

        self.forgetpassword.addWidget(self.forgetpassbutton)

        self.verticalLayout.addLayout(self.forgetpassword)

        self.verticalSpacer_16 = QSpacerItem(498, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_16)

        self.loginbutton = QPushButton(self.widget)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setMinimumSize(QSize(0, 60))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(14)
        self.loginbutton.setFont(font3)
        self.loginbutton.setStyleSheet(u"QPushButton {border-radius: 15px; color: white; }")

        self.verticalLayout.addWidget(self.loginbutton)

        self.widget_3 = QWidget(self.bg)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(1348, 0, 579, 1080))
        self.widget_3.setMinimumSize(QSize(0, 1080))
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

        self.gridLayout_4.addWidget(self.bg, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1938, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logintext.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.forgetpassbutton.setText(QCoreApplication.translate("MainWindow", u"Forgot Password", None))
#if QT_CONFIG(tooltip)
        self.loginbutton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.loginbutton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.image.setText("")
    # retranslateUi
