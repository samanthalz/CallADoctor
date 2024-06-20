from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import re, shutil, os, datetime
from connection import db


class RegisterClinicWidget(QWidget):
    back_btn_clicked = pyqtSignal()
        
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
        self.upload_img_btn = QPushButton(self.background)
        self.upload_img_btn.setObjectName(u"upload_img_btn")
        self.upload_img_btn.setGeometry(QRect(70, 420, 301, 51))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.upload_img_btn.setFont(font1)
        self.upload_img_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.upload_img_btn.clicked.connect(self.uploadImage)
        
        self.submit_btn = QPushButton(self.background)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(1400, 970, 301, 51))
        self.submit_btn.setFont(font1)
        self.submit_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.submit_btn.clicked.connect(self.validateForm)
        
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
        self.name_input.setStyleSheet(u" color: Black;\n"
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
        self.hour_input.setStyleSheet(u" color: Black;\n"
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
        self.startyear_input.setStyleSheet(u" color: Black;\n"
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
        self.services_input.setStyleSheet(u" color: Black;\n"
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
        self.address_input.setStyleSheet(u" color: Black;\n"
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
        self.load_states()

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
        self.phone_input.setStyleSheet(u" color: Black;\n"
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
        self.email_input.setStyleSheet(u" color: Black;\n"
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

        self.proof_input = QLineEdit(self.layoutWidget)
        self.proof_input.setObjectName(u"proof_input")
        self.proof_input.setMinimumSize(QSize(500, 40))
        self.proof_input.setMaximumSize(QSize(16777215, 40))
        self.proof_input.setBaseSize(QSize(0, 0))
        self.proof_input.setStyleSheet(u" color: Black;\n"
        "background-repeat: no-repeat; \n"
        "background-position: left center; \n"

        "border: 1px solid gray;\n"
        "")

        self.proof_layout.addWidget(self.proof_input)


        self.horizontalLayout_4.addLayout(self.proof_layout)

        self.upload_doc_btn = QPushButton(self.layoutWidget)
        self.upload_doc_btn.setObjectName(u"upload_doc_btn")
        self.upload_doc_btn.setMaximumSize(QSize(16777215, 51))
        self.upload_doc_btn.setFont(font1)
        self.upload_doc_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.upload_doc_btn.clicked.connect(self.uploadDocument)
        self.horizontalLayout_4.addWidget(self.upload_doc_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.back_btn = QPushButton(self.background)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(1060, 970, 301, 51))
        self.back_btn.setFont(font1)
        self.back_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.back_btn.clicked.connect(self.emitBackBtn)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.clinic_label.setText(QCoreApplication.translate("Form", u"Add Clinic", None))
        self.clinic_img.setText("")
        self.upload_img_btn.setText(QCoreApplication.translate("Form", u"upload Image", None))
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
        # Check if the clinic image is uploaded
        if not self.clinic_img.pixmap():
            QMessageBox.warning(self, "Image Required", "Please upload a clinic image.")
            return
        
        img_path = self.clinic_img_path
        clinic_name = self.name_input.text().strip()
        operating_hours = self.hour_input.text().strip()
        starting_year = self.startyear_input.text().strip()
        state = self.state_input.currentText()
        address = self.address_input.text().strip()
        phone_number = self.phone_input.text().strip()
        email_address = self.email_input.text().strip()
        proof_document = self.proof_input.text().strip()

        # Validation checks
        if not clinic_name:
            QMessageBox.warning(self, "Input Error", "Clinic name cannot be empty.")
            return
        if not operating_hours or not re.match(r'^\d{1,2}(am|pm)-\d{1,2}(am|pm)$', operating_hours):
            QMessageBox.warning(self, "Input Error", "Operating hours must be in format [number]am-[number]pm.")
            return
        if not (1000 <= int(starting_year) <= 2024):
            QMessageBox.warning(self, "Input Error", "Starting year must be between 1600 and 2024.")
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

        current_date = datetime.datetime.now().strftime("%y%m%d")
        
        # If all validations pass
        self.submitForm(clinic_name, operating_hours, starting_year, state, address, phone_number, email_address, proof_document, img_path, current_date)

    def submitForm(self, clinic_name, operating_hr, starting_year, state, address, phone_number, email, proof_submission, img_path, current_date):
        try:
        # Generate the new clinic ID
            new_clinic_id = self.generate_new_clinic_id()
            if new_clinic_id:
                # Upload the form data to the database with the new ID
                db.child("clinic").child(new_clinic_id).set({
                    "clinic_name": clinic_name,
                    "clinic_operating_hr": operating_hr,
                    "starting_year": starting_year,
                    "clinic_state": state,
                    "clinic_add": address,
                    "clinic_phone": phone_number,
                    "clinic_email": email,
                    "document_path": proof_submission,
                    "uploadDoc_status": "Yes",
                    "clinic_img": img_path,
                    "clinic_dor": current_date,
                    "clinic_status": "pending"
                })
                QMessageBox.information(self, "Success", "Form submitted successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to submit form: {str(e)}")

        self.clearForm()

    def clearForm(self):
        # Clear all form fields
        self.name_input.clear()  # Clear clinic name input
        self.hour_input.clear()  # Clear operating hours input
        self.startyear_input.clear()  # Clear starting year input
        self.state_input.setCurrentIndex(0)  # Reset state dropdown to default
        self.address_input.clear()  # Clear address input
        self.phone_input.clear()  # Clear phone number input
        self.email_input.clear()  # Clear email address input
        self.proof_input.clear()  # Clear proof document input
        self.clinic_img.clear()  # Clear clinic image label 
        self.clinic_img_path = ""  # Reset clinic image path variable 

    
    def generate_new_clinic_id(self):
        try:
            clinic_data = db.child("clinic").get().val()

            if clinic_data is None:
                raise ValueError("Clinic data is not available in the database.")
            
            # Get the maximum clinic ID currently in the database
            max_id = 0
            for cid in clinic_data.keys():
                if cid.startswith("clinic") and cid[6:].isdigit():
                    current_id = int(cid[6:])
                    max_id = max(max_id, current_id)

            # Increment the maximum ID to generate a new ID
            new_clinic_id = f"clinic{max_id + 1}"
            #print(f"new id is {new_clinic_id}")
            
            return new_clinic_id
        except Exception as e:
            print(f"Error generating new clinic ID: {e}")

    
    def uploadDocument(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Upload Document", "", "All Files (*);;Text Files (*.txt)", options=options)
        clinic_name = self.name_input.text()
        if fileName:
            try:
                # Copy the file to the desired directory
                destination_path = "CAD/Registered Clinic Documents/"
                new_file_name = f"{clinic_name}_doc.txt"
                shutil.copyfile(fileName, destination_path + new_file_name)

                QMessageBox.information(self, "Success", f"File uploaded successfully!")

                # Display the uploaded file name in the input field
                self.proof_input.setText(new_file_name)  # Set the text to the new file name

            except Exception as e:
                QMessageBox.warning(self, "Error", f"Error uploading file: {e}")
                
    def uploadImage(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            # Display the image
            pixmap = QPixmap(file_path)
            self.clinic_img.setPixmap(pixmap)
            self.clinic_img.setScaledContents(True)

            # Save the image
            image_name = os.path.basename(file_path)
            self.clinic_img_path = os.path.join("CAD/Images/clinic_img", image_name)
            pixmap.save(self.clinic_img_path)
                
    @pyqtSlot()
    def emitBackBtn(self):
        self.back_btn_clicked.emit()

