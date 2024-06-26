from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class ServicesWidget(QWidget):
    fad_btn_clicked = pyqtSignal()
    fac_btn_clicked = pyqtSignal()
    makeAppt_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    schedule_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    
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
        
        self.whitebg = QWidget(Form)
        self.whitebg.setObjectName(u"whitebg")
        self.whitebg.setGeometry(QRect(150, 0, 1771, 1080))
        self.whitebg.setStyleSheet(u"background-color: #F8F8F8;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-left-radius: 30px;")
        
        self.services_avail_title = QLabel(self.whitebg)
        self.services_avail_title.setObjectName(u"services_avail_title")
        self.services_avail_title.setGeometry(QRect(60, 40, 481, 81))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.services_avail_title.setFont(font)
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
        self.fadoctor_outer_frame = QFrame(self.whitebg)
        self.fadoctor_outer_frame.setObjectName(u"fadoctor_outer_frame")
        self.fadoctor_outer_frame.setGeometry(QRect(554, 191, 413, 539))
        self.fadoctor_outer_frame.setStyleSheet(u"border: 2px solid #B6D0E2; border-radius: 20px; ")
        self.fadoctor_outer_frame.setFrameShape(QFrame.StyledPanel)
        self.fadoctor_outer_frame.setFrameShadow(QFrame.Raised)
        self.fadoctor_inner_frame = QFrame(self.fadoctor_outer_frame)
        self.fadoctor_inner_frame.setObjectName(u"fadoctor_inner_frame")
        self.fadoctor_inner_frame.setGeometry(QRect(0, 0, 411, 551))
        self.fadoctor_inner_frame.setStyleSheet(u"border: none; margin: 0; padding:0; background-color: rgba(255, 255, 255, 0.5)")
        self.fadoctor_inner_frame.setFrameShape(QFrame.StyledPanel)
        self.fadoctor_inner_frame.setFrameShadow(QFrame.Plain)
        self.fadoctor_inner_frame.setLineWidth(0)
        self.fadoctor_inner_frame.setMidLineWidth(0)
        self.fadoctor_btn = QPushButton(self.fadoctor_inner_frame)
        self.fadoctor_btn.setObjectName(u"fadoctor_btn")
        self.fadoctor_btn.setGeometry(QRect(20, 480, 81, 41))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(14)
        self.fadoctor_btn.setFont(font2)
        self.fadoctor_btn.setStyleSheet(u"border: 2px solid #B6D0E2; border-radius: 10; background-color: #B6D0E2; color: white")
        self.fadoctor_btn.clicked.connect(self.emitFadBtn)
        
        self.layoutWidget = QWidget(self.fadoctor_inner_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 371, 451))
        self.fad_info_layout = QVBoxLayout(self.layoutWidget)
        self.fad_info_layout.setObjectName(u"fad_info_layout")
        self.fad_info_layout.setContentsMargins(0, 0, 0, 0)
        self.fadoctor_img = QLabel(self.layoutWidget)
        self.fadoctor_img.setObjectName(u"fadoctor_img")
        self.fadoctor_img.setStyleSheet(u"border: none; ")
        self.fadoctor_img.setPixmap(QPixmap(u"CAD/Images/services/services_doctor.png"))
        self.fadoctor_img.setScaledContents(True)

        self.fad_info_layout.addWidget(self.fadoctor_img)

        self.horizontalSpacer_5 = QSpacerItem(348, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.fad_info_layout.addItem(self.horizontalSpacer_5)

        self.fad_title_layout = QHBoxLayout()
        self.fad_title_layout.setObjectName(u"fad_title_layout")
        self.fadoctor_title = QLabel(self.layoutWidget)
        self.fadoctor_title.setObjectName(u"fadoctor_title")
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.fadoctor_title.setFont(font3)
        self.fadoctor_title.setStyleSheet(u"border: none;")
        self.fadoctor_title.setScaledContents(False)

        self.fad_title_layout.addWidget(self.fadoctor_title)

        self.horizontalSpacer_6 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.fad_title_layout.addItem(self.horizontalSpacer_6)


        self.fad_info_layout.addLayout(self.fad_title_layout)

        self.fadoctor_text = QLabel(self.layoutWidget)
        self.fadoctor_text.setObjectName(u"fadoctor_text")
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(10)
        self.fadoctor_text.setFont(font4)
        self.fadoctor_text.setStyleSheet(u"border: none;")
        self.fadoctor_text.setScaledContents(False)
        self.fadoctor_text.setWordWrap(True)

        self.fad_info_layout.addWidget(self.fadoctor_text)

        self.horizontalSpacer_7 = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.fad_info_layout.addItem(self.horizontalSpacer_7)

        self.faclinic_outer_frame = QFrame(self.whitebg)
        self.faclinic_outer_frame.setObjectName(u"faclinic_outer_frame")
        self.faclinic_outer_frame.setGeometry(QRect(91, 191, 413, 539))
        self.faclinic_outer_frame.setStyleSheet(u"border: 2px solid #B6D0E2; border-radius: 20px; ")
        self.faclinic_outer_frame.setFrameShape(QFrame.StyledPanel)
        self.faclinic_outer_frame.setFrameShadow(QFrame.Raised)
        self.faclinic_inner_frame = QFrame(self.faclinic_outer_frame)
        self.faclinic_inner_frame.setObjectName(u"faclinic_inner_frame")
        self.faclinic_inner_frame.setGeometry(QRect(0, 0, 411, 551))
        self.faclinic_inner_frame.setStyleSheet(u"border: none; margin: 0; padding:0; background-color: rgba(255, 255, 255, 0.5)")
        self.faclinic_inner_frame.setFrameShape(QFrame.StyledPanel)
        self.faclinic_inner_frame.setFrameShadow(QFrame.Plain)
        self.faclinic_inner_frame.setLineWidth(0)
        self.faclinic_inner_frame.setMidLineWidth(0)
        self.faclinic_btn = QPushButton(self.faclinic_inner_frame)
        self.faclinic_btn.setObjectName(u"faclinic_btn")
        self.faclinic_btn.setGeometry(QRect(20, 480, 81, 41))
        self.faclinic_btn.setFont(font2)
        self.faclinic_btn.setStyleSheet(u"border: 2px solid #B6D0E2; border-radius: 10; background-color: #B6D0E2; color: white")
        self.faclinic_btn.clicked.connect(self.emitFacBtn)
        
        self.layoutWidget_3 = QWidget(self.faclinic_inner_frame)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 30, 371, 451))
        self.faclinic_info_layout = QVBoxLayout(self.layoutWidget_3)
        self.faclinic_info_layout.setObjectName(u"faclinic_info_layout")
        self.faclinic_info_layout.setContentsMargins(0, 0, 0, 0)
        self.faclinic_img = QLabel(self.layoutWidget_3)
        self.faclinic_img.setObjectName(u"faclinic_img")
        self.faclinic_img.setStyleSheet(u"border: none; ")
        self.faclinic_img.setPixmap(QPixmap(u"CAD/Images/services/services_findClinic.png"))
        self.faclinic_img.setScaledContents(True)

        self.faclinic_info_layout.addWidget(self.faclinic_img)

        self.horizontalSpacer_11 = QSpacerItem(348, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.faclinic_info_layout.addItem(self.horizontalSpacer_11)

        self.faclinic_title_layout = QHBoxLayout()
        self.faclinic_title_layout.setObjectName(u"faclinic_title_layout")
        self.faclinic_title = QLabel(self.layoutWidget_3)
        self.faclinic_title.setObjectName(u"faclinic_title")
        self.faclinic_title.setFont(font3)
        self.faclinic_title.setStyleSheet(u"border: none;")
        self.faclinic_title.setScaledContents(False)

        self.faclinic_title_layout.addWidget(self.faclinic_title)

        self.horizontalSpacer_12 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.faclinic_title_layout.addItem(self.horizontalSpacer_12)


        self.faclinic_info_layout.addLayout(self.faclinic_title_layout)

        self.faclinic_text = QLabel(self.layoutWidget_3)
        self.faclinic_text.setObjectName(u"faclinic_text")
        self.faclinic_text.setFont(font4)
        self.faclinic_text.setStyleSheet(u"border: none;")
        self.faclinic_text.setScaledContents(False)
        self.faclinic_text.setWordWrap(True)

        self.faclinic_info_layout.addWidget(self.faclinic_text)

        self.horizontalSpacer_13 = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.faclinic_info_layout.addItem(self.horizontalSpacer_13)

        self.makeAppt_outer_frame = QFrame(self.whitebg)
        self.makeAppt_outer_frame.setObjectName(u"makeAppt_outer_frame")
        self.makeAppt_outer_frame.setGeometry(QRect(1017, 191, 413, 539))
        self.makeAppt_outer_frame.setStyleSheet(u"border: 2px solid #B6D0E2; border-radius: 20px; ")
        self.makeAppt_outer_frame.setFrameShape(QFrame.StyledPanel)
        self.makeAppt_outer_frame.setFrameShadow(QFrame.Raised)
        self.makeAppt_inner_frame = QFrame(self.makeAppt_outer_frame)
        self.makeAppt_inner_frame.setObjectName(u"makeAppt_inner_frame")
        self.makeAppt_inner_frame.setGeometry(QRect(0, 0, 411, 551))
        self.makeAppt_inner_frame.setStyleSheet(u"border: none; margin: 0; padding:0; background-color: rgba(255, 255, 255, 0.5)")
        self.makeAppt_inner_frame.setFrameShape(QFrame.StyledPanel)
        self.makeAppt_inner_frame.setFrameShadow(QFrame.Plain)
        self.makeAppt_inner_frame.setLineWidth(0)
        self.makeAppt_inner_frame.setMidLineWidth(0)
        self.makeAppt_btn = QPushButton(self.makeAppt_inner_frame)
        self.makeAppt_btn.setObjectName(u"makeAppt_btn")
        self.makeAppt_btn.setGeometry(QRect(20, 480, 81, 41))
        self.makeAppt_btn.setFont(font2)
        self.makeAppt_btn.setStyleSheet(u"border: 2px solid #B6D0E2; border-radius: 10; background-color: #B6D0E2; color: white")
        self.makeAppt_btn.clicked.connect(self.emitmakeApptBtn)
        
        self.layoutWidget_2 = QWidget(self.makeAppt_inner_frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 30, 371, 451))
        self.makeAppt_info_layout = QVBoxLayout(self.layoutWidget_2)
        self.makeAppt_info_layout.setObjectName(u"makeAppt_info_layout")
        self.makeAppt_info_layout.setContentsMargins(0, 0, 0, 0)
        self.makeAppt_img = QLabel(self.layoutWidget_2)
        self.makeAppt_img.setObjectName(u"makeAppt_img")
        self.makeAppt_img.setStyleSheet(u"border: none; ")
        self.makeAppt_img.setPixmap(QPixmap(u"CAD/Images/services/services_make_appointment.png"))
        self.makeAppt_img.setScaledContents(True)
        self.makeAppt_img.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.makeAppt_info_layout.addWidget(self.makeAppt_img)

        self.horizontalSpacer_8 = QSpacerItem(348, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.makeAppt_info_layout.addItem(self.horizontalSpacer_8)

        self.makeAppt_title_layout = QHBoxLayout()
        self.makeAppt_title_layout.setObjectName(u"makeAppt_title_layout")
        self.fadoctormakeAppt = QLabel(self.layoutWidget_2)
        self.fadoctormakeAppt.setObjectName(u"fadoctormakeAppt")
        self.fadoctormakeAppt.setFont(font3)
        self.fadoctormakeAppt.setStyleSheet(u"border: none;")
        self.fadoctormakeAppt.setScaledContents(False)

        self.makeAppt_title_layout.addWidget(self.fadoctormakeAppt)

        self.horizontalSpacer_9 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.makeAppt_title_layout.addItem(self.horizontalSpacer_9)


        self.makeAppt_info_layout.addLayout(self.makeAppt_title_layout)

        self.makeAppt_text = QLabel(self.layoutWidget_2)
        self.makeAppt_text.setObjectName(u"makeAppt_text")
        self.makeAppt_text.setFont(font4)
        self.makeAppt_text.setStyleSheet(u"border: none;")
        self.makeAppt_text.setScaledContents(False)
        self.makeAppt_text.setWordWrap(True)

        self.makeAppt_info_layout.addWidget(self.makeAppt_text)

        self.horizontalSpacer_10 = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.makeAppt_info_layout.addItem(self.horizontalSpacer_10)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.frame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(30, 19, 87, 871))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout.addWidget(self.home_navigation)

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
        self.verticalLayout.addWidget(self.appointments_navigation)

        self.services_navigation = QToolButton(self.layoutWidget_4)
        self.services_navigation.setObjectName(u"services_navigation")
        self.services_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.services_navigation.sizePolicy().hasHeightForWidth())
        self.services_navigation.setSizePolicy(sizePolicy)
        self.services_navigation.setFont(font5)
        self.services_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_navigation.setIcon(icon3)
        self.services_navigation.setIconSize(QSize(70, 70))
        self.services_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.services_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget_4)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setFont(font5)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settings_navigation.clicked.connect(self.emitProfileBtn)
        self.verticalLayout.addWidget(self.settings_navigation)

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
        self.verticalLayout.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.services_avail_title.setText(QCoreApplication.translate("Form", u"Services Available", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.fadoctor_btn.setText(QCoreApplication.translate("Form", u"Go \u2192", None))
        self.fadoctor_img.setText("")
        self.fadoctor_title.setText(QCoreApplication.translate("Form", u"Find A Doctor", None))
        self.fadoctor_text.setText(QCoreApplication.translate("Form", u"Quickly locate and connect with qualified medical professionals in your area. Whether you need a specialist, or a consultant, we ensures you find the right doctor for your health needs.", None))
        self.faclinic_btn.setText(QCoreApplication.translate("Form", u"Go \u2192", None))
        self.faclinic_img.setText("")
        self.faclinic_title.setText(QCoreApplication.translate("Form", u"Find A Clinic", None))
        self.faclinic_text.setText(QCoreApplication.translate("Form", u"Finding the right clinic has never been easier. Whether you need a routine check-up, or a specialist consultation, our comprehensive directory will help you locate the perfect healthcare provider.", None))
        self.makeAppt_btn.setText(QCoreApplication.translate("Form", u"Go \u2192", None))
        self.makeAppt_img.setText("")
        self.fadoctormakeAppt.setText(QCoreApplication.translate("Form", u"Make An Appointment", None))
        self.makeAppt_text.setText(QCoreApplication.translate("Form", u"Easily schedule your next medical appointment with just a few clicks. Choose your preferred date, time, and doctor to ensure timely and convenient care.", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Services", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi
    
    @pyqtSlot()
    def emitFadBtn(self):
        # Emit the custom signal
        self.fad_btn_clicked.emit()
        
    @pyqtSlot()
    def emitFacBtn(self):
        # Emit the custom signal
        self.fac_btn_clicked.emit()
        
    @pyqtSlot()
    def emitmakeApptBtn(self):
        # Emit the custom signal
        self.makeAppt_btn_clicked.emit()

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
        
    def initialize_db(self):
        return db 