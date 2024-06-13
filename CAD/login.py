from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class LoginWidget(QWidget):
    login_successful = pyqtSignal()
    
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
        self.loginwidget.setGeometry(QRect(160, 200, 701, 721))
        self.layoutWidget = QWidget(self.loginwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(102, 72, 506, 428))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logintext = QLabel(self.layoutWidget)
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
        self.ic_layout = QVBoxLayout()
        self.ic_layout.setSpacing(10)
        self.ic_layout.setObjectName(u"ic_layout")
        self.ic = QLabel(self.layoutWidget)
        self.ic.setObjectName(u"ic")
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(12)
        self.ic.setFont(font1)

        self.ic_layout.addWidget(self.ic)

        self.ic_input = QLineEdit(self.layoutWidget)
        self.ic_input.setObjectName(u"ic_input")
        self.ic_input.setMinimumSize(QSize(500, 40))
        self.ic_input.setBaseSize(QSize(0, 0))

        self.ic_layout.addWidget(self.ic_input)


        self.verticalLayout_14.addLayout(self.ic_layout)

        self.password_layout = QVBoxLayout()
        self.password_layout.setObjectName(u"password_layout")
        self.password = QLabel(self.layoutWidget)
        self.password.setObjectName(u"password")
        self.password.setFont(font1)

        self.password_layout.addWidget(self.password)

        self.password_input = QLineEdit(self.layoutWidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(0, 40))

        self.password_layout.addWidget(self.password_input)
        self.verticalLayout_14.addLayout(self.password_layout)
        self.verticalLayout.addLayout(self.verticalLayout_14)

        self.forgetpassword = QHBoxLayout()
        self.forgetpassword.setObjectName(u"forgetpassword")
        self.horizontalSpacer_9 = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.forgetpassword.addItem(self.horizontalSpacer_9)

        self.forgetpassbutton = QPushButton(self.layoutWidget)
        self.forgetpassbutton.setObjectName(u"forgetpassbutton")
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(9)
        self.forgetpassbutton.setFont(font2)
        self.forgetpassbutton.setStyleSheet(u"QPushButton { border: none; }")

        self.forgetpassword.addWidget(self.forgetpassbutton)


        self.verticalLayout.addLayout(self.forgetpassword)

        self.verticalSpacer_16 = QSpacerItem(498, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_16)

        self.loginbutton = QPushButton(self.layoutWidget)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setMinimumSize(QSize(0, 60))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(14)
        self.loginbutton.setFont(font3)
        self.loginbutton.setStyleSheet(u"border-radius: 15px; color: white; background-color: \"#B6D0E2\";")
        self.loginbutton.clicked.connect(self.validateLogin)

        self.verticalLayout.addWidget(self.loginbutton)

        self.registerbutton = QPushButton(self.loginwidget)
        self.registerbutton.setObjectName(u"registerbutton")
        self.registerbutton.setGeometry(QRect(200, 550, 331, 28))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(10)
        self.registerbutton.setFont(font4)
        self.registerbutton.setStyleSheet(u"border: none")
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
        self.logintext.setText(QCoreApplication.translate("Form", u"Login", None))
        self.ic.setText(QCoreApplication.translate("Form", u"IC Number", None))
        self.password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.forgetpassbutton.setText(QCoreApplication.translate("Form", u"Forgot Password", None))
#if QT_CONFIG(tooltip)
        self.loginbutton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.loginbutton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.registerbutton.setText(QCoreApplication.translate("Form", u"Don't have an account? Register here.", None))
        self.image.setText("")
    # retranslateUi
    
    def validateLogin(self):
        ic = self.ic_input.text()
        password = self.password_input.text()

        if not ic or not password:
            self.showMessageBox('Error', 'IC number and password cannot be empty.')
            return

        # Fetch data from Firebase
        patients = db.child('patients').get()
        for patient in patients.each():
            patient_data = patient.val()
            if patient_data['patient_ic'] == ic and patient_data['patient_pass'] == password:
                # go to home page
                self.login_successful.emit()
                #self.showMessageBox('Success', 'Login successful!', success=True)
                return

        self.showMessageBox('Error', 'Invalid IC number or password.')

    def showMessageBox(self, title, message, success=False):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        # if msgBox.exec() == QMessageBox.Ok and success:
        #     self.login_successful.emit()



