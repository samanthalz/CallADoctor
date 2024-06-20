from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class ViewClinicProfileWidget(QWidget):
        
    service_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    back_btn_clicked = pyqtSignal()
    makeAppointmentRequested = pyqtSignal(str, str)
    viewDocterRequested = pyqtSignal(str)
    
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
        self.fad_title.setGeometry(QRect(70, 140, 481, 81))
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
        self.profile_display_frame = QFrame(self.whitebg)
        self.profile_display_frame.setObjectName(u"profile_display_frame")
        self.profile_display_frame.setGeometry(QRect(50, 230, 1661, 691))
        self.profile_display_frame.setStyleSheet(u"background-color: white;")
        self.profile_display_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_display_frame.setFrameShadow(QFrame.Raised)
        
        self.clinic_img = QLabel(self.profile_display_frame)
        self.clinic_img.setObjectName(u"clinic_img")
        self.clinic_img.setGeometry(QRect(200, 90, 200, 200))
        self.clinic_img.setMinimumSize(QSize(200, 200))
        self.clinic_img.setMaximumSize(QSize(16777215, 16777215))
        #self.clinic_img.setStyleSheet(u"text-align: center;  border-radius: 100px; border: 1px solid black; ")
        self.clinic_img.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.profile_display_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(610, 40, 1011, 601))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.location_layout = QVBoxLayout()
        self.location_layout.setSpacing(10)
        self.location_layout.setObjectName(u"location_layout")
        self.location_label = QLabel(self.layoutWidget)
        self.location_label.setObjectName(u"location_label")
        self.location_label.setMinimumSize(QSize(0, 30))
        self.location_label.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.location_label.setFont(font2)
        self.location_label.setStyleSheet(u"text-align: center; border: none;")

        self.location_layout.addWidget(self.location_label)

        self.location_display = QLabel(self.layoutWidget)
        self.location_display.setObjectName(u"location_display")
        self.location_display.setMinimumSize(QSize(1000, 120))
        self.location_display.setMaximumSize(QSize(1000, 120))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(12)
        self.location_display.setFont(font3)
        self.location_display.setStyleSheet(u"text-align: center; border: 1px solid black; border-radius: 0px;")
        self.location_display.setWordWrap(True)

        self.location_layout.addWidget(self.location_display)


        self.verticalLayout.addLayout(self.location_layout)

        self.contact_layout = QVBoxLayout()
        self.contact_layout.setSpacing(10)
        self.contact_layout.setObjectName(u"contact_layout")
        self.contact_label = QLabel(self.layoutWidget)
        self.contact_label.setObjectName(u"contact_label")
        self.contact_label.setMinimumSize(QSize(0, 30))
        self.contact_label.setMaximumSize(QSize(16777215, 30))
        self.contact_label.setFont(font2)
        self.contact_label.setStyleSheet(u"text-align: center; border: none;")

        self.contact_layout.addWidget(self.contact_label)

        self.contact_display = QLabel(self.layoutWidget)
        self.contact_display.setObjectName(u"contact_display")
        self.contact_display.setMinimumSize(QSize(1000, 110))
        self.contact_display.setMaximumSize(QSize(1000, 110))
        self.contact_display.setFont(font3)
        self.contact_display.setStyleSheet(u"text-align: center; border: 1px solid black; border-radius: 0px;")
        self.contact_display.setWordWrap(True)

        self.contact_layout.addWidget(self.contact_display)


        self.verticalLayout.addLayout(self.contact_layout)

        self.ophour_layout = QVBoxLayout()
        self.ophour_layout.setSpacing(10)
        self.ophour_layout.setObjectName(u"ophour_layout")
        self.ophour_label = QLabel(self.layoutWidget)
        self.ophour_label.setObjectName(u"ophour_label")
        self.ophour_label.setMinimumSize(QSize(0, 30))
        self.ophour_label.setMaximumSize(QSize(16777215, 30))
        self.ophour_label.setFont(font2)
        self.ophour_label.setStyleSheet(u"text-align: center; border: none;")

        self.ophour_layout.addWidget(self.ophour_label)

        self.ophour_display = QLabel(self.layoutWidget)
        self.ophour_display.setObjectName(u"ophour_display")
        self.ophour_display.setMinimumSize(QSize(1000, 80))
        self.ophour_display.setMaximumSize(QSize(1000, 80))
        self.ophour_display.setFont(font3)
        self.ophour_display.setStyleSheet(u"text-align: center; border: 1px solid black; border-radius: 0px;")
        self.ophour_display.setWordWrap(True)

        self.ophour_layout.addWidget(self.ophour_display)


        self.verticalLayout.addLayout(self.ophour_layout)

        self.layoutWidget_5 = QWidget(self.profile_display_frame)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(100, 350, 400, 210))
        
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(15)
        
        self.clinic_name = QLabel(self.layoutWidget_5)
        self.clinic_name.setObjectName(u"clinic_name")
        self.clinic_name.setMinimumSize(QSize(400, 100))
        self.clinic_name.setMaximumSize(QSize(400, 100))
        self.clinic_name.setFont(font2)
        self.clinic_name.setStyleSheet(u"text-align: center; border: none;")
        self.clinic_name.setAlignment(Qt.AlignCenter)
        self.clinic_name.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.clinic_name)

        self.view_doc_btn = QPushButton(self.layoutWidget_5)
        self.view_doc_btn.setObjectName(u"view_doc_btn")
        self.view_doc_btn.setMinimumSize(QSize(400, 55))
        self.view_doc_btn.setMaximumSize(QSize(400, 55))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(10)
        self.view_doc_btn.setFont(font4)
        self.view_doc_btn.setStyleSheet(u"border-radius: 0 0 24pt 0; background-color: #B6D0E2; border: none;")
        self.view_doc_btn.clicked.connect(self.on_view_doc_button_clicked)
        self.verticalLayout_3.addWidget(self.view_doc_btn)
        
        self.make_appt_btn = QPushButton(self.layoutWidget_5)
        self.make_appt_btn.setObjectName(u"make_appt_btn")
        self.make_appt_btn.setMinimumSize(QSize(400, 55))
        self.make_appt_btn.setMaximumSize(QSize(400, 55))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(10)
        self.make_appt_btn.setFont(font4)
        self.make_appt_btn.setStyleSheet(u"border-radius: 0 0 24pt 0; background-color: #B6D0E2; border: none;")
        self.make_appt_btn.clicked.connect(self.on_make_appointment_button_clicked)
        self.verticalLayout_3.addWidget(self.make_appt_btn)

        self.back_button = QPushButton(self.whitebg)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setEnabled(True)
        self.back_button.setGeometry(QRect(60, 60, 181, 61))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setWeight(75)
        self.back_button.setFont(font5)
        self.back_button.setAutoFillBackground(False)
        self.back_button.setStyleSheet(u"background-color: rgba(182, 208, 226,0.8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.back_button.setIconSize(QSize(70, 70))
        self.back_button.clicked.connect(self.emitBackBtn)
        
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
        font6 = QFont()
        font6.setFamily(u"Source Sans Pro Semibold")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.home_navigation.setFont(font6)
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
        self.appointments_navigation.setFont(font6)
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
        self.services_navigation.setFont(font6)
        self.services_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
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
        self.settings_navigation.setFont(font6)
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
        self.logout_navigation.setFont(font6)
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
        self.fad_title.setText(QCoreApplication.translate("Form", u"Clinic Profile", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.clinic_img.setText("")
        self.location_label.setText(QCoreApplication.translate("Form", u"Location", None))
        self.contact_label.setText(QCoreApplication.translate("Form", u"Contact Details", None))
        self.ophour_label.setText(QCoreApplication.translate("Form", u"Operating Hours", None))
        self.make_appt_btn.setText(QCoreApplication.translate("Form", u"Make Appointment", None))
        self.view_doc_btn.setText(QCoreApplication.translate("Form", u"View Doctors Available", None))
        self.back_button.setText(QCoreApplication.translate("Form", u"< Back", None))
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
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
        
    @pyqtSlot()
    def emitBackBtn(self):
        # Emit the custom signal
        self.back_btn_clicked.emit()
        
    def display_clinic_profile(self, clinic_name, temp):
        clinic_info = self.fetch_clinic_info_from_db(clinic_name)  # Fetch info from the database
        self.update_ui_with_clinic_info(clinic_info)
        
        
    def fetch_clinic_info_from_db(self, clinic_name):
        # Fetch clinic info from the database using the clinic name
        try:
                # Modify the database query as per your actual database structure
                clinic_data = db.child("clinic").get().val()

                if clinic_data is None:
                        raise ValueError("Clinic data is not available in the database.")
                
                clinic_id = None
                clinic_info = None
                for cid, clinic in clinic_data.items():
                        if clinic.get("clinic_name") == clinic_name:
                                clinic_id = cid
                                clinic_info = clinic
                                break
                
                if clinic_id is None:
                        raise ValueError(f"Clinic '{clinic_name}' not found in the database.")

                # Set clinic_name as a property of the button
                self.make_appt_btn.setProperty("clinic_name", clinic_name)
                self.view_doc_btn.setProperty("clinic_name", clinic_name)
                #print(f"clinic info is {clinic_info}")
                return clinic_info

        except Exception as e:
                print(f"An error occurred while fetching clinic data: {e}")
                return {}

    def on_make_appointment_button_clicked(self):
        button = self.sender()  # Get the button that was clicked
        clinic_name = button.property("clinic_name")  # Retrieve the clinic ID from the button's property
        if clinic_name :
            self.makeAppointmentRequested.emit(clinic_name, "")
            
    def on_view_doc_button_clicked(self):
        button = self.sender()  # Get the button that was clicked
        clinic_name = button.property("clinic_name")  # Retrieve the clinic ID from the button's property
        if clinic_name :
            self.viewDocterRequested.emit(clinic_name)


    def update_ui_with_clinic_info(self, clinic_info):
        # Update the UI with the fetched doctor info
        self.clinic_img.setPixmap(QPixmap(clinic_info.get("clinic_img", "")))
        self.clinic_name.setText(clinic_info.get("clinic_name", "Unknown"))
        self.location_display.setText(clinic_info.get("clinic_add", "Unknown"))
        self.contact_display.setText(clinic_info.get("clinic_phone", "Unknown"))
        self.ophour_display.setText(clinic_info.get("clinic_operating_hr", "Unknown"))
        
        
        
