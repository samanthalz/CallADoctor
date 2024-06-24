from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class ViewDoctorProfileWidget(QWidget):
    service_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    back_btn_clicked = pyqtSignal()
    makeAppointmentRequested = pyqtSignal(str, str)
    profile_btn_clicked = pyqtSignal()
    schedule_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    
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
        
        self.whitebg = QWidget(Form)
        self.whitebg.setObjectName(u"whitebg")
        self.whitebg.setGeometry(QRect(150, 0, 1771, 1080))
        self.whitebg.setCursor(QCursor(Qt.ArrowCursor))
        self.whitebg.setStyleSheet(u"background-color: #F8F8F8;\n"
        "border-bottom-left-radius: 30px;\n"
        "border-top-left-radius: 30px;\n"
        "")
        self.noti_icon = QPushButton(self.whitebg)
        self.noti_icon.setObjectName(u"noti_icon")
        self.noti_icon.setGeometry(QRect(1380, 30, 70, 81))
        icon = QIcon()
        icon.addFile(u"CAD/Images/icon/notification.png", QSize(), QIcon.Normal, QIcon.Off)
        self.noti_icon.setIcon(icon)
        self.noti_icon.setIconSize(QSize(40, 40))
        self.fad_title = QLabel(self.whitebg)
        self.fad_title.setObjectName(u"fad_title")
        self.fad_title.setGeometry(QRect(70, 140, 481, 81))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.fad_title.setFont(font)
        
        self.back_button = QPushButton(self.whitebg)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setEnabled(True)
        self.back_button.setGeometry(QRect(60, 60, 181, 61))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setWeight(75)
        self.back_button.setFont(font5)
        self.back_button.setAutoFillBackground(False)
        self.back_button.setStyleSheet(u"background-color: rgba(182, 208, 226,0.8);\n"
        "color: rgb(255, 255, 255); border-radius: 10px;")
        self.back_button.setText("< Back")
        self.back_button.setIconSize(QSize(70, 70))
        self.back_button.clicked.connect(self.emitBackBtn)
        
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
        self.profile_btn.clicked.connect(self.emitProfileBtn)
        self.profile_display_frame = QFrame(self.whitebg)
        self.profile_display_frame.setObjectName(u"profile_display_frame")
        self.profile_display_frame.setGeometry(QRect(50, 230, 1661, 691))
        self.profile_display_frame.setStyleSheet(u"background-color: white;")
        self.profile_display_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_display_frame.setFrameShadow(QFrame.Raised)
        
        self.doc_img = QLabel(self.profile_display_frame)
        self.doc_img.setObjectName(u"doc_img")
        self.doc_img.setGeometry(QRect(130, 90, 284, 284))
        self.doc_img.setMinimumSize(QSize(284, 284))
        self.doc_img.setMaximumSize(QSize(284, 284))
        #self.doc_img.setStyleSheet(u"text-align: center;  border-radius: 142px; border: 1px solid black; ")
        self.doc_img.setAlignment(Qt.AlignCenter)
        self.doc_img.setScaledContents(True)
        
        self.widget = QWidget(self.profile_display_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(625, 68, 1011, 601))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.speciality_layout = QVBoxLayout()
        self.speciality_layout.setSpacing(10)
        self.speciality_layout.setObjectName(u"speciality_layout")
        self.doc_speciality_label = QLabel(self.widget)
        self.doc_speciality_label.setObjectName(u"doc_speciality_label")
        self.doc_speciality_label.setMinimumSize(QSize(0, 30))
        self.doc_speciality_label.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.doc_speciality_label.setFont(font2)
        self.doc_speciality_label.setStyleSheet(u"text-align: center; border: none;")

        self.speciality_layout.addWidget(self.doc_speciality_label)

        self.speciality_display = QLabel(self.widget)
        self.speciality_display.setObjectName(u"speciality_display")
        self.speciality_display.setMinimumSize(QSize(1000, 80))
        self.speciality_display.setMaximumSize(QSize(1000, 80))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(12)
        self.speciality_display.setFont(font3)
        self.speciality_display.setStyleSheet(u"text-align: center; border: 1px solid black; border-radius: 0px;")
        self.speciality_display.setWordWrap(True)

        self.speciality_layout.addWidget(self.speciality_display)


        self.verticalLayout.addLayout(self.speciality_layout)

        self.hour_layout = QVBoxLayout()
        self.hour_layout.setSpacing(10)
        self.hour_layout.setObjectName(u"hour_layout")
        self.available_hour_label = QLabel(self.widget)
        self.available_hour_label.setObjectName(u"available_hour_label")
        self.available_hour_label.setMinimumSize(QSize(0, 30))
        self.available_hour_label.setMaximumSize(QSize(16777215, 30))
        self.available_hour_label.setFont(font2)
        self.available_hour_label.setStyleSheet(u"text-align: center; border: none;")

        self.hour_layout.addWidget(self.available_hour_label)

        self.hour_display = QLabel(self.widget)
        self.hour_display.setObjectName(u"hour_display")
        self.hour_display.setMinimumSize(QSize(1000, 80))
        self.hour_display.setMaximumSize(QSize(1000, 80))
        self.hour_display.setFont(font3)
        self.hour_display.setStyleSheet(u"text-align: center; border: 1px solid black; border-radius: 0px;")
        self.hour_display.setWordWrap(True)

        self.hour_layout.addWidget(self.hour_display)


        self.verticalLayout.addLayout(self.hour_layout)

        self.qualification_layout = QVBoxLayout()
        self.qualification_layout.setSpacing(10)
        self.qualification_layout.setObjectName(u"qualification_layout")
        self.qualification_label = QLabel(self.widget)
        self.qualification_label.setObjectName(u"qualification_label")
        self.qualification_label.setMinimumSize(QSize(0, 30))
        self.qualification_label.setMaximumSize(QSize(16777215, 30))
        self.qualification_label.setFont(font2)
        self.qualification_label.setStyleSheet(u"text-align: center; border: none;")

        self.qualification_layout.addWidget(self.qualification_label)

        self.qualification_display = QLabel(self.widget)
        self.qualification_display.setObjectName(u"qualification_display")
        self.qualification_display.setMinimumSize(QSize(1000, 150))
        self.qualification_display.setMaximumSize(QSize(1000, 150))
        self.qualification_display.setFont(font3)
        self.qualification_display.setStyleSheet(u"text-align: center; border: 1px solid black; border-radius: 0px;")
        self.qualification_display.setWordWrap(True)

        self.qualification_layout.addWidget(self.qualification_display)


        self.verticalLayout.addLayout(self.qualification_layout)

        self.widget1 = QWidget(self.profile_display_frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(51, 381, 451, 301))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.doc_name = QLabel(self.widget1)
        self.doc_name.setObjectName(u"doc_name")
        self.doc_name.setMinimumSize(QSize(400, 30))
        self.doc_name.setMaximumSize(QSize(16777215, 30))
        self.doc_name.setFont(font2)
        self.doc_name.setStyleSheet(u"text-align: center; border: none;")
        self.doc_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.doc_name)

        self.clinic_name = QLabel(self.widget1)
        self.clinic_name.setObjectName(u"clinic_name")
        self.clinic_name.setMinimumSize(QSize(400, 30))
        self.clinic_name.setMaximumSize(QSize(16777215, 30))
        self.clinic_name.setFont(font3)
        self.clinic_name.setStyleSheet(u"text-align: center; border: none;")
        self.clinic_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.clinic_name)

        self.make_appt_btn = QPushButton(self.widget1)
        self.make_appt_btn.setObjectName(u"make_appt_btn")
        self.make_appt_btn.setMinimumSize(QSize(400, 55))
        self.make_appt_btn.setMaximumSize(QSize(16777215, 55))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(10)
        self.make_appt_btn.setFont(font4)
        self.make_appt_btn.setStyleSheet(u"border-radius: 0 0 24pt 0; background-color: #B6D0E2; border: none;")
        self.make_appt_btn.clicked.connect(self.on_make_appointment_button_clicked)


        self.verticalLayout_3.addWidget(self.make_appt_btn)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.frame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(30, 19, 87, 871))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.home_navigation.setStyleSheet(u"border: none; color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.home_navigation.clicked.connect(self.emitHomeBtn)
        self.verticalLayout_2.addWidget(self.home_navigation)

        self.appointments_navigation = QToolButton(self.layoutWidget_4)
        self.appointments_navigation.setObjectName(u"appointments_navigation")
        self.appointments_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.appointments_navigation.sizePolicy().hasHeightForWidth())
        self.appointments_navigation.setSizePolicy(sizePolicy)
        self.appointments_navigation.setFont(font5)
        self.appointments_navigation.setStyleSheet(u"border: none; color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/appointment_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appointments_navigation.setIcon(icon2)
        self.appointments_navigation.setIconSize(QSize(70, 70))
        self.appointments_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.appointments_navigation.clicked.connect(self.emitScheduleBtn)
        self.verticalLayout_2.addWidget(self.appointments_navigation)

        self.services_navigation = QToolButton(self.layoutWidget_4)
        self.services_navigation.setObjectName(u"services_navigation")
        self.services_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.services_navigation.sizePolicy().hasHeightForWidth())
        self.services_navigation.setSizePolicy(sizePolicy)
        self.services_navigation.setFont(font5)
        self.services_navigation.setStyleSheet(u"border: none; color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_navigation.setIcon(icon3)
        self.services_navigation.setIconSize(QSize(70, 70))
        self.services_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.services_navigation.clicked.connect(self.emitServiceBtn)
        self.verticalLayout_2.addWidget(self.services_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget_4)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setFont(font5)
        self.settings_navigation.setStyleSheet(u"border: none; color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settings_navigation.clicked.connect(self.emitProfileBtn)
        self.verticalLayout_2.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget_4)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setFont(font5)
        self.logout_navigation.setStyleSheet(u"border: none;color: white;")
        icon5 = QIcon()
        icon5.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)
        self.verticalLayout_2.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.noti_icon.setText("")
        self.fad_title.setText(QCoreApplication.translate("Form", u"Doctor Profile", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.doc_img.setText("")
        self.doc_speciality_label.setText(QCoreApplication.translate("Form", u"Speciality", None))
        self.available_hour_label.setText(QCoreApplication.translate("Form", u"Available Hours", None))
        self.qualification_label.setText(QCoreApplication.translate("Form", u"Qualifications", None))
        self.make_appt_btn.setText(QCoreApplication.translate("Form", u"Make Appointment", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Services", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

    def display_doctor_profile(self, doctor_id, clinic_name):
        doctor_info = self.fetch_doctor_info_from_db(doctor_id, clinic_name)  # Fetch info from the database
        self.update_ui_with_doctor_info(doctor_info)  # Update the UI with doctor info

    def fetch_doctor_info_from_db(self, doctor_id, clinic_name):
        db = self.initialize_db()
        # Fetch doctor info from the database using the doctor ID and clinic name
        try:
           
            # Modify the database query as per your actual database structure
            clinic_data = db.child("clinic").get().val()

            if clinic_data is None:
                raise ValueError("Clinic data is not available in the database.")
            
            clinic_id = None
            for cid, clinic in clinic_data.items():
                if clinic.get("clinic_name") == clinic_name:
                    clinic_id = cid
                    break
            
            if clinic_id is None:
                raise ValueError(f"Clinic '{clinic_name}' not found in the database.")

            #print(f"Found Clinic ID: {clinic_id} for Clinic Name: {clinic_name}")

            clinic = clinic_data.get(clinic_id)

            if clinic is None:
                raise ValueError(f"Clinic with ID '{clinic_id}' not found in the database.")

            #print(f"Passed Doctor ID: {doctor_id}, Clinic Name: {clinic_name}, Clinic ID: {clinic_id}")
            
            doctors_data = clinic.get("doctors", {})

            if doctor_id in doctors_data:
                doctor_info = doctors_data[doctor_id]
                doctor_info["clinic_name"] = clinic_name
                #print(f"Doctor info is {doctor_info}")
                
                self.make_appt_btn.setProperty("clinic_name", clinic_name)  # Store the clinic ID as a property of the button
                self.make_appt_btn.setProperty("doctor_name", doctor_info.get("doctor_name", "Unknown"))  # Store the doctor name as a property of the button
            
                return doctor_info
            else:
                raise ValueError(f"Doctor with ID '{doctor_id}' not found in clinic '{clinic_name}'.")
            

        except Exception as e:
            print(f"An error occurred while fetching doctor data: {e}")
            return {}


    def on_make_appointment_button_clicked(self):
        button = self.sender()  # Get the button that was clicked
        clinic_name = button.property("clinic_name")  # Retrieve the clinic ID from the button's property
        doctor_name = button.property("doctor_name")  # Retrieve the doctor name from the button's property
        if clinic_name and doctor_name:
            self.makeAppointmentRequested.emit(clinic_name, doctor_name)

    def update_ui_with_doctor_info(self, doctor_info):
        # Update the UI with the fetched doctor info
        self.doc_name.setText(doctor_info.get("doctor_name", "Unknown"))
        self.clinic_name.setText(doctor_info.get("clinic_name", "Unknown"))
        self.speciality_display.setText(doctor_info.get("specialization", "Unknown"))
        #self.contact_number_label.setText(doctor_info.get("contact_number", "Unknown"))
        self.hour_display.setText(doctor_info.get("doctor_hours", "Unknown"))
        self.doc_img.setPixmap(QPixmap(doctor_info.get("doctor_img", "")))
        self.qualification_display.setText(doctor_info.get("qualification", "Unknown"))

    @pyqtSlot()
    def emitServiceBtn(self):
        # Emit the custom signal
        self.service_btn_clicked.emit()
        
    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
        
    @pyqtSlot()
    def emitBackBtn(self):
        # Emit the custom signal
        self.back_btn_clicked.emit()
        
    @pyqtSlot()
    def emitProfileBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()

    @pyqtSlot()
    def emitScheduleBtn(self):
        # Emit the custom signal
        self.schedule_btn_clicked.emit()
        
    @pyqtSlot()
    def emitHomeBtn(self):
        # Emit the custom signal
        self.home_btn_clicked.emit()

    def initialize_db(self):
        return db 