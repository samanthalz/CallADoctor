# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_clinicAociuF.ui'
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
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(31, 20, 87, 851))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_navigation = QToolButton(self.layoutWidget_2)
        self.home_navigation.setObjectName(u"home_navigation")
        self.home_navigation.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        self.home_navigation.setMinimumSize(QSize(85, 96))
        self.home_navigation.setMaximumSize(QSize(85, 96))
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

        self.verticalLayout.addWidget(self.home_navigation)

        self.clinic_navigation = QToolButton(self.layoutWidget_2)
        self.clinic_navigation.setObjectName(u"clinic_navigation")
        self.clinic_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.clinic_navigation.sizePolicy().hasHeightForWidth())
        self.clinic_navigation.setSizePolicy(sizePolicy)
        self.clinic_navigation.setMinimumSize(QSize(85, 96))
        self.clinic_navigation.setMaximumSize(QSize(85, 96))
        self.clinic_navigation.setFont(font)
        self.clinic_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"../Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clinic_navigation.setIcon(icon1)
        self.clinic_navigation.setIconSize(QSize(70, 70))
        self.clinic_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.clinic_navigation)

        self.feedback_navigation = QToolButton(self.layoutWidget_2)
        self.feedback_navigation.setObjectName(u"feedback_navigation")
        self.feedback_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.feedback_navigation.sizePolicy().hasHeightForWidth())
        self.feedback_navigation.setSizePolicy(sizePolicy)
        self.feedback_navigation.setMinimumSize(QSize(85, 96))
        self.feedback_navigation.setMaximumSize(QSize(85, 96))
        self.feedback_navigation.setFont(font)
        self.feedback_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"../Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.feedback_navigation.setIcon(icon2)
        self.feedback_navigation.setIconSize(QSize(70, 70))
        self.feedback_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.feedback_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget_2)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setMinimumSize(QSize(85, 96))
        self.settings_navigation.setMaximumSize(QSize(85, 96))
        self.settings_navigation.setFont(font)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"../Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon3)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget_2)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setMinimumSize(QSize(85, 96))
        self.logout_navigation.setMaximumSize(QSize(85, 96))
        self.logout_navigation.setFont(font)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"../Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon4)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.logout_navigation)

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
        icon5 = QIcon()
        icon5.addFile(u"../Images/icon/notification.png", QSize(), QIcon.Normal, QIcon.Off)
        self.noti_icon.setIcon(icon5)
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
        self.profile_btn.setGeometry(QRect(100, 25, 121, 31))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(16)
        self.profile_btn.setFont(font1)
        self.profile_btn.setStyleSheet(u"border: none")
        self.clinic_label = QLabel(self.background)
        self.clinic_label.setObjectName(u"clinic_label")
        self.clinic_label.setGeometry(QRect(40, 40, 961, 61))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(22)
        self.clinic_label.setFont(font2)
        self.clinic_label.setWordWrap(True)
        self.clinic_img = QLabel(self.background)
        self.clinic_img.setObjectName(u"clinic_img")
        self.clinic_img.setGeometry(QRect(120, 180, 200, 200))
        self.clinic_img.setStyleSheet(u"border-radius: 100px; \n"
"background-color: #B6D0E2;  \n"
"color: white; \n"
"font-size: 16px;\n"
"text-align: center;")
        self.change_img_btn = QPushButton(self.background)
        self.change_img_btn.setObjectName(u"change_img_btn")
        self.change_img_btn.setGeometry(QRect(70, 420, 301, 51))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.change_img_btn.setFont(font3)
        self.change_img_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.submit_btn = QPushButton(self.background)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(1010, 960, 301, 51))
        self.submit_btn.setFont(font3)
        self.submit_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.widget = QWidget(self.background)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(550, 200, 1171, 731))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_layout = QVBoxLayout()
        self.name_layout.setSpacing(10)
        self.name_layout.setObjectName(u"name_layout")
        self.name = QLabel(self.widget)
        self.name.setObjectName(u"name")
        self.name.setMaximumSize(QSize(16777215, 23))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(12)
        self.name.setFont(font4)

        self.name_layout.addWidget(self.name)

        self.name_input = QLineEdit(self.widget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMinimumSize(QSize(500, 40))
        self.name_input.setMaximumSize(QSize(16777215, 40))
        self.name_input.setBaseSize(QSize(0, 0))
        self.name_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.name_layout.addWidget(self.name_input)


        self.horizontalLayout.addLayout(self.name_layout)

        self.hour_layout = QVBoxLayout()
        self.hour_layout.setSpacing(10)
        self.hour_layout.setObjectName(u"hour_layout")
        self.hour_label = QLabel(self.widget)
        self.hour_label.setObjectName(u"hour_label")
        self.hour_label.setMaximumSize(QSize(16777215, 23))
        self.hour_label.setFont(font4)

        self.hour_layout.addWidget(self.hour_label)

        self.hour_input = QLineEdit(self.widget)
        self.hour_input.setObjectName(u"hour_input")
        self.hour_input.setMinimumSize(QSize(500, 40))
        self.hour_input.setMaximumSize(QSize(16777215, 40))
        self.hour_input.setBaseSize(QSize(0, 0))
        self.hour_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.hour_layout.addWidget(self.hour_input)


        self.horizontalLayout.addLayout(self.hour_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startyear_layout = QVBoxLayout()
        self.startyear_layout.setSpacing(10)
        self.startyear_layout.setObjectName(u"startyear_layout")
        self.startyear_label = QLabel(self.widget)
        self.startyear_label.setObjectName(u"startyear_label")
        self.startyear_label.setMaximumSize(QSize(16777215, 23))
        self.startyear_label.setFont(font4)

        self.startyear_layout.addWidget(self.startyear_label)

        self.startyear_input = QLineEdit(self.widget)
        self.startyear_input.setObjectName(u"startyear_input")
        self.startyear_input.setMinimumSize(QSize(500, 40))
        self.startyear_input.setMaximumSize(QSize(16777215, 40))
        self.startyear_input.setBaseSize(QSize(0, 0))
        self.startyear_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.startyear_layout.addWidget(self.startyear_input)


        self.horizontalLayout_2.addLayout(self.startyear_layout)

        self.services_layout = QVBoxLayout()
        self.services_layout.setSpacing(10)
        self.services_layout.setObjectName(u"services_layout")
        self.services_label = QLabel(self.widget)
        self.services_label.setObjectName(u"services_label")
        self.services_label.setMaximumSize(QSize(16777215, 23))
        self.services_label.setFont(font4)

        self.services_layout.addWidget(self.services_label)

        self.services_input = QLineEdit(self.widget)
        self.services_input.setObjectName(u"services_input")
        self.services_input.setMinimumSize(QSize(500, 40))
        self.services_input.setMaximumSize(QSize(16777215, 40))
        self.services_input.setBaseSize(QSize(0, 0))
        self.services_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.services_layout.addWidget(self.services_input)


        self.horizontalLayout_2.addLayout(self.services_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.address_layout = QVBoxLayout()
        self.address_layout.setSpacing(10)
        self.address_layout.setObjectName(u"address_layout")
        self.address_label = QLabel(self.widget)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMaximumSize(QSize(16777215, 23))
        self.address_label.setFont(font4)

        self.address_layout.addWidget(self.address_label)

        self.address_input = QLineEdit(self.widget)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setMinimumSize(QSize(500, 40))
        self.address_input.setMaximumSize(QSize(16777215, 40))
        self.address_input.setBaseSize(QSize(0, 0))
        self.address_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.address_layout.addWidget(self.address_input)


        self.verticalLayout_2.addLayout(self.address_layout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.phone_layout = QVBoxLayout()
        self.phone_layout.setSpacing(10)
        self.phone_layout.setObjectName(u"phone_layout")
        self.phone_label = QLabel(self.widget)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setMaximumSize(QSize(16777215, 23))
        self.phone_label.setFont(font4)

        self.phone_layout.addWidget(self.phone_label)

        self.phone_input = QLineEdit(self.widget)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setMinimumSize(QSize(500, 40))
        self.phone_input.setMaximumSize(QSize(16777215, 40))
        self.phone_input.setBaseSize(QSize(0, 0))
        self.phone_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.phone_layout.addWidget(self.phone_input)


        self.horizontalLayout_3.addLayout(self.phone_layout)

        self.email_layout = QVBoxLayout()
        self.email_layout.setSpacing(10)
        self.email_layout.setObjectName(u"email_layout")
        self.email_label = QLabel(self.widget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setMaximumSize(QSize(16777215, 23))
        self.email_label.setFont(font4)

        self.email_layout.addWidget(self.email_label)

        self.email_input = QLineEdit(self.widget)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setMinimumSize(QSize(500, 40))
        self.email_input.setMaximumSize(QSize(16777215, 40))
        self.email_input.setBaseSize(QSize(0, 0))
        self.email_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.email_layout.addWidget(self.email_input)


        self.horizontalLayout_3.addLayout(self.email_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(100)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.proof_layout = QVBoxLayout()
        self.proof_layout.setSpacing(10)
        self.proof_layout.setObjectName(u"proof_layout")
        self.proof_label = QLabel(self.widget)
        self.proof_label.setObjectName(u"proof_label")
        self.proof_label.setMaximumSize(QSize(16777215, 23))
        self.proof_label.setFont(font4)

        self.proof_layout.addWidget(self.proof_label)

        self.prood_input = QLineEdit(self.widget)
        self.prood_input.setObjectName(u"prood_input")
        self.prood_input.setMinimumSize(QSize(500, 40))
        self.prood_input.setMaximumSize(QSize(16777215, 40))
        self.prood_input.setBaseSize(QSize(0, 0))
        self.prood_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.proof_layout.addWidget(self.prood_input)


        self.horizontalLayout_4.addLayout(self.proof_layout)

        self.upload_doc_btn = QPushButton(self.widget)
        self.upload_doc_btn.setObjectName(u"upload_doc_btn")
        self.upload_doc_btn.setMaximumSize(QSize(16777215, 51))
        self.upload_doc_btn.setFont(font3)
        self.upload_doc_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")

        self.horizontalLayout_4.addWidget(self.upload_doc_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.clinic_navigation.setText(QCoreApplication.translate("Form", u"Clinics", None))
        self.feedback_navigation.setText(QCoreApplication.translate("Form", u"Feedback", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
        self.noti_icon.setText("")
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Admin", None))
        self.clinic_label.setText(QCoreApplication.translate("Form", u"Add Clinic", None))
        self.clinic_img.setText("")
        self.change_img_btn.setText(QCoreApplication.translate("Form", u"Change Image", None))
        self.submit_btn.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.name.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.hour_label.setText(QCoreApplication.translate("Form", u"Operating Hours", None))
        self.startyear_label.setText(QCoreApplication.translate("Form", u"Starting year", None))
        self.services_label.setText(QCoreApplication.translate("Form", u"Types of services", None))
        self.address_label.setText(QCoreApplication.translate("Form", u"Address", None))
        self.phone_label.setText(QCoreApplication.translate("Form", u"Phone number", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"Email address", None))
        self.proof_label.setText(QCoreApplication.translate("Form", u"Submit proof of Government registered doctors", None))
        self.upload_doc_btn.setText(QCoreApplication.translate("Form", u"Upload Documents", None))
    # retranslateUi

