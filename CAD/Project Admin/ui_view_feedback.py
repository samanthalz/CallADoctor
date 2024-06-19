from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class ViewFeedbackWidget(QWidget):

    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        
        Form.setAutoFillBackground(True)
        p = Form.palette()
        p.setColor(Form.backgroundRole(), QColor('#B6D0E2'))
        Form.setPalette(p)
        
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 141, 891))
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
        icon.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon1.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon2.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon4.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon5.addFile(u"CAD/Images/icon/notification.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.name_label = QLabel(self.background)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(60, 170, 221, 61))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(18)
        self.name_label.setFont(font2)
        self.name_label.setWordWrap(True)
        self.back_button = QPushButton(self.background)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setEnabled(True)
        self.back_button.setGeometry(QRect(40, 50, 301, 71))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.back_button.setFont(font3)
        self.back_button.setAutoFillBackground(False)
        self.back_button.setStyleSheet(u"background-color: rgba(182, 208, 226,0.8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-left: 30px;\n"
"text-align: left;")
        self.back_button.setIconSize(QSize(70, 70))
        self.fb_outer_frame = QFrame(self.background)
        self.fb_outer_frame.setObjectName(u"fb_outer_frame")
        self.fb_outer_frame.setGeometry(QRect(60, 230, 1661, 801))
        self.fb_outer_frame.setStyleSheet(u"border: 1px solid #dcdcdc; border-radius: 8px; margin: 5px;")
        self.fb_outer_frame.setFrameShape(QFrame.StyledPanel)
        self.fb_outer_frame.setFrameShadow(QFrame.Raised)
        self.fb_inner_frame = QFrame(self.fb_outer_frame)
        self.fb_inner_frame.setObjectName(u"fb_inner_frame")
        self.fb_inner_frame.setGeometry(QRect(0, 0, 1661, 771))
        self.fb_inner_frame.setStyleSheet(u" border: none; background-color: transparent;")
        self.fb_inner_frame.setFrameShape(QFrame.StyledPanel)
        self.fb_inner_frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.fb_inner_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 30, 1585, 721))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.subject_layout = QVBoxLayout()
        self.subject_layout.setObjectName(u"subject_layout")
        self.subject_label = QLabel(self.layoutWidget)
        self.subject_label.setObjectName(u"subject_label")
        self.subject_label.setFont(font1)
        self.subject_label.setWordWrap(True)

        self.subject_layout.addWidget(self.subject_label)

        self.subject_display = QLabel(self.layoutWidget)
        self.subject_display.setObjectName(u"subject_display")
        self.subject_display.setMinimumSize(QSize(1581, 60))
        self.subject_display.setMaximumSize(QSize(1581, 60))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(10)
        self.subject_display.setFont(font4)
        self.subject_display.setStyleSheet(u"background-color: white; border: none; border-radius: 0; padding-left: 10px;")
        self.subject_display.setScaledContents(False)
        self.subject_display.setWordWrap(False)

        self.subject_layout.addWidget(self.subject_display)


        self.verticalLayout_2.addLayout(self.subject_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.email_layout = QVBoxLayout()
        self.email_layout.setObjectName(u"email_layout")
        self.email_label = QLabel(self.layoutWidget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font1)
        self.email_label.setWordWrap(True)

        self.email_layout.addWidget(self.email_label)

        self.email_display = QLabel(self.layoutWidget)
        self.email_display.setObjectName(u"email_display")
        self.email_display.setMinimumSize(QSize(0, 60))
        self.email_display.setMaximumSize(QSize(16777215, 60))
        self.email_display.setFont(font4)
        self.email_display.setStyleSheet(u"background-color: white; border: none; border-radius: 0; padding-left: 10px;")

        self.email_layout.addWidget(self.email_display)


        self.verticalLayout_2.addLayout(self.email_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.feeback_layout = QVBoxLayout()
        self.feeback_layout.setObjectName(u"feeback_layout")
        self.feedback_label = QLabel(self.layoutWidget)
        self.feedback_label.setObjectName(u"feedback_label")
        self.feedback_label.setFont(font1)
        self.feedback_label.setWordWrap(True)

        self.feeback_layout.addWidget(self.feedback_label)

        self.feedback_display = QLabel(self.layoutWidget)
        self.feedback_display.setObjectName(u"feedback_display")
        self.feedback_display.setMinimumSize(QSize(0, 270))
        self.feedback_display.setMaximumSize(QSize(16777215, 270))
        self.feedback_display.setFont(font4)
        self.feedback_display.setStyleSheet(u"background-color: white; border: none; border-radius: 0; padding-left: 10px;")
        self.feedback_display.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.feeback_layout.addWidget(self.feedback_display)


        self.verticalLayout_2.addLayout(self.feeback_layout)


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
        self.name_label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.back_button.setText(QCoreApplication.translate("Form", u"< Back to Inbox", None))
        self.subject_label.setText(QCoreApplication.translate("Form", u"Subject", None))
        self.subject_display.setText(QCoreApplication.translate("Form", u"Compliment", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"Email Address", None))
        self.email_display.setText(QCoreApplication.translate("Form", u"email@andrewfakedomain.net", None))
        self.feedback_label.setText(QCoreApplication.translate("Form", u"Feedback", None))
        self.feedback_display.setText(QCoreApplication.translate("Form", u"The features are convenient to use!", None))
    # retranslateUi

