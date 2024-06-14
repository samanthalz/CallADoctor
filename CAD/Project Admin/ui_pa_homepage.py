# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pa_homepageFovpEM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
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
        self.num_upcoming_appt_label.setGeometry(QRect(20, 20, 961, 61))
        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(22)
        self.num_upcoming_appt_label.setFont(font)
        self.num_upcoming_appt_label.setWordWrap(True)
        self.num_appt_number_label = QLabel(self.num_appt_frame)
        self.num_appt_number_label.setObjectName(u"num_appt_number_label")
        self.num_appt_number_label.setGeometry(QRect(30, 100, 51, 71))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(48)
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
        self.upcomin_appt_frame = QFrame(self.appointment_frame)
        self.upcomin_appt_frame.setObjectName(u"upcomin_appt_frame")
        self.upcomin_appt_frame.setGeometry(QRect(30, 30, 450, 551))
        self.upcomin_appt_frame.setStyleSheet(u"background-color : #ffffff;")
        self.upcomin_appt_frame.setFrameShape(QFrame.StyledPanel)
        self.upcomin_appt_frame.setFrameShadow(QFrame.Raised)
        self.upcoming_label = QLabel(self.upcomin_appt_frame)
        self.upcoming_label.setObjectName(u"upcoming_label")
        self.upcoming_label.setGeometry(QRect(30, 20, 211, 41))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(11)
        self.upcoming_label.setFont(font2)
        self.upcoming_label.setStyleSheet(u"border : none;\n"
"")
        self.clinicAppt_frame = QFrame(self.upcomin_appt_frame)
        self.clinicAppt_frame.setObjectName(u"clinicAppt_frame")
        self.clinicAppt_frame.setGeometry(QRect(20, 70, 401, 81))
        self.clinicAppt_frame.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame.setFrameShadow(QFrame.Raised)
        self.clinic_name_label = QLabel(self.clinicAppt_frame)
        self.clinic_name_label.setObjectName(u"clinic_name_label")
        self.clinic_name_label.setGeometry(QRect(90, 30, 121, 21))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)
        self.clinic_name_label.setFont(font3)
        self.clinic_name_label.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label = QLabel(self.clinicAppt_frame)
        self.clinic_logo_label.setObjectName(u"clinic_logo_label")
        self.clinic_logo_label.setGeometry(QRect(10, 10, 54, 54))
        font4 = QFont()
        font4.setFamily(u"Cascadia Code")
        font4.setPointSize(9)
        self.clinic_logo_label.setFont(font4)
        self.clinic_logo_label.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.clinicAppt_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 91, 41))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(10)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);\n"
"color: #128983; text-align: center;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.clinicAppt_frame_2 = QFrame(self.upcomin_appt_frame)
        self.clinicAppt_frame_2.setObjectName(u"clinicAppt_frame_2")
        self.clinicAppt_frame_2.setGeometry(QRect(20, 170, 401, 81))
        self.clinicAppt_frame_2.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame_2.setFrameShadow(QFrame.Raised)
        self.clinic_name_label_2 = QLabel(self.clinicAppt_frame_2)
        self.clinic_name_label_2.setObjectName(u"clinic_name_label_2")
        self.clinic_name_label_2.setGeometry(QRect(90, 30, 121, 21))
        self.clinic_name_label_2.setFont(font3)
        self.clinic_name_label_2.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_2 = QLabel(self.clinicAppt_frame_2)
        self.clinic_logo_label_2.setObjectName(u"clinic_logo_label_2")
        self.clinic_logo_label_2.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_2.setFont(font4)
        self.clinic_logo_label_2.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_2.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.clinicAppt_frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 20, 91, 41))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"background-color: rgba(246, 32, 136, 0.15);\n"
"color: #F62088; text-align: center;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.upcomin_appt_frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(290, 30, 131, 31))
        self.comboBox.setFont(font5)
        self.upcomin_appt_frame_2 = QFrame(self.appointment_frame)
        self.upcomin_appt_frame_2.setObjectName(u"upcomin_appt_frame_2")
        self.upcomin_appt_frame_2.setGeometry(QRect(510, 30, 450, 551))
        self.upcomin_appt_frame_2.setStyleSheet(u"background-color : #ffffff;")
        self.upcomin_appt_frame_2.setFrameShape(QFrame.StyledPanel)
        self.upcomin_appt_frame_2.setFrameShadow(QFrame.Raised)
        self.upcoming_label_2 = QLabel(self.upcomin_appt_frame_2)
        self.upcoming_label_2.setObjectName(u"upcoming_label_2")
        self.upcoming_label_2.setGeometry(QRect(30, 20, 381, 41))
        self.upcoming_label_2.setFont(font2)
        self.upcoming_label_2.setStyleSheet(u"border : none;\n"
"")
        self.clinicAppt_frame_6 = QFrame(self.upcomin_appt_frame_2)
        self.clinicAppt_frame_6.setObjectName(u"clinicAppt_frame_6")
        self.clinicAppt_frame_6.setGeometry(QRect(20, 70, 401, 431))
        self.clinicAppt_frame_6.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame_6.setFrameShadow(QFrame.Raised)
        self.clinic_name_label_6 = QLabel(self.clinicAppt_frame_6)
        self.clinic_name_label_6.setObjectName(u"clinic_name_label_6")
        self.clinic_name_label_6.setGeometry(QRect(100, 30, 121, 21))
        self.clinic_name_label_6.setFont(font3)
        self.clinic_name_label_6.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_6 = QLabel(self.clinicAppt_frame_6)
        self.clinic_logo_label_6.setObjectName(u"clinic_logo_label_6")
        self.clinic_logo_label_6.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_6.setFont(font4)
        self.clinic_logo_label_6.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_6.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.clinicAppt_frame_6)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 100, 360, 3))
        self.line.setMinimumSize(QSize(357, 3))
        self.line.setMaximumSize(QSize(16777215, 3))
        self.line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        self.line.setFrameShape(QFrame.StyledPanel)
        self.line.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.clinicAppt_frame_6)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 120, 401, 311))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"border: none;")
        self.label_3.setLineWidth(0)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_7.setFont(font7)
        self.label_7.setStyleSheet(u"border: none;")

        self.horizontalLayout.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)
        self.label_8.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(135)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"border: none;")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)
        self.label_9.setStyleSheet(u"border: none;")
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"border: none;")
        self.label_6.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)
        self.label_10.setStyleSheet(u"border: none;")
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(self.upcomin_appt_frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 510, 93, 28))
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(9)
        font8.setUnderline(True)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"color: #007E85; border: none;")
        self.active_pres_frame = QFrame(self.background)
        self.active_pres_frame.setObjectName(u"active_pres_frame")
        self.active_pres_frame.setGeometry(QRect(1120, 170, 481, 831))
        self.active_pres_frame.setStyleSheet(u"border: 2px solid #FFFFFF;\n"
"border-radius: 16px;\n"
"background-color: white")
        self.active_pres_frame.setFrameShape(QFrame.StyledPanel)
        self.active_pres_frame.setFrameShadow(QFrame.Raised)
        self.upcoming_label_3 = QLabel(self.active_pres_frame)
        self.upcoming_label_3.setObjectName(u"upcoming_label_3")
        self.upcoming_label_3.setGeometry(QRect(20, 10, 441, 41))
        self.upcoming_label_3.setFont(font2)
        self.upcoming_label_3.setStyleSheet(u"border : none;\n"
"")
        self.clinicAppt_frame_3 = QFrame(self.active_pres_frame)
        self.clinicAppt_frame_3.setObjectName(u"clinicAppt_frame_3")
        self.clinicAppt_frame_3.setGeometry(QRect(20, 70, 401, 81))
        self.clinicAppt_frame_3.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame_3.setFrameShadow(QFrame.Raised)
        self.clinic_name_label_3 = QLabel(self.clinicAppt_frame_3)
        self.clinic_name_label_3.setObjectName(u"clinic_name_label_3")
        self.clinic_name_label_3.setGeometry(QRect(30, 10, 121, 21))
        self.clinic_name_label_3.setFont(font6)
        self.clinic_name_label_3.setStyleSheet(u"border : none;\n"
"")
        self.label_11 = QLabel(self.clinicAppt_frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(310, 20, 71, 41))
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"background-color: #B6D0E2;\n"
"color: white; text-align: center;")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.clinic_name_label_4 = QLabel(self.clinicAppt_frame_3)
        self.clinic_name_label_4.setObjectName(u"clinic_name_label_4")
        self.clinic_name_label_4.setGeometry(QRect(30, 40, 121, 21))
        self.clinic_name_label_4.setFont(font5)
        self.clinic_name_label_4.setStyleSheet(u"border : none;\n"
"")
        self.noti_icon = QPushButton(self.background)
        self.noti_icon.setObjectName(u"noti_icon")
        self.noti_icon.setGeometry(QRect(1380, 30, 70, 81))
        icon = QIcon()
        icon.addFile(u"../Images/icon/notification.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.profile_icon.setPixmap(QPixmap(u"../Images/icon/profile_icon.png"))
        self.profile_icon.setScaledContents(True)
        self.profile_btn = QPushButton(self.user_frame)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setGeometry(QRect(120, 25, 71, 31))
        font9 = QFont()
        font9.setFamily(u"Consolas")
        font9.setPointSize(16)
        self.profile_btn.setFont(font9)
        self.profile_btn.setStyleSheet(u"border: none")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 90, 111, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_navigation = QToolButton(self.frame)
        self.home_navigation.setObjectName(u"home_navigation")
        self.home_navigation.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        font10 = QFont()
        font10.setFamily(u"Source Sans Pro Semibold")
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)
        self.home_navigation.setFont(font10)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"../Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.home_navigation)

        self.appointments_navigation = QToolButton(self.frame)
        self.appointments_navigation.setObjectName(u"appointments_navigation")
        self.appointments_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.appointments_navigation.sizePolicy().hasHeightForWidth())
        self.appointments_navigation.setSizePolicy(sizePolicy)
        self.appointments_navigation.setFont(font10)
        self.appointments_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"../Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appointments_navigation.setIcon(icon2)
        self.appointments_navigation.setIconSize(QSize(70, 70))
        self.appointments_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.appointments_navigation)

        self.services_navigation = QToolButton(self.frame)
        self.services_navigation.setObjectName(u"services_navigation")
        self.services_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.services_navigation.sizePolicy().hasHeightForWidth())
        self.services_navigation.setSizePolicy(sizePolicy)
        self.services_navigation.setFont(font10)
        self.services_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"../Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_navigation.setIcon(icon3)
        self.services_navigation.setIconSize(QSize(70, 70))
        self.services_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.services_navigation)

        self.settings_navigation = QToolButton(self.frame)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setFont(font10)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"../Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.frame)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setFont(font10)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon5 = QIcon()
        icon5.addFile(u"../Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.num_upcoming_appt_label.setText(QCoreApplication.translate("Form", u"Total Clinic Addition Request:", None))
        self.num_appt_number_label.setText(QCoreApplication.translate("Form", u"2", None))
        self.upcoming_label.setText(QCoreApplication.translate("Form", u"Clinic List", None))
        self.clinic_name_label.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label.setText(QCoreApplication.translate("Form", u"A", None))
        self.label.setText(QCoreApplication.translate("Form", u"Approved", None))
        self.clinic_name_label_2.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label_2.setText(QCoreApplication.translate("Form", u"A", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pending", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Recent", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Oldest", None))

        self.upcoming_label_2.setText(QCoreApplication.translate("Form", u"Request Details", None))
        self.clinic_name_label_6.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label_6.setText(QCoreApplication.translate("Form", u"A", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Phone: ", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"+60322845678", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"info@bangsarclinic.my", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Address:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"No. 23, Jalan Telawi 3, Bangsar Baru, 59100 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur, Malaysia.", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Operating Hours:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"24 Hours", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"View More", None))
        self.upcoming_label_3.setText(QCoreApplication.translate("Form", u"Feedbacks", None))
        self.clinic_name_label_3.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"View", None))
        self.clinic_name_label_4.setText(QCoreApplication.translate("Form", u"Date", None))
        self.noti_icon.setText("")
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Feedbacks", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

