# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find_doctorDlqbfB.ui'
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
        self.navbar = QFrame(Form)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setGeometry(QRect(0, 0, 111, 901))
        self.navbar.setFrameShape(QFrame.StyledPanel)
        self.navbar.setFrameShadow(QFrame.Raised)
        self.home_navigation = QToolButton(self.navbar)
        self.home_navigation.setObjectName(u"home_navigation")
        self.home_navigation.setEnabled(True)
        self.home_navigation.setGeometry(QRect(20, 80, 73, 94))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Source Sans Pro Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_navigation.setFont(font)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon = QIcon()
        icon.addFile(u"../Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.appointments_navigation = QToolButton(self.navbar)
        self.appointments_navigation.setObjectName(u"appointments_navigation")
        self.appointments_navigation.setEnabled(True)
        self.appointments_navigation.setGeometry(QRect(10, 250, 88, 94))
        sizePolicy.setHeightForWidth(self.appointments_navigation.sizePolicy().hasHeightForWidth())
        self.appointments_navigation.setSizePolicy(sizePolicy)
        self.appointments_navigation.setFont(font)
        self.appointments_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"../Images/nav_images/appointment_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appointments_navigation.setIcon(icon1)
        self.appointments_navigation.setIconSize(QSize(70, 70))
        self.appointments_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.services_navigation = QToolButton(self.navbar)
        self.services_navigation.setObjectName(u"services_navigation")
        self.services_navigation.setEnabled(True)
        self.services_navigation.setGeometry(QRect(20, 430, 73, 94))
        sizePolicy.setHeightForWidth(self.services_navigation.sizePolicy().hasHeightForWidth())
        self.services_navigation.setSizePolicy(sizePolicy)
        self.services_navigation.setFont(font)
        self.services_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"../Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_navigation.setIcon(icon2)
        self.services_navigation.setIconSize(QSize(70, 70))
        self.services_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settings_navigation = QToolButton(self.navbar)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        self.settings_navigation.setGeometry(QRect(20, 580, 73, 94))
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setFont(font)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"../Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon3)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.logout_navigation = QToolButton(self.navbar)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        self.logout_navigation.setGeometry(QRect(20, 770, 73, 94))
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setFont(font)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"../Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon4)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
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
        icon5 = QIcon()
        icon5.addFile(u"../Images/icon/notification.png", QSize(), QIcon.Normal, QIcon.Off)
        self.noti_icon.setIcon(icon5)
        self.noti_icon.setIconSize(QSize(40, 40))
        self.fad_title = QLabel(self.whitebg)
        self.fad_title.setObjectName(u"fad_title")
        self.fad_title.setGeometry(QRect(60, 40, 481, 81))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(28)
        font1.setBold(True)
        font1.setWeight(75)
        self.fad_title.setFont(font1)
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
        self.profile_icon.setPixmap(QPixmap(u"../Images/icon/profile_icon.png"))
        self.profile_icon.setScaledContents(True)
        self.profile_btn = QPushButton(self.user_frame)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setGeometry(QRect(120, 25, 71, 31))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(16)
        self.profile_btn.setFont(font2)
        self.profile_btn.setStyleSheet(u"border: none")
        self.scrollArea = QScrollArea(self.whitebg)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(80, 240, 1641, 841))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1641, 841))
        self.doc_info_outer = QFrame(self.scrollAreaWidgetContents)
        self.doc_info_outer.setObjectName(u"doc_info_outer")
        self.doc_info_outer.setGeometry(QRect(0, 0, 388, 535))
        self.doc_info_outer.setStyleSheet(u"border: 1px solid black; \n"
"border-radius: 24px; ")
        self.doc_info_outer.setFrameShape(QFrame.StyledPanel)
        self.doc_info_outer.setFrameShadow(QFrame.Raised)
        self.doc_info_inner = QFrame(self.doc_info_outer)
        self.doc_info_inner.setObjectName(u"doc_info_inner")
        self.doc_info_inner.setGeometry(QRect(-1, 0, 401, 541))
        self.doc_info_inner.setStyleSheet(u"border: none; background-color: transparent;")
        self.doc_info_inner.setFrameShape(QFrame.StyledPanel)
        self.doc_info_inner.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.doc_info_inner)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 480, 396, 57))
        self.btnlayout = QHBoxLayout(self.layoutWidget)
        self.btnlayout.setObjectName(u"btnlayout")
        self.btnlayout.setContentsMargins(0, 0, 0, 0)
        self.view_profile_btn = QPushButton(self.layoutWidget)
        self.view_profile_btn.setObjectName(u"view_profile_btn")
        self.view_profile_btn.setMinimumSize(QSize(194, 55))
        self.view_profile_btn.setStyleSheet(u"border-radius: 0 0 24pt 0; background-color: #B6D0E2; border: none;")

        self.btnlayout.addWidget(self.view_profile_btn)

        self.make_appt_btn = QPushButton(self.layoutWidget)
        self.make_appt_btn.setObjectName(u"make_appt_btn")
        self.make_appt_btn.setMinimumSize(QSize(194, 55))
        self.make_appt_btn.setStyleSheet(u"border-radius: 0 0 24pt 0; background-color: #B6D0E2; border: none;")

        self.btnlayout.addWidget(self.make_appt_btn)

        self.widget = QWidget(self.doc_info_inner)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 31, 326, 451))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.doc_img = QLabel(self.widget)
        self.doc_img.setObjectName(u"doc_img")
        self.doc_img.setMinimumSize(QSize(160, 160))
        self.doc_img.setStyleSheet(u"text-align: center; border: none;")

        self.verticalLayout.addWidget(self.doc_img)

        self.verticalSpacer_3 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.doc_name = QLabel(self.widget)
        self.doc_name.setObjectName(u"doc_name")
        self.doc_name.setStyleSheet(u"text-align: center; border: none;")

        self.verticalLayout.addWidget(self.doc_name)

        self.doc_speciality = QLabel(self.widget)
        self.doc_speciality.setObjectName(u"doc_speciality")
        self.doc_speciality.setStyleSheet(u"text-align: center; border: none;")

        self.verticalLayout.addWidget(self.doc_speciality)

        self.verticalSpacer = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(324, 3))
        self.line.setMaximumSize(QSize(16777215, 3))
        self.line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        self.line.setFrameShape(QFrame.StyledPanel)
        self.line.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.line)

        self.clinic_name = QLabel(self.widget)
        self.clinic_name.setObjectName(u"clinic_name")
        self.clinic_name.setStyleSheet(u"text-align: center; border: none;")

        self.verticalLayout.addWidget(self.clinic_name)

        self.verticalSpacer_2 = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget1 = QWidget(self.whitebg)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(81, 141, 1641, 48))
        self.seopdown_layout = QHBoxLayout(self.widget1)
        self.seopdown_layout.setSpacing(80)
        self.seopdown_layout.setObjectName(u"seopdown_layout")
        self.seopdown_layout.setContentsMargins(0, 0, 0, 0)
        self.clinic_dropdown = QComboBox(self.widget1)
        self.clinic_dropdown.addItem(u"Search or Select a Clinic")
        self.clinic_dropdown.addItem("")
        self.clinic_dropdown.setObjectName(u"clinic_dropdown")
        self.clinic_dropdown.setMinimumSize(QSize(321, 41))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(11)
        self.clinic_dropdown.setFont(font3)
        self.clinic_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
"border-radius: 5px; \n"
"background-color: #FFFFFF; \n"
"box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); \n"
"padding: 10px; \n"
"font-family: Consolas;\n"
"font-size: 11pt;")
        self.clinic_dropdown.setEditable(True)
        self.clinic_dropdown.setIconSize(QSize(50, 50))
        self.clinic_dropdown.setFrame(True)

        self.seopdown_layout.addWidget(self.clinic_dropdown)

        self.speciality_dropdown = QComboBox(self.widget1)
        self.speciality_dropdown.addItem(u"Search or Select a Specialities")
        self.speciality_dropdown.addItem("")
        self.speciality_dropdown.setObjectName(u"speciality_dropdown")
        self.speciality_dropdown.setMinimumSize(QSize(321, 41))
        self.speciality_dropdown.setFont(font3)
        self.speciality_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
"border-radius: 5px; \n"
"background-color: #FFFFFF; \n"
"box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); \n"
"padding: 10px; \n"
"font-family: Consolas;\n"
"font-size: 11pt;")
        self.speciality_dropdown.setEditable(True)
        self.speciality_dropdown.setIconSize(QSize(50, 50))
        self.speciality_dropdown.setFrame(True)

        self.seopdown_layout.addWidget(self.speciality_dropdown)

        self.doc_dropdown = QComboBox(self.widget1)
        self.doc_dropdown.addItem(u"Search or Select a Doctor")
        self.doc_dropdown.addItem("")
        self.doc_dropdown.setObjectName(u"doc_dropdown")
        self.doc_dropdown.setMinimumSize(QSize(321, 41))
        self.doc_dropdown.setFont(font3)
        self.doc_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
"border-radius: 5px; \n"
"background-color: #FFFFFF; \n"
"box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); \n"
"padding: 10px; \n"
"font-family: Consolas;\n"
"font-size: 11pt;")
        self.doc_dropdown.setEditable(True)
        self.doc_dropdown.setIconSize(QSize(50, 50))
        self.doc_dropdown.setFrame(True)

        self.seopdown_layout.addWidget(self.doc_dropdown)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"Home", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Appointments", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Services", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
        self.noti_icon.setText("")
        self.fad_title.setText(QCoreApplication.translate("Form", u"Find A Doctor", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.view_profile_btn.setText(QCoreApplication.translate("Form", u"View Profile", None))
        self.make_appt_btn.setText(QCoreApplication.translate("Form", u"Make Appointment", None))
        self.doc_img.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.doc_name.setText(QCoreApplication.translate("Form", u"Doc Name", None))
        self.doc_speciality.setText(QCoreApplication.translate("Form", u"Speciality", None))
        self.clinic_name.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_dropdown.setItemText(1, QCoreApplication.translate("Form", u"test", None))

        self.speciality_dropdown.setItemText(1, QCoreApplication.translate("Form", u"test", None))

        self.doc_dropdown.setItemText(1, QCoreApplication.translate("Form", u"test", None))

    # retranslateUi

