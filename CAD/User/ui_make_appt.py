from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QTextCharFormat)
from PyQt5.QtWidgets import *
from datetime import datetime, timedelta
import re
from connection import db

class CustomCalendarWidget(QCalendarWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set the minimum and maximum selectable dates
        self.tomorrow = QDate.currentDate().addDays(1)
        self.setMinimumDate(self.tomorrow)
        self.setMaximumDate(self.tomorrow.addMonths(6))
        self.custom_font = QFont("Consolas", 11)
        self.selected_date = None

        # Disable dates before tomorrow
        self.disablePastDates()

    def disablePastDates(self):
        format = QTextCharFormat()
        format.setForeground(QColor(Qt.gray))
        date = self.minimumDate().addDays(-1)  # Start from the day before minimum date
        while date >= self.minimumDate().addMonths(-6):
            self.setDateTextFormat(date, format)
            date = date.addDays(-1)

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)

        # Set custom font
        painter.setFont(self.custom_font)

        # # Highlight the selected date
        # if self.selected_date == date:
        #     painter.save()
        #     painter.setBrush(QColor(200, 200, 255, 150))  # Light blue background
        #     painter.drawRect(rect)
        #     painter.restore()

    def mousePressEvent(self, event):
        clicked_date = self.clickedDate(event.pos())
        if clicked_date:
            if self.isDateEnabled(clicked_date):
                self.selected_date = clicked_date
                self.updateCells()
            else:
                print("Selected date is disabled.")

    def clickedDate(self, pos):
        cell_width = self.width() / 7  # Assuming a 7-column calendar layout
        cell_height = self.height() / 6  # Assuming a 6-row calendar layout
        row = int(pos.y() // cell_height)
        col = int(pos.x() // cell_width)

        if 0 <= row < 6 and 0 <= col < 7:
                date = self.minimumDate().addDays(row * 7 + col)
                return date

        return None




    def isDateEnabled(self, date):
        return self.minimumDate() <= date <= self.maximumDate()

class MakeApptWidget(QWidget):
    service_btn_clicked = pyqtSignal()
    cancel_btn_clicked = pyqtSignal()
    redirect_appt = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    schedule_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    

    def __init__(self, parent=None):
        super().__init__(parent)
        self.user_id = 0
        self.clinic_data_list = []
        self.setupUi(self)
        self.fetch_clinic_data()
        
    
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
        self.fad_title.setGeometry(QRect(60, 40, 481, 81))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.fad_title.setFont(font)
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
        
        self.label = QLabel(self.whitebg)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(690, 190, 591, 41))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        
        self.calendarWidget = CustomCalendarWidget(self.whitebg)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(690, 250, 1021, 631))
        self.calendarWidget.setStyleSheet(u"color: black; ")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)
        
        self.cancel_btn = QPushButton(self.whitebg)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(950, 940, 321, 50))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        self.cancel_btn.setFont(font3)
        self.cancel_btn.setStyleSheet(u"background-color: \"#D3D3D3\"; border-radius: 10px;")
        self.cancel_btn.clicked.connect(self.emitCancelBtn)
        
        self.makeapt_btn = QPushButton(self.whitebg)
        self.makeapt_btn.setObjectName(u"makeapt_btn")
        self.makeapt_btn.setGeometry(QRect(1360, 940, 321, 50))
        self.makeapt_btn.setFont(font3)
        self.makeapt_btn.setStyleSheet(u"background-color: \"#B6D0E2\"; border-radius: 10px;")
        self.makeapt_btn.clicked.connect(self.save_appointment_to_db)
        
        self.layoutWidget = QWidget(self.whitebg)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(54, 146, 521, 871))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.clinic_layout = QVBoxLayout()
        self.clinic_layout.setObjectName(u"clinic_layout")
        self.clinic_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.clinic_label = QLabel(self.layoutWidget)
        self.clinic_label.setObjectName(u"clinic_label")
        self.clinic_label.setMinimumSize(QSize(210, 32))
        self.clinic_label.setMaximumSize(QSize(210, 32))
        self.clinic_label.setFont(font2)

        self.clinic_layout.addWidget(self.clinic_label)

        self.clinic_dropdown = QComboBox(self.layoutWidget)
        self.clinic_dropdown.setObjectName(u"clinic_dropdown")
        self.clinic_dropdown.setMinimumSize(QSize(321, 41))
        self.clinic_dropdown.setMaximumSize(QSize(321, 41))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(11)
        self.clinic_dropdown.setFont(font4)
        self.clinic_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
        "border-radius: 5px; \n"
        "background-color: #FFFFFF; \n"
        "padding: 10px; \n"
        "font-family: Consolas;\n"
        "font-size: 11pt;")
        self.clinic_dropdown.setEditable(False)
        self.clinic_dropdown.setIconSize(QSize(50, 50))
        self.clinic_dropdown.setFrame(True)

        self.clinic_layout.addWidget(self.clinic_dropdown)
        
        self.load_clinics()
        self.clinic_dropdown.currentIndexChanged.connect(self.load_doctors)
        self.clinic_dropdown.currentIndexChanged.connect(self.load_time_slots)
        

        self.verticalLayout.addLayout(self.clinic_layout)

        self.doc_layout = QVBoxLayout()
        self.doc_layout.setObjectName(u"doc_layout")
        self.doc_label = QLabel(self.layoutWidget)
        self.doc_label.setObjectName(u"doc_label")
        self.doc_label.setMaximumSize(QSize(321, 32))
        self.doc_label.setFont(font2)

        self.doc_layout.addWidget(self.doc_label)

        self.doc_dropdown = QComboBox(self.layoutWidget)
        self.doc_dropdown.setObjectName(u"doc_dropdown")
        self.doc_dropdown.setMinimumSize(QSize(321, 41))
        self.doc_dropdown.setMaximumSize(QSize(321, 41))
        self.doc_dropdown.setFont(font4)
        self.doc_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
        "border-radius: 5px; \n"
        "background-color: #FFFFFF; \n"
        "padding: 10px; \n"
        "font-family: Consolas;\n"
        "font-size: 11pt;")
        self.doc_dropdown.setEditable(False)
        self.doc_dropdown.setIconSize(QSize(50, 50))
        self.doc_dropdown.setFrame(True)
        self.load_doctors()
        self.doc_dropdown.currentIndexChanged.connect(self.load_specialties)
        self.doc_layout.addWidget(self.doc_dropdown)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 40))
        self.checkBox.setIconSize(QSize(50, 50))
        self.checkBox.setText("Allow admin to reassign doctor")
        self.checkBox.setFont(font4)
        
        self.doc_layout.addWidget(self.checkBox)
        
        self.checkBoxLabel = QLabel(self.layoutWidget)
        self.checkBoxLabel.setObjectName(u"checkBoxLabel")
        self.checkBoxLabel.setMinimumSize(QSize(0, 50))
        self.checkBoxLabel.setMaximumSize(QSize(16777215, 50))
        self.checkBoxLabel.setWordWrap(True)
        self.checkBoxLabel.setText("Allow admin to reassign new doctor if chosen doctor is unavailable. If this is not checked, the appointment will be rejected if the chosen doctor is unavailable.")
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(9)
        self.checkBoxLabel.setFont(font3)
        self.doc_layout.addWidget(self.checkBoxLabel)


        self.verticalLayout.addLayout(self.doc_layout)

        self.time_layout = QVBoxLayout()
        self.time_layout.setObjectName(u"time_layout")
        self.time_label = QLabel(self.layoutWidget)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMaximumSize(QSize(321, 32))
        self.time_label.setFont(font2)

        self.time_layout.addWidget(self.time_label)

        self.time_dropdown = QComboBox(self.layoutWidget)
        self.time_dropdown.setObjectName(u"time_dropdown")
        self.time_dropdown.setMinimumSize(QSize(321, 41))
        self.time_dropdown.setMaximumSize(QSize(321, 41))
        self.time_dropdown.setFont(font4)
        self.time_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
        "border-radius: 5px; \n"
        "background-color: #FFFFFF; \n"
        "padding: 10px; \n"
        "font-family: Consolas;\n"
        "font-size: 11pt;")
        self.time_dropdown.setEditable(False)
        self.time_dropdown.setIconSize(QSize(50, 50))
        self.time_dropdown.setFrame(True)

        self.time_layout.addWidget(self.time_dropdown)
        self.load_time_slots()

        self.verticalLayout.addLayout(self.time_layout)

        self.speciality_layout = QVBoxLayout()
        self.speciality_layout.setObjectName(u"speciality_layout")
        self.speciality_label = QLabel(self.layoutWidget)
        self.speciality_label.setObjectName(u"speciality_label")
        self.speciality_label.setMaximumSize(QSize(349, 32))
        self.speciality_label.setFont(font2)

        self.speciality_layout.addWidget(self.speciality_label)

        self.speciality_dropdown = QComboBox(self.layoutWidget)
        self.speciality_dropdown.setObjectName(u"speciality_dropdown")
        self.speciality_dropdown.setMinimumSize(QSize(321, 41))
        self.speciality_dropdown.setMaximumSize(QSize(321, 41))
        self.speciality_dropdown.setFont(font4)
        self.speciality_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
        "border-radius: 5px; \n"
        "background-color: #FFFFFF; \n"
        "padding: 10px; \n"
        "font-family: Consolas;\n"
        "font-size: 11pt;")
        self.speciality_dropdown.setEditable(False)
        self.speciality_dropdown.setIconSize(QSize(50, 50))
        self.speciality_dropdown.setFrame(True)
        self.load_specialties()
        self.speciality_layout.addWidget(self.speciality_dropdown)


        self.verticalLayout.addLayout(self.speciality_layout)

        self.med_layout = QVBoxLayout()
        self.med_layout.setObjectName(u"med_layout")
        self.med_label = QLabel(self.layoutWidget)
        self.med_label.setObjectName(u"med_label")
        self.med_label.setMaximumSize(QSize(405, 32))
        self.med_label.setFont(font2)

        self.med_layout.addWidget(self.med_label)

        self.med_input = QLineEdit(self.layoutWidget)
        self.med_input.setObjectName(u"med_input")
        self.med_input.setMinimumSize(QSize(0, 60))
        self.med_input.setMaximumSize(QSize(16777215, 120))
        self.med_input.setStyleSheet(u"border: 1px solid; border-radius: 0;")
        self.med_input.setPlaceholderText("Type here...")
        self.med_layout.addWidget(self.med_input)


        self.verticalLayout.addLayout(self.med_layout)

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
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
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
        self.appointments_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
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
        self.services_navigation.setStyleSheet(u"border: none; \n""color: white;")
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
        self.settings_navigation.setStyleSheet(u"border: none; \n""color: white;")
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
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
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
        self.fad_title.setText(QCoreApplication.translate("Form", u"Make Appointment", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.label.setText(QCoreApplication.translate("Form", u"Choose a Date*", None))
        self.cancel_btn.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.makeapt_btn.setText(QCoreApplication.translate("Form", u"Make Appointment", None))
        
        self.clinic_label.setText(QCoreApplication.translate("Form", u"Select Clinic*", None))
        self.doc_label.setText(QCoreApplication.translate("Form", u"Select Doctor*", None))
        self.time_label.setText(QCoreApplication.translate("Form", u"Select Time*", None))
        self.speciality_label.setText(QCoreApplication.translate("Form", u"Select Specialities*", None))
        self.med_label.setText(QCoreApplication.translate("Form", u"Medical Concern / Requests*", None))

        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Services", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

    @pyqtSlot()
    def emitServiceBtn(self):
        # Emit the custom signal
        self.service_btn_clicked.emit()
        
    @pyqtSlot()
    def emitCancelBtn(self):
        # Emit the custom signal
        self.cancel_btn_clicked.emit()
        
    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
        
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
        
    def fetch_clinic_data(self):
        try:
            clinics = db.child("clinic").get()
            
            if clinics.each():
                self.clinic_data_list = [clinic.val() for clinic in clinics.each()]
                #print("Fetched Clinics Data:", self.clinic_data_list)  # Debug: Print the fetched data
                #self.populate_clinic_info()
            else:
                print("No clinics data found.")
        except Exception as e:
            print(f"An error occurred while fetching data: {e}")    
            
    def load_clinics(self):
        try:
                clinics_data = db.child("clinic").get()
                clinic_names = [clinic.val().get("clinic_name", "") for clinic in clinics_data.each()]
                clinic_names = sorted(set(clinic_names))  # Sort and remove duplicates
                clinic_names.insert(0, "Search or Select a Clinic")  
                self.clinic_dropdown.addItems(clinic_names)
        except Exception as e:
                print(f"An error occurred while loading clinics: {e}")
                
    def load_doctors(self):
        selected_clinic = self.clinic_dropdown.currentText()

        try:
                doctors_data = db.child("clinic").get()
                doctor_names = []

                for clinic in doctors_data.each():
                        if selected_clinic == "Search or Select a Clinic" or clinic.val().get("clinic_name", "") == selected_clinic:
                                doctors = clinic.val().get("doctors", {})
                                for doctor_id, doctor in doctors.items():
                                        doctor_name = doctor.get("doctor_name", "")
                                        if doctor_name:
                                                doctor_names.append(doctor_name)
                                if selected_clinic != "Search or Select a Clinic":
                                        break  # No need to continue once the selected clinic is found

                # Sort and remove duplicates
                doctor_names = sorted(set(doctor_names))
                doctor_names.insert(0, "Search or Select a Doctor")
                self.doc_dropdown.clear()
                self.doc_dropdown.addItems(doctor_names)
        except Exception as e:
                print(f"An error occurred while loading doctors: {e}")
                
    def load_time_slots(self):
        selected_clinic = self.clinic_dropdown.currentText()

        if selected_clinic == "Search or Select a Clinic":
                self.time_dropdown.clear()
                self.time_dropdown.addItem("Select a Time Slot")
                return

        try:
                clinics_data = db.child("clinic").get()
                clinic_operating_hours = None

                for clinic in clinics_data.each():
                        if clinic.val().get("clinic_name", "") == selected_clinic:
                                clinic_operating_hours = clinic.val().get("clinic_operating_hr", "")
                                break

                if not clinic_operating_hours:
                        raise ValueError(f"No operating hours found for clinic: {selected_clinic}")

                # Parse the operating hours
                start_time_str, end_time_str = clinic_operating_hours.lower().replace(' ', '').split('to')
                start_time = datetime.strptime(start_time_str, '%I%p')
                end_time = datetime.strptime(end_time_str, '%I%p')
                
                # Generate the list of time slots with one-hour intervals
                time_slots = []
                current_time = start_time
                while current_time <= end_time:
                        time_slots.append(current_time.strftime('%I:%M %p').lower())
                        current_time += timedelta(hours=1)

                self.time_dropdown.clear()
                self.time_dropdown.addItems(time_slots)
        except Exception as e:
                print(f"An error occurred while loading time slots: {e}")

    def load_specialties(self):
        selected_doctor = self.doc_dropdown.currentText()

        if selected_doctor == "Search or Select a Doctor":
                self.speciality_dropdown.clear()
                self.speciality_dropdown.addItem("Select a Specialty")
                return

        try:
                doctors_data = db.child("clinic").get()
                specialties = []

                for clinic in doctors_data.each():
                        doctors = clinic.val().get("doctors", {})
                        for doctor_id, doctor in doctors.items():
                                if doctor.get("doctor_name", "") == selected_doctor:
                                        specialization = doctor.get("specialization", "")
                                        if specialization:
                                                # Split multiple specializations by comma and 'and'
                                                for spec in re.split(',| and ', specialization):
                                                        if spec.strip():
                                                                specialties.append(spec.strip())
                                        break  # No need to continue once the selected doctor is found

                # Remove duplicates and sort
                specialties = sorted(set(specialties))
                specialties.insert(0, "Select a Specialty")
                self.speciality_dropdown.clear()
                self.speciality_dropdown.addItems(specialties)
        except Exception as e:
                print(f"An error occurred while loading specialties: {e}")

    def prefill_appointment_form(self, clinic_name, doctor_name):
        # Pre-fill the clinic dropdown
        clinic_index = self.clinic_dropdown.findText(clinic_name)
        if clinic_index != -1:
            self.clinic_dropdown.setCurrentIndex(clinic_index)

        # If doctor_name is not empty, load and pre-fill the doctors for the selected clinic
        if doctor_name:
            self.load_doctors()

            # Pre-fill the doctor dropdown
            doctor_index = self.doc_dropdown.findText(doctor_name)
            if doctor_index != -1:
                self.doc_dropdown.setCurrentIndex(doctor_index)



            
            
    def get_selected_data(self):
        clinic = self.clinic_dropdown.currentText()
        doctor = self.doc_dropdown.currentText()
        time = self.time_dropdown.currentText()
        speciality = self.speciality_dropdown.currentText()
        date = self.calendarWidget.selectedDate().toString("yyMMdd")
        med_concern = self.med_input.text() if self.med_input.text() != "Write here..." else ""
        admin_reassign = "yes" if self.checkBox.isChecked() else "no"
        return clinic, doctor, time, speciality, date, med_concern, admin_reassign

    def generate_new_appt_id(self):
        try:
            appointments = db.child("appointment").get()
            max_id = 0
            if appointments.each():
                for appointment in appointments.each():
                    print(f"appt is {appointment}")
                    appt_id = appointment.key()
                    id_num = int(appt_id.replace("appt_id", ""))
                    if id_num > max_id:
                        max_id = id_num
                        print(f"current max id: {max_id}")
            new_id = max_id + 1
            return f"appt_id{new_id}"
        except Exception as e:
            print(f"Error generating new appointment ID: {e}")
            return None
    
    def set_user_id(self, user_id): 
        self.user_id = user_id
        
    def save_appointment_to_db(self):
        clinic, doctor, time, speciality, date, med_concern, admin_reassign = self.get_selected_data()
        new_appt_id = self.generate_new_appt_id()
        
        if not new_appt_id:
            print("Failed to generate new appointment ID.")
            return
         
        print(f"user id is {self.user_id}")
        
        appointment_data = {
            "clinic_id": clinic,
            "date": date,
            "doctor_id": doctor,
            "patient_id": self.user_id, 
            "record_id": 1,  # Replace with actual record ID
            "time": time,
            "speciality": speciality,
            "med_concern": med_concern,
            "admin_reassign": admin_reassign
        }

        try:
            db.child("appointment").child(new_appt_id).set(appointment_data)
            print(f"Appointment {new_appt_id} saved successfully.")
            
            # Display message box if appointment saved successfully
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Appointment made successfully.")
            msgBox.setInformativeText("Please wait 3-5 days for clinic admin to approve.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.buttonClicked.connect(self.redirectToAppointmentWidget)
            msgBox.exec_()
        
        except Exception as e:
            print(f"Error saving appointment: {e}")


    def redirectToAppointmentWidget(self, button):
        if button.text() == "OK":
            self.redirect_appt.emit()
            

