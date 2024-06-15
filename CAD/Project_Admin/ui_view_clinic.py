from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class ViewClinicWidget(QWidget):
        
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
        font.setPointSize(16)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet(u"border: none")
        self.search_clinic = QLineEdit(self.background)
        self.search_clinic.setObjectName(u"search_clinic")
        self.search_clinic.setGeometry(QRect(40, 40, 831, 71))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(11)
        self.search_clinic.setFont(font1)
        self.search_clinic.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 60px; color: Black;\n"
" background-image: url(\"C:/Users/Samantha Law/Documents/INTI/CAD/CallADoctor/CAD/Images/icon/search_icon.png\"); \n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")
        self.search_clinic.setClearButtonEnabled(False)
        self.request_detail_outer = QFrame(self.background)
        self.request_detail_outer.setObjectName(u"request_detail_outer")
        self.request_detail_outer.setGeometry(QRect(979, 200, 751, 841))
        self.request_detail_outer.setStyleSheet(u"background-color : #ffffff;")
        self.request_detail_outer.setFrameShape(QFrame.StyledPanel)
        self.request_detail_outer.setFrameShadow(QFrame.Raised)
        self.clinic_details_inner = QFrame(self.request_detail_outer)
        self.clinic_details_inner.setObjectName(u"clinic_details_inner")
        self.clinic_details_inner.setGeometry(QRect(20, 20, 711, 771))
        self.clinic_details_inner.setFrameShape(QFrame.StyledPanel)
        self.clinic_details_inner.setFrameShadow(QFrame.Raised)
        self.clinic_name = QLabel(self.clinic_details_inner)
        self.clinic_name.setObjectName(u"clinic_name")
        self.clinic_name.setGeometry(QRect(100, 30, 121, 21))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(10)
        self.clinic_name.setFont(font2)
        self.clinic_name.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo = QLabel(self.clinic_details_inner)
        self.clinic_logo.setObjectName(u"clinic_logo")
        self.clinic_logo.setGeometry(QRect(10, 10, 54, 54))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(9)
        self.clinic_logo.setFont(font3)
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
        self.line.setGeometry(QRect(20, 100, 671, 3))
        self.line.setMinimumSize(QSize(357, 3))
        self.line.setMaximumSize(QSize(16777215, 3))
        self.line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        self.line.setFrameShape(QFrame.StyledPanel)
        self.line.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.clinic_details_inner)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(3, 123, 701, 641))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.phone_layout = QHBoxLayout()
        self.phone_layout.setObjectName(u"phone_layout")
        self.phone_label = QLabel(self.layoutWidget)
        self.phone_label.setObjectName(u"phone_label")
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.phone_label.setFont(font4)
        self.phone_label.setStyleSheet(u"border: none;")
        self.phone_label.setLineWidth(0)

        self.phone_layout.addWidget(self.phone_label)

        self.phone_display = QLabel(self.layoutWidget)
        self.phone_display.setObjectName(u"phone_display")
        self.phone_display.setMinimumSize(QSize(390, 102))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setWeight(50)
        self.phone_display.setFont(font5)
        self.phone_display.setStyleSheet(u"border: none;")

        self.phone_layout.addWidget(self.phone_display)


        self.verticalLayout_2.addLayout(self.phone_layout)

        self.email_layout = QHBoxLayout()
        self.email_layout.setObjectName(u"email_layout")
        self.email_label = QLabel(self.layoutWidget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font4)
        self.email_label.setStyleSheet(u"border: none;")

        self.email_layout.addWidget(self.email_label)

        self.email_display = QLabel(self.layoutWidget)
        self.email_display.setObjectName(u"email_display")
        self.email_display.setMinimumSize(QSize(390, 102))
        self.email_display.setFont(font5)
        self.email_display.setStyleSheet(u"border: none;")

        self.email_layout.addWidget(self.email_display)


        self.verticalLayout_2.addLayout(self.email_layout)

        self.add_layout = QHBoxLayout()
        self.add_layout.setSpacing(135)
        self.add_layout.setObjectName(u"add_layout")
        self.add_label = QLabel(self.layoutWidget)
        self.add_label.setObjectName(u"add_label")
        self.add_label.setFont(font4)
        self.add_label.setStyleSheet(u"border: none;")

        self.add_layout.addWidget(self.add_label)

        self.add_display = QLabel(self.layoutWidget)
        self.add_display.setObjectName(u"add_display")
        self.add_display.setFont(font5)
        self.add_display.setStyleSheet(u"border: none;")
        self.add_display.setScaledContents(False)
        self.add_display.setWordWrap(True)

        self.add_layout.addWidget(self.add_display)


        self.verticalLayout_2.addLayout(self.add_layout)

        self.opening_hr_layout = QHBoxLayout()
        self.opening_hr_layout.setObjectName(u"opening_hr_layout")
        self.opening_hr_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.opening_hr_label = QLabel(self.layoutWidget)
        self.opening_hr_label.setObjectName(u"opening_hr_label")
        self.opening_hr_label.setFont(font4)
        self.opening_hr_label.setStyleSheet(u"border: none;")
        self.opening_hr_label.setWordWrap(True)

        self.opening_hr_layout.addWidget(self.opening_hr_label)

        self.hour_display = QLabel(self.layoutWidget)
        self.hour_display.setObjectName(u"hour_display")
        self.hour_display.setMinimumSize(QSize(390, 0))
        self.hour_display.setFont(font5)
        self.hour_display.setStyleSheet(u"border: none;")
        self.hour_display.setScaledContents(False)
        self.hour_display.setWordWrap(True)

        self.opening_hr_layout.addWidget(self.hour_display)


        self.verticalLayout_2.addLayout(self.opening_hr_layout)

        self.doc_layout = QHBoxLayout()
        self.doc_layout.setSpacing(0)
        self.doc_layout.setObjectName(u"doc_layout")
        self.doc_label = QLabel(self.layoutWidget)
        self.doc_label.setObjectName(u"doc_label")
        self.doc_label.setFont(font4)
        self.doc_label.setStyleSheet(u"border: none;")
        self.doc_label.setWordWrap(True)

        self.doc_layout.addWidget(self.doc_label)

        self.doc_display = QLabel(self.layoutWidget)
        self.doc_display.setObjectName(u"doc_display")
        self.doc_display.setMinimumSize(QSize(200, 0))
        self.doc_display.setMaximumSize(QSize(50, 16777215))
        self.doc_display.setFont(font5)
        self.doc_display.setStyleSheet(u"border: none;")
        self.doc_display.setScaledContents(False)
        self.doc_display.setWordWrap(True)

        self.doc_layout.addWidget(self.doc_display)

        self.view_doc_btn = QPushButton(self.layoutWidget)
        self.view_doc_btn.setObjectName(u"view_doc_btn")
        self.view_doc_btn.setMaximumSize(QSize(190, 16777215))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(9)
        font6.setUnderline(True)
        self.view_doc_btn.setFont(font6)
        self.view_doc_btn.setStyleSheet(u"color: #007E85; border: none;")

        self.doc_layout.addWidget(self.view_doc_btn)


        self.verticalLayout_2.addLayout(self.doc_layout)

        self.date_req_layout = QHBoxLayout()
        self.date_req_layout.setObjectName(u"date_req_layout")
        self.date_req_label = QLabel(self.layoutWidget)
        self.date_req_label.setObjectName(u"date_req_label")
        self.date_req_label.setFont(font4)
        self.date_req_label.setStyleSheet(u"border: none;")
        self.date_req_label.setWordWrap(True)

        self.date_req_layout.addWidget(self.date_req_label)

        self.date_req_display = QLabel(self.layoutWidget)
        self.date_req_display.setObjectName(u"date_req_display")
        self.date_req_display.setMinimumSize(QSize(390, 0))
        self.date_req_display.setFont(font5)
        self.date_req_display.setStyleSheet(u"border: none;")
        self.date_req_display.setScaledContents(False)
        self.date_req_display.setWordWrap(True)

        self.date_req_layout.addWidget(self.date_req_display)


        self.verticalLayout_2.addLayout(self.date_req_layout)

        self.change_img_btn = QPushButton(self.request_detail_outer)
        self.change_img_btn.setObjectName(u"change_img_btn")
        self.change_img_btn.setGeometry(QRect(550, 790, 181, 41))
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.change_img_btn.setFont(font7)
        self.change_img_btn.setStyleSheet(u"background-color: #E73030; border-radius: 16px; color: white;\\n border: 1px solid gray;")
        self.filter = QComboBox(self.background)
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.setObjectName(u"filter")
        self.filter.setGeometry(QRect(710, 170, 151, 31))
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(12)
        self.filter.setFont(font8)
        self.filter.setStyleSheet(u"\n"
"border: 1px solid gray;")
        self.upcoming_label = QLabel(self.background)
        self.upcoming_label.setObjectName(u"upcoming_label")
        self.upcoming_label.setGeometry(QRect(50, 160, 341, 41))
        font9 = QFont()
        font9.setFamily(u"Cascadia Code")
        font9.setPointSize(16)
        self.upcoming_label.setFont(font9)
        self.upcoming_label.setStyleSheet(u"border : none;\n"
"")
        self.clinic_frame_2 = QFrame(self.background)
        self.clinic_frame_2.setObjectName(u"clinic_frame_2")
        self.clinic_frame_2.setGeometry(QRect(60, 390, 801, 81))
        self.clinic_frame_2.setFrameShape(QFrame.StyledPanel)
        self.clinic_frame_2.setFrameShadow(QFrame.Raised)
        self.clinic_name_label_2 = QLabel(self.clinic_frame_2)
        self.clinic_name_label_2.setObjectName(u"clinic_name_label_2")
        self.clinic_name_label_2.setGeometry(QRect(90, 30, 121, 21))
        self.clinic_name_label_2.setFont(font2)
        self.clinic_name_label_2.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_2 = QLabel(self.clinic_frame_2)
        self.clinic_logo_label_2.setObjectName(u"clinic_logo_label_2")
        self.clinic_logo_label_2.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_2.setFont(font3)
        self.clinic_logo_label_2.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_2.setAlignment(Qt.AlignCenter)
        self.status_2 = QLabel(self.clinic_frame_2)
        self.status_2.setObjectName(u"status_2")
        self.status_2.setGeometry(QRect(690, 20, 91, 41))
        font10 = QFont()
        font10.setFamily(u"Consolas")
        font10.setPointSize(10)
        self.status_2.setFont(font10)
        self.status_2.setStyleSheet(u"background-color: rgba(246, 32, 136, 0.15);\n"
"color: #F62088; text-align: center;\n"
"")
        self.status_2.setAlignment(Qt.AlignCenter)
        self.clinic_frame = QFrame(self.background)
        self.clinic_frame.setObjectName(u"clinic_frame")
        self.clinic_frame.setGeometry(QRect(60, 290, 801, 81))
        self.clinic_frame.setFrameShape(QFrame.StyledPanel)
        self.clinic_frame.setFrameShadow(QFrame.Raised)
        self.clinic_name_label = QLabel(self.clinic_frame)
        self.clinic_name_label.setObjectName(u"clinic_name_label")
        self.clinic_name_label.setGeometry(QRect(90, 30, 121, 21))
        self.clinic_name_label.setFont(font2)
        self.clinic_name_label.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label = QLabel(self.clinic_frame)
        self.clinic_logo_label.setObjectName(u"clinic_logo_label")
        self.clinic_logo_label.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label.setFont(font3)
        self.clinic_logo_label.setStyleSheet(u"background-color: #B6D0E2; \n"
"border-radius: 25px; \n"
"border: 2px solid #B6D0F7; \n"
"min-width: 50px; \n"
"min-height: 50px; \n"
"max-width: 50px;\n"
"max-height: 50px; ")
        self.clinic_logo_label.setAlignment(Qt.AlignCenter)
        self.status = QLabel(self.clinic_frame)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(690, 20, 91, 41))
        self.status.setFont(font10)
        self.status.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);\n"
"color: #128983; text-align: center;\n"
"")
        self.status.setAlignment(Qt.AlignCenter)
        self.req_detail_label = QLabel(self.background)
        self.req_detail_label.setObjectName(u"req_detail_label")
        self.req_detail_label.setGeometry(QRect(990, 150, 571, 41))
        self.req_detail_label.setFont(font)
        self.req_detail_label.setStyleSheet(u"border : none;\n"
"")
        self.view_feedback_btn = QPushButton(self.background)
        self.view_feedback_btn.setObjectName(u"view_feedback_btn")
        self.view_feedback_btn.setGeometry(QRect(60, 220, 801, 51))
        font11 = QFont()
        font11.setFamily(u"Consolas")
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setWeight(75)
        self.view_feedback_btn.setFont(font11)
        self.view_feedback_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
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
        font12 = QFont()
        font12.setFamily(u"Source Sans Pro Semibold")
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setWeight(75)
        self.home_navigation.setFont(font12)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
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
        self.clinic_navigation.setFont(font12)
        self.clinic_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clinic_navigation.setIcon(icon2)
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
        self.feedback_navigation.setFont(font12)
        self.feedback_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.feedback_navigation.setIcon(icon3)
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
        self.settings_navigation.setFont(font12)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
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
        self.logout_navigation.setFont(font12)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon5 = QIcon()
        icon5.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.noti_icon.setText("")
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Admin", None))
        self.search_clinic.setText("")
        self.search_clinic.setPlaceholderText(QCoreApplication.translate("Form", u"Search Clinic Name", None))
        self.clinic_name.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo.setText(QCoreApplication.translate("Form", u"A", None))
        self.phone_label.setText(QCoreApplication.translate("Form", u"Phone: ", None))
        self.phone_display.setText(QCoreApplication.translate("Form", u"+60322845678", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.email_display.setText(QCoreApplication.translate("Form", u"info@bangsarclinic.my", None))
        self.add_label.setText(QCoreApplication.translate("Form", u"Address:", None))
        self.add_display.setText(QCoreApplication.translate("Form", u"No. 23, Jalan Telawi 3, Bangsar Baru, 59100 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur, Malaysia.", None))
        self.opening_hr_label.setText(QCoreApplication.translate("Form", u"Operating Hours:", None))
        self.hour_display.setText(QCoreApplication.translate("Form", u"24 Hours", None))
        self.doc_label.setText(QCoreApplication.translate("Form", u"Documents", None))
        self.doc_display.setText(QCoreApplication.translate("Form", u"Yes", None))
        self.view_doc_btn.setText(QCoreApplication.translate("Form", u"View Document", None))
        self.date_req_label.setText(QCoreApplication.translate("Form", u"Date of request", None))
        self.date_req_display.setText(QCoreApplication.translate("Form", u"31 May 2024", None))
        self.change_img_btn.setText(QCoreApplication.translate("Form", u"Remove Clinic", None))
        self.filter.setItemText(0, QCoreApplication.translate("Form", u"Recent", None))
        self.filter.setItemText(1, QCoreApplication.translate("Form", u"Oldest", None))

        self.upcoming_label.setText(QCoreApplication.translate("Form", u"Clinic List", None))
        self.clinic_name_label_2.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label_2.setText(QCoreApplication.translate("Form", u"A", None))
        self.status_2.setText(QCoreApplication.translate("Form", u"Pending", None))
        self.clinic_name_label.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label.setText(QCoreApplication.translate("Form", u"A", None))
        self.status.setText(QCoreApplication.translate("Form", u"Approved", None))
        self.req_detail_label.setText(QCoreApplication.translate("Form", u"Clinic Details", None))
        self.view_feedback_btn.setText(QCoreApplication.translate("Form", u"Add New Clinic", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.clinic_navigation.setText(QCoreApplication.translate("Form", u"Clinics", None))
        self.feedback_navigation.setText(QCoreApplication.translate("Form", u"Feedback", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

