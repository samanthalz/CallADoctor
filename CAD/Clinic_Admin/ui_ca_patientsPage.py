from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from datetime import datetime
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
        self.selected_status = ""
        self.clinic_id = ""
        self.patient_data_list = []
        self.setupUi(self)
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
        self.search_patient.setGeometry(QRect(40, 40, 681, 71))
        self.search_patient.setMinimumSize(QSize(681, 71))
        self.search_patient.setMaximumSize(QSize(681, 71))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(11)
        self.search_patient.setFont(font1)
        self.search_patient.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 60px; color: Black;\n"
" background-image: url(\"C:/Users/Samantha Law/Documents/INTI/CAD/CallADoctor/CAD/Images/icon/search_icon.png\"); \n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"border: 1px solid gray;\n"
)
        self.search_patient.setClearButtonEnabled(False)
        
        
        
        self.filter = QComboBox(self.background)
        self.filter.setObjectName(u"filter")
        self.filter.setGeometry(QRect(710, 170, 151, 31))
        self.filter.setMinimumSize(QSize(151, 31))
        self.filter.setMaximumSize(QSize(151, 31))
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(12)
        self.filter.setFont(font7)
        self.filter.setStyleSheet(u"border: 1px solid gray;")
        self.filter.activated.connect(self.updateSelectedStatus)
        self.load_status()

        
        self.patient_list_label = QLabel(self.background)
        self.patient_list_label.setObjectName(u"patient_list_label")
        self.patient_list_label.setGeometry(QRect(50, 160, 341, 41))
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(16)
        self.patient_list_label.setFont(font8)
        self.patient_list_label.setStyleSheet(u"border : none;\n")
        self.patient_details_label = QLabel(self.background)
        self.patient_details_label.setObjectName(u"patient_details_label")
        self.patient_details_label.setGeometry(QRect(990, 150, 571, 41))
        font9 = QFont()
        font9.setFamily(u"Consolas")
        font9.setPointSize(16)
        self.patient_details_label.setFont(font9)
        self.patient_details_label.setStyleSheet(u"border : none;\n")
        
        self.clear_btn = QPushButton(self.background)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(760, 50, 140, 51))
        font11 = QFont()
        font11.setFamily(u"Consolas")
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setWeight(50)
        self.clear_btn.setFont(font11)
        self.clear_btn.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 10px; color: black; border: 1px solid gray;")
        self.clear_btn.clicked.connect(self.clear_search)
        
        self.search_btn = QPushButton(self.background)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(930, 50, 140, 51))
        self.search_btn.setFont(font11)
        self.search_btn.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 10px; color: black; border: 1px solid gray;")
        self.search_btn.clicked.connect(self.search_patients)
        
        self.scrollArea = QScrollArea(self.background)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(50, 220, 811, 821))
        self.scrollArea.setMinimumSize(QSize(811, 821))
        self.scrollArea.setMaximumSize(QSize(811, 821))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 811, 821))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.vLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.vLayout.setSpacing(10)
        self.vLayout.setObjectName(u"vlayout")
        self.vLayout.setContentsMargins(0, 0, 0, 0)
        
        
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

        self.verticalLayout_3.addWidget(self.logout_navigation_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Clinic name", None))
        self.search_patient.setPlaceholderText(QCoreApplication.translate("Form", u"Search Patient Name", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
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
        
    def initialize_db(self):
        return db
        
    def fetch_patient_data(self):
        # Clear list
        self.patient_data_list = []
        db = self.initialize_db()

        try:
            # Fetch all appointments
            appointments = db.child("appointment").get().val()
            
            if appointments:
                for appointment_id, appointment_data in appointments.items():
                    # Check if the appointment is associated with the clinic
                    if appointment_data.get("clinic_id").lower() == self.clinic_id.lower():
                        patient_id = appointment_data.get("patient_id", "N/A")
                        med_concern = appointment_data.get("med_concern", "N/A")
                        time = appointment_data.get("time", "N/A")
                        date = appointment_data.get("date", "N/A")
                        doctorId = appointment_data.get("doctor_id", "N/A")
                        status = appointment_data.get("status", "N/A")
                        
                        # Initialize patient_data dictionary with appointment details
                        patient_data = {
                            "med_concern": med_concern,
                            "time": time,
                            "date": date,
                            "status": status
                        }

                        # Fetch doctor name using doctorId from the appointment
                        doctor_name = "N/A"
                        doctor_info = db.child("clinic").child(self.clinic_id).child("doctors").child(doctorId).get().val()
                        if doctor_info:
                            doctor_name = doctor_info.get("doctor_name", "N/A")
                        patient_data["doctor_name"] = doctor_name

                        # Fetch patient name using patient_id from the appointment
                        patients = db.child("patients").get().val()
                        if patients and patient_id in patients:
                            patient_info = patients.get(patient_id)
                            patient_name = patient_info.get("patient_name", "N/A")  # Extract patient name
                            patient_data["patient_name"] = patient_name

                        # Save all relevant patient data to the list
                        self.patient_data_list.append(patient_data)
            
            #print(f"list is {self.patient_data_list}")
            # Populate patient information on the UI
            self.populate_patient_info()

        except Exception as e:
            print(f"An error occurred while fetching data: {e}")


    def clear_layout(self):
        while self.vLayout.count():
                item = self.vLayout.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.deleteLater()
                        
    def populate_patient_info(self, search_query=None):
        self.clear_layout()

        visible_patients = []

        for i, patient_data in enumerate(self.patient_data_list):
                if isinstance(patient_data, dict):
                        patient_name = patient_data.get("patient_name", "").lower()
                        appt_status = patient_data.get("status", "").lower()

                if self.selected_status and appt_status.lower() != self.selected_status.lower():
                        continue

                # Check search query if provided
                if not search_query or search_query.lower() in patient_name:
                    patient_frame = self.create_patient_list_frame(patient_data)
                    if patient_frame:
                            visible_patients.append(patient_frame)
                        
        #print(f"no of visible frames is {len(visible_patients)}")
        # Add visible clinics to the layout in reverse order
        for patient_frame in reversed(visible_patients):
                self.vLayout.addWidget(patient_frame)

        self.scrollAreaWidgetContents.setLayout(self.vLayout)
        self.vLayout.setAlignment(Qt.AlignTop)
        self.vLayout.update()
        self.scrollAreaWidgetContents.update()
        
    def create_patient_list_frame(self, patient_data):
        patient_frame = QFrame(self.scrollAreaWidgetContents)
        patient_frame.setObjectName(u"patient_frame")
        patient_frame.setGeometry(QRect(0, 0, 801, 81))
        patient_frame.setMinimumSize(QSize(801, 81))
        patient_frame.setMaximumSize(QSize(801, 81))
        patient_frame.setFrameShape(QFrame.StyledPanel)
        patient_frame.setFrameShadow(QFrame.Raised)
        patient_name_label1 = QLabel(patient_frame)
        patient_name_label1.setObjectName(u"patient_name_label1")
        patient_name_label1.setGeometry(QRect(90, 30, 121, 21))
        patient_name_label1.setMinimumSize(QSize(121, 21))
        patient_name_label1.setMaximumSize(QSize(121, 21))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        patient_name_label1.setFont(font3)
        patient_name_label1.setStyleSheet(u"border : none;\n")
        patient_name_label1.setText(patient_data.get("patient_name", "Unknown"))
        
        patient_name_label1.mousePressEvent = lambda event, patient=patient_data: self.create_popup_widget(patient)
        
        patient_profile_logo1 = QLabel(patient_frame)
        patient_profile_logo1.setObjectName(u"patient_profile_logo1")
        patient_profile_logo1.setGeometry(QRect(10, 10, 60, 60))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(9)
        patient_profile_logo1.setFont(font2)
        patient_profile_logo1.setStyleSheet(u"background-color: transparent; \n")       
        patient_profile_logo1.setAlignment(Qt.AlignCenter)
        
        appt_time_label = QLabel(patient_frame)
        appt_time_label.setObjectName(u"appt_time_label")
        appt_time_label.setGeometry(QRect(690, 20, 91, 41))
        appt_time_label.setMinimumSize(QSize(91, 41))
        appt_time_label.setMaximumSize(QSize(91, 41))
        appt_time_label.setFont(font3)
        appt_time_label.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);color: #128983; text-align: center;\n")
        appt_time_label.setAlignment(Qt.AlignCenter)
        appt_time_label.setText(patient_data.get("time", "Unknown"))
        
        status = QLabel(patient_frame)
        status.setObjectName(u"status")
        status.setGeometry(QRect(570, 20, 91, 41))
        status.setMinimumSize(QSize(91, 41))
        status.setMaximumSize(QSize(91, 41))
        status.setFont(font3)
        status.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);color: #128983; text-align: center;\n")
        status.setAlignment(Qt.AlignCenter)
        status.setText(patient_data.get("status", "Unknown"))

        return patient_frame

    def set_user_id(self, user_id): 
        user_id = user_id.lower()
        clinics = db.child("clinic").get().val()
        for clinic_id, clinic_data in clinics.items():
                clinic_name = clinic_data.get("clinic_name")
                if clinic_name.lower().replace(" ", "") == user_id:
                      self.clinic_id = clinic_id
                      break
                  
                  
    def load_status(self):
        status = [
            "All",
            "Pending",
            "Approved",
            "Rejected"
        ]
        self.filter.addItems(status)   
        
    def updateSelectedStatus(self, index):
        selected_text = self.filter.itemText(index)

        if index == 0:
                self.selected_status = ""
        else:
                self.selected_status = selected_text
        self.hide_patient_details_frame()
        self.populate_patient_info()
        self.hide_patient_details_frame()
        
    def create_patient_details_frame(self, patient_data): 
        patient_details_outer_frame = QFrame(self.background)
        patient_details_outer_frame.setObjectName(u"patient_details_outer_frame")
        patient_details_outer_frame.setGeometry(QRect(979, 200, 751, 841))
        patient_details_outer_frame.setStyleSheet(u"background-color : #ffffff;")
        patient_details_outer_frame.setFrameShape(QFrame.StyledPanel)
        patient_details_outer_frame.setFrameShadow(QFrame.Raised)
        patient_details_inner = QFrame(patient_details_outer_frame)
        patient_details_inner.setObjectName(u"patient_details_inner")
        patient_details_inner.setGeometry(QRect(20, 30, 721, 751))
        patient_details_inner.setFrameShape(QFrame.StyledPanel)
        patient_details_inner.setFrameShadow(QFrame.Raised)
        patient_logo_2 = QLabel(patient_details_inner)
        patient_logo_2.setObjectName(u"patient_logo_2")
        patient_logo_2.setGeometry(QRect(9, 9, 54, 54))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(9)
        patient_logo_2.setFont(font2)
        patient_logo_2.setStyleSheet(u"background-color: #B6D0E2; border-radius: 25px;border: 2px solid #B6D0F7;")
        patient_logo_2.setAlignment(Qt.AlignCenter)
        patient_logo_2.setPixmap(QPixmap(u"CAD/Images/icon/profile_icon.png"))
                
        patient_name_display = QLabel(patient_details_inner)
        patient_name_display.setObjectName(u"patient_name_display")
        patient_name_display.setGeometry(QRect(9, 69, 120, 22))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        patient_name_display.setFont(font3)
        patient_name_display.setStyleSheet(u"border : none;\n")
        patient_name_display.setText(patient_data.get("patient_name", "Unknown"))
        
        line_2 = QFrame(patient_details_inner)
        line_2.setObjectName(u"line_2")
        line_2.setGeometry(QRect(9, 205, 703, 3))
        line_2.setMinimumSize(QSize(357, 3))
        line_2.setMaximumSize(QSize(16777215, 3))
        line_2.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        line_2.setFrameShape(QFrame.StyledPanel)
        line_2.setFrameShadow(QFrame.Raised)
        diagnosis_display = QLabel(patient_details_inner)
        diagnosis_display.setObjectName(u"diagnosis_display")
        diagnosis_display.setGeometry(QRect(320, 300, 390, 148))
        diagnosis_display.setMinimumSize(QSize(390, 148))
        diagnosis_display.setMaximumSize(QSize(390, 148))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setWeight(50)
        diagnosis_display.setFont(font4)
        diagnosis_display.setStyleSheet(u"border: none;")
        diagnosis_display.setScaledContents(False)
        diagnosis_display.setWordWrap(True)
        diagnosis_display.setText(patient_data.get("med_concern", "Unknown"))
        
        diagnosis_label = QLabel(patient_details_inner)
        diagnosis_label.setObjectName(u"diagnosis_label")
        diagnosis_label.setGeometry(QRect(13, 300, 301, 148))
        diagnosis_label.setMinimumSize(QSize(301, 148))
        diagnosis_label.setMaximumSize(QSize(301, 148))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        diagnosis_label.setFont(font5)
        diagnosis_label.setStyleSheet(u"border: none;")
        diagnosis_label.setWordWrap(True)
        diagnosis_label.setText("Diagnosis:")
        
        last_checked_by_label = QLabel(patient_details_inner)
        last_checked_by_label.setObjectName(u"last_checked_by_label")
        last_checked_by_label.setGeometry(QRect(13, 210, 301, 148))
        last_checked_by_label.setMinimumSize(QSize(301, 148))
        last_checked_by_label.setMaximumSize(QSize(301, 148))
        last_checked_by_label.setFont(font5)
        last_checked_by_label.setStyleSheet(u"border: none;")
        last_checked_by_label.setWordWrap(True)
        last_checked_by_label.setText("Last checked by:")
        
        dr_name_display = QLabel(patient_details_inner)
        dr_name_display.setObjectName(u"dr_name_display")
        dr_name_display.setGeometry(QRect(320, 210, 390, 148))
        dr_name_display.setMinimumSize(QSize(390, 148))
        dr_name_display.setMaximumSize(QSize(390, 148))
        dr_name_display.setFont(font4)
        dr_name_display.setStyleSheet(u"border: none;")
        dr_name_display.setScaledContents(False)
        dr_name_display.setWordWrap(True)
        dr_name_display.setText(patient_data.get("doctor_name", "Unknown"))
        
        date_label = QLabel(patient_details_inner)
        date_label.setObjectName(u"date_label")
        date_label.setGeometry(QRect(13, 400, 301, 148))
        date_label.setMinimumSize(QSize(301, 148))
        date_label.setMaximumSize(QSize(301, 148))
        date_label.setFont(font5)
        date_label.setStyleSheet(u"border: none;")
        date_label.setWordWrap(True)
        date_label.setText("Date:")
        
        date_display = QLabel(patient_details_inner)
        date_display.setObjectName(u"date_display")
        date_display.setGeometry(QRect(320, 400, 390, 148))
        date_display.setMinimumSize(QSize(390, 148))
        date_display.setMaximumSize(QSize(390, 148))
        date_display.setFont(font4)
        date_display.setStyleSheet(u"border: none;")
        date_display.setScaledContents(False)
        date_display.setWordWrap(True)
        #date_display.setText(patient_data.get("date", "Unknown"))
        
        # Fetch the date string from fb_data
        date_str = patient_data.get("date", "Unknown")
        # Check if the date is valid and not "Unknown"
        if date_str != "Unknown":
            # Parse the date string to a datetime object
            date_obj = datetime.strptime(date_str, "%y%m%d")
            
            # Format the datetime object to the desired string format
            formatted_date = date_obj.strftime("%d %B %Y")
        else:
            formatted_date = "Unknown"

        # Set the text to the formatted date
        date_display.setText(formatted_date)
        
        time_display = QLabel(patient_details_inner)
        time_display.setObjectName(u"time_display")
        time_display.setGeometry(QRect(320, 500, 390, 148))
        time_display.setMinimumSize(QSize(390, 148))
        time_display.setMaximumSize(QSize(390, 148))
        time_display.setFont(font4)
        time_display.setStyleSheet(u"border: none;")
        time_display.setScaledContents(False)
        time_display.setWordWrap(True)
        time_display.setText(patient_data.get("time", "Unknown"))
        
        time_label = QLabel(patient_details_inner)
        time_label.setObjectName(u"time_label")
        time_label.setGeometry(QRect(13, 500, 301, 148))
        time_label.setMinimumSize(QSize(301, 148))
        time_label.setMaximumSize(QSize(301, 148))
        time_label.setFont(font5)
        time_label.setStyleSheet(u"border: none;")
        time_label.setWordWrap(True)
        time_label.setText("Time:")
        
        reject_btn = QPushButton(patient_details_inner)
        reject_btn.setObjectName(u"reject_btn")
        reject_btn.setGeometry(QRect(510, 700, 181, 41))
        reject_btn.setMinimumSize(QSize(181, 41))
        reject_btn.setMaximumSize(QSize(181, 41))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        reject_btn.setFont(font6)
        reject_btn.setStyleSheet(u"background-color: #E73030; border-radius: 16px; color: white; border: 1px solid gray;")
        reject_btn.setText("Reject")
        approved_btn = QPushButton(patient_details_inner)
        approved_btn.setObjectName(u"approved_btn")
        approved_btn.setGeometry(QRect(320, 700, 181, 41))
        approved_btn.setMinimumSize(QSize(181, 41))
        approved_btn.setMaximumSize(QSize(181, 41))
        approved_btn.setFont(font6)
        approved_btn.setText("Approve")
        approved_btn.setStyleSheet(u"background-color: rgb(18, 137, 131);border-radius: 16px; color: white; border: 1px solid gray;")
        
        return patient_details_outer_frame
        
        
    def create_popup_widget(self, patient_data):
        self.hide_patient_details_frame()
        self.patient_details_frame = self.create_patient_details_frame(patient_data)
        self.patient_details_frame.setVisible(True)
        
    def hide_patient_details_frame(self):
        if self.patient_details_frame:
            self.patient_details_frame.setVisible(False)
            
    def search_patients(self):
        search_text = self.search_patient.text().strip().lower()
        if search_text:
                self.hide_patient_details_frame()
                self.populate_patient_info(search_text)
                self.hide_patient_details_frame()
                
        else:
                self.hide_patient_details_frame()
                self.populate_patient_info()
                self.hide_patient_details_frame()

    def clear_search(self):
        self.search_patient.clear()
        self.hide_patient_details_frame()

        # Remove all widgets from the layout
        while self.vLayout.count():
                widget = self.vLayout.takeAt(0).widget()
                if widget:
                        widget.deleteLater()
        self.hide_patient_details_frame()
        self.populate_patient_info()
        self.hide_patient_details_frame()
