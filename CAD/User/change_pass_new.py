from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db  

class ChangePassNewWidget(QWidget):
    update_successful = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.email = ""
        self.setupUi()
        self.user_email = None  # Initialize user_email attribute

    def setupUi(self):
        self.setObjectName(u"Form")
        self.resize(1920, 1080)

        self.bg = QFrame(self)
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

        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.New_pw = QLabel(self.widget)
        self.New_pw.setObjectName(u"New_pw")
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.New_pw.setFont(font)
        self.New_pw.setStyleSheet(u"color:rgb(21, 48, 96)")
        self.New_pw.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.New_pw.setText(QCoreApplication.translate("Form", u"New Password", None))
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
        self.label_2.setText(QCoreApplication.translate("Form", u"Set the new password for your account so you can login", None))
        self.verticalLayout.addWidget(self.label_2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(130, 130, 130);")
        self.label_5.setText(QCoreApplication.translate("Form", u"and access all features.", None))
        self.verticalLayout.addWidget(self.label_5)

        self.verticalSpacer_4 = QSpacerItem(14, 43, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_ = QLabel(self.widget)
        self.label_.setObjectName(u"label_")
        self.label_.setFont(font1)
        self.label_.setStyleSheet(u"color: rgb(21, 48, 96);")
        self.label_.setText(QCoreApplication.translate("Form", u"Enter new password", None))
        self.verticalLayout.addWidget(self.label_)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.verticalLayout.addWidget(self.lineEdit)

        self.verticalSpacer_5 = QSpacerItem(14, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"color: rgb(21, 48, 96);")
        self.label_1.setText(QCoreApplication.translate("Form", u"Confirm password", None))
        self.verticalLayout.addWidget(self.label_1)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
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
        self.updatepw.setText(QCoreApplication.translate("Form", u"Update Password", None))
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

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Set the new password for your account so you can login", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"and access all features.", None))
        self.label_.setText(QCoreApplication.translate("Form", u"Enter new password", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"Confirm password", None))

    @pyqtSlot()
    def emitUpdate(self):
        if self.validatePasswords():
            #email = self.lineEdit.text().strip()  # Get the email from a valid source
            self.updatePasswordInDb(self.email, self.lineEdit.text())

    def set_email(self, email):
        self.email = email
        
    def validatePasswords(self):
        new_password = self.lineEdit.text()
        confirm_password = self.lineEdit_2.text()

        if not new_password or not confirm_password:
            self.error_message = "Password fields cannot be empty."
            self.showErrorMessage()
            return False
        if new_password != confirm_password:
            self.error_message = "Passwords do not match."
            self.showErrorMessage()
            return False
        return True

    def updatePasswordInDb(self, email, new_password):
        try:
            # Fetch all patients from the database
            patients = db.child("patients").get()

            if patients.each():
                for patient in patients.each():
                    patient_data = patient.val()
                    if patient_data['patient_email'] == email:
                        user_id = patient.key()
                        db.child("patients").child(user_id).update({"patient_pass": new_password})
                        print(f"Password updated for {email}")
                        self.update_successful.emit()  # Emit signal for successful update
                        QMessageBox.information(self, "Success", "Password updated successfully.")
                        return
                else:
                    self.error_message = f"No user found with email {email}"
                    self.showErrorMessage()
            
            else:
                self.error_message = "No patients found in the database."
                self.showErrorMessage()
        
        except Exception as e:
            # Handle any exceptions that occur during database operation
            self.error_message = f"Error updating password in DB: {e}"
            print(f"Firebase Error: {e}")
            self.showErrorMessage()

    def showErrorMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(self.error_message)
        msg.setWindowTitle("Error")
        msg.exec_()

