from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class PAHomeWidget(QWidget):
    clinic_btn_clicked = pyqtSignal()
    feedback_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    redirect_fb = pyqtSignal(dict)
        
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fb_data_list = []
        self.clinic_data_list = []
        self.setupUi(self)
        self.fetch_clinic_data()
        self.fetch_fb_data()
        self.clinic_details_frame = None
        self.temp_clinic_name = ""
        
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
        font.setFamily(u"Consolas")
        font.setPointSize(22)
        self.num_clinic_req_label.setFont(font)
        self.num_clinic_req_label.setWordWrap(True)
        
        self.clinic_req__label = QLabel(self.clinic_req_frame)
        self.clinic_req__label.setObjectName(u"clinic_req__label")
        self.clinic_req__label.setGeometry(QRect(30, 100, 51, 71))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(48)
        self.clinic_req__label.setFont(font1)
        #self.clinic_req__label.setText(str(self.calc_new_addition()))
        self.calc_new_addition()
        
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
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(11)
        self.feedback_label.setFont(font2)
        self.feedback_label.setStyleSheet(u"border : none;")
        self.widget = QWidget(self.feedback_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 441, 731))
        self.fb_list_layout = QVBoxLayout(self.widget)
        self.fb_list_layout.setSpacing(10)
        self.fb_list_layout.setObjectName(u"fb_list_layout")
        self.fb_list_layout.setContentsMargins(0, 0, 0, 0)
        

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
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(16)
        self.profile_btn.setFont(font5)
        self.profile_btn.setStyleSheet(u"border: none")
        self.upcomin_appt_frame = QFrame(self.background)
        self.upcomin_appt_frame.setObjectName(u"upcomin_appt_frame")
        self.upcomin_appt_frame.setGeometry(QRect(60, 430, 450, 551))
        self.upcomin_appt_frame.setStyleSheet(u"background-color : #ffffff;")
        self.upcomin_appt_frame.setFrameShape(QFrame.StyledPanel)
        self.upcomin_appt_frame.setFrameShadow(QFrame.Raised)
        self.upcoming_label = QLabel(self.upcomin_appt_frame)
        self.upcoming_label.setObjectName(u"upcoming_label")
        self.upcoming_label.setGeometry(QRect(30, 20, 211, 41))
        self.upcoming_label.setFont(font2)
        self.upcoming_label.setStyleSheet(u"border : none;\n"
"")
        self.widget1 = QWidget(self.upcomin_appt_frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 70, 401, 461))
        self.clinic_list_layout = QVBoxLayout(self.widget1)
        self.clinic_list_layout.setSpacing(10)
        self.clinic_list_layout.setObjectName(u"clinic_list_layout")
        self.clinic_list_layout.setContentsMargins(0, 0, 0, 0)

        
        
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(31, 20, 87, 851))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.home_navigation = QToolButton(self.layoutWidget1)
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
        self.home_navigation.setStyleSheet(u"border: none; \ncolor: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.home_navigation)

        self.clinic_navigation = QToolButton(self.layoutWidget1)
        self.clinic_navigation.setObjectName(u"clinic_navigation")
        self.clinic_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.clinic_navigation.sizePolicy().hasHeightForWidth())
        self.clinic_navigation.setSizePolicy(sizePolicy)
        self.clinic_navigation.setMinimumSize(QSize(85, 96))
        self.clinic_navigation.setMaximumSize(QSize(85, 96))
        self.clinic_navigation.setFont(font10)
        self.clinic_navigation.setStyleSheet(u"border: none;color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clinic_navigation.setIcon(icon2)
        self.clinic_navigation.setIconSize(QSize(70, 70))
        self.clinic_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.clinic_navigation.clicked.connect(self.emitClinicBtn)
        self.verticalLayout.addWidget(self.clinic_navigation)

        self.feedback_navigation = QToolButton(self.layoutWidget1)
        self.feedback_navigation.setObjectName(u"feedback_navigation")
        self.feedback_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.feedback_navigation.sizePolicy().hasHeightForWidth())
        self.feedback_navigation.setSizePolicy(sizePolicy)
        self.feedback_navigation.setMinimumSize(QSize(85, 96))
        self.feedback_navigation.setMaximumSize(QSize(85, 96))
        self.feedback_navigation.setFont(font10)
        self.feedback_navigation.setStyleSheet(u"border: none; color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.feedback_navigation.setIcon(icon3)
        self.feedback_navigation.setIconSize(QSize(70, 70))
        self.feedback_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.feedback_navigation.clicked.connect(self.emitFeedbackBtn)
        self.verticalLayout.addWidget(self.feedback_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget1)
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
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settings_navigation.clicked.connect(self.emitSettingsBtn)

        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget1)
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
        self.num_clinic_req_label.setText(QCoreApplication.translate("Form", u"Total Clinic Addition Request:", None))
        self.feedback_label.setText(QCoreApplication.translate("Form", u"Feedbacks", None))
       
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Admin", None))
        self.upcoming_label.setText(QCoreApplication.translate("Form", u"Clinic List", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.clinic_navigation.setText(QCoreApplication.translate("Form", u"Clinics", None))
        self.feedback_navigation.setText(QCoreApplication.translate("Form", u"Feedback", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

    @pyqtSlot()
    def emitClinicBtn(self):
        self.clinic_btn_clicked.emit()
        
    @pyqtSlot()
    def emitFeedbackBtn(self):
        self.feedback_btn_clicked.emit()
        
    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
    
    @pyqtSlot()
    def emitSettingsBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()

    def fetch_clinic_data(self):
        db = self.initialize_db()
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
                      
    def create_clinic_list_frame(self, clinic_data):
        clinicReq_frame = QFrame(self.widget1)
        clinicReq_frame.setObjectName(u"clinicReq_frame")
        clinicReq_frame.setMinimumSize(QSize(399, 81))
        clinicReq_frame.setMaximumSize(QSize(399, 81))
        clinicReq_frame.setFrameShape(QFrame.StyledPanel)
        clinicReq_frame.setFrameShadow(QFrame.Raised)
        clinic_name_label = QLabel(clinicReq_frame)
        clinic_name_label.setObjectName(u"clinic_name_label")
        clinic_name_label.setGeometry(QRect(90, 30, 121, 21))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        clinic_name_label.setFont(font6)
        clinic_name_label.setStyleSheet(u"border : none;\n")
        clinic_name_label.setText(clinic_data.get("clinic_name", "Unknown"))
        clinic_name_label.mousePressEvent = lambda event, clinic=clinic_data: self.create_popup_widget(clinic)
        
        clinic_logo_label = QLabel(clinicReq_frame)
        clinic_logo_label.setObjectName(u"clinic_logo_label")
        clinic_logo_label.setGeometry(QRect(10, 10, 54, 54))
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(9)
        clinic_logo_label.setFont(font7)
        clinic_logo_label.setStyleSheet(u"background-color: transparent;"
        "border-radius: 25px;"
        "min-width: 50px;"
        "min-height: 50px;"
        "max-width: 50px;"
        "max-height: 50px;")
        clinic_logo_label.setAlignment(Qt.AlignCenter)
        clinic_img_path = clinic_data.get("clinic_img", "Path Not Found")
        if clinic_img_path:
                pixmap = QPixmap(clinic_img_path)
                clinic_logo_label.setPixmap(pixmap.scaled(clinic_logo_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        label = QLabel(clinicReq_frame)
        label.setObjectName(u"label")
        label.setGeometry(QRect(290, 20, 91, 41))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(10)
        label.setFont(font4)
        label.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);\n"
"color: #128983; text-align: center;\n"
"")
        label.setAlignment(Qt.AlignCenter)
        label.setText(clinic_data.get("clinic_status", "Unknown"))
        
        return clinicReq_frame
        
    def clear_layout(self):
        while self.clinic_list_layout.count():
                item = self.clinic_list_layout.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.destroy()
                        
    def clear_layout_1(self):
        while self.fb_list_layout.count():
                item = self.fb_list_layout.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.deleteLater()
                        
    def populate_clinic_info(self):
        self.clear_layout()
        visible_clinics = []

        for i, clinic_data in enumerate(self.clinic_data_list):
                clinic_frame = self.create_clinic_list_frame(clinic_data)
                if clinic_frame:
                        visible_clinics.append(clinic_frame)

        # Add visible clinics to the layout in reverse order
        for clinic_frame in reversed(visible_clinics[:5]):
                self.clinic_list_layout.addWidget(clinic_frame)

        self.widget1.setLayout(self.clinic_list_layout)
        self.clinic_list_layout.setAlignment(Qt.AlignTop)
        self.clinic_list_layout.update()
        self.widget1.update()

    def create_popup_widget(self, clinic_data):
        self.hide_clinic_details_frame()
        self.clinic_details_frame = self.create_clinic_details_frame(clinic_data)
        self.clinic_details_frame.setVisible(True)

    def hide_clinic_details_frame(self):
        if self.clinic_details_frame:
            self.clinic_details_frame.setVisible(False)

    def create_clinic_details_frame(self, clinic_data):
        request_detail_outer = QFrame(self.background)
        request_detail_outer.setObjectName(u"request_detail_outer")
        request_detail_outer.setGeometry(QRect(540, 430, 450, 551))
        request_detail_outer.setStyleSheet(u"background-color : #ffffff;")
        request_detail_outer.setFrameShape(QFrame.StyledPanel)
        request_detail_outer.setFrameShadow(QFrame.Raised)
        req_detail_label = QLabel(request_detail_outer)
        req_detail_label.setObjectName(u"req_detail_label")
        req_detail_label.setGeometry(QRect(30, 20, 381, 41))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(11)
        req_detail_label.setFont(font2)
        req_detail_label.setStyleSheet(u"border : none;\n")
        clinic_details_inner = QFrame(request_detail_outer)
        clinic_details_inner.setObjectName(u"clinic_details_inner")
        clinic_details_inner.setGeometry(QRect(20, 70, 401, 431))
        clinic_details_inner.setFrameShape(QFrame.StyledPanel)
        clinic_details_inner.setFrameShadow(QFrame.Raised)
        clinic_name = QLabel(clinic_details_inner)
        clinic_name.setObjectName(u"clinic_name")
        clinic_name.setGeometry(QRect(100, 30, 121, 21))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        clinic_name.setFont(font6)
        clinic_name.setStyleSheet(u"border : none;\n")
        clinic_name.setText(clinic_data.get("clinic_name", "Unknown"))
        self.temp_clinic_name = clinic_data["clinic_name"]
        
        clinic_logo = QLabel(clinic_details_inner)
        clinic_logo.setObjectName(u"clinic_logo")
        clinic_logo.setGeometry(QRect(10, 10, 54, 54))
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(9)
        clinic_logo.setFont(font7)
        clinic_logo.setStyleSheet(u"background-color: transparent;"
        "border-radius: 25px;"
        "min-width: 50px;"
        "min-height: 50px;"
        "max-width: 50px;"
        "max-height: 50px;")
        clinic_logo.setAlignment(Qt.AlignCenter)
        
        clinic_img_path = clinic_data.get("clinic_img", "")
        if clinic_img_path:
                pixmap = QPixmap(clinic_img_path)
                clinic_logo.setPixmap(pixmap.scaled(clinic_logo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        
        line = QFrame(clinic_details_inner)
        line.setObjectName(u"line")
        line.setGeometry(QRect(20, 100, 360, 3))
        line.setMinimumSize(QSize(357, 3))
        line.setMaximumSize(QSize(16777215, 3))
        line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        line.setFrameShape(QFrame.StyledPanel)
        line.setFrameShadow(QFrame.Raised)
        widget2 = QWidget(clinic_details_inner)
        widget2.setObjectName(u"widget2")
        widget2.setGeometry(QRect(2, 123, 391, 313))
        req_detail_layout = QVBoxLayout(widget2)
        req_detail_layout.setObjectName(u"req_detail_layout")
        req_detail_layout.setContentsMargins(0, 0, 0, 0)
        phone_layout = QHBoxLayout()
        phone_layout.setObjectName(u"phone_layout")
        phone_label = QLabel(widget2)
        phone_label.setObjectName(u"phone_label")
        phone_label.setMinimumSize(QSize(150, 71))
        phone_label.setMaximumSize(QSize(150, 71))
        phone_label.setFont(font3)
        phone_label.setStyleSheet(u"border: none;")
        phone_label.setLineWidth(0)
        phone_label.setText("Phone Number: ")
        phone_layout.addWidget(phone_label)

        phone_display = QLabel(widget2)
        phone_display.setObjectName(u"phone_display")
        phone_display.setMinimumSize(QSize(196, 71))
        phone_display.setMaximumSize(QSize(196, 71))
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setWeight(50)
        phone_display.setFont(font8)
        phone_display.setStyleSheet(u"border: none;")
        phone_display.setText(clinic_data.get("clinic_phone", "Unknown"))
        phone_layout.addWidget(phone_display)


        req_detail_layout.addLayout(phone_layout)

        email_layout = QHBoxLayout()
        email_layout.setObjectName(u"email_layout")
        email_label = QLabel(widget2)
        email_label.setObjectName(u"email_label")
        email_label.setMinimumSize(QSize(150, 71))
        email_label.setMaximumSize(QSize(150, 71))
        email_label.setFont(font3)
        email_label.setStyleSheet(u"border: none;")
        email_label.setText("Email: ")
        email_layout.addWidget(email_label)

        email_display = QLabel(widget2)
        email_display.setObjectName(u"email_display")
        email_display.setMinimumSize(QSize(196, 71))
        email_display.setMaximumSize(QSize(196, 71))
        email_display.setFont(font8)
        email_display.setStyleSheet(u"border: none;")
        email_display.setText(clinic_data.get("clinic_email", "Unknown"))
        email_layout.addWidget(email_display)


        req_detail_layout.addLayout(email_layout)

        add_layout = QHBoxLayout()
        add_layout.setObjectName(u"add_layout")
        add_label = QLabel(widget2)
        add_label.setObjectName(u"add_label")
        add_label.setMinimumSize(QSize(150, 72))
        add_label.setMaximumSize(QSize(150, 72))
        add_label.setFont(font3)
        add_label.setStyleSheet(u"border: none;")
        add_label.setText("Address: ")
        add_layout.addWidget(add_label)

        add_display = QLabel(widget2)
        add_display.setObjectName(u"add_display")
        add_display.setMinimumSize(QSize(196, 72))
        add_display.setMaximumSize(QSize(196, 72))
        add_display.setFont(font8)
        add_display.setStyleSheet(u"border: none;")
        add_display.setScaledContents(False)
        add_display.setWordWrap(True)
        add_display.setText(clinic_data.get("clinic_add", "Unknown"))
        add_layout.addWidget(add_display)


        req_detail_layout.addLayout(add_layout)

        opening_hr_layout = QHBoxLayout()
        opening_hr_layout.setObjectName(u"opening_hr_layout")
        opening_hr_layout.setSizeConstraint(QLayout.SetFixedSize)
        opening_hr_text = QLabel(widget2)
        opening_hr_text.setObjectName(u"opening_hr_text")
        opening_hr_text.setMinimumSize(QSize(150, 71))
        opening_hr_text.setMaximumSize(QSize(150, 71))
        opening_hr_text.setFont(font3)
        opening_hr_text.setStyleSheet(u"border: none;")
        opening_hr_text.setWordWrap(True)
        opening_hr_text.setText("Operating Hours: ")
        opening_hr_layout.addWidget(opening_hr_text)

        hour_display = QLabel(widget2)
        hour_display.setObjectName(u"hour_display")
        hour_display.setMinimumSize(QSize(196, 71))
        hour_display.setMaximumSize(QSize(196, 71))
        hour_display.setFont(font8)
        hour_display.setStyleSheet(u"border: none;")
        hour_display.setScaledContents(False)
        hour_display.setWordWrap(True)
        hour_display.setText(clinic_data.get("clinic_operating_hr", "Unknown"))
        opening_hr_layout.addWidget(hour_display)


        req_detail_layout.addLayout(opening_hr_layout)

        view_detail_btn = QPushButton(request_detail_outer)
        view_detail_btn.setObjectName(u"view_detail_btn")
        view_detail_btn.setGeometry(QRect(320, 510, 93, 28))
        font9 = QFont()
        font9.setFamily(u"Consolas")
        font9.setPointSize(9)
        font9.setUnderline(True)
        view_detail_btn.setFont(font9)
        view_detail_btn.setStyleSheet(u"color: #007E85; border: none;")
        return request_detail_outer
    
    def fetch_fb_data(self):
        db = self.initialize_db()
        try:
            feedbacks = db.child("feedback").get()
            
            if feedbacks.each():
                self.fb_data_list = []
                
                # Iterate through each feedback entry
                for fb in feedbacks.each():
                    feedback_data = fb.val()
                    user_id = feedback_data.get("user_id")
                    
                    # Fetch the patient name using the user_id
                    patient_name = db.child("patients").child(user_id).child("patient_name").get().val()
                    
                    # Add the patient name to the feedback data
                    feedback_data["patient_name"] = patient_name
                    
                    # Add the feedback data with patient name to the list
                    self.fb_data_list.append(feedback_data)
                
                # Populate the feedback information on the UI
                self.populate_fb_info()
            else:
                print("No feedback data found.")
        except Exception as e:
            print(f"An error occurred while fetching data: {e}")

    def create_fb_list_frame(self, fb_data):
        feedback_detail_frame = QFrame(self.widget)
        feedback_detail_frame.setObjectName(u"feedback_detail_frame")
        feedback_detail_frame.setMinimumSize(QSize(439, 81))
        feedback_detail_frame.setMaximumSize(QSize(439, 81))
        feedback_detail_frame.setFrameShape(QFrame.StyledPanel)
        feedback_detail_frame.setFrameShadow(QFrame.Raised)
        name_display = QLabel(feedback_detail_frame)
        name_display.setObjectName(u"name_display")
        name_display.setGeometry(QRect(30, 10, 121, 21))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        name_display.setFont(font3)
        name_display.setStyleSheet(u"border : none;\n")
        name_display.setText(fb_data.get("patient_name", "Unknown"))
        
        date_feedback_display = QLabel(feedback_detail_frame)
        date_feedback_display.setObjectName(u"date_feedback_display")
        date_feedback_display.setGeometry(QRect(30, 40, 121, 21))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(10)
        date_feedback_display.setFont(font4)
        date_feedback_display.setStyleSheet(u"border : none;\n")
        date_feedback_display.setText(fb_data.get("date", "Unknown"))
        
        view_feedback_btn = QPushButton(feedback_detail_frame)
        view_feedback_btn.setObjectName(u"view_feedback_btn")
        view_feedback_btn.setGeometry(QRect(330, 20, 93, 51))
        view_feedback_btn.setFont(font4)
        view_feedback_btn.setStyleSheet(u"background-color: #B6D0E2;color: white; text-align: center;")
        view_feedback_btn.setText("View")

        view_feedback_btn.clicked.connect(lambda: self.redirect_to_fb_inbox(fb_data))
        
        return feedback_detail_frame
    
    def populate_fb_info(self):
        self.clear_layout_1()
        visible_fb = []

        for i, fb_data in enumerate(self.fb_data_list):
                #print(f"db data is {fb_data}")
                fb_frame = self.create_fb_list_frame(fb_data)
                if fb_frame:
                        visible_fb.append(fb_frame)

        # Add visible clinics to the layout
        for fb_frame in reversed(visible_fb):
                self.fb_list_layout.addWidget(fb_frame)
        self.widget.setLayout(self.fb_list_layout)
        self.fb_list_layout.setAlignment(Qt.AlignTop)
        self.fb_list_layout.update()
        self.widget.update()
    
    @pyqtSlot()
    def redirect_to_fb_inbox(self, fb_data):
        self.redirect_fb.emit(fb_data)
    
    def calc_new_addition(self):
        db = self.initialize_db()
        clinic_data = db.child("clinic").get().val()
        clinic_dor_list = [clinic["clinic_dor"] for clinic in clinic_data.values() if "clinic_dor" in clinic]
        #print(f"dates {clinic_dor_list}")
        today_date = QDate.currentDate()
        count = 0
        
        for date in clinic_dor_list:
                # Parse clinic_dor_yymmdd to create a QDate object
                clinic_dor_str = str(date)
                year = 2000 + int(clinic_dor_str[:2])
                month = int(clinic_dor_str[2:4])
                day = int(clinic_dor_str[4:])
                clinic_dor = QDate(year, month, day)
                
                # Calculate the number of days from today's date
                days_difference = today_date.daysTo(clinic_dor)
                
                # Count if the date is from today onwards
                if days_difference >= 0:
                        count += 1
        print(f"count is {count}")
        self.clinic_req__label.setText(str(count))
    
    def initialize_db(self):
        return db