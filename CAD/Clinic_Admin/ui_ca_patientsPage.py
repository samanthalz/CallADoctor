from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class CA_patientsPageWidget(QWidget):
    home_navigation_btn_clicked = pyqtSignal()
    doctors_navigation_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    settings_navigation_btn_clicked = pyqtSignal()
    approved_btn_clicked = pyqtSignal()
    reject_btn_clicked = pyqtSignal()
    redirect_fb = pyqtSignal(dict)


    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.clinic_id = ""
        self.patient_data_list = []
        self.patient_details_frame = None
        self.temp_patient_name = ""


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
        self.noti_icon = QPushButton(self.background)
        self.noti_icon.setObjectName(u"noti_icon")
        self.noti_icon.setGeometry(QRect(1380, 30, 70, 81))
        icon = QIcon()
        icon.addFile(u"CAD/Images/icon/notification.png", QSize(), QIcon.Normal, QIcon.Off)
        self.noti_icon.setIcon(icon)
        self.noti_icon.setIconSize(QSize(40, 40))
        self.user_frame = QFrame(self.background)
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
        self.profile_btn.setGeometry(QRect(100, 25, 121, 31))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(10)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet(u"border: none")
        
        self.search_patient = QLineEdit(self.background)
        self.search_patient.setObjectName(u"search_patient")
        self.search_patient.setGeometry(QRect(40, 40, 831, 71))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(11)
        self.search_patient.setFont(font1)
        self.search_patient.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 60px; color: Black;\n"
" background-image: url(\"C:/Users/Samantha Law/Documents/INTI/CAD/CallADoctor/CAD/Images/icon/search_icon.png\"); \n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"

"border: 1px solid gray;\n"
"")
        self.search_patient.setClearButtonEnabled(False)
              

        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        font6.setUnderline(True)
        self.filter = QComboBox(self.background)
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.setObjectName(u"filter")
        self.filter.setGeometry(QRect(710, 170, 151, 31))
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(12)
        self.filter.setFont(font7)
        self.filter.setStyleSheet(u"\n"
"border: 1px solid gray;")
        self.patient_list_label = QLabel(self.background)
        self.patient_list_label.setObjectName(u"patient_list_label")
        self.patient_list_label.setGeometry(QRect(50, 160, 341, 41))
        font8 = QFont()
        font8.setFamily(u"Cascadia Code")
        font8.setPointSize(16)
        self.patient_list_label.setFont(font8)
        self.patient_list_label.setStyleSheet(u"border : none;\n"
"")
        self.patient_details_label = QLabel(self.background)
        self.patient_details_label.setObjectName(u"patient_details_label")
        self.patient_details_label.setGeometry(QRect(990, 150, 571, 41))
        font9 = QFont()
        font9.setFamily(u"Consolas")
        font9.setPointSize(16)
        self.patient_details_label.setFont(font9)
        self.patient_details_label.setStyleSheet(u"border : none;\n"
"")
        self.patient_list_frame = QFrame(self.background)
        self.patient_list_frame.setObjectName(u"patient_list_frame")
        self.patient_list_frame.setGeometry(QRect(50, 230, 801, 801))
        self.patient_list_frame.setFrameShape(QFrame.StyledPanel)
        self.patient_list_frame.setFrameShadow(QFrame.Raised)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.frame)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(30, 10, 87, 851))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.home_navigation_2 = QToolButton(self.layoutWidget_3)
        self.home_navigation_2.setObjectName(u"home_navigation_2")
        self.home_navigation_2.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation_2.sizePolicy().hasHeightForWidth())
        self.home_navigation_2.setSizePolicy(sizePolicy)
        self.home_navigation_2.setMinimumSize(QSize(85, 96))
        self.home_navigation_2.setMaximumSize(QSize(85, 96))
        font10 = QFont()
        font10.setFamily(u"Source Sans Pro Semibold")
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)
        self.home_navigation_2.setFont(font10)
        self.home_navigation_2.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation_2.setIcon(icon1)
        self.home_navigation_2.setIconSize(QSize(70, 70))
        self.home_navigation_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.home_navigation_2.clicked.connect(self.emitHomeBtn)

        self.verticalLayout_3.addWidget(self.home_navigation_2)

        self.doctors_navigation = QToolButton(self.layoutWidget_3)
        self.doctors_navigation.setObjectName(u"doctors_navigation")
        self.doctors_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.doctors_navigation.sizePolicy().hasHeightForWidth())
        self.doctors_navigation.setSizePolicy(sizePolicy)
        self.doctors_navigation.setMinimumSize(QSize(85, 96))
        self.doctors_navigation.setMaximumSize(QSize(85, 96))
        self.doctors_navigation.setFont(font10)
        self.doctors_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.doctors_navigation.setIcon(icon2)
        self.doctors_navigation.setIconSize(QSize(70, 70))
        self.doctors_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.doctors_navigation.clicked.connect(self.emitDoctorsBtn)

        self.verticalLayout_3.addWidget(self.doctors_navigation)

        self.patients_navigation = QToolButton(self.layoutWidget_3)
        self.patients_navigation.setObjectName(u"patients_navigation")
        self.patients_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.patients_navigation.sizePolicy().hasHeightForWidth())
        self.patients_navigation.setSizePolicy(sizePolicy)
        self.patients_navigation.setMinimumSize(QSize(85, 96))
        self.patients_navigation.setMaximumSize(QSize(85, 96))
        self.patients_navigation.setFont(font10)
        self.patients_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patients_navigation.setIcon(icon3)
        self.patients_navigation.setIconSize(QSize(70, 70))
        self.patients_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.patients_navigation)

        self.settings_navigation_2 = QToolButton(self.layoutWidget_3)
        self.settings_navigation_2.setObjectName(u"settings_navigation_2")
        self.settings_navigation_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation_2.sizePolicy().hasHeightForWidth())
        self.settings_navigation_2.setSizePolicy(sizePolicy)
        self.settings_navigation_2.setMinimumSize(QSize(85, 96))
        self.settings_navigation_2.setMaximumSize(QSize(85, 96))
        self.settings_navigation_2.setFont(font10)
        self.settings_navigation_2.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation_2.setIcon(icon4)
        self.settings_navigation_2.setIconSize(QSize(70, 70))
        self.settings_navigation_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.settings_navigation_2.clicked.connect(self.emitSettingsBtn)

        self.verticalLayout_3.addWidget(self.settings_navigation_2)

        self.logout_navigation_2 = QToolButton(self.layoutWidget_3)
        self.logout_navigation_2.setObjectName(u"logout_navigation_2")
        self.logout_navigation_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation_2.sizePolicy().hasHeightForWidth())
        self.logout_navigation_2.setSizePolicy(sizePolicy)
        self.logout_navigation_2.setMinimumSize(QSize(85, 96))
        self.logout_navigation_2.setMaximumSize(QSize(85, 96))
        self.logout_navigation_2.setFont(font10)
        self.logout_navigation_2.setStyleSheet(u"border: none; \n"
"color: white;")
        icon5 = QIcon()
        icon5.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation_2.setIcon(icon5)
        self.logout_navigation_2.setIconSize(QSize(70, 70))
        self.logout_navigation_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.logout_navigation_2.clicked.connect(self.emitLogoutBtn)

        self.verticalLayout_3.addWidget(self.logout_navigation_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)


    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.noti_icon.setText("")
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Clinic name", None))
        self.search_patient.setText(QCoreApplication.translate("Form", u"Search for Patient", None))
        self.search_patient.setPlaceholderText(QCoreApplication.translate("Form", u"Search Clinic Name", None))
        self.filter.setItemText(0, QCoreApplication.translate("Form", u"Recent", None))
        self.filter.setItemText(1, QCoreApplication.translate("Form", u"Oldest", None))

        self.patient_list_label.setText(QCoreApplication.translate("Form", u"Patient List", None))
        self.patient_details_label.setText(QCoreApplication.translate("Form", u"Patient Details", None))
        self.home_navigation_2.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.doctors_navigation.setText(QCoreApplication.translate("Form", u"Doctors", None))
        self.patients_navigation.setText(QCoreApplication.translate("Form", u"Patients", None))
        self.settings_navigation_2.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation_2.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

    @pyqtSlot()
    def emitHomeBtn(self):
        self.home_navigation_btn_clicked.emit()

    @pyqtSlot()
    def emitDoctorsBtn(self):
        self.doctors_navigation_btn_clicked.emit()

    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
    
    @pyqtSlot()
    def emitSettingsBtn(self):
        # Emit the custom signal
        self.settings_navigation_btn_clicked.emit()

    @pyqtSlot()
    def emitProfileBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()

    @pyqtSlot()
    def emitApprovedBtn(self):
        # Emit the custom signal
        self.approved_btn_clicked.emit()

    @pyqtSlot()
    def emitRejectBtn(self):
        # Emit the custom signal
        self.reject_btn_clicked.emit()

    def fetch_patient_data(self):

        # clear list
        self.patient_data_list = []
        db = self.initialize_db()  # Assuming this method initializes your Firebase connection
        try:
            patients = db.child("patients").get().val()

            
            for patient_id, patient_data in patients.items():

                # Fetch all appointments
                appointments = db.child("appointment").get().val()
                
                if appointments:
                        for appointment_id, appointment_data in appointments.items():

                            # Check if appointment is associated with the current patient and clinic
                            if appointment_data.get("patient_id") == patient_id and appointment_data.get("clinic_id").lower() == self.clinic_id.lower():
                
                                med_concern = appointment_data.get("med_concern", "N/A")  # Replace "N/A" with default if not found
                                time = appointment_data.get("time", "N/A")
                                date = appointment_data.get("date", "N/A")
                                doctorId = appointment_data.get("doctor_id", "N/A")

                                doctor_name = ""
                                doctors = db.child("doctors").get().val()
                                for doctor_id, doctor_data in doctors.items():
                                
                                    doctor_name = doctor_data.get("name")
                                   
                                    if doctor_id == doctorId:
                        
                                        doctor_name = doctor_name
                                        break
                                if not doctor_name : 
                                      doctor_name = "N/A"
                                # Add fetched data to patient data
                                patient_data["med_concern"] = med_concern
                                patient_data["time"] = time
                                patient_data["date"] = date
                                patient_data["doctor_name"] = doctor_name

                        

                                # Save patient data only if they have appointment details
                                self.patient_data_list.append(patient_data)
                               

                                break  # Assuming only one appointment per patient is needed
                        
                # Populate patient information on the UI
                self.populate_patient_info()

        except Exception as e:
                print(f"An error occurred while fetching data: {e}")

    def create_patient_list_frame(self, patient_data):   
        patient_frame1 = QFrame(self.patient_list_frame)
        patient_frame1.setObjectName(u"patient_frame1")
        patient_frame1.setGeometry(QRect(0, 20, 801, 81))
        patient_frame1.setFrameShape(QFrame.StyledPanel)
        patient_frame1.setFrameShadow(QFrame.Raised)
        
        patient_name_label1 = QLabel(patient_frame1)
        patient_name_label1.setObjectName(u"patient_name_label1")
        patient_name_label1.setGeometry(QRect(90, 30, 121, 21))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)
        patient_name_label1.setFont(font3)
        patient_name_label1.setStyleSheet(u"border : none;\n"
"")
        patient_name_label1.setText(patient_data.get("patient_name", "Unknown"))

        patient_profile_logo1 = QLabel(patient_frame1)
        patient_profile_logo1.setObjectName(u"patient_profile_logo1")
        patient_profile_logo1.setGeometry(QRect(10, 10, 54, 54))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(9)
        patient_profile_logo1.setFont(font2)
        patient_profile_logo1.setStyleSheet(u"background-color: #B6D0E2; \n"
"border-radius: 25px; \n"
"border: 2px solid #B6D0F7; \n"
"min-width: 50px; \n"
"min-height: 50px; \n"
"max-width: 50px;\n"
"max-height: 50px; ")
        patient_profile_logo1.setAlignment(Qt.AlignCenter)
        patient_img_path = patient_data.get("patient_img", "Path Not Found")
        if patient_img_path:
                pixmap = QPixmap(patient_img_path)
                patient_profile_logo1.setPixmap(pixmap.scaled(patient_profile_logo1.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        appt_time_label = QLabel(patient_frame1)
        appt_time_label.setObjectName(u"appt_time_label")
        appt_time_label.setGeometry(QRect(690, 20, 91, 41))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(10)
        appt_time_label.setFont(font)
        appt_time_label.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);\n"
"color: #128983; text-align: center;\n"
"")
        appt_time_label.setAlignment(Qt.AlignCenter)

        appt_time_label.setText(patient_data.get("time", "Unknown"))
        
        status = QLabel(patient_frame1)
        status.setObjectName(u"status")
        status.setGeometry(QRect(570, 20, 91, 41))
        status.setFont(font)
        status.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);\n"
        "color: #128983; text-align: center;\n"
        "")
        status.setAlignment(Qt.AlignCenter)
        status.setText(appointment_data.get("status", "Unknown"))

        return patient_frame1
    
    def clear_layout(self):
        while self.patient_list_frame.count():
                item = self.patient_list_frame.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.destroy()  

    def populate_patient_info(self, search_query=None):
        visible_patients = []
        

        for i, patient_data in enumerate(self.patient_data_list):
                if isinstance(patient_data, dict):
                        clinic_name = patient_data.get("clinic_name", "").lower()
                        patient_status = patient_data.get("status", "").lower()

                if self.selected_status and patient_status.lower() != self.selected_status.lower():
                        continue

                # Check search query if provided
                if not search_query or search_query.lower() in clinic_name:
                        patient_frame = self.create_patient_list_frame(patient_data)
                if patient_frame:
                        visible_patients.append(patient_frame)

        # Add visible clinics to the layout in reverse order
        for patient_frame in reversed(visible_patients):
                self.vLayout.addWidget(patient_frame)

        self.scrollAreaWidgetContents.setLayout(self.vLayout)
        self.vLayout.setAlignment(Qt.AlignTop)
        self.vLayout.update()
        self.scrollAreaWidgetContents.update()
        

         # Debug: Final update status
        print("Layout and widget updated.")

    def create_popup_widget(self, patient_data):
        self.hide_patient_details_frame()
        self.patient_details_frame = self.create_patient_details_frame(patient_data)
        self.patient_details_frame.setVisible(True)

    def hide_patient_details_frame(self):
        if self.patient_details_frame:
            self.patient_details_frame.setVisible(False)

    def create_patient_details_frame(self, patient_data):
        patient_details_outer_frame = QFrame(self.background)
        patient_details_outer_frame.setObjectName(u"patient_details_outer_frame")
        patient_details_outer_frame.setGeometry(QRect(979, 200, 751, 841))
        patient_details_outer_frame.setStyleSheet(u"background-color : #ffffff;")
        patient_details_outer_frame.setFrameShape(QFrame.StyledPanel)
        patient_details_outer_frame.setFrameShadow(QFrame.Raised)
        
        clinic_details_inner = QFrame(patient_details_outer_frame)
        clinic_details_inner.setObjectName(u"clinic_details_inner")
        clinic_details_inner.setGeometry(QRect(20, 30, 721, 751))
        clinic_details_inner.setFrameShape(QFrame.StyledPanel)
        clinic_details_inner.setFrameShadow(QFrame.Raised)
        
        patient_logo_2 = QLabel(clinic_details_inner)
        patient_logo_2.setObjectName(u"patient_logo_2")
        patient_logo_2.setGeometry(QRect(9, 9, 54, 54))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(9)
        patient_logo_2.setFont(font2)
        patient_logo_2.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        patient_logo_2.setAlignment(Qt.AlignCenter)
        patient_img_path = patient_data.get("patient_img","")
        if patient_img_path:
                pixmap = QPixmap(patient_img_path)
                patient_logo_2.setPixmap(pixmap.scaled(patient_logo_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        patient_name_display = QLabel(clinic_details_inner)
        patient_name_display.setObjectName(u"patient_name_display")
        patient_name_display.setGeometry(QRect(9, 69, 120, 22))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)
        patient_name_display.setFont(font3)
        patient_name_display.setText(patient_data.get("patient_name", "Unknown"))
        patient_name_display.setStyleSheet(u"border : none;\n"
"")
        line_2 = QFrame(clinic_details_inner)
        line_2.setObjectName(u"line_2")
        line_2.setGeometry(QRect(9, 205, 703, 3))
        line_2.setMinimumSize(QSize(357, 3))
        line_2.setMaximumSize(QSize(16777215, 3))
        line_2.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        line_2.setFrameShape(QFrame.StyledPanel)
        line_2.setFrameShadow(QFrame.Raised)
        
        diagnosis_display = QLabel(clinic_details_inner)
        diagnosis_display.setObjectName(u"diagnosis_display")
        diagnosis_display.setGeometry(QRect(320, 300, 390, 148))
        diagnosis_display.setMinimumSize(QSize(390, 0))

        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setWeight(50)
       
        diagnosis_display.setFont(font4)
        diagnosis_display.setStyleSheet(u"border: none;")
        diagnosis_display.setText(patient_data.get("med_concern", "Unknown"))
        diagnosis_display.setScaledContents(False)
        diagnosis_display.setWordWrap(True)
        
        diagnosis_label_2 = QLabel(clinic_details_inner)
        diagnosis_label_2.setObjectName(u"diagnosis_label_2")
        diagnosis_label_2.setGeometry(QRect(13, 300, 301, 148))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        diagnosis_label_2.setFont(font5)
        diagnosis_label_2.setStyleSheet(u"border: none;")
        diagnosis_label_2.setWordWrap(True)
        diagnosis_label_2.setText("Diagnosis:")

        last_checked_by_label = QLabel(clinic_details_inner)
        last_checked_by_label.setObjectName(u"last_checked_by_label")
        last_checked_by_label.setGeometry(QRect(13, 210, 301, 148))
        last_checked_by_label.setFont(font5)
        last_checked_by_label.setStyleSheet(u"border: none;")
        last_checked_by_label.setWordWrap(True)
        last_checked_by_label.setText("Last checked by:")

        dr_name_display = QLabel(clinic_details_inner)
        dr_name_display.setObjectName(u"dr_name_display")
        dr_name_display.setGeometry(QRect(320, 210, 390, 148))
        dr_name_display.setMinimumSize(QSize(390, 0))
        dr_name_display.setFont(font4)
        dr_name_display.setStyleSheet(u"border: none;")
        dr_name_display.setScaledContents(False)
        dr_name_display.setWordWrap(True)
        dr_name_display.setText(patient_data.get("doctor_name", "Unknown"))

        date_label = QLabel(clinic_details_inner)
        date_label.setObjectName(u"date_label")
        date_label.setGeometry(QRect(13, 400, 301, 148))
        date_label.setFont(font5)
        date_label.setStyleSheet(u"border: none;")
        date_label.setWordWrap(True)
        date_label.setText("Date:")

        date_display = QLabel(clinic_details_inner)
        date_display.setObjectName(u"date_display")
        date_display.setGeometry(QRect(320, 400, 390, 148))
        date_display.setMinimumSize(QSize(390, 0))
        date_display.setFont(font4)
        date_display.setStyleSheet(u"border: none;")
        date_display.setScaledContents(False)
        date_display.setWordWrap(True)
        date_display.setText(patient_data.get("date", "Unknown"))
        
        
        time_display_3 = QLabel(clinic_details_inner)
        time_display_3.setObjectName(u"time_display_3")
        time_display_3.setGeometry(QRect(320, 500, 390, 148))
        time_display_3.setMinimumSize(QSize(390, 0))
        time_display_3.setFont(font4)
        time_display_3.setStyleSheet(u"border: none;")
        time_display_3.setScaledContents(False)
        time_display_3.setWordWrap(True)
        time_display_3.setText(patient_data.get("time", "Unknown"))

        time_label_3 = QLabel(clinic_details_inner)
        time_label_3.setObjectName(u"time_label_3")
        time_label_3.setGeometry(QRect(13, 500, 301, 148))
        time_label_3.setFont(font5)
        time_label_3.setStyleSheet(u"border: none;")
        time_label_3.setWordWrap(True)   
        time_label_3.setText("Time:")

        reject_btn = QPushButton(clinic_details_inner)
        reject_btn.setObjectName(u"reject_btn")
        reject_btn.setGeometry(QRect(510, 700, 181, 41))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        reject_btn.setFont(font6)
        reject_btn.setStyleSheet(u"background-color: #E73030; border-radius: 16px; color: white; border: 1px solid gray;")
        reject_btn.setText("Reject")
        reject_btn.clicked.connect(self.reject_patient)

        approved_btn = QPushButton(clinic_details_inner)
        approved_btn.setObjectName(u"approved_btn")
        approved_btn.setGeometry(QRect(320, 700, 181, 41))
        approved_btn.setFont(font6)
        approved_btn.setStyleSheet(u"background-color: rgba(18, 137, 131);\n"
"border-radius: 16px; color: white; border: 1px solid gray;")
        approved_btn.setText("Approved")
        approved_btn.clicked.connect(self.approved_patient)

        return patient_details_outer_frame

    def load_status(self):
        states = [
            "All",
            "Pending",
            "Approved"
        ]
        self.filter.addItems(states)

    def reject_patient(self, patient_name):
        appointment_id = None

        if not self.patient_data_list:
            return None

        try:
            # Fetch all appointments directly from the database
            appointment_data_list = db.child("appointment").get().val()
            print("Appointments fetched:", appointment_data_list)
        except Exception as e:
            print(f"Failed to fetch appointment data: {e}")
            return

        # Find the appointment ID by patient name
        for aid, appointment_data in appointment_data_list.items():
            if appointment_data.get("patient_name") == patient_name:
                appointment_id = aid
                break

        if appointment_id:
            try:
                # Remove the appointment from the database
                db.child("appointment").child(appointment_id).remove()
                QMessageBox.information(self, "Success", "Patient appointment rejected and removed from the database.")

                # Remove the rejected appointment from patient_data_list
                self.patient_data_list = [patient for patient in self.patient_data_list if patient.get("patient_name") != patient_name]

                # Refresh the patient list after removal
                self.populate_patient_info()

            except Exception as e:
                print(f"Failed to remove appointment: {e}")
                QMessageBox.critical(self, "Error", f"Failed to reject patient appointment: {str(e)}")

        else:
            QMessageBox.warning(self, "No Appointment Found", "Please select a valid patient to reject their appointment.")

    def approved_patient(self, patient_name):
        db = self.initialize_db()
        appointment_id = None

        if not self.patient_data_list:
            return None

        # Fetch the appointment data directly from the database
        try:
            appointment_data_list = db.child("appointment").get().val()
        except Exception as e:
            print(f"Failed to fetch appointment data: {e}")
            return

        # Find the appointment ID by patient name
        for aid, appointment_data in appointment_data_list.items():
            if appointment_data.get("patient_name") == patient_name:
                appointment_id = aid

        if appointment_id:
            try:
                # Update appointment_status to "approved"
                db.child("appointment").child(appointment_id).update({"appointment_status": "approved"})

                QMessageBox.information(self, "Success", "Patient appointment approved successfully.")

                # Optionally, update the local data list and UI
                for patient in self.patient_data_list:
                    if patient.get("patient_name") == patient_name:
                        patient["appointment_status"] = "approved"
                        break

                self.populate_patient_info()

            except Exception as e:
                print(f"Failed to approve appointment: {e}")
                QMessageBox.critical(self, "Error", f"Failed to approve patient appointment: {str(e)}")
        else:
            QMessageBox.warning(self, "No Appointment Found", "Please select a valid patient to approve their appointment.")

    def initialize_db(self):
        return db
    
    def set_user_id(self, user_id): 
        #self.clinic_id = user_id
        user_id = user_id.lower()
        clinics = db.child("clinic").get().val()
        for clinic_id, clinic_data in clinics.items():
                clinic_name = clinic_data.get("clinic_name")
                if clinic_name.lower().replace(" ", "") == user_id:
                      self.clinic_id = clinic_id
                      break
        self.fetch_patient_data()