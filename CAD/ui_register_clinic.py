from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import re
from connection import db


class RegisterClinicWidget(QWidget):
        
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        
        Form.setAutoFillBackground(True)
        p = Form.palette()
        p.setColor(Form.backgroundRole(), QColor('#B6D0E2'))
        Form.setPalette(p)
        self.background = QWidget(Form)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(150, 0, 1771, 1061))
        self.background.setStyleSheet(u"background-color: #F8F8F8;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-left-radius: 30px;\n"
"text-align: center;")
        self.clinic_label = QLabel(self.background)
        self.clinic_label.setObjectName(u"clinic_label")
        self.clinic_label.setGeometry(QRect(40, 40, 961, 61))
        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(22)
        self.clinic_label.setFont(font)
        self.clinic_label.setWordWrap(True)
        self.clinic_img = QLabel(self.background)
        self.clinic_img.setObjectName(u"clinic_img")
        self.clinic_img.setGeometry(QRect(120, 180, 200, 200))
        self.clinic_img.setStyleSheet(u"border-radius: 100px; \n"
"background-color: #B6D0E2;  \n"
"color: white; \n"
"font-size: 16px;\n"
"text-align: center;")
        self.change_img_btn = QPushButton(self.background)
        self.change_img_btn.setObjectName(u"change_img_btn")
        self.change_img_btn.setGeometry(QRect(70, 420, 301, 51))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.change_img_btn.setFont(font1)
        self.change_img_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.submit_btn = QPushButton(self.background)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(1400, 970, 301, 51))
        self.submit_btn.setFont(font1)
        self.submit_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.layoutWidget = QWidget(self.background)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(540, 202, 1181, 751))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_layout = QVBoxLayout()
        self.name_layout.setSpacing(10)
        self.name_layout.setObjectName(u"name_layout")
        self.name = QLabel(self.layoutWidget)
        self.name.setObjectName(u"name")
        self.name.setMaximumSize(QSize(16777215, 23))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(12)
        self.name.setFont(font2)

        self.name_layout.addWidget(self.name)

        self.name_input = QLineEdit(self.layoutWidget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMinimumSize(QSize(500, 40))
        self.name_input.setMaximumSize(QSize(16777215, 40))
        self.name_input.setBaseSize(QSize(0, 0))
        self.name_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"

"border: 1px solid gray;\n"
"")

        self.name_layout.addWidget(self.name_input)


        self.horizontalLayout.addLayout(self.name_layout)

        self.hour_layout = QVBoxLayout()
        self.hour_layout.setSpacing(10)
        self.hour_layout.setObjectName(u"hour_layout")
        self.hour_label = QLabel(self.layoutWidget)
        self.hour_label.setObjectName(u"hour_label")
        self.hour_label.setMaximumSize(QSize(16777215, 23))
        self.hour_label.setFont(font2)

        self.hour_layout.addWidget(self.hour_label)

        self.hour_input = QLineEdit(self.layoutWidget)
        self.hour_input.setObjectName(u"hour_input")
        self.hour_input.setMinimumSize(QSize(500, 40))
        self.hour_input.setMaximumSize(QSize(16777215, 40))
        self.hour_input.setBaseSize(QSize(0, 0))
        self.hour_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"

"border: 1px solid gray;\n"
"")

        self.hour_layout.addWidget(self.hour_input)


        self.horizontalLayout.addLayout(self.hour_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startyear_layout = QVBoxLayout()
        self.startyear_layout.setSpacing(10)
        self.startyear_layout.setObjectName(u"startyear_layout")
        self.startyear_label = QLabel(self.layoutWidget)
        self.startyear_label.setObjectName(u"startyear_label")
        self.startyear_label.setMaximumSize(QSize(16777215, 23))
        self.startyear_label.setFont(font2)

        self.startyear_layout.addWidget(self.startyear_label)

        self.startyear_input = QLineEdit(self.layoutWidget)
        self.startyear_input.setObjectName(u"startyear_input")
        self.startyear_input.setMinimumSize(QSize(500, 40))
        self.startyear_input.setMaximumSize(QSize(16777215, 40))
        self.startyear_input.setBaseSize(QSize(0, 0))
        self.startyear_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"

"border: 1px solid gray;\n"
"")

        self.startyear_layout.addWidget(self.startyear_input)


        self.horizontalLayout_2.addLayout(self.startyear_layout)

        self.services_layout = QVBoxLayout()
        self.services_layout.setSpacing(10)
        self.services_layout.setObjectName(u"services_layout")
        self.services_label = QLabel(self.layoutWidget)
        self.services_label.setObjectName(u"services_label")
        self.services_label.setMaximumSize(QSize(16777215, 23))
        self.services_label.setFont(font2)

        self.services_layout.addWidget(self.services_label)

        self.services_input = QLineEdit(self.layoutWidget)
        self.services_input.setObjectName(u"services_input")
        self.services_input.setMinimumSize(QSize(500, 40))
        self.services_input.setMaximumSize(QSize(16777215, 40))
        self.services_input.setBaseSize(QSize(0, 0))
        self.services_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"

"border: 1px solid gray;\n"
"")

        self.services_layout.addWidget(self.services_input)


        self.horizontalLayout_2.addLayout(self.services_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.add_layout = QVBoxLayout()
        self.add_layout.setSpacing(10)
        self.add_layout.setObjectName(u"add_layout")
        self.address_label = QLabel(self.layoutWidget)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMinimumSize(QSize(0, 23))
        self.address_label.setMaximumSize(QSize(16777215, 23))
        self.address_label.setFont(font2)

        self.add_layout.addWidget(self.address_label)

        self.address_input = QLineEdit(self.layoutWidget)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setMinimumSize(QSize(500, 140))
        self.address_input.setMaximumSize(QSize(16777215, 140))
        self.address_input.setBaseSize(QSize(0, 0))
        self.address_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-position: left center; \n"
"border: 1px solid gray;\n"
"border-radius: 0px; \n"
"")

        self.add_layout.addWidget(self.address_input)


        self.horizontalLayout_5.addLayout(self.add_layout)

        self.state_layout = QVBoxLayout()
        self.state_layout.setSpacing(0)
        self.state_layout.setObjectName(u"state_layout")
        self.state_label = QLabel(self.layoutWidget)
        self.state_label.setObjectName(u"state_label")
        self.state_label.setMinimumSize(QSize(379, 23))
        self.state_label.setMaximumSize(QSize(16777215, 23))
        self.state_label.setFont(font2)

        self.state_layout.addWidget(self.state_label)

        self.state_input = QComboBox(self.layoutWidget)
        self.state_input.addItem("")
        self.state_input.setObjectName(u"state_input")
        self.state_input.setMinimumSize(QSize(379, 40))
        self.state_input.setMaximumSize(QSize(16777215, 40))
        self.state_input.setStyleSheet(u"border: 1px solid #000000;\n"
"border-radius: 0px; \n"
"background-color: #FFFFFF; \n"
"padding: 10px; \n"
"font-family: Consolas;\n"
"font-size: 11pt;")

        self.state_layout.addWidget(self.state_input)


        self.horizontalLayout_5.addLayout(self.state_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.phone_layout = QVBoxLayout()
        self.phone_layout.setSpacing(10)
        self.phone_layout.setObjectName(u"phone_layout")
        self.phone_label = QLabel(self.layoutWidget)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setMaximumSize(QSize(16777215, 23))
        self.phone_label.setFont(font2)

        self.phone_layout.addWidget(self.phone_label)

        self.phone_input = QLineEdit(self.layoutWidget)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setMinimumSize(QSize(500, 40))
        self.phone_input.setMaximumSize(QSize(16777215, 40))
        self.phone_input.setBaseSize(QSize(0, 0))
        self.phone_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"

"border: 1px solid gray;\n"
"")

        self.phone_layout.addWidget(self.phone_input)


        self.horizontalLayout_3.addLayout(self.phone_layout)

        self.email_layout = QVBoxLayout()
        self.email_layout.setSpacing(10)
        self.email_layout.setObjectName(u"email_layout")
        self.email_label = QLabel(self.layoutWidget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setMaximumSize(QSize(16777215, 23))
        self.email_label.setFont(font2)

        self.email_layout.addWidget(self.email_label)

        self.email_input = QLineEdit(self.layoutWidget)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setMinimumSize(QSize(500, 40))
        self.email_input.setMaximumSize(QSize(16777215, 40))
        self.email_input.setBaseSize(QSize(0, 0))
        self.email_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"

"border: 1px solid gray;\n"
"")

        self.email_layout.addWidget(self.email_input)


        self.horizontalLayout_3.addLayout(self.email_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(100)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.proof_layout = QVBoxLayout()
        self.proof_layout.setSpacing(10)
        self.proof_layout.setObjectName(u"proof_layout")
        self.proof_label = QLabel(self.layoutWidget)
        self.proof_label.setObjectName(u"proof_label")
        self.proof_label.setMaximumSize(QSize(16777215, 23))
        self.proof_label.setFont(font2)

        self.proof_layout.addWidget(self.proof_label)

        self.prood_input = QLineEdit(self.layoutWidget)
        self.prood_input.setObjectName(u"prood_input")
        self.prood_input.setMinimumSize(QSize(500, 40))
        self.prood_input.setMaximumSize(QSize(16777215, 40))
        self.prood_input.setBaseSize(QSize(0, 0))
        self.prood_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"

"border: 1px solid gray;\n"
"")

        self.proof_layout.addWidget(self.prood_input)


        self.horizontalLayout_4.addLayout(self.proof_layout)

        self.upload_doc_btn = QPushButton(self.layoutWidget)
        self.upload_doc_btn.setObjectName(u"upload_doc_btn")
        self.upload_doc_btn.setMaximumSize(QSize(16777215, 51))
        self.upload_doc_btn.setFont(font1)
        self.upload_doc_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")

        self.horizontalLayout_4.addWidget(self.upload_doc_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.back_btn = QPushButton(self.background)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(1060, 970, 301, 51))
        self.back_btn.setFont(font1)
        self.back_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.clinic_label.setText(QCoreApplication.translate("Form", u"Add Clinic", None))
        self.clinic_img.setText("")
        self.change_img_btn.setText(QCoreApplication.translate("Form", u"Change Image", None))
        self.submit_btn.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.name.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.hour_label.setText(QCoreApplication.translate("Form", u"Operating Hours", None))
        self.startyear_label.setText(QCoreApplication.translate("Form", u"Starting year", None))
        self.services_label.setText(QCoreApplication.translate("Form", u"Types of services", None))
        self.address_label.setText(QCoreApplication.translate("Form", u"Address", None))
        self.state_label.setText(QCoreApplication.translate("Form", u"State", None))
        self.state_input.setItemText(0, QCoreApplication.translate("Form", u"Choose a State", None))

        self.state_input.setCurrentText(QCoreApplication.translate("Form", u"Choose a State", None))
        self.phone_label.setText(QCoreApplication.translate("Form", u"Phone number", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"Email address", None))
        self.proof_label.setText(QCoreApplication.translate("Form", u"Submit proof of Government registered doctors", None))
        self.upload_doc_btn.setText(QCoreApplication.translate("Form", u"Upload Documents", None))
        self.back_btn.setText(QCoreApplication.translate("Form", u"Back", None))
    # retranslateUi

    def load_states(self):
        states = [
            "All",
            "Johor",
            "Kedah",
            "Kelantan",
            "Kuala Lumpur",
            "Labuan",
            "Melaka",
            "Negeri Sembilan",
            "Pahang",
            "Perak",
            "Perlis",
            "Penang",
            "Putrajaya",
            "Sabah",
            "Sarawak",
            "Selangor",
            "Terengganu"
        ]
        self.state_input.addItems(states)
        
    def validateForm(self):
        clinic_name = self.name_input.text().strip()
        operating_hours = self.hour_input.text().strip()
        starting_year = self.startyear_input.text().strip()
        state = self.state_input.currentText()
        address = self.address_input.text().strip()
        phone_number = self.phone_input.text().strip()
        email_address = self.email_input.text().strip()
        proof_document = self.prood_input.text().strip()

        # Validation checks
        if not clinic_name:
            QMessageBox.warning(self, "Input Error", "Clinic name cannot be empty.")
            return
        if not operating_hours or not re.match(r'^\d{1,2}(am|pm)-\d{1,2}(am|pm)$', operating_hours):
            QMessageBox.warning(self, "Input Error", "Operating hours must be in format 1am-2pm.")
            return
        if not starting_year or not re.match(r'^\d{4}$', starting_year):
            QMessageBox.warning(self, "Input Error", "Starting year must be a 4-digit number.")
            return
        if state == "Choose a State":
            QMessageBox.warning(self, "Input Error", "Please select a state.")
            return
        if not address:
            QMessageBox.warning(self, "Input Error", "Address cannot be empty.")
            return
        if not phone_number or not re.match(r'^0\d{7,9}$', phone_number):
            QMessageBox.warning(self, "Input Error", "Phone number must be 8-10 digits and start with 0.")
            return
        if not email_address or not re.match(r'^[^@]+@[^@]+\.[^@]+$', email_address):
            QMessageBox.warning(self, "Input Error", "Please enter a valid email address.")
            return
        if not proof_document:
            QMessageBox.warning(self, "Input Error", "Please upload proof of Government registered doctors.")
            return

        # If all validations pass
        QMessageBox.information(self, "Success", "Form submitted successfully!")


