from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QBitmap)
from PyQt5.QtWidgets import *


from connection import db
from datetime import date


class HomeWidget(QWidget):
    service_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    appt_btn_clicked = pyqtSignal()
        
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user_id = 0
        self.num_upcoming_appt, self.upcoming_appt_info = 0, 0
        self.setupUi(self)

    def create_active_pres_frame(self, medicine):

        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)

        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(11)

        self.prescription_frame = QFrame(self.active_pres_frame)
        self.prescription_frame.setObjectName(u"prescription_frame")
        self.prescription_frame.setGeometry(QRect(0, 50, 481, 71))
        self.prescription_frame.setFixedHeight(71)  # Set the fixed height of the frame
        self.prescription_frame.setStyleSheet(u"border : none;\n""border-radius : 0;\n""background-color : #FFFFFF;")
        self.prescription_frame.setFrameShape(QFrame.StyledPanel)
        self.prescription_frame.setFrameShadow(QFrame.Raised)
        self.medicineName_label = QLabel(self.prescription_frame)
        self.medicineName_label.setObjectName(u"medicineName_label")
        self.medicineName_label.setGeometry(QRect(60, 10, 241, 16))
        self.medicineName_label.setFont(font2)
        self.medicineName_label.setText(medicine)
        self.medicine_quantity_label = QLabel(self.prescription_frame)
        self.medicine_quantity_label.setObjectName(u"medicine_quantity_label")
        self.medicine_quantity_label.setGeometry(QRect(60, 30, 161, 21))
        self.medicine_quantity_label.setFont(font3)
        self.medicine_quantity_label.setStyleSheet(u"border : none;\n""color : #6ea0c4;\n""")
        self.medicine_quantity_label.setText("Quantity") # Placeholder

        return self.prescription_frame


    def get_medical_records(self):
        db = self.initialize_db()
        medical_records = db.child("medical_records").get().val()
        today = date.today()
        current_date = today.strftime("%y%m%d")
        active_medication_list = []
        medicine_frames = []
        if medical_records: 
            for record_id, record_info in enumerate(medical_records):
                if int(record_info.get('patient_id')) == int(self.user_id):
                     if  int(record_info.get('end_date')) >= int(current_date): 
                          for medicine in record_info.get('medicine'):
                                active_medication_list.append(medicine)
            
            for medicine in active_medication_list:
                #Create a frame for each medication
                medicine_frame = self.create_active_pres_frame(medicine)
                if medicine_frame:
                    medicine_frames.append(medicine_frame)
            
        # Add visible appointments to the layout
        for medicine_frame in medicine_frames:
                self.verticalLayout_activePres.addWidget(medicine_frame)

        # Refresh the layout after adding all frames
        self.verticalLayout_activePres.update()
                     

    def create_appointments_frame(self, clinic_name, clinic_logo, toa, appt_date, time, position):
        self.clinicAppt_frame = QFrame(self.upcoming_appt_frame)
        self.clinicAppt_frame.setObjectName(u"clinicAppt_frame")
        self.clinicAppt_frame.setFixedHeight(81)  # Set the fixed height of the frame
        self.clinicAppt_frame.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame.setFrameShadow(QFrame.Raised)

        self.clinic_name_label = QLabel(self.clinicAppt_frame)
        self.clinic_name_label.setObjectName(u"clinic_name_label")
        self.clinic_name_label.setGeometry(QRect(90, 10, 121, 21))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)
        self.clinic_name_label.setFont(font3)
        self.clinic_name_label.setStyleSheet(u"border : none;\n")
        self.clinic_name_label.setText(clinic_name)

        self.clinic_logo_label = QLabel(self.clinicAppt_frame)
        self.clinic_logo_label.setObjectName(u"clinic_logo_label")
        self.clinic_logo_label.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label.setStyleSheet(u"background-color: #B6D0E2; border-radius: 25px; /* Radius to make it round */\n")
        self.clinic_logo_label.setAlignment(Qt.AlignCenter)
        if clinic_logo:
                pixmap = QPixmap(clinic_logo) # clinic_logo is the image path
                pixmap = pixmap.scaled(self.clinic_logo_label.size()) #, Qt.KeepAspectRatio, Qt.SmoothTransformation
        # # Create a mask to make the QLabel circular
        # mask = QBitmap(pixmap.mask())
        # self.clinic_logo_label.setMask(mask)
        self.clinic_logo_label.setPixmap(pixmap)

        self.toa_label = QLabel(self.clinicAppt_frame)
        self.toa_label.setObjectName(u"toa_label")
        self.toa_label.setGeometry(QRect(90, 30, 161, 21))
        self.toa_label.setFont(font3)
        self.toa_label.setStyleSheet(u"border : none;\n""color : #6ea0c4;\n")
        self.toa_label.setText(toa)

        self.date_time_frame = QFrame(self.clinicAppt_frame)
        self.date_time_frame.setObjectName(u"date_time_frame")
        self.date_time_frame.setGeometry(QRect(280, 20, 100, 41))
        self.date_time_frame.setStyleSheet(u"border-radius: 10px;\n""background-color: #dbe7f0;")
        self.date_time_frame.setFrameShape(QFrame.StyledPanel)
        self.date_time_frame.setFrameShadow(QFrame.Raised)

        self.date_label = QLabel(self.date_time_frame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(10, 0, 80, 13))
        font5 = QFont()
        font5.setFamily(u"Cascadia Code")
        self.date_label.setFont(font5)
        self.date_label.setStyleSheet(u"border : none;\n")
        self.date_label.setText(appt_date)

        self.time_label = QLabel(self.date_time_frame)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(10, 20, 80, 13))
        self.time_label.setFont(font5)
        self.time_label.setStyleSheet(u"border : none;\n")
        self.time_label.setText(time)

        return self.clinicAppt_frame

    

    def get_upcoming_appt_data(self):
        db = self.initialize_db()
        appointment_data = db.child("appointment").get().val()
        clinics = db.child("clinic").get().val()
        num_upcoming_appt = 0 # Initialize as 0
        upcoming_appt_info = []
        upcoming_appt_frames = []
        past_appt_frames = []
        today = date.today()
        current_date = today.strftime("%y%m%d")
        if appointment_data: 
            for appt_id, appt_info in appointment_data.items():
                if int(appt_info.get('patient_id')) == int(self.user_id):
                    clinic_id = appt_info['clinic_id']
                    print(f'Clinic_id {clinic_id}')
                    for i, clinic in clinics.items():
                        print(f"In for clinic {i} in clinics ")
                        if i == clinic_id:
                             clinic_logo = clinic.get("clinic_img") # image path
                             clinic_name = clinic.get("clinic_name")
                             print(f"clinic_logo{clinic_logo}")
                             break
                    if not clinic_logo:
                         clinic_logo = "CAD/Images/clinic_img/clinic_1.png"
                    toa = appt_info['speciality']
                    appt_date = appt_info['date']
                    appt_date = self.translate_date(appt_date)
                    time = appt_info['time']

                    if  int(appt_info.get('date')) >= int(current_date): # upcoming appointments
                        num_upcoming_appt += 1
                        upcoming_appt_info.append(appt_info)
                        #Create a frame for each appointment
                        appt_frame = self.create_appointments_frame(clinic_name, clinic_logo, toa, appt_date, time, num_upcoming_appt)
                               
                        if appt_frame:
                                upcoming_appt_frames.append(appt_frame)
                
                    elif int(appt_info.get('date')) < int(current_date): # past appointments 
                        appt_frame = self.create_appointments_frame(clinic_name, clinic_logo, toa, appt_date, time, num_upcoming_appt)
                        if appt_frame:
                                past_appt_frames.append(appt_frame)

        # Add visible appointments to the layout
        for appt_frame in upcoming_appt_frames:
                self.verticalLayout_upcomingAppt.addWidget(appt_frame)

        for appt_frame in past_appt_frames:
             self.verticalLayout_pastAppt.addWidget(appt_frame)

        # Refresh the layout after adding all frames
        self.verticalLayout_upcomingAppt.update()


        return num_upcoming_appt, upcoming_appt_info # appt info is a list of dictionaries
    
    
    def translate_date(self, date_str): # date_str = appt_data['date'] for appt_data in appt_info    ("240620")
        day = date_str[-2:]
        month = date_str[2:4]
        year = '20' + date_str[:2] 

        monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        month = monthList[int(month) - 1]

        date_str = day + " " + month + " " + year

        return date_str # returns in format 20 Jun 2024 (used for display)
    

    def set_user_id(self, user_id): 
        self.user_id = user_id
        # Assign values after user_id is initialized
        self.num_upcoming_appt, self.upcoming_appt_info = self.get_upcoming_appt_data()
        self.get_medical_records()
        self.num_appt_number_label.setText(QCoreApplication.translate("Form", str(self.num_upcoming_appt), None))
        
        

    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)

        font7 = QFont()
        font7.setFamily(u"Source Sans Pro Semibold")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)

        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(16)

        font5 = QFont()
        font5.setFamily(u"Cascadia Code")

        font4 = QFont()
        font4.setFamily(u"Cascadia Code")
        font4.setPointSize(9)

        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)

        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(11)

        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(48)

        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(22)

        Form.setAutoFillBackground(True)
        p = Form.palette()
        p.setColor(Form.backgroundRole(), QColor('#B6D0E2'))
        Form.setPalette(p)
        self.background = QWidget(Form)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(150, 0, 1771, 1061))
        self.background.setStyleSheet(u"background-color: #F8F8F8;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-left-radius: 30px;")
        self.num_appt_frame = QFrame(self.background)
        self.num_appt_frame.setObjectName(u"num_appt_frame")
        self.num_appt_frame.setGeometry(QRect(50, 140, 1000, 230))
        self.num_appt_frame.setStyleSheet(u"border-radius: 10px;\n"
"    background-color: #B6D0E2;\n"
"    background-image: qlineargradient(\n"
"        spread: pad, \n"
"        x1: 0, y1: 0, \n"
"        x2: 0, y2: 1, \n"
"        stop: 0 #B6D0E2, \n"
"        stop: 1 #FFFFFF\n"
"    );")
        self.num_appt_frame.setFrameShape(QFrame.StyledPanel)
        self.num_appt_frame.setFrameShadow(QFrame.Raised)
        self.num_upcoming_appt_label = QLabel(self.num_appt_frame)
        self.num_upcoming_appt_label.setObjectName(u"num_upcoming_appt_label")
        self.num_upcoming_appt_label.setGeometry(QRect(20, 20, 951, 61))
        
        self.num_upcoming_appt_label.setFont(font)
        self.num_upcoming_appt_label.setWordWrap(True)
        self.num_appt_number_label = QLabel(self.num_appt_frame)
        self.num_appt_number_label.setObjectName(u"num_appt_number_label")
        self.num_appt_number_label.setGeometry(QRect(30, 100, 51, 71))
        
        self.num_appt_number_label.setFont(font1)
        self.appointment_frame = QFrame(self.background)
        self.appointment_frame.setObjectName(u"appointment_frame")
        self.appointment_frame.setGeometry(QRect(50, 410, 1000, 600))
        self.appointment_frame.setStyleSheet(u"border: 2px solid #F8F8F8;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.appointment_frame.setFrameShape(QFrame.StyledPanel)
        self.appointment_frame.setFrameShadow(QFrame.Raised)
        self.appointment_frame.setLineWidth(6)


        # Upcoming Appointments Frame
        self.upcoming_appt_frame = QFrame(self.appointment_frame)
        self.upcoming_appt_frame.setObjectName(u"upcoming_appt_frame")
        self.upcoming_appt_frame.setGeometry(QRect(30, 30, 450, 531))
        self.upcoming_appt_frame.setStyleSheet(u"background-color : #ffffff;")
        self.upcoming_appt_frame.setFrameShape(QFrame.StyledPanel)
        self.upcoming_appt_frame.setFrameShadow(QFrame.Raised)

        # Create a vertical layout and set it to the frame
        self.verticalLayout_upcomingAppt = QVBoxLayout(self.upcoming_appt_frame)
        self.verticalLayout_upcomingAppt.setContentsMargins(0, 0, 0, 0)  # Set the margins to zero
        self.verticalLayout_upcomingAppt.setSpacing(10)  # Set spacing between items

        # Create the upcoming label
        self.upcoming_label = QLabel(self.upcoming_appt_frame)
        self.upcoming_label.setObjectName(u"upcoming_label")
        self.upcoming_label.setFixedHeight(41)  # Set the fixed height of the frame
        self.upcoming_label.setGeometry(QRect(30, 20, 101, 41))  #(QtCore.QRect(30, 20, 101, 41))
        self.upcoming_label.setFont(font2)
        self.upcoming_label.setStyleSheet(u"border : none;")


        # Past Appointments Frame
        self.past_appt_frame = QFrame(self.appointment_frame)
        self.past_appt_frame.setObjectName(u"past_appt_frame")
        self.past_appt_frame.setGeometry(QRect(510, 30, 450, 531))
        self.past_appt_frame.setStyleSheet(u"background-color : #ffffff;")
        self.past_appt_frame.setFrameShape(QFrame.StyledPanel)
        self.past_appt_frame.setFrameShadow(QFrame.Raised)

        # Create a vertical layout and set it to the frame
        self.verticalLayout_pastAppt = QVBoxLayout(self.past_appt_frame)
        self.verticalLayout_pastAppt.setContentsMargins(0, 0, 0, 0)  # Set the margins to zero
        self.verticalLayout_pastAppt.setSpacing(10)  # Set spacing between items

        self.past_label = QLabel(self.past_appt_frame)
        self.past_label.setObjectName(u"past_label")
        self.past_label.setFixedHeight(41)  # Set the fixed height of the frame
        self.past_label.setGeometry(QRect(30, 20, 101, 41))
        self.past_label.setFont(font2)
        self.past_label.setStyleSheet(u"border : none;")
        


         # Active Prescriptions outer frame : 
        self.active_pres_frame = QFrame(self.background)
        self.active_pres_frame.setObjectName(u"active_pres_frame")
        self.active_pres_frame.setGeometry(QRect(1120, 170, 481, 831))
        self.active_pres_frame.setStyleSheet(u"border: 2px solid #FFFFFF;\n""border-radius: 10px;")
        self.active_pres_frame.setFrameShape(QFrame.StyledPanel)
        self.active_pres_frame.setFrameShadow(QFrame.Raised)
        # Create a vertical layout and set it to the frame
        self.verticalLayout_activePres = QVBoxLayout(self.active_pres_frame)
        self.active_pres_frame.setLayout(self.verticalLayout_activePres)
        self.active_pres_label = QLabel(self.active_pres_frame)
        self.active_pres_label.setObjectName(u"active_pres_label")
        self.active_pres_label.setGeometry(QRect(20, 10, 451, 41))
        self.active_pres_label.setFont(font2)
        self.active_pres_label.setStyleSheet(u"border : none;\n""")
        
        #############################################################################################33
        # Prescription repeat : 
        # self.prescription_frame = QFrame(self.active_pres_frame)
        # self.prescription_frame.setObjectName(u"prescription_frame")
        # self.prescription_frame.setGeometry(QRect(0, 50, 481, 71))
        # self.prescription_frame.setStyleSheet(u"border : none;\n""border-radius : 0;\n""background-color : #FFFFFF;")
        # self.prescription_frame.setFrameShape(QFrame.StyledPanel)
        # self.prescription_frame.setFrameShadow(QFrame.Raised)
        # self.medicineName_label = QLabel(self.prescription_frame)
        # self.medicineName_label.setObjectName(u"medicineName_label")
        # self.medicineName_label.setGeometry(QRect(60, 10, 241, 16))
        # self.medicineName_label.setFont(font2)
        # self.medicine_quantity_label = QLabel(self.prescription_frame)
        # self.medicine_quantity_label.setObjectName(u"medicine_quantity_label")
        # self.medicine_quantity_label.setGeometry(QRect(60, 30, 161, 21))
        # self.medicine_quantity_label.setFont(font3)
        # self.medicine_quantity_label.setStyleSheet(u"border : none;\n""color : #6ea0c4;\n""")
        ##########################################################################################################
        
        # Notification, profile, nav bar
        
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
        self.profile_btn.setGeometry(QRect(120, 25, 71, 31))
        
        self.profile_btn.setFont(font6)
        self.profile_btn.setStyleSheet(u"border: none")
        self.profile_btn.clicked.connect(self.emitProfileBtn)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 19, 87, 871))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_navigation = QToolButton(self.widget)
        self.home_navigation.setObjectName(u"home_navigation")
        self.home_navigation.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        self.home_navigation.setMinimumSize(QSize(85, 96))
        self.home_navigation.setMaximumSize(QSize(85, 96))
        
        self.home_navigation.setFont(font7)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.home_navigation)

        self.appointments_navigation = QToolButton(self.widget)
        self.appointments_navigation.setObjectName(u"appointments_navigation")
        self.appointments_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.appointments_navigation.sizePolicy().hasHeightForWidth())
        self.appointments_navigation.setSizePolicy(sizePolicy)
        self.appointments_navigation.setFont(font7)
        self.appointments_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/appointment_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appointments_navigation.setIcon(icon2)
        self.appointments_navigation.setIconSize(QSize(70, 70))
        self.appointments_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.appointments_navigation.clicked.connect(self.emitApptBtn)
        self.verticalLayout.addWidget(self.appointments_navigation)

        self.services_navigation = QToolButton(self.widget)
        self.services_navigation.setObjectName(u"services_navigation")
        self.services_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.services_navigation.sizePolicy().hasHeightForWidth())
        self.services_navigation.setSizePolicy(sizePolicy)
        self.services_navigation.setFont(font7)
        self.services_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_navigation.setIcon(icon3)
        self.services_navigation.setIconSize(QSize(70, 70))
        self.services_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.services_navigation.clicked.connect(self.emitServiceBtn)

        self.verticalLayout.addWidget(self.services_navigation)

        self.settings_navigation = QToolButton(self.widget)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setFont(font7)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settings_navigation.clicked.connect(self.emitProfileBtn)
        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.widget)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setFont(font7)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon5 = QIcon()
        icon5.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)
        
        self.verticalLayout.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

        # nav bar, profile, noti
        
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Services", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))

        # Fixed : 
        self.num_upcoming_appt_label.setText(QCoreApplication.translate("Form", u"Number of upcoming appointments :", None))
        self.num_appt_number_label.setText(QCoreApplication.translate("Form", str(self.num_upcoming_appt), None))
        self.upcoming_label.setText(QCoreApplication.translate("Form", u"Upcoming", None))
        self.past_label.setText(QCoreApplication.translate("Form", u"Past", None))
        self.active_pres_label.setText(QCoreApplication.translate("Form", u"Active Prescriptions", None))

        # Variables (active prescriptions) : 
        # self.medicineName_label.setText(QCoreApplication.translate("Form", u"Medicine Name", None))
        # self.medicine_quantity_label.setText(QCoreApplication.translate("Form", u"Quantity", None))


    # retranslateUi

    @pyqtSlot()
    def emitServiceBtn(self):
        # Emit the custom signal
        self.service_btn_clicked.emit()
        
    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
        
        
    @pyqtSlot()
    def emitProfileBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()
        
    @pyqtSlot()
    def emitApptBtn(self):
        # Emit the custom signal
        self.appt_btn_clicked.emit()

    def initialize_db(self):
        return db 
    



        