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
    doc_name_btn_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        Form.setStyleSheet(u"background-color: \"#B6D0E2\" ")
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
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")
        self.search_patient.setClearButtonEnabled(False)
        self.patient_details_outer_frame = QFrame(self.background)
        self.patient_details_outer_frame.setObjectName(u"patient_details_outer_frame")
        self.patient_details_outer_frame.setGeometry(QRect(979, 200, 751, 841))
        self.patient_details_outer_frame.setStyleSheet(u"background-color : #ffffff;")
        self.patient_details_outer_frame.setFrameShape(QFrame.StyledPanel)
        self.patient_details_outer_frame.setFrameShadow(QFrame.Raised)
        self.clinic_details_inner = QFrame(self.patient_details_outer_frame)
        self.clinic_details_inner.setObjectName(u"clinic_details_inner")
        self.clinic_details_inner.setGeometry(QRect(20, 30, 721, 751))
        self.clinic_details_inner.setFrameShape(QFrame.StyledPanel)
        self.clinic_details_inner.setFrameShadow(QFrame.Raised)
        self.patient_logo_2 = QLabel(self.clinic_details_inner)
        self.patient_logo_2.setObjectName(u"patient_logo_2")
        self.patient_logo_2.setGeometry(QRect(9, 9, 54, 54))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(9)
        self.patient_logo_2.setFont(font2)
        self.patient_logo_2.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.patient_logo_2.setAlignment(Qt.AlignCenter)
        self.patient_name_display = QLabel(self.clinic_details_inner)
        self.patient_name_display.setObjectName(u"patient_name_display")
        self.patient_name_display.setGeometry(QRect(9, 69, 120, 22))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)
        self.patient_name_display.setFont(font3)
        self.patient_name_display.setStyleSheet(u"border : none;\n"
"")
        self.line_2 = QFrame(self.clinic_details_inner)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(9, 205, 703, 3))
        self.line_2.setMinimumSize(QSize(357, 3))
        self.line_2.setMaximumSize(QSize(16777215, 3))
        self.line_2.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        self.line_2.setFrameShape(QFrame.StyledPanel)
        self.line_2.setFrameShadow(QFrame.Raised)
        self.diagnosis_display = QLabel(self.clinic_details_inner)
        self.diagnosis_display.setObjectName(u"diagnosis_display")
        self.diagnosis_display.setGeometry(QRect(320, 300, 390, 148))
        self.diagnosis_display.setMinimumSize(QSize(390, 0))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setWeight(50)
        self.diagnosis_display.setFont(font4)
        self.diagnosis_display.setStyleSheet(u"border: none;")
        self.diagnosis_display.setScaledContents(False)
        self.diagnosis_display.setWordWrap(True)
        self.diagnosis_label_2 = QLabel(self.clinic_details_inner)
        self.diagnosis_label_2.setObjectName(u"diagnosis_label_2")
        self.diagnosis_label_2.setGeometry(QRect(13, 300, 301, 148))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.diagnosis_label_2.setFont(font5)
        self.diagnosis_label_2.setStyleSheet(u"border: none;")
        self.diagnosis_label_2.setWordWrap(True)
        self.last_checked_by_label = QLabel(self.clinic_details_inner)
        self.last_checked_by_label.setObjectName(u"last_checked_by_label")
        self.last_checked_by_label.setGeometry(QRect(13, 210, 301, 148))
        self.last_checked_by_label.setFont(font5)
        self.last_checked_by_label.setStyleSheet(u"border: none;")
        self.last_checked_by_label.setWordWrap(True)
        self.dr_name_display = QLabel(self.clinic_details_inner)
        self.dr_name_display.setObjectName(u"dr_name_display")
        self.dr_name_display.setGeometry(QRect(320, 210, 390, 148))
        self.dr_name_display.setMinimumSize(QSize(390, 0))
        self.dr_name_display.setFont(font4)
        self.dr_name_display.setStyleSheet(u"border: none;")
        self.dr_name_display.setScaledContents(False)
        self.dr_name_display.setWordWrap(True)
        self.date_label = QLabel(self.clinic_details_inner)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(13, 400, 301, 148))
        self.date_label.setFont(font5)
        self.date_label.setStyleSheet(u"border: none;")
        self.date_label.setWordWrap(True)
        self.date_display = QLabel(self.clinic_details_inner)
        self.date_display.setObjectName(u"date_display")
        self.date_display.setGeometry(QRect(320, 400, 390, 148))
        self.date_display.setMinimumSize(QSize(390, 0))
        self.date_display.setFont(font4)
        self.date_display.setStyleSheet(u"border: none;")
        self.date_display.setScaledContents(False)
        self.date_display.setWordWrap(True)
        self.doctor_preferred_label = QLabel(self.clinic_details_inner)
        self.doctor_preferred_label.setObjectName(u"doctor_preferred_label")
        self.doctor_preferred_label.setGeometry(QRect(13, 610, 301, 148))
        self.doctor_preferred_label.setFont(font5)
        self.doctor_preferred_label.setStyleSheet(u"border: none;")
        self.doctor_preferred_label.setWordWrap(True)
        self.time_display_3 = QLabel(self.clinic_details_inner)
        self.time_display_3.setObjectName(u"time_display_3")
        self.time_display_3.setGeometry(QRect(320, 500, 390, 148))
        self.time_display_3.setMinimumSize(QSize(390, 0))
        self.time_display_3.setFont(font4)
        self.time_display_3.setStyleSheet(u"border: none;")
        self.time_display_3.setScaledContents(False)
        self.time_display_3.setWordWrap(True)
        self.time_label_3 = QLabel(self.clinic_details_inner)
        self.time_label_3.setObjectName(u"time_label_3")
        self.time_label_3.setGeometry(QRect(13, 500, 301, 148))
        self.time_label_3.setFont(font5)
        self.time_label_3.setStyleSheet(u"border: none;")
        self.time_label_3.setWordWrap(True)
        self.doc_name_btn = QPushButton(self.clinic_details_inner)
        self.doc_name_btn.setObjectName(u"doc_name_btn")
        self.doc_name_btn.setGeometry(QRect(240, 630, 211, 91))

        self.doc_name_btn.clicked.connect(self.emitViewDocBtn)                

        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        font6.setUnderline(True)
        self.doc_name_btn.setFont(font6)
        self.doc_name_btn.setStyleSheet(u"color: #007E85; border: none;")
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
        self.patient_frame1 = QFrame(self.patient_list_frame)
        self.patient_frame1.setObjectName(u"patient_frame1")
        self.patient_frame1.setGeometry(QRect(0, 20, 801, 81))
        self.patient_frame1.setFrameShape(QFrame.StyledPanel)
        self.patient_frame1.setFrameShadow(QFrame.Raised)
        self.patient_name_label1 = QLabel(self.patient_frame1)
        self.patient_name_label1.setObjectName(u"patient_name_label1")
        self.patient_name_label1.setGeometry(QRect(90, 30, 121, 21))
        self.patient_name_label1.setFont(font3)
        self.patient_name_label1.setStyleSheet(u"border : none;\n"
"")
        self.patient_profile_logo1 = QLabel(self.patient_frame1)
        self.patient_profile_logo1.setObjectName(u"patient_profile_logo1")
        self.patient_profile_logo1.setGeometry(QRect(10, 10, 54, 54))
        self.patient_profile_logo1.setFont(font2)
        self.patient_profile_logo1.setStyleSheet(u"background-color: #B6D0E2; \n"
"border-radius: 25px; \n"
"border: 2px solid #B6D0F7; \n"
"min-width: 50px; \n"
"min-height: 50px; \n"
"max-width: 50px;\n"
"max-height: 50px; ")
        self.patient_profile_logo1.setAlignment(Qt.AlignCenter)
        self.appt_time_label = QLabel(self.patient_frame1)
        self.appt_time_label.setObjectName(u"appt_time_label")
        self.appt_time_label.setGeometry(QRect(690, 20, 91, 41))
        self.appt_time_label.setFont(font)
        self.appt_time_label.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);\n"
"color: #128983; text-align: center;\n"
"")
        self.appt_time_label.setAlignment(Qt.AlignCenter)
        self.patient_frame2 = QFrame(self.patient_list_frame)
        self.patient_frame2.setObjectName(u"patient_frame2")
        self.patient_frame2.setGeometry(QRect(0, 130, 801, 81))
        self.patient_frame2.setFrameShape(QFrame.StyledPanel)
        self.patient_frame2.setFrameShadow(QFrame.Raised)
        self.patient_name_label2 = QLabel(self.patient_frame2)
        self.patient_name_label2.setObjectName(u"patient_name_label2")
        self.patient_name_label2.setGeometry(QRect(90, 30, 121, 21))
        self.patient_name_label2.setFont(font3)
        self.patient_name_label2.setStyleSheet(u"border : none;\n"
"")
        self.patient_profile_logo_2 = QLabel(self.patient_frame2)
        self.patient_profile_logo_2.setObjectName(u"patient_profile_logo_2")
        self.patient_profile_logo_2.setGeometry(QRect(10, 10, 54, 54))
        self.patient_profile_logo_2.setFont(font2)
        self.patient_profile_logo_2.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.patient_profile_logo_2.setAlignment(Qt.AlignCenter)
        self.appt_time_label2 = QLabel(self.patient_frame2)
        self.appt_time_label2.setObjectName(u"appt_time_label2")
        self.appt_time_label2.setGeometry(QRect(690, 20, 91, 41))
        self.appt_time_label2.setFont(font)
        self.appt_time_label2.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);\n"
"color: #128983; text-align: center;\n"
"")
        self.appt_time_label2.setAlignment(Qt.AlignCenter)
        self.patient_frame2_2 = QFrame(self.patient_list_frame)
        self.patient_frame2_2.setObjectName(u"patient_frame2_2")
        self.patient_frame2_2.setGeometry(QRect(0, 240, 801, 81))
        self.patient_frame2_2.setFrameShape(QFrame.StyledPanel)
        self.patient_frame2_2.setFrameShadow(QFrame.Raised)
        self.patient_name_label2_2 = QLabel(self.patient_frame2_2)
        self.patient_name_label2_2.setObjectName(u"patient_name_label2_2")
        self.patient_name_label2_2.setGeometry(QRect(90, 30, 121, 21))
        self.patient_name_label2_2.setFont(font3)
        self.patient_name_label2_2.setStyleSheet(u"border : none;\n"
"")
        self.patient_profile_logo_3 = QLabel(self.patient_frame2_2)
        self.patient_profile_logo_3.setObjectName(u"patient_profile_logo_3")
        self.patient_profile_logo_3.setGeometry(QRect(10, 10, 54, 54))
        self.patient_profile_logo_3.setFont(font2)
        self.patient_profile_logo_3.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.patient_profile_logo_3.setAlignment(Qt.AlignCenter)
        self.appt_time_label2_2 = QLabel(self.patient_frame2_2)
        self.appt_time_label2_2.setObjectName(u"appt_time_label2_2")
        self.appt_time_label2_2.setGeometry(QRect(690, 20, 91, 41))
        self.appt_time_label2_2.setFont(font)
        self.appt_time_label2_2.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);\n"
"color: #128983; text-align: center;\n"
"")
        self.appt_time_label2_2.setAlignment(Qt.AlignCenter)
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
        self.patient_logo_2.setText(QCoreApplication.translate("Form", u"A", None))
        self.patient_name_display.setText(QCoreApplication.translate("Form", u"Patient Name", None))
        self.diagnosis_display.setText(QCoreApplication.translate("Form", u"diagnosis", None))
        self.diagnosis_label_2.setText(QCoreApplication.translate("Form", u"Diagnosis : ", None))
        self.last_checked_by_label.setText(QCoreApplication.translate("Form", u"Last Checked By:", None))
        self.dr_name_display.setText(QCoreApplication.translate("Form", u"Dr name", None))
        self.date_label.setText(QCoreApplication.translate("Form", u"Date:", None))
        self.date_display.setText(QCoreApplication.translate("Form", u"date", None))
        self.doctor_preferred_label.setText(QCoreApplication.translate("Form", u"Doctor preferred:", None))
        self.time_display_3.setText(QCoreApplication.translate("Form", u"Time", None))
        self.time_label_3.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.doc_name_btn.setText(QCoreApplication.translate("Form", u"Dr name", None))
        self.filter.setItemText(0, QCoreApplication.translate("Form", u"Recent", None))
        self.filter.setItemText(1, QCoreApplication.translate("Form", u"Oldest", None))

        self.patient_list_label.setText(QCoreApplication.translate("Form", u"Patient List", None))
        self.patient_details_label.setText(QCoreApplication.translate("Form", u"Patient Details", None))
        self.patient_name_label1.setText(QCoreApplication.translate("Form", u"Patient Name", None))
        self.patient_profile_logo1.setText(QCoreApplication.translate("Form", u"PN", None))
        self.appt_time_label.setText(QCoreApplication.translate("Form", u"Time", None))
        self.patient_name_label2.setText(QCoreApplication.translate("Form", u"Patient Name", None))
        self.patient_profile_logo_2.setText(QCoreApplication.translate("Form", u"PN", None))
        self.appt_time_label2.setText(QCoreApplication.translate("Form", u"Time", None))
        self.patient_name_label2_2.setText(QCoreApplication.translate("Form", u"Patient Name", None))
        self.patient_profile_logo_3.setText(QCoreApplication.translate("Form", u"PN", None))
        self.appt_time_label2_2.setText(QCoreApplication.translate("Form", u"Time", None))
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
    def emitViewDocBtn(self):
        # Emit the custom signal
        self.doc_name_btn_clicked.emit()
