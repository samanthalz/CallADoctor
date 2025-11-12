from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from datetime import datetime
from connection import db

class ProfileSettingsWidget(QWidget):
    logout_btn_clicked = pyqtSignal()
    service_btn_clicked = pyqtSignal()
    schedule_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    feedback_btn_clicked = pyqtSignal()
    change_pass_btn_clicked = pyqtSignal()
    tnc_btn_clicked = pyqtSignal()
    privacy_btn_clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.patient_id = 0
        self.setupUi(self)
        
    
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        
        Form.setAutoFillBackground(True)
        p = Form.palette()
        p.setColor(Form.backgroundRole(), QColor('#B6D0E2'))
        Form.setPalette(p)
        
        self.whitebg = QWidget(Form)
        self.whitebg.setObjectName(u"whitebg")
        self.whitebg.setGeometry(QRect(150, 0, 1771, 1080))
        self.whitebg.setStyleSheet(u"background-color: #F8F8F8;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-left-radius: 30px;")
        self.settings_label = QLabel(self.whitebg)
        self.settings_label.setObjectName(u"settings_label")
        self.settings_label.setGeometry(QRect(60, 40, 481, 81))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.settings_label.setFont(font)
        self.user_frame = QFrame(self.whitebg)
        self.user_frame.setObjectName(u"user_frame")
        self.user_frame.setGeometry(QRect(1480, 30, 251, 80))
        self.user_frame.setStyleSheet(u"border-radius: 20px; border: 2px solid #808080")
        self.user_frame.setFrameShape(QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QFrame.Raised)
        self.profile_icon = QLabel(self.user_frame)
        self.profile_icon.setObjectName(u"profile_icon")
        self.profile_icon.setGeometry(QRect(10, 10, 60, 60))
        self.profile_icon.setStyleSheet(u"border: none")
        self.profile_icon.setPixmap(QPixmap(u"CAD/Images/icon/profile_icon.png"))
        self.profile_icon.setScaledContents(True)
        self.profile_btn = QPushButton(self.user_frame)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setGeometry(QRect(120, 25, 71, 31))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(16)
        self.profile_btn.setFont(font1)
        self.profile_btn.setStyleSheet(u"border: none")
        
        self.updateFrame = QFrame(self.whitebg)
        self.updateFrame.setObjectName(u"updateFrame")
        self.updateFrame.setGeometry(QRect(180, 170, 741, 821))
        self.layoutWidget = QWidget(self.updateFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 31, 518, 751))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.name_layout = QVBoxLayout()
        self.name_layout.setSpacing(10)
        self.name_layout.setObjectName(u"name_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(175, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.profile_icon_2 = QLabel(self.layoutWidget)
        self.profile_icon_2.setObjectName(u"profile_icon_2")
        self.profile_icon_2.setMinimumSize(QSize(150, 150))
        self.profile_icon_2.setMaximumSize(QSize(150, 150))
        self.profile_icon_2.setStyleSheet(u"border: none")
        self.profile_icon_2.setPixmap(QPixmap(u"CAD/Images/icon/profile_icon.png"))
        self.profile_icon_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.profile_icon_2)

        self.horizontalSpacer_2 = QSpacerItem(175, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.name_layout.addLayout(self.horizontalLayout)

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
        self.name_input.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")
        self.name_input.setFrame(True)

        self.name_layout.addWidget(self.name_input)


        self.verticalLayout_2.addLayout(self.name_layout)

        self.ic_layout = QVBoxLayout()
        self.ic_layout.setObjectName(u"ic_layout")
        self.ic = QLabel(self.layoutWidget)
        self.ic.setObjectName(u"ic")
        self.ic.setFont(font2)

        self.ic_layout.addWidget(self.ic)

        self.ic_input = QLineEdit(self.layoutWidget)
        self.ic_input.setObjectName(u"ic_input")
        self.ic_input.setMinimumSize(QSize(0, 40))
        self.ic_input.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")

        self.ic_layout.addWidget(self.ic_input)


        self.verticalLayout_2.addLayout(self.ic_layout)

        self.phone_layout = QVBoxLayout()
        self.phone_layout.setObjectName(u"phone_layout")
        self.phonenum = QLabel(self.layoutWidget)
        self.phonenum.setObjectName(u"phonenum")
        self.phonenum.setFont(font2)

        self.phone_layout.addWidget(self.phonenum)

        self.phone_input = QLineEdit(self.layoutWidget)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setMinimumSize(QSize(0, 40))
        self.phone_input.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")

        self.phone_layout.addWidget(self.phone_input)


        self.verticalLayout_2.addLayout(self.phone_layout)

        self.email_layout = QVBoxLayout()
        self.email_layout.setObjectName(u"email_layout")
        self.email = QLabel(self.layoutWidget)
        self.email.setObjectName(u"email")
        self.email.setFont(font2)

        self.email_layout.addWidget(self.email)

        self.email_input = QLineEdit(self.layoutWidget)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setMinimumSize(QSize(0, 40))
        self.email_input.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")

        self.email_layout.addWidget(self.email_input)


        self.verticalLayout_2.addLayout(self.email_layout)

        self.add_layout = QVBoxLayout()
        self.add_layout.setObjectName(u"add_layout")
        self.add = QLabel(self.layoutWidget)
        self.add.setObjectName(u"add")
        self.add.setFont(font2)

        self.add_layout.addWidget(self.add)

        self.address_input = QTextEdit(self.layoutWidget)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setMaximumSize(QSize(16777215, 80))
        self.address_input.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")

        self.add_layout.addWidget(self.address_input)


        self.verticalLayout_2.addLayout(self.add_layout)

        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.update_btn = QPushButton(self.layoutWidget)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setMinimumSize(QSize(0, 60))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(14)
        self.update_btn.setFont(font3)
        self.update_btn.setStyleSheet(u"border-radius: 15px; color: white; background-color: \"#B6D0E2\";")
        self.update_btn.clicked.connect(self.upload_data_to_db)
        self.verticalLayout_2.addWidget(self.update_btn)

        self.layoutWidget_2 = QWidget(self.whitebg)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(1150, 390, 548, 351))
        self.btn_layout = QVBoxLayout(self.layoutWidget_2)
        self.btn_layout.setSpacing(50)
        self.btn_layout.setObjectName(u"btn_layout")
        self.btn_layout.setContentsMargins(0, 0, 0, 0)
        self.change_pass_btn = QPushButton(self.layoutWidget_2)
        self.change_pass_btn.setObjectName(u"change_pass_btn")
        self.change_pass_btn.setMinimumSize(QSize(546, 0))
        self.change_pass_btn.setMaximumSize(QSize(546, 16777215))
        self.change_pass_btn.setFont(font3)
        self.change_pass_btn.setStyleSheet(u"border-radius: 10; background-color: transparent; color: black")
        self.change_pass_btn.clicked.connect(self.emitChangePassBtn)
        
        self.btn_layout.addWidget(self.change_pass_btn)

        self.policy_btn = QPushButton(self.layoutWidget_2)
        self.policy_btn.setObjectName(u"policy_btn")
        self.policy_btn.setMinimumSize(QSize(546, 0))
        self.policy_btn.setMaximumSize(QSize(546, 16777215))
        self.policy_btn.setFont(font3)
        self.policy_btn.setStyleSheet(u"border-radius: 10; background-color: transparent; color: black")
        self.policy_btn.clicked.connect(self.emitPrivacyBtn)
        self.btn_layout.addWidget(self.policy_btn)

        self.tnc_btn = QPushButton(self.layoutWidget_2)
        self.tnc_btn.setObjectName(u"tnc_btn")
        self.tnc_btn.setMinimumSize(QSize(546, 0))
        self.tnc_btn.setMaximumSize(QSize(546, 16777215))
        self.tnc_btn.setFont(font3)
        self.tnc_btn.setStyleSheet(u"border-radius: 10; background-color: transparent; color: black")
        self.tnc_btn.clicked.connect(self.emitTncBtn)

        self.btn_layout.addWidget(self.tnc_btn)

        self.fb_btn = QPushButton(self.layoutWidget_2)
        self.fb_btn.setObjectName(u"fb_btn")
        self.fb_btn.setMinimumSize(QSize(546, 0))
        self.fb_btn.setMaximumSize(QSize(546, 16777215))
        self.fb_btn.setFont(font3)
        self.fb_btn.setStyleSheet(u"border-radius: 10; background-color: transparent; color: black")
        self.fb_btn.clicked.connect(self.emitFeedbackBtn)
        self.btn_layout.addWidget(self.fb_btn)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.frame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(30, 19, 87, 871))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_navigation = QToolButton(self.layoutWidget_4)
        self.home_navigation.setObjectName(u"home_navigation")
        self.home_navigation.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        self.home_navigation.setMinimumSize(QSize(85, 96))
        self.home_navigation.setMaximumSize(QSize(85, 96))
        font5 = QFont()
        font5.setFamily(u"Source Sans Pro Semibold")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.home_navigation.setFont(font5)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon = QIcon()
        icon.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.home_navigation.clicked.connect(self.emitHomeBtn)
        self.verticalLayout.addWidget(self.home_navigation)

        self.appointments_navigation = QToolButton(self.layoutWidget_4)
        self.appointments_navigation.setObjectName(u"appointments_navigation")
        self.appointments_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.appointments_navigation.sizePolicy().hasHeightForWidth())
        self.appointments_navigation.setSizePolicy(sizePolicy)
        self.appointments_navigation.setFont(font5)
        self.appointments_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/appointment_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appointments_navigation.setIcon(icon1)
        self.appointments_navigation.setIconSize(QSize(70, 70))
        self.appointments_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.appointments_navigation.clicked.connect(self.emitScheduleBtn)
        self.verticalLayout.addWidget(self.appointments_navigation)

        self.services_navigation = QToolButton(self.layoutWidget_4)
        self.services_navigation.setObjectName(u"services_navigation")
        self.services_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.services_navigation.sizePolicy().hasHeightForWidth())
        self.services_navigation.setSizePolicy(sizePolicy)
        self.services_navigation.setFont(font5)
        self.services_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_navigation.setIcon(icon2)
        self.services_navigation.setIconSize(QSize(70, 70))
        self.services_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.services_navigation.clicked.connect(self.emitServiceBtn)
        self.verticalLayout.addWidget(self.services_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget_4)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setFont(font5)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon3)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget_4)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setFont(font5)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon4)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)
        self.verticalLayout.addWidget(self.logout_navigation)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.settings_label.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.profile_icon_2.setText("")
        self.name.setText(QCoreApplication.translate("Form", u"Name", None))
        self.ic.setText(QCoreApplication.translate("Form", u"IC Number", None))
        self.phonenum.setText(QCoreApplication.translate("Form", u"Phone Number (eg. 601XXXXXXXXX)", None))
        self.email.setText(QCoreApplication.translate("Form", u"Email Address", None))
        self.add.setText(QCoreApplication.translate("Form", u"Address", None))
#if QT_CONFIG(tooltip)
        self.update_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.update_btn.setText(QCoreApplication.translate("Form", u"Update", None))
        self.change_pass_btn.setText(QCoreApplication.translate("Form", u"Change Password                     >", None))
        self.policy_btn.setText(QCoreApplication.translate("Form", u"Privacy policy                      >", None))
        self.tnc_btn.setText(QCoreApplication.translate("Form", u"Terms and Conditions                >", None))
        self.fb_btn.setText(QCoreApplication.translate("Form", u"Send Feedback                       >", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Services", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
        
    @pyqtSlot()
    def emitServiceBtn(self):
        # Emit the custom signal
        self.service_btn_clicked.emit()
        
    @pyqtSlot()
    def emitScheduleBtn(self):
        # Emit the custom signal
        self.schedule_btn_clicked.emit()
        
    @pyqtSlot()
    def emitHomeBtn(self):
        # Emit the custom signal
        self.home_btn_clicked.emit()

    @pyqtSlot()
    def emitFeedbackBtn(self):
        # Emit the custom signal
        self.feedback_btn_clicked.emit()
        
    @pyqtSlot()
    def emitChangePassBtn(self):
        # Emit the custom signal
        self.change_pass_btn_clicked.emit()
        
    @pyqtSlot()
    def emitTncBtn(self):
        # Emit the custom signal
        self.tnc_btn_clicked.emit()
        
    @pyqtSlot()
    def emitPrivacyBtn(self):
        # Emit the custom signal
        self.privacy_btn_clicked.emit()
        
    def set_user_id(self, user_id): 
        self.patient_id = user_id
        # print("enter set user id for user profile")
        # print(f"set user id is {self.patient_id}")
        
    def fetch_patient_data(self):
        db = self.initialize_db()
        try:
                patient_data = db.child("patients").child(self.patient_id).get().val()
                if patient_data:
                        return patient_data
                else:
                        raise ValueError("No patient data found for the given ID.")
        except Exception as e:
                print(f"An error occurred while fetching patient data: {e}")
                return None
        
    def set_default_texts(self):
        #print(f"id is {self.patient_id}")
        if self.patient_id:
            patient_data = self.fetch_patient_data()
            
            if patient_data:
                self.name_input.setText(patient_data.get("patient_name", ""))
                self.ic_input.setText(patient_data.get("patient_ic", ""))
                self.phone_input.setText(patient_data.get("patient_phone", ""))
                self.email_input.setText(patient_data.get("patient_email", ""))
                self.address_input.setText(patient_data.get("patient_address", ""))
        else:
                print("error")

    def upload_data_to_db(self):
        name = self.name_input.text().strip()
        ic = self.ic_input.text().strip()
        phone = self.phone_input.text().strip()
        email = self.email_input.text().strip()
        address = self.address_input.toPlainText().strip()

        if not name or not ic or not phone or not email or not address:
            QMessageBox.warning(self, "Missing Data", "Please fill in all fields.")
            return
    
        if not name.replace(' ', '').isalpha():
            QMessageBox.warning(self, "Validation Error", "Name can only contain letters.")
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
    
        #need change
        birth_year_str = ic[:2] if len(ic) >= 2 else '00'
        birth_year = int(birth_year_str) + 1900  # Assuming the IC represents the birth year in YY format
        current_year = datetime.now().year

        age = current_year - birth_year

        try:
            db.child("patients").child(self.patient_id).update({
                "patient_name": name,
                "patient_ic": ic,
                "patient_phone": phone,
                "patient_email": email,
                "patient_address": address,
                'patient_age': age
            })
            QMessageBox.information(self, "Success", "Data updated successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update data: {str(e)}")
            
    def initialize_db(self):
        return db 
        
