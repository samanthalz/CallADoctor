from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class CA_homepageWidget(QWidget):
    login_successful = pyqtSignal(int)
    #user_id = pyqtSignal(str)
    apply_btn_clicked = pyqtSignal()
    open_ca_homepage = pyqtSignal()
    view_detail_btn_clicked = pyqtSignal()
    doctors_navigation_btn_clicked = pyqtSignal()
    patients_navigation_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    settings_navigation_btn_clicked = pyqtSignal()
    redirect_fb = pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.clinic_id = ""
        self.doc_data_list = []
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
        
        self.feedback_frame = QFrame(self.background)
        self.feedback_frame.setObjectName(u"feedback_frame")
        self.feedback_frame.setGeometry(QRect(1090, 180, 481, 831))
        self.feedback_frame.setStyleSheet(u"border: 2px solid #FFFFFF;\n"
"border-radius: 16px;\n"
"background-color: white")
        self.feedback_frame.setFrameShape(QFrame.StyledPanel)
        self.feedback_frame.setFrameShadow(QFrame.Raised)
        self.upcomin_appt_frame_2 = QFrame(self.feedback_frame)
        self.upcomin_appt_frame_2.setObjectName(u"upcomin_appt_frame_2")
        self.upcomin_appt_frame_2.setGeometry(QRect(20, 20, 450, 551))
        self.upcomin_appt_frame_2.setStyleSheet(u"background-color : #ffffff;")
        self.upcomin_appt_frame_2.setFrameShape(QFrame.StyledPanel)
        self.upcomin_appt_frame_2.setFrameShadow(QFrame.Raised)
        self.upcoming_label_2 = QLabel(self.upcomin_appt_frame_2)
        self.upcoming_label_2.setObjectName(u"upcoming_label_2")
        self.upcoming_label_2.setGeometry(QRect(30, 20, 211, 41))
        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(11)
        self.upcoming_label_2.setFont(font)
        self.upcoming_label_2.setStyleSheet(u"border : none;\n"
"")
        

        self.widget2 = QWidget(self.upcomin_appt_frame_2)
        self.widget2.setObjectName(u"widget")
        self.widget2.setGeometry(QRect(20, 70, 403, 241))
        self.verticalLayout_4 = QVBoxLayout(self.widget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)


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
        self.profile_btn.setGeometry(QRect(110, 25, 111, 31))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        self.profile_btn.setFont(font3)
        self.profile_btn.setStyleSheet(u"border: none")

        self.clinic_req_frame = QFrame(self.background)
        self.clinic_req_frame.setObjectName(u"clinic_req_frame")
        self.clinic_req_frame.setGeometry(QRect(50, 140, 1000, 230))
        self.clinic_req_frame.setStyleSheet(u"border-radius: 10px;\n"
"    background-color: #B6D0E2;\n"
"    background-image: qlineargradient(\n"
"        spread: pad, \n"
"        x1: 0, y1: 0, \n"
"        x2: 0, y2: 1, \n"
"        stop: 0 #B6D0E2, \n"
"        stop: 1 #FFFFFF\n"
"    );")
        
        self.profile_btn.clicked.connect(self.emitProfileBtn)

        self.clinic_req_frame.setFrameShape(QFrame.StyledPanel)
        self.clinic_req_frame.setFrameShadow(QFrame.Raised)
        self.visit_for_today_label = QLabel(self.clinic_req_frame)
        self.visit_for_today_label.setObjectName(u"visit_for_today_label")
        self.visit_for_today_label.setGeometry(QRect(20, 20, 961, 61))
        font4 = QFont()
        font4.setFamily(u"Cascadia Code")
        font4.setPointSize(22)
        self.visit_for_today_label.setFont(font4)
        self.visit_for_today_label.setWordWrap(True)
        self.clinic_req__label = QLabel(self.clinic_req_frame)
        self.clinic_req__label.setObjectName(u"clinic_req__label")
        self.clinic_req__label.setGeometry(QRect(30, 100, 141, 71))
        font5 = QFont()
        font5.setFamily(u"Cascadia Code")
        font5.setPointSize(48)
        self.clinic_req__label.setFont(font5)

        self.details_frame = QFrame(self.background)
        self.details_frame.setObjectName(u"details_frame")
        self.details_frame.setGeometry(QRect(50, 420, 1000, 600))
        self.details_frame.setStyleSheet(u"border: 2px solid #F8F8F8;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.details_frame.setFrameShape(QFrame.StyledPanel)
        self.details_frame.setFrameShadow(QFrame.Raised)
        self.details_frame.setLineWidth(6)

        self.upcomin_appt_frame = QFrame(self.details_frame)
        self.upcomin_appt_frame.setObjectName(u"upcomin_appt_frame")
        self.upcomin_appt_frame.setGeometry(QRect(30, 30, 450, 551))
        self.upcomin_appt_frame.setStyleSheet(u"background-color : #ffffff;")
        self.upcomin_appt_frame.setFrameShape(QFrame.StyledPanel)
        self.upcomin_appt_frame.setFrameShadow(QFrame.Raised)
        self.upcoming_label = QLabel(self.upcomin_appt_frame)
        self.upcoming_label.setObjectName(u"upcoming_label")
        self.upcoming_label.setGeometry(QRect(30, 20, 211, 41))
        self.upcoming_label.setFont(font)
        self.upcoming_label.setStyleSheet(u"border : none;\n"
"")
        
        
        self.widget = QWidget(self.upcomin_appt_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 403, 431))
        self.patientlist_layout = QVBoxLayout(self.widget)
        self.patientlist_layout.setObjectName(u"patientlist_layout")
        self.patientlist_layout.setSpacing(10)
        self.patientlist_layout.setContentsMargins(0, 0, 0, 0)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(31, 20, 87, 851))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.home_navigation = QToolButton(self.layoutWidget)
        self.home_navigation.setObjectName(u"home_navigation")
        self.home_navigation.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        self.home_navigation.setMinimumSize(QSize(85, 96))
        self.home_navigation.setMaximumSize(QSize(85, 96))
        font9 = QFont()
        font9.setFamily(u"Source Sans Pro Semibold")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        self.home_navigation.setFont(font9)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        
       

        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.home_navigation)

        self.doctors_navigation = QToolButton(self.layoutWidget)
        self.doctors_navigation.setObjectName(u"doctors_navigation")
        self.doctors_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.doctors_navigation.sizePolicy().hasHeightForWidth())
        self.doctors_navigation.setSizePolicy(sizePolicy)
        self.doctors_navigation.setMinimumSize(QSize(85, 96))
        self.doctors_navigation.setMaximumSize(QSize(85, 96))
        self.doctors_navigation.setFont(font9)
        self.doctors_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.doctors_navigation.setIcon(icon2)
        self.doctors_navigation.setIconSize(QSize(70, 70))
        self.doctors_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.doctors_navigation.clicked.connect(self.emitDoctorsBtn)

        self.verticalLayout.addWidget(self.doctors_navigation)

        self.patients_navigation = QToolButton(self.layoutWidget)
        self.patients_navigation.setObjectName(u"patients_navigation")
        self.patients_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.patients_navigation.sizePolicy().hasHeightForWidth())
        self.patients_navigation.setSizePolicy(sizePolicy)
        self.patients_navigation.setMinimumSize(QSize(85, 96))
        self.patients_navigation.setMaximumSize(QSize(85, 96))
        self.patients_navigation.setFont(font9)
        self.patients_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        
        self.patients_navigation.clicked.connect(self.emitPatientsBtn)

        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patients_navigation.setIcon(icon3)
        self.patients_navigation.setIconSize(QSize(70, 70))
        self.patients_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.patients_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setMinimumSize(QSize(85, 96))
        self.settings_navigation.setMaximumSize(QSize(85, 96))
        self.settings_navigation.setFont(font9)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        
        self.settings_navigation.clicked.connect(self.emitSettingsBtn)

        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setMinimumSize(QSize(85, 96))
        self.logout_navigation.setMaximumSize(QSize(85, 96))
        self.logout_navigation.setFont(font9)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        
        #self.logout_btn_clicked.connect(self.emitLogoutBtn)
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)


        icon5 = QIcon()
        icon5.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)


        """self.view_patient_details_button = QPushButton('View Patient Details')
        #self.logout_button = QPushButton('Logout') """

        """ layout = QVBoxLayout()
        layout.addWidget(self.view_patient_details_button)
        layout.addWidget(self.logout_button)
        self.setLayout(layout) """

        # Connect button clicks to methods
        """ self.view_patient_details_button.clicked.connect(self.show_view_patient_details_message)
        self.logout_button.clicked.connect(self.show_logout_message) """

    """ def show_view_patient_details_message(self):
        QMessageBox.information(self, 'Info', 'View Patient Details button clicked.')

    def show_logout_message(self):
        QMessageBox.information(self, 'Info', 'Logout button clicked.') """
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.upcoming_label_2.setText(QCoreApplication.translate("Form", u"Doctor List", None))
        #self.doc_name_label_6.setText(QCoreApplication.translate("Form", u"Dr Name", None))
        #self.doc_logo_label_2.setText(QCoreApplication.translate("Form", u"A", None))
        #self.patient_visit_reason_label_6.setText(QCoreApplication.translate("Form", u"Clinic A", None))
        #self.doc_name_label_7.setText(QCoreApplication.translate("Form", u"Dr Name", None))
        #self.clinic_name_label.setText(QCoreApplication.translate("Form", u"Clinic A", None))
        #self.doc_logo_label_3.setText(QCoreApplication.translate("Form", u"DR", None))
        #self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Recent", None))
        #self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Oldest", None))

        
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Clinic", None))
        self.visit_for_today_label.setText(QCoreApplication.translate("Form", u"Visits for today:", None))
        self.clinic_req__label.setText(QCoreApplication.translate("Form", u"10", None))
        self.upcoming_label.setText(QCoreApplication.translate("Form", u"Patient List", None))
       

        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.doctors_navigation.setText(QCoreApplication.translate("Form", u"Doctors", None))
        self.patients_navigation.setText(QCoreApplication.translate("Form", u"Patients", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

    @pyqtSlot()
    def emitDoctorsBtn(self):
        self.doctors_navigation_btn_clicked.emit()
        
    @pyqtSlot()
    def emitViewDetailBtn(self):
        self.view_detail_btn_clicked.emit()

    @pyqtSlot()
    def emitPatientsBtn(self):
        self.patients_navigation_btn_clicked.emit()    
        
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
        patientReq_frame = QFrame(self.widget)
        patientReq_frame.setObjectName(u"patientReq_frame")
        patientReq_frame.setGeometry(QRect(20, 70, 401, 81))
        patientReq_frame.setMinimumSize(QSize(401, 81))
        patientReq_frame.setMaximumSize(QSize(401, 81))
        patientReq_frame.setFrameShape(QFrame.StyledPanel)
        patientReq_frame.setFrameShadow(QFrame.Raised)
        patient_name_label = QLabel(patientReq_frame)
        patient_name_label.setObjectName(u"patient_name_label")
        patient_name_label.setGeometry(QRect(90, 30, 121, 21))
        patient_name_label.setMinimumSize(QSize(121, 21))
        patient_name_label.setMaximumSize(QSize(121, 21))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(10)
        patient_name_label.setFont(font1)
        patient_name_label.setStyleSheet(u"border : none;\n"
"")
        patient_name_label.mousePressEvent = lambda event, patient=patient_data: self.create_popup_widget(patient)


        patient_logo_label = QLabel(patientReq_frame)
        patient_logo_label.setObjectName(u"patient_logo_label")
        patient_logo_label.setGeometry(QRect(10, 10, 54, 54))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(9)
        patient_logo_label.setFont(font2)
        patient_logo_label.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        
        patient_logo_label.setAlignment(Qt.AlignCenter)
        patient_logo_label.setAlignment(Qt.AlignCenter)
        patient_img_path = patient_data.get("patient_img", "Path Not Found")
        if patient_img_path:
                pixmap = QPixmap(patient_img_path)
                patient_logo_label.setPixmap(pixmap.scaled(patient_logo_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))



        label = QLabel(patientReq_frame)
        label.setObjectName(u"label")
        label.setGeometry(QRect(290, 20, 91, 41))
        label.setMinimumSize(QSize(91, 41))
        label.setMaximumSize(QSize(91, 41))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        label.setFont(font3)
        label.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.10);\n"
"color: #128983; text-align: center;\n"
"")

        label.setAlignment(Qt.AlignCenter)
        patient_visit_reason_label = QLabel(patientReq_frame)
        patient_visit_reason_label.setObjectName(u"patient_visit_reason_label")
        patient_visit_reason_label.setGeometry(QRect(90, 60, 55, 16))
        patient_visit_reason_label.setMinimumSize(QSize(55, 16))
        patient_visit_reason_label.setMaximumSize(QSize(55, 16))
        patient_visit_reason_label.setStyleSheet(u"color: #128983")
        
        label.setText(patient_data.get("time", "Unknown"))
        patient_name_label.setText(patient_data.get("patient_name", "Unknown"))
        patient_visit_reason_label.setText(patient_data.get("med_concern", "Unknown"))

        return patientReq_frame
    
      
    def clear_layout(self):
        while self.patientlist_layout.count():
                item = self.patientlist_layout.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.destroy()

    def populate_patient_info(self):
        visible_patients = []
        

        for i, patient_data in enumerate(self.patient_data_list):
                patient_frame = self.create_patient_list_frame(patient_data)
                if patient_frame:
                        visible_patients.append(patient_frame)

        #print(f"Number of frames in visible_patients: {len(visible_patients)}")
        # Clear existing layout
        for i in reversed(range(self.patientlist_layout.count())):
                widget = self.patientlist_layout.itemAt(i).widget()
                if widget is not None:
                        widget.deleteLater()

        # Add visible appointments to the layout in reverse order
        for appt_frame in reversed(visible_patients):
                self.patientlist_layout.addWidget(appt_frame)

        #print(f"Number of frames added to the layout: {len(list(reversed(visible_patients))[:5])}")

        self.widget.setLayout(self.patientlist_layout)
        self.patientlist_layout.setAlignment(Qt.AlignTop)
        self.patientlist_layout.update()
        self.widget.update()
        

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
        request_detail_outer = QFrame(self.background)
        request_detail_outer.setObjectName(u"request_detail_outer")
        request_detail_outer.setGeometry(QRect(540, 430, 450, 551)) 
        request_detail_outer.setStyleSheet(u"background-color : #ffffff;")
        request_detail_outer.setFrameShape(QFrame.StyledPanel)
        request_detail_outer.setFrameShadow(QFrame.Raised)
        req_detail_label = QLabel(request_detail_outer)
        req_detail_label.setObjectName(u"req_detail_label")
        req_detail_label.setGeometry(QRect(30, 20, 381, 41))
        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(11)
        req_detail_label.setFont(font)
        req_detail_label.setStyleSheet(u"border : none;\n"
"")
        clinic_details_inner = QFrame(request_detail_outer)
        clinic_details_inner.setObjectName(u"clinic_details_inner")
        clinic_details_inner.setGeometry(QRect(20, 70, 411, 421))
        clinic_details_inner.setFrameShape(QFrame.StyledPanel)
        clinic_details_inner.setFrameShadow(QFrame.Raised)
        verticalLayout_2 = QVBoxLayout(clinic_details_inner)
        verticalLayout_2.setObjectName(u"verticalLayout_2")
        patient_logo = QLabel(clinic_details_inner)
        patient_logo.setObjectName(u"patient_logo")
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(9)
        patient_logo.setFont(font2)
        patient_logo.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        patient_logo.setAlignment(Qt.AlignCenter)
        patient_logo.setAlignment(Qt.AlignCenter)
        patient_logo.setAlignment(Qt.AlignCenter)

        patient_img_path = patient_data.get("patient_img","")
        if patient_img_path:
                pixmap = QPixmap(patient_img_path)
                patient_logo.setPixmap(pixmap.scaled(patient_logo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        verticalLayout_2.addWidget(patient_logo)

        patient_name = QLabel(clinic_details_inner)
        patient_name.setObjectName(u"patient_name")
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(10)
        patient_name.setFont(font1)
        patient_name.setText(patient_data.get("patient_name", "Unknown"))
        patient_name.setStyleSheet(u"border : none;\n"
"")

        

        verticalLayout_2.addWidget(patient_name)

        line = QFrame(clinic_details_inner)
        line.setObjectName(u"line")
        line.setMinimumSize(QSize(357, 3))
        line.setMaximumSize(QSize(16777215, 3))
        line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        line.setFrameShape(QFrame.StyledPanel)
        line.setFrameShadow(QFrame.Raised)

        verticalLayout_2.addWidget(line)

        splitter = QSplitter(clinic_details_inner)
        splitter.setObjectName(u"splitter")
        splitter.setOrientation(Qt.Horizontal)
        lastCheck_label = QLabel(splitter)
        lastCheck_label.setObjectName(u"lastCheck_label")
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        lastCheck_label.setFont(font6)
        lastCheck_label.setStyleSheet(u"border: none;")
        lastCheck_label.setLineWidth(0)
        lastCheck_label.setText("Last Checked:")
        splitter.addWidget(lastCheck_label)
        doctor_display = QLabel(splitter)
        doctor_display.setObjectName(u"doctor_display")
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setWeight(50)
        doctor_display.setFont(font7)
        doctor_display.setStyleSheet(u"border: none;")
        doctor_display.setText(patient_data.get("med_concern", "Unknown"))
        doctor_display.setScaledContents(False)
        doctor_display.setWordWrap(True)
        doctor_display.setText(patient_data.get("doctor_name", "Unknown"))
        splitter.addWidget(doctor_display)

        verticalLayout_2.addWidget(splitter)

        splitter_2 = QSplitter(clinic_details_inner)
        splitter_2.setObjectName(u"splitter_2")
        splitter_2.setOrientation(Qt.Horizontal)
        diagnosis_label = QLabel(splitter_2)
        diagnosis_label.setObjectName(u"diagnosis_label")
        diagnosis_label.setFont(font6)
        diagnosis_label.setStyleSheet(u"border: none;")
        diagnosis_label.setText("Diagnosis:")
        splitter_2.addWidget(diagnosis_label)
        diagnosis_display = QLabel(splitter_2)
        diagnosis_display.setObjectName(u"diagnosis_display")
        diagnosis_display.setFont(font7)
        diagnosis_display.setStyleSheet(u"border: none;")
        diagnosis_display.setScaledContents(False)
        diagnosis_display.setWordWrap(True)
        diagnosis_display.setText(patient_data.get("med_concern", "Unknown"))
        splitter_2.addWidget(diagnosis_display)

        verticalLayout_2.addWidget(splitter_2)

        splitter_3 = QSplitter(clinic_details_inner)
        splitter_3.setObjectName(u"splitter_3")
        splitter_3.setOrientation(Qt.Horizontal)
        date_text = QLabel(splitter_3)
        date_text.setObjectName(u"date_text")
        date_text.setFont(font6)
        date_text.setStyleSheet(u"border: none;")
        date_text.setWordWrap(True)
        date_text.setText("Date:")
        splitter_3.addWidget(date_text)
        hour_display = QLabel(splitter_3)
        hour_display.setObjectName(u"hour_display")
        hour_display.setFont(font7)
        hour_display.setText(patient_data.get("date", "Unknown"))
        hour_display.setStyleSheet(u"border: none;")
        hour_display.setScaledContents(False)
        hour_display.setWordWrap(True)
        splitter_3.addWidget(hour_display)

        verticalLayout_2.addWidget(splitter_3)

        view_detail_btn = QPushButton(request_detail_outer)
        view_detail_btn.setObjectName(u"view_detail_btn")
        view_detail_btn.setGeometry(QRect(320, 510, 93, 28))   
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(9)
        font8.setUnderline(True)
        view_detail_btn.setFont(font8)
        view_detail_btn.setStyleSheet(u"color: #007E85; border: none;")
        view_detail_btn.clicked.connect(self.emitViewDetailBtn)
        return request_detail_outer
    
    def fetch_doc_data(self):
        db = self.initialize_db()  # Assuming this method initializes your Firebase connection
        try:
                clinics = db.child("clinic").get()
         
                
                if clinics.each():
                        print(f"if clinic.each():{clinics}")
                        self.doctor_data_list = []
                        
                        for clinic in clinics.each():
                                print(f"for clinic in clinics.each():{clinics}")
                                clinic_data = clinic.val()
                                clinic_id = clinic.key()  # Assuming clinic ID is stored as the key
                                
                              
                                
                                if clinic_id == self.clinic_id:
                                        print(f"if clinic_id == self.clinic_id:{clinic_id}")
                                        doctors = clinic_data.get("doctors", {})
                                        
                                        for doctor_id, doctor_info in doctors.items():
                                                print(f"for doctor_id, doctor_info in doctors.items():{doctor_id}")
                                                doctor_name = doctor_info.get("name", "Unknown")
                                                
                                                # Add fetched doctor data to the list
                                                self.doctor_data_list.append({"doctor_id": doctor_id, "doctor_name": doctor_name})

                                            
                                        
                                        break  # Assuming each clinic_id is unique and we only need to process the relevant clinic
                                
                                # Populate doctor information on the UI
                                self.populate_doctor_info()
                else:
                        print("No clinics data found.")
                        
        except Exception as e:
                print(f"An error occurred while fetching data: {e}")

    def create_doctor_list_frame(self, doc_data):
        clinicReq_frame_6 = QFrame(clinicReq_frame_6)
        clinicReq_frame_6.setObjectName(u"clinicReq_frame_6")
        clinicReq_frame_6.setGeometry(QRect(20, 70, 401, 81))
        clinicReq_frame_6.setFrameShape(QFrame.StyledPanel)
        clinicReq_frame_6.setFrameShadow(QFrame.Raised)
        doc_name_label_6 = QLabel(clinicReq_frame_6)
        doc_name_label_6.setObjectName(u"doc_name_label_6")
        doc_name_label_6.setGeometry(QRect(90, 30, 121, 21))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(10)
        doc_name_label_6.setFont(font1)
        doc_name_label_6.setStyleSheet(u"border : none;\n"
"")
        doc_name_label_6.setText(doc_data.get("doctor_name", "Unknown"))

        doc_logo_label_2 = QLabel(clinicReq_frame_6)
        doc_logo_label_2.setObjectName(u"doc_logo_label_2")
        doc_logo_label_2.setGeometry(QRect(10, 10, 54, 54))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(9)
        doc_logo_label_2.setFont(font2)
        doc_logo_label_2.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        doc_logo_label_2.setAlignment(Qt.AlignCenter)


        patient_visit_reason_label_6 = QLabel(clinicReq_frame_6)
        patient_visit_reason_label_6.setObjectName(u"patient_visit_reason_label_6")
        patient_visit_reason_label_6.setGeometry(QRect(90, 60, 55, 16))
        patient_visit_reason_label_6.setStyleSheet(u"color: #128983")
        patientReq_frame_7 = QFrame(clinicReq_frame_6)
        patientReq_frame_7.setObjectName(u"patientReq_frame_7")
        patientReq_frame_7.setGeometry(QRect(20, 170, 401, 81))
        patientReq_frame_7.setFrameShape(QFrame.StyledPanel)
        patientReq_frame_7.setFrameShadow(QFrame.Raised)


        doc_name_label_7 = QLabel(patientReq_frame_7)
        doc_name_label_7.setObjectName(u"doc_name_label_7")
        doc_name_label_7.setGeometry(QRect(90, 30, 151, 21))
        doc_name_label_7.setFont(font1)
        doc_name_label_7.setStyleSheet(u"border : none;\n"
"")
        clinic_name_label = QLabel(patientReq_frame_7)
        clinic_name_label.setObjectName(u"clinic_name_label")
        clinic_name_label.setGeometry(QRect(90, 60, 55, 16))
        clinic_name_label.setStyleSheet(u"color: #128983")
        doc_logo_label_3 = QLabel(patientReq_frame_7)
        doc_logo_label_3.setObjectName(u"doc_logo_label_3")
        doc_logo_label_3.setGeometry(QRect(10, 10, 54, 54))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(9)

        doc_logo_label_3.setFont(font2)
        doc_logo_label_3.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        doc_logo_label_3.setAlignment(Qt.AlignCenter)
        
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)

   
    def populate_doctor_info(self):
        visible_doctors = []
        
        for i, doctor_data in enumerate(self.doc_data_list):
                print(f"for doc data in data{doctor_data}")
                doctor_frame = self.create_doctor_list_frame(doctor_data)
                if doctor_frame:
                        visible_doctors.append(doctor_frame)


        print(f"Number of frames in visible_doctors: {len(visible_doctors)}")
        # Clear existing layout
        for i in reversed(range(self.verticalLayout_4.count())):
                print(f"for i in reversed(range(self.verticalLayout_4.count())")
                widget = self.verticalLayout_4.itemAt(i).widget()
                if widget is not None:
                        widget.deleteLater()

        # Add visible doctors to the layout in reverse order
        for appt_frame in reversed(visible_doctors):
                print(f" for appt_frame in reversed(visible_doctors):")
                self.verticalLayout_4.addWidget(appt_frame)

        print(f"Number of frames added to the doc layout: {len(list(reversed(visible_doctors))[:5])}")

        self.widget.setLayout(self.verticalLayout_4)
        self.verticalLayout_4.setAlignment(Qt.AlignTop)
        self.verticalLayout_4.update()
        self.widget.update()
        
        
         # Debug: Final update status
        print("Layout and widget updated.")


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
        self.fetch_doc_data()



         
                
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWin = CA_homepageWidget()
    mainWin.showMaximized()
    sys.exit(app.exec_())