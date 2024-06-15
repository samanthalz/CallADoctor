from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class PA_Home(QWidget):
        
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
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
        self.clinic_req_frame.setFrameShape(QFrame.StyledPanel)
        self.clinic_req_frame.setFrameShadow(QFrame.Raised)
        self.num_clinic_req_label = QLabel(self.clinic_req_frame)
        self.num_clinic_req_label.setObjectName(u"num_clinic_req_label")
        self.num_clinic_req_label.setGeometry(QRect(20, 20, 961, 61))
        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(22)
        self.num_clinic_req_label.setFont(font)
        self.num_clinic_req_label.setWordWrap(True)
        self.clinic_req__label = QLabel(self.clinic_req_frame)
        self.clinic_req__label.setObjectName(u"clinic_req__label")
        self.clinic_req__label.setGeometry(QRect(30, 100, 51, 71))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(48)
        self.clinic_req__label.setFont(font1)
        self.details_frame = QFrame(self.background)
        self.details_frame.setObjectName(u"details_frame")
        self.details_frame.setGeometry(QRect(50, 410, 1000, 600))
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
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(11)
        self.upcoming_label.setFont(font2)
        self.upcoming_label.setStyleSheet(u"border : none;\n"
"")
        self.clinicReq_frame = QFrame(self.upcomin_appt_frame)
        self.clinicReq_frame.setObjectName(u"clinicReq_frame")
        self.clinicReq_frame.setGeometry(QRect(20, 70, 401, 81))
        self.clinicReq_frame.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame.setFrameShadow(QFrame.Raised)
        self.clinic_name_label = QLabel(self.clinicReq_frame)
        self.clinic_name_label.setObjectName(u"clinic_name_label")
        self.clinic_name_label.setGeometry(QRect(90, 30, 121, 21))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)
        self.clinic_name_label.setFont(font3)
        self.clinic_name_label.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label = QLabel(self.clinicReq_frame)
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
        self.label = QLabel(self.clinicReq_frame)
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
        self.clinicReq_frame_2 = QFrame(self.upcomin_appt_frame)
        self.clinicReq_frame_2.setObjectName(u"clinicReq_frame_2")
        self.clinicReq_frame_2.setGeometry(QRect(20, 170, 401, 81))
        self.clinicReq_frame_2.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame_2.setFrameShadow(QFrame.Raised)
        self.clinic_name_label_2 = QLabel(self.clinicReq_frame_2)
        self.clinic_name_label_2.setObjectName(u"clinic_name_label_2")
        self.clinic_name_label_2.setGeometry(QRect(90, 30, 121, 21))
        self.clinic_name_label_2.setFont(font3)
        self.clinic_name_label_2.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_2 = QLabel(self.clinicReq_frame_2)
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
        self.label_2 = QLabel(self.clinicReq_frame_2)
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
        self.request_detail_outer = QFrame(self.details_frame)
        self.request_detail_outer.setObjectName(u"request_detail_outer")
        self.request_detail_outer.setGeometry(QRect(510, 30, 450, 551))
        self.request_detail_outer.setStyleSheet(u"background-color : #ffffff;")
        self.request_detail_outer.setFrameShape(QFrame.StyledPanel)
        self.request_detail_outer.setFrameShadow(QFrame.Raised)
        self.req_detail_label = QLabel(self.request_detail_outer)
        self.req_detail_label.setObjectName(u"req_detail_label")
        self.req_detail_label.setGeometry(QRect(30, 20, 381, 41))
        self.req_detail_label.setFont(font2)
        self.req_detail_label.setStyleSheet(u"border : none;\n"
"")
        self.clinic_details_inner = QFrame(self.request_detail_outer)
        self.clinic_details_inner.setObjectName(u"clinic_details_inner")
        self.clinic_details_inner.setGeometry(QRect(20, 70, 401, 431))
        self.clinic_details_inner.setFrameShape(QFrame.StyledPanel)
        self.clinic_details_inner.setFrameShadow(QFrame.Raised)
        self.clinic_name = QLabel(self.clinic_details_inner)
        self.clinic_name.setObjectName(u"clinic_name")
        self.clinic_name.setGeometry(QRect(100, 30, 121, 21))
        self.clinic_name.setFont(font3)
        self.clinic_name.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo = QLabel(self.clinic_details_inner)
        self.clinic_logo.setObjectName(u"clinic_logo")
        self.clinic_logo.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo.setFont(font4)
        self.clinic_logo.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.clinic_details_inner)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 100, 360, 3))
        self.line.setMinimumSize(QSize(357, 3))
        self.line.setMaximumSize(QSize(16777215, 3))
        self.line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        self.line.setFrameShape(QFrame.StyledPanel)
        self.line.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.clinic_details_inner)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 120, 401, 311))
        self.layout = QVBoxLayout(self.widget)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.phone_layout = QHBoxLayout()
        self.phone_layout.setObjectName(u"phone_layout")
        self.phone_label = QLabel(self.widget)
        self.phone_label.setObjectName(u"phone_label")
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.phone_label.setFont(font6)
        self.phone_label.setStyleSheet(u"border: none;")
        self.phone_label.setLineWidth(0)

        self.phone_layout.addWidget(self.phone_label)

        self.phone_display = QLabel(self.widget)
        self.phone_display.setObjectName(u"phone_display")
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setWeight(50)
        self.phone_display.setFont(font7)
        self.phone_display.setStyleSheet(u"border: none;")

        self.phone_layout.addWidget(self.phone_display)


        self.layout.addLayout(self.phone_layout)

        self.email_layout = QHBoxLayout()
        self.email_layout.setObjectName(u"email_layout")
        self.email_label = QLabel(self.widget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font6)
        self.email_label.setStyleSheet(u"border: none;")

        self.email_layout.addWidget(self.email_label)

        self.email_display = QLabel(self.widget)
        self.email_display.setObjectName(u"email_display")
        self.email_display.setFont(font7)
        self.email_display.setStyleSheet(u"border: none;")

        self.email_layout.addWidget(self.email_display)


        self.layout.addLayout(self.email_layout)

        self.add_layout = QHBoxLayout()
        self.add_layout.setSpacing(135)
        self.add_layout.setObjectName(u"add_layout")
        self.add_label = QLabel(self.widget)
        self.add_label.setObjectName(u"add_label")
        self.add_label.setFont(font6)
        self.add_label.setStyleSheet(u"border: none;")

        self.add_layout.addWidget(self.add_label)

        self.add_display = QLabel(self.widget)
        self.add_display.setObjectName(u"add_display")
        self.add_display.setFont(font7)
        self.add_display.setStyleSheet(u"border: none;")
        self.add_display.setScaledContents(False)
        self.add_display.setWordWrap(True)

        self.add_layout.addWidget(self.add_display)


        self.layout.addLayout(self.add_layout)

        self.opening_hr_layout = QHBoxLayout()
        self.opening_hr_layout.setObjectName(u"opening_hr_layout")
        self.opening_hr_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.opening_hr_text = QLabel(self.widget)
        self.opening_hr_text.setObjectName(u"opening_hr_text")
        self.opening_hr_text.setFont(font6)
        self.opening_hr_text.setStyleSheet(u"border: none;")
        self.opening_hr_text.setWordWrap(True)

        self.opening_hr_layout.addWidget(self.opening_hr_text)

        self.hour_display = QLabel(self.widget)
        self.hour_display.setObjectName(u"hour_display")
        self.hour_display.setFont(font7)
        self.hour_display.setStyleSheet(u"border: none;")
        self.hour_display.setScaledContents(False)
        self.hour_display.setWordWrap(True)

        self.opening_hr_layout.addWidget(self.hour_display)


        self.layout.addLayout(self.opening_hr_layout)

        self.view_detail_btn = QPushButton(self.request_detail_outer)
        self.view_detail_btn.setObjectName(u"view_detail_btn")
        self.view_detail_btn.setGeometry(QRect(320, 510, 93, 28))
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(9)
        font8.setUnderline(True)
        self.view_detail_btn.setFont(font8)
        self.view_detail_btn.setStyleSheet(u"color: #007E85; border: none;")
        self.feedback_frame = QFrame(self.background)
        self.feedback_frame.setObjectName(u"feedback_frame")
        self.feedback_frame.setGeometry(QRect(1120, 170, 481, 831))
        self.feedback_frame.setStyleSheet(u"border: 2px solid #FFFFFF;\n"
"border-radius: 16px;\n"
"background-color: white")
        self.feedback_frame.setFrameShape(QFrame.StyledPanel)
        self.feedback_frame.setFrameShadow(QFrame.Raised)
        self.feedback_label = QLabel(self.feedback_frame)
        self.feedback_label.setObjectName(u"feedback_label")
        self.feedback_label.setGeometry(QRect(20, 10, 441, 41))
        self.feedback_label.setFont(font2)
        self.feedback_label.setStyleSheet(u"border : none;\n"
"")
        self.feedback_detail_frame = QFrame(self.feedback_frame)
        self.feedback_detail_frame.setObjectName(u"feedback_detail_frame")
        self.feedback_detail_frame.setGeometry(QRect(20, 70, 401, 81))
        self.feedback_detail_frame.setFrameShape(QFrame.StyledPanel)
        self.feedback_detail_frame.setFrameShadow(QFrame.Raised)
        self.name_display = QLabel(self.feedback_detail_frame)
        self.name_display.setObjectName(u"name_display")
        self.name_display.setGeometry(QRect(30, 10, 121, 21))
        self.name_display.setFont(font6)
        self.name_display.setStyleSheet(u"border : none;\n"
"")
        self.date_feedback_display = QLabel(self.feedback_detail_frame)
        self.date_feedback_display.setObjectName(u"date_feedback_display")
        self.date_feedback_display.setGeometry(QRect(30, 40, 121, 21))
        self.date_feedback_display.setFont(font5)
        self.date_feedback_display.setStyleSheet(u"border : none;\n"
"")
        self.view_feedback_btn = QPushButton(self.feedback_detail_frame)
        self.view_feedback_btn.setObjectName(u"view_feedback_btn")
        self.view_feedback_btn.setGeometry(QRect(290, 20, 93, 51))
        self.view_feedback_btn.setFont(font5)
        self.view_feedback_btn.setStyleSheet(u"background-color: #B6D0E2;\n"
"color: white; text-align: center;")
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
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(31, 20, 87, 851))
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

        self.verticalLayout.addWidget(self.home_navigation)

        self.clinic_navigation = QToolButton(self.widget)
        self.clinic_navigation.setObjectName(u"clinic_navigation")
        self.clinic_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.clinic_navigation.sizePolicy().hasHeightForWidth())
        self.clinic_navigation.setSizePolicy(sizePolicy)
        self.clinic_navigation.setMinimumSize(QSize(85, 96))
        self.clinic_navigation.setMaximumSize(QSize(85, 96))
        self.clinic_navigation.setFont(font10)
        self.clinic_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"../Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clinic_navigation.setIcon(icon2)
        self.clinic_navigation.setIconSize(QSize(70, 70))
        self.clinic_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.clinic_navigation)

        self.feedback_navigation = QToolButton(self.widget)
        self.feedback_navigation.setObjectName(u"feedback_navigation")
        self.feedback_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.feedback_navigation.sizePolicy().hasHeightForWidth())
        self.feedback_navigation.setSizePolicy(sizePolicy)
        self.feedback_navigation.setMinimumSize(QSize(85, 96))
        self.feedback_navigation.setMaximumSize(QSize(85, 96))
        self.feedback_navigation.setFont(font10)
        self.feedback_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"../Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.feedback_navigation.setIcon(icon3)
        self.feedback_navigation.setIconSize(QSize(70, 70))
        self.feedback_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.feedback_navigation)

        self.settings_navigation = QToolButton(self.widget)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setMinimumSize(QSize(85, 96))
        self.settings_navigation.setMaximumSize(QSize(85, 96))
        self.settings_navigation.setFont(font10)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"../Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.widget)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setMinimumSize(QSize(85, 96))
        self.logout_navigation.setMaximumSize(QSize(85, 96))
        self.logout_navigation.setFont(font10)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon5 = QIcon()
        icon5.addFile(u"../Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.num_clinic_req_label.setText(QCoreApplication.translate("Form", u"Total Clinic Addition Request:", None))
        self.clinic_req__label.setText(QCoreApplication.translate("Form", u"2", None))
        self.upcoming_label.setText(QCoreApplication.translate("Form", u"Clinic List", None))
        self.clinic_name_label.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label.setText(QCoreApplication.translate("Form", u"A", None))
        self.label.setText(QCoreApplication.translate("Form", u"Approved", None))
        self.clinic_name_label_2.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label_2.setText(QCoreApplication.translate("Form", u"A", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pending", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Recent", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Oldest", None))

        self.req_detail_label.setText(QCoreApplication.translate("Form", u"Request Details", None))
        self.clinic_name.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo.setText(QCoreApplication.translate("Form", u"A", None))
        self.phone_label.setText(QCoreApplication.translate("Form", u"Phone: ", None))
        self.phone_display.setText(QCoreApplication.translate("Form", u"+60322845678", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.email_display.setText(QCoreApplication.translate("Form", u"info@bangsarclinic.my", None))
        self.add_label.setText(QCoreApplication.translate("Form", u"Address:", None))
        self.add_display.setText(QCoreApplication.translate("Form", u"No. 23, Jalan Telawi 3, Bangsar Baru, 59100 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur, Malaysia.", None))
        self.opening_hr_text.setText(QCoreApplication.translate("Form", u"Operating Hours:", None))
        self.hour_display.setText(QCoreApplication.translate("Form", u"24 Hours", None))
        self.view_detail_btn.setText(QCoreApplication.translate("Form", u"View More", None))
        self.feedback_label.setText(QCoreApplication.translate("Form", u"Feedbacks", None))
        self.name_display.setText(QCoreApplication.translate("Form", u"Name", None))
        self.date_feedback_display.setText(QCoreApplication.translate("Form", u"Date", None))
        self.view_feedback_btn.setText(QCoreApplication.translate("Form", u"View", None))
        self.noti_icon.setText("")
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.feedback_navigation.setText(QCoreApplication.translate("Form", u"Feedbacks", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

