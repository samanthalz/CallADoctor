from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from datetime import datetime
from connection import db, auth
from password_tools.password_strength import check_password_strength

class RegisterWidget(QWidget, QObject):
    registration_successful = pyqtSignal()  # Custom signal
    privacy_label_clicked = pyqtSignal()
    tnc_label_clicked = pyqtSignal()
    
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
        self.registerwidget = QWidget(self.widget_2)
        self.registerwidget.setObjectName(u"registerwidget")
        self.registerwidget.setGeometry(QRect(170, 40, 671, 991))
        self.loginbutton = QPushButton(self.registerwidget)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(190, 910, 331, 28))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(10)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet(u"border: none")
        self.layoutWidget = QWidget(self.registerwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 73, 504, 831))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.registertext = QLabel(self.layoutWidget)
        self.registertext.setObjectName(u"registertext")
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(36)
        font1.setBold(True)
        font1.setWeight(75)
        self.registertext.setFont(font1)
        self.registertext.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.registertext)

        self.verticalSpacer_13 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_13)

        self.name_layout = QVBoxLayout()
        self.name_layout.setSpacing(10)
        self.name_layout.setObjectName(u"name_layout")
        self.name = QLabel(self.layoutWidget)
        self.name.setObjectName(u"name")
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(12)
        self.name.setFont(font2)

        self.name_layout.addWidget(self.name)

        self.name_input = QLineEdit(self.layoutWidget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMinimumSize(QSize(500, 40))
        self.name_input.setBaseSize(QSize(0, 0))

        self.name_layout.addWidget(self.name_input)


        self.verticalLayout.addLayout(self.name_layout)

        self.ic_layout = QVBoxLayout()
        self.ic_layout.setObjectName(u"ic_layout")
        self.ic = QLabel(self.layoutWidget)
        self.ic.setObjectName(u"ic")
        self.ic.setFont(font2)

        self.ic_layout.addWidget(self.ic)

        self.ic_input = QLineEdit(self.layoutWidget)
        self.ic_input.setObjectName(u"ic_input")
        self.ic_input.setMinimumSize(QSize(0, 40))

        self.ic_layout.addWidget(self.ic_input)


        self.verticalLayout.addLayout(self.ic_layout)

        self.phone_layout = QVBoxLayout()
        self.phone_layout.setObjectName(u"phone_layout")
        self.phonenum = QLabel(self.layoutWidget)
        self.phonenum.setObjectName(u"phonenum")
        self.phonenum.setFont(font2)

        self.phone_layout.addWidget(self.phonenum)

        self.phone_input = QLineEdit(self.layoutWidget)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setMinimumSize(QSize(0, 40))

        self.phone_layout.addWidget(self.phone_input)


        self.verticalLayout.addLayout(self.phone_layout)

        self.email_layout = QVBoxLayout()
        self.email_layout.setObjectName(u"email_layout")
        self.email = QLabel(self.layoutWidget)
        self.email.setObjectName(u"email")
        self.email.setFont(font2)

        self.email_layout.addWidget(self.email)

        self.email_input = QLineEdit(self.layoutWidget)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setMinimumSize(QSize(0, 40))

        self.email_layout.addWidget(self.email_input)


        self.verticalLayout.addLayout(self.email_layout)

        self.address_layout = QVBoxLayout()
        self.address_layout.setObjectName(u"address_layout")
        self.address = QLabel(self.layoutWidget)
        self.address.setObjectName(u"address")
        self.address.setFont(font2)

        self.address_layout.addWidget(self.address)

        self.address_input = QTextEdit(self.layoutWidget)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setMaximumSize(QSize(500, 80))

        self.address_layout.addWidget(self.address_input)


        self.verticalLayout.addLayout(self.address_layout)

        self.password_layout = QVBoxLayout()
        self.password_layout.setObjectName(u"password_layout")
        self.password = QLabel(self.layoutWidget)
        self.password.setObjectName(u"password")
        self.password.setFont(font2)

        self.password_layout.addWidget(self.password)

        self.password_input = QLineEdit(self.layoutWidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(0, 40))

        self.password_layout.addWidget(self.password_input)


        self.verticalLayout.addLayout(self.password_layout)

        self.confirmpass = QVBoxLayout()
        self.confirmpass.setObjectName(u"confirmpass")
        self.confirmpass_2 = QLabel(self.layoutWidget)
        self.confirmpass_2.setObjectName(u"confirmpass_2")
        self.confirmpass_2.setFont(font2)

        self.confirmpass.addWidget(self.confirmpass_2)

        self.confirmpass_input = QLineEdit(self.layoutWidget)
        self.confirmpass_input.setObjectName(u"confirmpass_input")
        self.confirmpass_input.setMinimumSize(QSize(0, 40))

        self.confirmpass.addWidget(self.confirmpass_input)


        self.verticalLayout.addLayout(self.confirmpass)
        
        self.checkbox_layout = QHBoxLayout()
        self.checkbox_layout.setSpacing(4)
        self.checkbox_layout.setObjectName(u"checkbox_layout")
        self.verticalSpacer = QSpacerItem(300, 33, QSizePolicy.Maximum, QSizePolicy.Preferred)

        self.checkbox_layout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tnc_layout = QHBoxLayout()
        self.tnc_layout.setObjectName(u"tnc_layout")
        self.tnc_checkbox = QCheckBox(self.widget_2)
        self.tnc_checkbox.setObjectName(u"tnc_checkbox")
        font3 = QFont()
        font3.setPointSize(36)
        self.tnc_checkbox.setFont(font3)
        self.tnc_checkbox.setStyleSheet(u"QCheckBox::indicator {width:20px;height:20px;}")
        self.tnc_checkbox.setIconSize(QSize(50, 50))
        self.tnc_checkbox.setChecked(False)

        self.tnc_layout.addWidget(self.tnc_checkbox)

        self.tnc_label = QLabel(self.widget_2)
        self.tnc_label.setObjectName(u"tnc_label")
        self.tnc_label.setMinimumSize(QSize(279, 20))
        self.tnc_label.setMaximumSize(QSize(279, 20))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(9)
        self.tnc_label.setFont(font4)
        self.tnc_label.installEventFilter(self)

        self.tnc_layout.addWidget(self.tnc_label)

        self.verticalLayout_2.addLayout(self.tnc_layout)

        self.privacy_layout = QHBoxLayout()
        self.privacy_layout.setObjectName(u"privacy_layout")
        self.privacy_checkbox = QCheckBox(self.widget_2)
        self.privacy_checkbox.setObjectName(u"privacy_checkbox")
        self.privacy_checkbox.setFont(font3)
        self.privacy_checkbox.setStyleSheet(u"QCheckBox::indicator {width:20px;height:20px;}")
        self.privacy_checkbox.setIconSize(QSize(50, 50))
        self.privacy_checkbox.setChecked(False)

        self.privacy_layout.addWidget(self.privacy_checkbox)

        self.privacy_label = QLabel(self.widget_2)
        self.privacy_label.setObjectName(u"privacy_label")
        self.privacy_label.setMinimumSize(QSize(279, 20))
        self.privacy_label.setMaximumSize(QSize(279, 20))
        self.privacy_label.setFont(font4)
        
        self.privacy_label.installEventFilter(self)
        self.privacy_layout.addWidget(self.privacy_label)

        self.verticalLayout_2.addLayout(self.privacy_layout)

        self.checkbox_layout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.checkbox_layout)


        self.registerbutton = QPushButton(self.layoutWidget)
        self.registerbutton.setObjectName(u"registerbutton")
        self.registerbutton.setMinimumSize(QSize(0, 60))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(14)
        self.registerbutton.setFont(font3)
        self.registerbutton.setStyleSheet(u"border-radius: 15px; color: white; background-color: \"#B6D0E2\";")
        self.registerbutton.clicked.connect(self.validate_form)

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
        self.loginbutton.setText(QCoreApplication.translate("Form", u"Already have an account? Login here.", None))
        self.registertext.setText(QCoreApplication.translate("Form", u"Register", None))
        self.name.setText(QCoreApplication.translate("Form", u"Name", None))
        self.ic.setText(QCoreApplication.translate("Form", u"IC Number", None))
        self.phonenum.setText(QCoreApplication.translate("Form", u"Phone Number (eg. 601XXXXXXXXX)", None))
        self.email.setText(QCoreApplication.translate("Form", u"Email Address", None))
        self.address.setText(QCoreApplication.translate("Form", u"Address", None))
        self.password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.confirmpass_2.setText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.tnc_checkbox.setText("")
        self.tnc_label.setText(QCoreApplication.translate("Form", u"I accept the <u>Terms & Conditions</u>", None))
        self.privacy_checkbox.setText("")
        self.privacy_label.setText(QCoreApplication.translate("Form", u"I accept the <u>Privacy Policy</u>", None))
#if QT_CONFIG(tooltip)
        self.registerbutton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.registerbutton.setText(QCoreApplication.translate("Form", u"Register", None))
        self.image.setText("")
    # retranslateUi
    
    
    def validate_form(self):
        name = self.name_input.text().strip()
        ic = self.ic_input.text().strip()
        phone = self.phone_input.text().strip()
        email = self.email_input.text().strip()
        address = self.address_input.toPlainText().strip()
        password = self.password_input.text().strip()
        confirm_password = self.confirmpass_input.text().strip()
        
        # --- Validation ---
        if not all([name, ic, phone, email, address, password, confirm_password]):
            QMessageBox.warning(self, "Validation Error", "All fields are required.")
            return
        
        if not name.replace(' ', '').isalpha():
            QMessageBox.warning(self, "Validation Error", "Name can only contain letters and spaces.")
            return
        
        if len(ic) != 12 or not ic.isdigit():
            QMessageBox.warning(self, "Validation Error", "IC must be 12 digits with no special characters.")
            return
        
        if not phone.startswith("601") or not phone[3:].isdigit() or len(phone) < 11 or len(phone) > 12:
            QMessageBox.warning(self, "Validation Error", "Phone number format is invalid.")
            return
        
        if "@" not in email or "." not in email:
            QMessageBox.warning(self, "Validation Error", "Invalid email format.")
            return
        
        pw_strength = check_password_strength(password)
        if pw_strength != "Strong Password":
            QMessageBox.warning(self, "Validation Error", pw_strength)
            return
        
        if password != confirm_password:
            QMessageBox.warning(self, "Validation Error", "Passwords do not match.")
            return
        
        if not self.privacy_checkbox.isChecked():
            QMessageBox.warning(self, "Validation Error", "You must agree to the privacy policy.")
            return
        
        if not self.tnc_checkbox.isChecked():
            QMessageBox.warning(self, "Validation Error", "You must agree to the terms and conditions.")
            return
        
        # --- Compute age from IC ---
        birth_year_str = ic[:2] if len(ic) >= 2 else '00'
        birth_year = int(birth_year_str) + (1900 if int(birth_year_str) > 25 else 2000)  # simple cutoff for YY
        current_year = datetime.now().year
        age = current_year - birth_year
        
        # --- Create Firebase Auth user ---
        try:
            user = auth.create_user_with_email_and_password(email, password)
            refreshed = auth.refresh(user['refreshToken'])
            id_token = refreshed['idToken']
            auth.send_email_verification(id_token)
            
            uid = user['localId']

            # Save patient info to Realtime Database
            patient_data = {
                'patient_name': name,
                'patient_ic': ic,
                'patient_age': age,
                'patient_phone': phone,
                'patient_email': email,
                'patient_pass': password,
                'patient_address': address,
                'rights': 0,
                'firebase_uid': uid
            }
            
            db.child("patients").child(uid).update(patient_data)
            
            # Show verification message
            QMessageBox.information(
                self,
                "Registration Successful",
                "Your account has been created!\n\nA verification email has been sent to your inbox.\nPlease verify your email before logging in."
            )

            self.registration_successful.emit()  # move back to login screen

        except Exception as e:
            QMessageBox.critical(self, "Registration Error", f"Failed to register: {str(e)}")


    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if source is self.privacy_label:
                # Emit the custom signal when the privacy_label is clicked
                self.privacy_label_clicked.emit()
                return True
            elif source is self.tnc_label:
                # Emit the custom signal when the tnc_label is clicked
                self.tnc_label_clicked.emit()
                return True
        return super().eventFilter(source, event)



