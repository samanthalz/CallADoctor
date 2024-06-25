from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QBitmap)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from connection import db
from datetime import date

class Doc_HomeWidget(QWidget):
    patients_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.user_id = 0
        self.num_upcoming_appt, self.upcoming_appt_info = 0, 0
        self.setupUi(self)
        #self.set_user_id("doctor1") # for testing, call direct in init
    
    def set_user_id(self, user_id): 
        self.user_id = user_id
        # Assign values after doctor_id is initialized
        self.num_upcoming_appt, self.upcoming_appt_info = self.get_upcoming_appt_data()
        self.get_todays_appt(self.upcoming_appt_info)
        self.num_appt_number_label.setText(QCoreApplication.translate("Form", str(self.num_upcoming_appt), None))

    def create_appointments_frame(self, patient_name, toa, appt_date, time):
        self.patientAppt_frame = QFrame(self.upcoming_appt_frame)
        self.patientAppt_frame.setObjectName(u"patientAppt_frame")
        self.patientAppt_frame.setFixedHeight(81)  # Set the fixed height of the frame
        self.patientAppt_frame.setFrameShape(QFrame.StyledPanel)
        self.patientAppt_frame.setFrameShadow(QFrame.Raised)

        self.patient_name_label = QLabel(self.patientAppt_frame)
        self.patient_name_label.setObjectName(u"patient_name_label")
        self.patient_name_label.setGeometry(QRect(90, 10, 121, 21))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)
        self.patient_name_label.setFont(font3)
        self.patient_name_label.setStyleSheet(u"border : none;\n")
        self.patient_name_label.setText(patient_name)

        self.patient_logo_label = QLabel(self.patientAppt_frame)
        self.patient_logo_label.setObjectName(u"patient_logo_label")
        self.patient_logo_label.setGeometry(QRect(10, 10, 54, 54))
        self.patient_logo_label.setStyleSheet(u"background-color: #B6D0E2; border-radius: 25px; /* Radius to make it round */\n")
        self.patient_logo_label.setAlignment(Qt.AlignCenter)
        # if patient_logo:
        #         pixmap = QPixmap(patient_logo) # patient_logo is the image path
        #         pixmap = pixmap.scaled(self.patient_logo_label.size()) #, Qt.KeepAspectRatio, Qt.SmoothTransformation
        # # Create a mask to make the QLabel circular
        # mask = QBitmap(pixmap.mask())
        # self.patient_logo_label.setMask(mask)
        #self.patient_logo_label.setPixmap(pixmap)

        self.toa_label = QLabel(self.patientAppt_frame)
        self.toa_label.setObjectName(u"toa_label")
        self.toa_label.setGeometry(QRect(90, 30, 161, 21))
        self.toa_label.setFont(font3)
        self.toa_label.setStyleSheet(u"border : none;\n""color : #6ea0c4;\n")
        self.toa_label.setText(toa)

        self.date_time_frame = QFrame(self.patientAppt_frame)
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

        return self.patientAppt_frame

    

    def get_upcoming_appt_data(self):
        appointment_data = db.child("appointment").get().val()
        patient_data = db.child("patients").get().val()
        num_upcoming_appt = 0 # Initialize as 0
        upcoming_appt_info = []
        upcoming_appt_frames = []
        past_appt_frames = []
        today = date.today()
        current_date = today.strftime("%y%m%d")
        if appointment_data: 
            for appt_id, appt_info in appointment_data.items():
                if appt_info.get('doctor_id') == self.user_id:
                    patient_ic = appt_info['patient_id']
                    for i, patient_info in patient_data.items():
                        if int(patient_info.get("patient_ic")) == int(patient_ic):
                             patient_name = patient_info.get('patient_name')
                             break

                    toa = appt_info['speciality']
                    appt_date = appt_info['date']
                    appt_date = self.translate_date(appt_date)
                    time = appt_info['time']

                    if  int(appt_info.get('date')) >= int(current_date): # upcoming appointments
                        num_upcoming_appt += 1
                        upcoming_appt_info.append(appt_info)
                        #Create a frame for each appointment
                        appt_frame = self.create_appointments_frame(patient_name, toa, appt_date, time)
                               
                        if appt_frame:
                                upcoming_appt_frames.append(appt_frame)
                
                    elif int(appt_info.get('date')) < int(current_date): # past appointments 
                        appt_frame = self.create_appointments_frame(patient_name, toa, appt_date, time)
                        if appt_frame:
                                past_appt_frames.append(appt_frame)

        # Add visible appointments to the layout
        for appt_frame in upcoming_appt_frames:
                self.verticalLayout_upcomingAppt.addWidget(appt_frame)

        for appt_frame in past_appt_frames:
             self.verticalLayout_pastAppt.addWidget(appt_frame)

        # Refresh the layout after adding all frames
        self.verticalLayout_upcomingAppt.update()
        self.verticalLayout_pastAppt.update()


        return num_upcoming_appt, upcoming_appt_info # appt info is a list of dictionaries
    
    def create_todays_appt_frame(self, patient_name, appt_time):

        self.appt_frame1 = QtWidgets.QFrame(self.schedule_frame)
        self.appt_frame1.setGeometry(QtCore.QRect(0, 50, 481, 71))
        self.appt_frame1.setFixedHeight(71)
        self.appt_frame1.setStyleSheet("border : none;\n"
"border-radius : 0;\n"
"background-color : #FFFFFF;")
        self.appt_frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appt_frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appt_frame1.setObjectName("appt_frame1")
        self.patientName_label = QtWidgets.QLabel(self.appt_frame1)
        self.patientName_label.setGeometry(QtCore.QRect(60, 10, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        self.patientName_label.setFont(font)
        self.patientName_label.setObjectName("patientName_label")
        self.patientName_label.setText(patient_name)
        self.appt_time_label = QtWidgets.QLabel(self.appt_frame1)
        self.appt_time_label.setGeometry(QtCore.QRect(60, 30, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.appt_time_label.setFont(font)
        self.appt_time_label.setStyleSheet("border : none;\n"
"color : #6ea0c4;\n"
"")
        self.appt_time_label.setObjectName("appt_time_label")
        self.appt_time_label.setText(appt_time)

        return self.appt_frame1


    def get_todays_appt(self, upcoming_appt_info):
        patient_data = db.child("patients").get().val()
        today = date.today()
        current_date = today.strftime("%y%m%d")
        appt_frames = []

        for appt in upcoming_appt_info:
            if int(appt['date']) == int(current_date) : # today's date
                #Create a frame for each medication
                patient_id = appt.get('patient_id')
                for i, patient_info in patient_data.items():
                    if int(patient_info.get("patient_ic")) == int(patient_id):
                        patient_name = patient_info.get('patient_name')
                        break
                appt_time = appt['time']
                appt_frame = self.create_todays_appt_frame(patient_name, appt_time)
                if appt_frame:
                    appt_frames.append(appt_frame)
            
        # Add visible appointments to the layout
        for appt_frame in appt_frames:
                self.verticalLayout_schedule.addWidget(appt_frame)

        # Refresh the layout after adding all frames
        self.verticalLayout_schedule.update()
    
    
    def translate_date(self, date_str): # date_str = appt_data['date'] for appt_data in appt_info    ("240620")
        day = date_str[-2:]
        month = date_str[2:4]
        year = '20' + date_str[:2] 

        monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        month = monthList[int(month) - 1]

        date_str = day + " " + month + " " + year

        return date_str # returns in format 20 Jun 2024 (used for display)


    def setupUi(self, Form):
        Form.setObjectName("Form")
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
"border-top-left-radius: 30px;")

        
        self.user_frame = QtWidgets.QFrame(self.background)
        self.user_frame.setGeometry(QtCore.QRect(1480, 30, 251, 80))
        self.user_frame.setStyleSheet("border-radius: 20px; border: 2px solid #808080")
        self.user_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_frame.setObjectName("user_frame")
        self.profile_icon = QtWidgets.QLabel(self.user_frame)
        self.profile_icon.setGeometry(QtCore.QRect(10, 10, 60, 60))
        self.profile_icon.setStyleSheet("border: none")
        self.profile_icon.setText("")
        self.profile_icon.setPixmap(QtGui.QPixmap("CAD/Images/icon/profile_icon.png"))
        self.profile_icon.setScaledContents(True)
        self.profile_icon.setObjectName("profile_icon")
        self.profile_btn = QtWidgets.QPushButton(self.user_frame)
        self.profile_btn.setGeometry(QtCore.QRect(100, 25, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet("border: none")
        self.profile_btn.setObjectName("profile_btn")
        self.num_appt_frame = QtWidgets.QFrame(self.background)
        self.num_appt_frame.setGeometry(QtCore.QRect(40, 120, 1000, 230))
        self.num_appt_frame.setStyleSheet("border-radius: 10px;\n"
"    background-color: #B6D0E2;\n"
"    background-image: qlineargradient(\n"
"        spread: pad, \n"
"        x1: 0, y1: 0, \n"
"        x2: 0, y2: 1, \n"
"        stop: 0 #B6D0E2, \n"
"        stop: 1 #FFFFFF\n"
"    );")
        
        self.num_appt_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.num_appt_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.num_appt_frame.setObjectName("num_appt_frame")
        self.num_upcoming_appt_label = QtWidgets.QLabel(self.num_appt_frame)
        self.num_upcoming_appt_label.setGeometry(QtCore.QRect(20, 20, 951, 61))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(22)
        self.num_upcoming_appt_label.setFont(font)
        self.num_upcoming_appt_label.setWordWrap(True)
        self.num_upcoming_appt_label.setObjectName("num_upcoming_appt_label")
        self.num_appt_number_label = QtWidgets.QLabel(self.num_appt_frame)
        self.num_appt_number_label.setGeometry(QtCore.QRect(30, 100, 51, 71))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(48)
        self.num_appt_number_label.setFont(font)
        self.num_appt_number_label.setObjectName("num_appt_number_label")
        self.appointment_frame = QtWidgets.QFrame(self.background)
        self.appointment_frame.setGeometry(QtCore.QRect(40, 390, 1000, 600))
        self.appointment_frame.setStyleSheet("border: 2px solid #F8F8F8;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.appointment_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appointment_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appointment_frame.setLineWidth(6)
        self.appointment_frame.setObjectName("appointment_frame")
        
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


        self.upcoming_label = QtWidgets.QLabel(self.appointment_frame)
        self.upcoming_label.setGeometry(QtCore.QRect(40, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        self.upcoming_label.setFont(font)
        self.upcoming_label.setStyleSheet("border : none;\n""")
        self.upcoming_label.setObjectName("upcoming_label")
       
        self.past_label = QtWidgets.QLabel(self.appointment_frame)
        self.past_label.setGeometry(QtCore.QRect(500, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        self.past_label.setFont(font)
        self.past_label.setStyleSheet("border : none;\n""")
        self.past_label.setObjectName("past_label")
        
        
        self.schedule_frame = QtWidgets.QFrame(self.background)
        self.schedule_frame.setGeometry(QtCore.QRect(1170, 140, 481, 831))
        self.schedule_frame.setStyleSheet("border: 2px solid #FFFFFF;\n"
"border-radius: 10px;")
        self.schedule_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        # Create a vertical layout and set it to the frame
        self.verticalLayout_schedule = QVBoxLayout(self.schedule_frame)
        self.schedule_frame.setLayout(self.verticalLayout_schedule)
        self.schedule_frame.setObjectName("schedule_frame")
        self.todays_schedule_label = QtWidgets.QLabel(self.schedule_frame)
        self.todays_schedule_label.setGeometry(QtCore.QRect(20, 10, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        self.todays_schedule_label.setFont(font)
        self.todays_schedule_label.setStyleSheet("border : none;\n"
"")
        self.todays_schedule_label.setObjectName("todays_schedule_label")
        

        
        # Nav frame & Layout 
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.navigation_layout = QtWidgets.QWidget(self.frame)
        self.navigation_layout.setGeometry(QtCore.QRect(31, 20, 87, 851))
        self.navigation_layout.setObjectName("navigation_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.navigation_layout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Navigation buttons : 
        self.home_navigation = QtWidgets.QToolButton(self.navigation_layout)
        self.home_navigation.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        self.home_navigation.setMinimumSize(QtCore.QSize(85, 96))
        self.home_navigation.setMaximumSize(QtCore.QSize(85, 96))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_navigation.setFont(font)
        self.home_navigation.setStyleSheet("border: none; \n"
"color: white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("CAD/Images/nav_images/home_page_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QtCore.QSize(70, 70))
        self.home_navigation.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.home_navigation.setObjectName("home_navigation")
        self.home_navigation.clicked.connect(self.emitHomeBtn)
        self.verticalLayout.addWidget(self.home_navigation)

        self.patients_navigation = QtWidgets.QToolButton(self.navigation_layout)
        self.patients_navigation.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patients_navigation.sizePolicy().hasHeightForWidth())
        self.patients_navigation.setSizePolicy(sizePolicy)
        self.patients_navigation.setMinimumSize(QtCore.QSize(85, 96))
        self.patients_navigation.setMaximumSize(QtCore.QSize(85, 96))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.patients_navigation.setFont(font)
        self.patients_navigation.setStyleSheet("border: none; \n"
"color: white;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("CAD/Images/nav_images/services_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.patients_navigation.setIcon(icon3)
        self.patients_navigation.setIconSize(QtCore.QSize(70, 70))
        self.patients_navigation.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.patients_navigation.setObjectName("patients_navigation")
        self.patients_navigation.clicked.connect(self.emitPatientsBtn)
        self.verticalLayout.addWidget(self.patients_navigation)
        self.settings_navigation = QtWidgets.QToolButton(self.navigation_layout)
        self.settings_navigation.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setMinimumSize(QtCore.QSize(85, 96))
        self.settings_navigation.setMaximumSize(QtCore.QSize(85, 96))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.settings_navigation.setFont(font)
        self.settings_navigation.setStyleSheet("border: none; \n"
"color: white;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("CAD/Images/nav_images/settings_page_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QtCore.QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.settings_navigation.setObjectName("settings_navigation")
        self.settings_navigation.clicked.connect(self.emitProfileBtn)
        self.verticalLayout.addWidget(self.settings_navigation)
        self.logout_navigation = QtWidgets.QToolButton(self.navigation_layout)
        self.logout_navigation.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setMinimumSize(QtCore.QSize(85, 96))
        self.logout_navigation.setMaximumSize(QtCore.QSize(85, 96))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logout_navigation.setFont(font)
        self.logout_navigation.setStyleSheet("border: none; \n"
"color: white;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("CAD/Images/nav_images/logout_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QtCore.QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.logout_navigation.setObjectName("logout_navigation")
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)
        self.verticalLayout.addWidget(self.logout_navigation)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.profile_btn.setText(_translate("Form", "Doctor"))
        self.num_upcoming_appt_label.setText(_translate("Form", "Number of upcoming appointments :"))
        self.num_appt_number_label.setText(_translate("Form", "0"))

        self.upcoming_label.setText(_translate("Form", "Upcoming"))
        self.past_label.setText(_translate("Form", "Past"))
        self.todays_schedule_label.setText(_translate("Form", "Today\'s Schedule"))
        
        
        
        self.home_navigation.setText(_translate("Form", "   Home   "))
        #self.schedule_navigation.setText(_translate("Form", "Schedule"))
        self.patients_navigation.setText(_translate("Form", "Patients"))
        self.settings_navigation.setText(_translate("Form", "Settings"))
        self.logout_navigation.setText(_translate("Form", "Logout"))

    @pyqtSlot()
    def emitHomeBtn(self):
        # Emit the custom signal
        self.home_btn_clicked.emit()     

    @pyqtSlot()
    def emitPatientsBtn(self):
        # Emit the custom signal
        self.patients_btn_clicked.emit()
        
    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
        
        
    @pyqtSlot()
    def emitProfileBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()


# # If run directly from this page
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Doc_HomeWidget()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
