from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db
import requests


class FindClinicWidget(QWidget):
    service_btn_clicked = pyqtSignal()
        
    def __init__(self, parent=None):
        super().__init__(parent)
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
        self.fac_title = QLabel(self.whitebg)
        self.fac_title.setObjectName(u"fac_title")
        self.fac_title.setGeometry(QRect(60, 40, 481, 81))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.fac_title.setFont(font)
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
        
        self.scrollArea = QScrollArea(self.whitebg)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(80, 240, 1640, 800))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1640, 800))

        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setAlignment(Qt.AlignTop)
        self.gridLayout.setHorizontalSpacing(150)  
        self.gridLayout.setVerticalSpacing(50)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        
        self.layoutWidget1 = QWidget(self.whitebg)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(80, 140, 1381, 48))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setSpacing(250)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.state_dropdown = QComboBox(self.layoutWidget1)
        self.state_dropdown.addItem(u"Search or Select a State")
        self.state_dropdown.addItem("")
        self.state_dropdown.setObjectName(u"state_dropdown")
        self.state_dropdown.setMinimumSize(QSize(321, 41))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(11)
        self.state_dropdown.setFont(font2)
        self.state_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
"border-radius: 5px; \n"
"background-color: #FFFFFF; \n"
"padding: 10px; \n"
"font-family: Consolas;\n"
"font-size: 11pt;")
        self.state_dropdown.setEditable(True)
        self.state_dropdown.setIconSize(QSize(50, 50))
        self.state_dropdown.setFrame(True)

        self.horizontalLayout_4.addWidget(self.state_dropdown)

        self.clinic_dropdown = QComboBox(self.layoutWidget1)
        self.clinic_dropdown.addItem(u"Search or Select a Clinic")
        self.clinic_dropdown.addItem("")
        self.clinic_dropdown.setObjectName(u"clinic_dropdown")
        self.clinic_dropdown.setMinimumSize(QSize(321, 41))
        self.clinic_dropdown.setFont(font2)
        self.clinic_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
"border-radius: 5px; \n"
"background-color: #FFFFFF; \n"
"padding: 10px; \n"
"font-family: Consolas;\n"
"font-size: 11pt;")
        self.clinic_dropdown.setEditable(True)
        self.clinic_dropdown.setIconSize(QSize(50, 50))
        self.clinic_dropdown.setFrame(True)

        self.horizontalLayout_4.addWidget(self.clinic_dropdown)

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
        font3 = QFont()
        font3.setFamily(u"Source Sans Pro Semibold")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.home_navigation.setFont(font3)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.home_navigation)

        self.appointments_navigation = QToolButton(self.layoutWidget_4)
        self.appointments_navigation.setObjectName(u"appointments_navigation")
        self.appointments_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.appointments_navigation.sizePolicy().hasHeightForWidth())
        self.appointments_navigation.setSizePolicy(sizePolicy)
        self.appointments_navigation.setFont(font3)
        self.appointments_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/appointment_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appointments_navigation.setIcon(icon2)
        self.appointments_navigation.setIconSize(QSize(70, 70))
        self.appointments_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.appointments_navigation)

        self.services_navigation = QToolButton(self.layoutWidget_4)
        self.services_navigation.setObjectName(u"services_navigation")
        self.services_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.services_navigation.sizePolicy().hasHeightForWidth())
        self.services_navigation.setSizePolicy(sizePolicy)
        self.services_navigation.setFont(font3)
        self.services_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_navigation.setIcon(icon3)
        self.services_navigation.setIconSize(QSize(70, 70))
        self.services_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.services_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget_4)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setFont(font3)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget_4)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setFont(font3)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon5 = QIcon()
        icon5.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.noti_icon.setText("")
        self.fac_title.setText(QCoreApplication.translate("Form", u"Find A Clinic", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        #self.view_clinic_btn.setText(QCoreApplication.translate("Form", u"View Clinic", None))
        #self.make_appt_btn.setText(QCoreApplication.translate("Form", u"Make Appointment", None))
        #self.clinic_logo.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        #self.clinic_name.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        #self.location.setText(QCoreApplication.translate("Form", u"Location", None))
        #self.view_clinic_btn_5.setText(QCoreApplication.translate("Form", u"View Clinic", None))
        #self.make_appt_btn_5.setText(QCoreApplication.translate("Form", u"Make Appointment", None))
        #self.clinic_logo_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        #self.clinic_name_5.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        #self.location_5.setText(QCoreApplication.translate("Form", u"Location", None))
        #self.view_clinic_btn_6.setText(QCoreApplication.translate("Form", u"View Clinic", None))
        #self.make_appt_btn_6.setText(QCoreApplication.translate("Form", u"Make Appointment", None))
        #self.clinic_logo_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        #self.clinic_name_6.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        #self.location_6.setText(QCoreApplication.translate("Form", u"Location", None))
        self.state_dropdown.setItemText(1, QCoreApplication.translate("Form", u"test", None))

        self.clinic_dropdown.setItemText(1, QCoreApplication.translate("Form", u"test", None))

        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Services", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi
    
    def fetch_clinic_data(self):
        try:
            clinics = db.child("clinic").get()
            
            if clinics.each():
                self.clinic_data_list = [clinic.val() for clinic in clinics.each()]
                #print("Fetched Clinics Data:", self.clinic_data_list)  # Debug: Print the fetched data
                self.populate_clinic_info()
            else:
                print("No clinics data found.")
        except Exception as e:
            print(f"An error occurred while fetching data: {e}")
            
    def populate_clinic_info(self):
        for i, clinic in enumerate(self.clinic_data_list):
                if isinstance(clinic, dict):
                        clinic_outer = QFrame(self.scrollAreaWidgetContents)
                        clinic_outer.setObjectName("clinic_info_outer")
                        clinic_outer.setStyleSheet("border: 1px solid black; \nborder-radius: 24px; ")
                        clinic_outer.setMinimumSize(QSize(388, 535))
                        clinic_outer.setMaximumSize(QSize(388, 535))

                        clinic_inner = QFrame(clinic_outer)
                        clinic_inner.setObjectName("clinic_info_inner")
                        clinic_inner.setGeometry(QRect(0, 0, 388, 535))
                        clinic_inner.setStyleSheet("border: none; background-color: transparent;")

                        layoutWidget = QWidget(clinic_inner)
                        layoutWidget.setObjectName("layoutWidget")
                        layoutWidget.setGeometry(QRect(1, 480, 386, 55))

                        horizontalLayout = QHBoxLayout(layoutWidget)
                        horizontalLayout.setObjectName("horizontalLayout")
                        horizontalLayout.setContentsMargins(0, 0, 0, 0)

                        view_clinic_btn = QPushButton(layoutWidget)
                        view_clinic_btn.setObjectName("view_clinic_btn")
                        view_clinic_btn.setMinimumSize(QSize(193, 55))
                        view_clinic_btn.setStyleSheet("border-radius: 0 0 24pt 0; background-color: #B6D0E2; border: none;")
                        view_clinic_btn.setText("View Clinic")
                        font = QFont("Consolas", 10)
                        view_clinic_btn.setFont(font)
                        

                        horizontalLayout.addWidget(view_clinic_btn)

                        make_appt_btn = QPushButton(layoutWidget)
                        make_appt_btn.setObjectName("make_appt_btn")
                        make_appt_btn.setMinimumSize(QSize(193, 55))
                        make_appt_btn.setStyleSheet("border-radius: 0 0 24pt 0; background-color: #B6D0E2; border: none;")
                        make_appt_btn.setText("Make Appointment")
                        font = QFont("Consolas", 10)
                        make_appt_btn.setFont(font)

                        horizontalLayout.addWidget(make_appt_btn)

                        layoutWidget_2 = QWidget(clinic_inner)
                        layoutWidget_2.setObjectName("layoutWidget_2")
                        layoutWidget_2.setGeometry(QRect(30, 30, 326, 451))

                        verticalLayout = QVBoxLayout(layoutWidget_2)
                        verticalLayout.setObjectName("verticalLayout")
                        verticalLayout.setContentsMargins(0, 0, 0, 0)

                        clinic_logo_label = QLabel(layoutWidget_2)
                        clinic_logo_label.setObjectName("clinic_logo")
                        clinic_logo_label.setMinimumSize(QSize(324, 160))
                        #clinic_logo_label.setMaximumSize(QSize(324, 160))
                        clinic_logo_label.setStyleSheet("border: none;") 

                        clinic_logo_label.setAlignment(Qt.AlignCenter)

                        clinic_img_path = clinic.get("clinic_img", "")
                        if clinic_img_path:
                                pixmap = QPixmap(clinic_img_path)
                                clinic_logo_label.setPixmap(pixmap.scaled(clinic_logo_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

                        verticalLayout.addWidget(clinic_logo_label)

                        verticalSpacer_3 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Fixed)
                        verticalLayout.addItem(verticalSpacer_3)

                        clinic_name_label = QLabel(layoutWidget_2)
                        clinic_name_label.setObjectName("clinic_name")
                        clinic_name_label.setStyleSheet("text-align: center; border: none;")
                        clinic_name_label.setText(clinic.get("clinic_name", "Unknown"))
                        font = QFont("Consolas", 12, QFont.Bold)
                        clinic_name_label.setFont(font)

                        verticalLayout.addWidget(clinic_name_label)
                        
                        line = QFrame(layoutWidget_2)
                        line.setObjectName("line")
                        line.setMinimumSize(QSize(324, 3))
                        line.setMaximumSize(QSize(324, 3))
                        line.setStyleSheet("background-color: #B6D0E2; border: none;")
                        line.setFrameShape(QFrame.HLine)
                        line.setFrameShadow(QFrame.Sunken)

                        verticalLayout.addWidget(line)

                        location_label = QLabel(layoutWidget_2)
                        location_label.setObjectName("location")
                        location_label.setStyleSheet("text-align: center; border: none;")
                        location_text = f"<b>Location:</b> {clinic.get('clinic_add', 'Unknown')}"
                        location_label.setText(location_text)
                        font = QFont("Consolas", 11)
                        location_label.setFont(font)

                        verticalLayout.addWidget(location_label)

                        # Calculate row and column
                        row = i // 3
                        col = i % 3
                        self.gridLayout.addWidget(clinic_outer, row, col)

        

