from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,QMouseEvent,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class ViewClinicWidget(QWidget):
    feedback_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clinic_data_list = []
        self.selected_state = ""
        self.setupUi(self)
        self.fetch_clinic_data()
        self.clinic_details_frame = None
        
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
        self.search_clinic.setGeometry(QRect(40, 40, 681, 71))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(11)
        self.search_clinic.setFont(font1)
        self.search_clinic.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 60px; color: Black;\n"
        " background-image: url(\"C:/Users/Samantha Law/Documents/INTI/CAD/CallADoctor/CAD/Images/icon/search_icon.png\"); \n"
        "background-repeat: no-repeat; \n"
        "background-position: left center; \n"
        "border: 1px solid gray;\n"
        "")
        self.search_clinic.setClearButtonEnabled(False)
        
        
        self.filter = QComboBox(self.background)
        self.filter.setObjectName(u"filter")
        self.filter.setGeometry(QRect(710, 170, 151, 31))
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(12)
        self.filter.setFont(font8)
        self.filter.setStyleSheet(u"border: 1px solid gray;")
        self.filter.activated.connect(self.updateSelectedState)
        self.load_states()
        
        self.clinic_list_label = QLabel(self.background)
        self.clinic_list_label.setObjectName(u"clinic_list_label")
        self.clinic_list_label.setGeometry(QRect(50, 160, 341, 41))
        font9 = QFont()
        font9.setFamily(u"Consolas")
        font9.setPointSize(16)
        self.clinic_list_label.setFont(font9)
        self.clinic_list_label.setStyleSheet(u"border : none;\n"
"")
        self.req_detail_label = QLabel(self.background)
        self.req_detail_label.setObjectName(u"req_detail_label")
        self.req_detail_label.setGeometry(QRect(990, 150, 571, 41))
        self.req_detail_label.setFont(font)
        self.req_detail_label.setStyleSheet(u"border : none;\n"
"")
        
        self.clear_btn = QPushButton(self.background)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(760, 50, 140, 51))
        font11 = QFont()
        font11.setFamily(u"Consolas")
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setWeight(50)
        self.clear_btn.setFont(font11)
        self.clear_btn.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 10px; color: black; border: 1px solid gray;")
        self.clear_btn.clicked.connect(self.clear_search)
        
        self.search_btn = QPushButton(self.background)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(930, 50, 140, 51))
        self.search_btn.setFont(font11)
        self.search_btn.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 10px; color: black; border: 1px solid gray;")
        self.search_btn.clicked.connect(self.search_clinics)
        
        self.scrollArea = QScrollArea(self.background)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(50, 290, 821, 731))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 821, 731))
        
        self.vLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.vLayout.setSpacing(10)
        self.vLayout.setObjectName(u"vlayout")
        self.vLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setLayout(self.vLayout)

        
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
        font13 = QFont()
        font13.setFamily(u"Source Sans Pro Semibold")
        font13.setPointSize(10)
        font13.setBold(True)
        font13.setWeight(75)
        self.home_navigation.setFont(font13)
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
        self.clinic_navigation.setFont(font13)
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
        self.feedback_navigation.setFont(font13)
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
        self.settings_navigation.setFont(font13)
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
        self.logout_navigation.setFont(font13)
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
        self.noti_icon.setText("")
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Admin", None))
        self.search_clinic.setPlaceholderText(QCoreApplication.translate("Form", u"Search Clinic Name", None))

        self.clinic_list_label.setText(QCoreApplication.translate("Form", u"Clinic List", None))
        self.req_detail_label.setText(QCoreApplication.translate("Form", u"Clinic Details", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.clinic_navigation.setText(QCoreApplication.translate("Form", u"Clinics", None))
        self.feedback_navigation.setText(QCoreApplication.translate("Form", u"Feedback", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()


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
            
    def clear_layout(self):
        while self.vLayout.count():
                item = self.vLayout.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.deleteLater()


    def create_clinic_list_frame(self, clinic_data):
        clinic_frame = QFrame(self.scrollAreaWidgetContents)
        clinic_frame.setObjectName(u"clinic_frame")
        clinic_frame.setGeometry(QRect(10, 10, 800, 80))
        font12 = QFont()
        font12.setFamily(u"Consolas")
        font12.setPointSize(10)
        clinic_frame.setFont(font12)
        clinic_frame.setStyleSheet(u"border: 1px solid gray; border-radius: 10px;")
        clinic_frame.setFrameShape(QFrame.StyledPanel)
        clinic_frame.setFrameShadow(QFrame.Raised)
        clinic_frame.setMaximumSize(800, 80)
        clinic_frame.setMinimumSize(800, 80)

        clinic_name_label = QLabel(clinic_frame)
        clinic_name_label.setObjectName(u"clinic_name_label")
        clinic_name_label.setGeometry(QRect(90, 30, 520, 21))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(10)
        clinic_name_label.setFont(font2)
        clinic_name_label.setStyleSheet(u"border : none;")
        clinic_name_label.setText(clinic_data.get("clinic_name", "Unknown"))
        
        clinic_name_label.mousePressEvent = lambda event, clinic=clinic_data: self.create_popup_widget(clinic)

        clinic_logo_label = QLabel(clinic_frame)
        clinic_logo_label.setObjectName(u"clinic_logo_label")
        clinic_logo_label.setGeometry(QRect(10, 10, 60, 60))
        clinic_logo_label.setStyleSheet(u"border : none;"
                                        "border-radius: 25px; "
                                        "width: 60px; "
                                        "height: 60px; ")
        clinic_logo_label.setAlignment(Qt.AlignCenter)
        
        clinic_img_path = clinic_data.get("clinic_img", "Path Not Found")
        if clinic_img_path:
                pixmap = QPixmap(clinic_img_path)
                clinic_logo_label.setPixmap(pixmap.scaled(clinic_logo_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


        status = QLabel(clinic_frame)
        status.setObjectName(u"status")
        status.setGeometry(QRect(690, 20, 91, 41))
        status.setFont(font12)
        status.setStyleSheet(u"background-color: rgba(12, 89, 83, 0.15); "
                                "color: #128983; "
                                "text-align: center; "
                                "border: none;")
        status.setAlignment(Qt.AlignCenter)
        status.setText(clinic_data.get("clinic_status", "Unknown"))

        return clinic_frame


    def populate_clinic_info(self, search_query=None):
        self.clear_layout()

        visible_clinics = []

        for i, clinic_data in enumerate(self.clinic_data_list):
                if isinstance(clinic_data, dict):
                        clinic_name = clinic_data.get("clinic_name", "").lower()
                        clinic_state = clinic_data.get("clinic_state", "").lower()


                if self.selected_state and clinic_state.lower() != self.selected_state.lower():
                        continue

                # Check search query if provided
                if not search_query or search_query.lower() in clinic_name:
                        clinic_frame = self.create_clinic_list_frame(clinic_data)
                        if clinic_frame:
                                visible_clinics.append(clinic_frame)

        # Add visible clinics to the layout
        for clinic_frame in visible_clinics:
                self.vLayout.addWidget(clinic_frame)

        self.scrollAreaWidgetContents.setLayout(self.vLayout)
        self.vLayout.setAlignment(Qt.AlignTop) 
        self.vLayout.update()
        self.scrollAreaWidgetContents.update()


    def create_clinic_details_frame(self, clinic_data):
        request_detail_outer = QFrame(self.background)
        request_detail_outer.setObjectName(u"request_detail_outer")
        request_detail_outer.setGeometry(QRect(979, 200, 751, 841))
        request_detail_outer.setStyleSheet(u"background-color : #ffffff;")
        request_detail_outer.setFrameShape(QFrame.StyledPanel)
        request_detail_outer.setFrameShadow(QFrame.Raised)
        
        clinic_details_inner = QFrame(request_detail_outer)
        clinic_details_inner.setObjectName(u"clinic_details_inner")
        clinic_details_inner.setGeometry(QRect(20, 20, 711, 771))
        clinic_details_inner.setFrameShape(QFrame.StyledPanel)
        clinic_details_inner.setFrameShadow(QFrame.Raised)
        
        clinic_name = QLabel(clinic_details_inner)
        clinic_name.setObjectName(u"clinic_name")
        clinic_name.setGeometry(QRect(100, 30, 570, 20))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(10)
        clinic_name.setFont(font2)
        clinic_name.setStyleSheet(u"border : none;\n")
        clinic_name.setText(clinic_data.get("clinic_name", "Unknown"))
        
        clinic_logo = QLabel(clinic_details_inner)
        clinic_logo.setObjectName(u"clinic_logo")
        clinic_logo.setGeometry(QRect(10, 10, 60, 60))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(9)
        clinic_logo.setFont(font3)
        clinic_logo.setStyleSheet(u"border-radius: 25px;"
        "border: none; "
        "min-width: 60px; "
        "min-height: 60px; "
        "max-width: 60px; "
        "max-height: 60px;")
        clinic_logo.setAlignment(Qt.AlignCenter)
        
        clinic_img_path = clinic_data.get("clinic_img", "")
        if clinic_img_path:
                pixmap = QPixmap(clinic_img_path)
                clinic_logo.setPixmap(pixmap.scaled(clinic_logo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        
        line = QFrame(clinic_details_inner)
        line.setObjectName(u"line")
        line.setGeometry(QRect(20, 100, 671, 3))
        line.setMinimumSize(QSize(357, 3))
        line.setMaximumSize(QSize(16777215, 3))
        line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        line.setFrameShape(QFrame.StyledPanel)
        line.setFrameShadow(QFrame.Raised)
        
        layoutWidget = QWidget(clinic_details_inner)
        layoutWidget.setObjectName(u"layoutWidget")
        layoutWidget.setGeometry(QRect(3, 123, 701, 641))
        verticalLayout_2 = QVBoxLayout(layoutWidget)
        verticalLayout_2.setObjectName(u"verticalLayout_2")
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        phone_layout = QHBoxLayout()
        phone_layout.setObjectName(u"phone_layout")
        phone_label = QLabel(layoutWidget)
        phone_label.setObjectName(u"phone_label")
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        phone_label.setFont(font4)
        phone_label.setStyleSheet(u"border: none;")
        phone_label.setLineWidth(0)
        phone_label.setText("Phone Number: ")
        phone_layout.addWidget(phone_label)

        phone_display = QLabel(layoutWidget)
        phone_display.setObjectName(u"phone_display")
        phone_display.setMinimumSize(QSize(390, 102))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setWeight(50)
        phone_display.setFont(font5)
        phone_display.setStyleSheet(u"border: none;")
        phone_display.setText(clinic_data.get("clinic_phone", "Unknown"))
        phone_layout.addWidget(phone_display)

        verticalLayout_2.addLayout(phone_layout)

        email_layout = QHBoxLayout()
        email_layout.setObjectName(u"email_layout")
        email_label = QLabel(layoutWidget)
        email_label.setObjectName(u"email_label")
        email_label.setFont(font4)
        email_label.setStyleSheet(u"border: none;")
        email_label.setText("Email: ")
        email_layout.addWidget(email_label)

        email_display = QLabel(layoutWidget)
        email_display.setObjectName(u"email_display")
        email_display.setMinimumSize(QSize(390, 102))
        email_display.setFont(font5)
        email_display.setStyleSheet(u"border: none;")
        email_display.setText(clinic_data.get("clinic_email", "Unknown"))
        email_layout.addWidget(email_display)


        verticalLayout_2.addLayout(email_layout)

        add_layout = QHBoxLayout()
        add_layout.setSpacing(135)
        add_layout.setObjectName(u"add_layout")
        add_label = QLabel(layoutWidget)
        add_label.setObjectName(u"add_label")
        add_label.setFont(font4)
        add_label.setStyleSheet(u"border: none;")
        add_label.setText("Address: ")
        add_label.setMinimumSize(172, 98)
        add_label.setMaximumSize(172, 98)
        add_layout.addWidget(add_label)

        add_display = QLabel(layoutWidget)
        add_display.setObjectName(u"add_display")
        add_display.setFont(font5)
        add_display.setStyleSheet(u"border: none;")
        add_display.setScaledContents(False)
        add_display.setWordWrap(True)
        add_display.setText(clinic_data.get("clinic_add", "Unknown"))
        add_layout.addWidget(add_display)


        verticalLayout_2.addLayout(add_layout)

        opening_hr_layout = QHBoxLayout()
        opening_hr_layout.setObjectName(u"opening_hr_layout")
        opening_hr_layout.setSizeConstraint(QLayout.SetFixedSize)
        opening_hr_label = QLabel(layoutWidget)
        opening_hr_label.setObjectName(u"opening_hr_label")
        opening_hr_label.setFont(font4)
        opening_hr_label.setStyleSheet(u"border: none;")
        opening_hr_label.setWordWrap(True)
        opening_hr_label.setText("Operating Hours: ")
        opening_hr_layout.addWidget(opening_hr_label)

        hour_display = QLabel(layoutWidget)
        hour_display.setObjectName(u"hour_display")
        hour_display.setMinimumSize(QSize(390, 0))
        hour_display.setFont(font5)
        hour_display.setStyleSheet(u"border: none;")
        hour_display.setScaledContents(False)
        hour_display.setWordWrap(True)
        hour_display.setText(clinic_data.get("clinic_operating_hr", "Unknown"))
        opening_hr_layout.addWidget(hour_display)


        verticalLayout_2.addLayout(opening_hr_layout)

        doc_layout = QHBoxLayout()
        doc_layout.setSpacing(0)
        doc_layout.setObjectName(u"doc_layout")
        doc_label = QLabel(layoutWidget)
        doc_label.setObjectName(u"doc_label")
        doc_label.setFont(font4)
        doc_label.setStyleSheet(u"border: none;")
        doc_label.setWordWrap(True)
        doc_label.setText("Documents: ")
        doc_layout.addWidget(doc_label)

        doc_display = QLabel(layoutWidget)
        doc_display.setObjectName(u"doc_display")
        doc_display.setMinimumSize(QSize(200, 0))
        doc_display.setMaximumSize(QSize(50, 16777215))
        doc_display.setFont(font5)
        doc_display.setStyleSheet(u"border: none;")
        doc_display.setScaledContents(False)
        doc_display.setWordWrap(True)
        doc_display.setText(clinic_data.get("uploadDoc_status", "Unknown"))
        doc_layout.addWidget(doc_display)

        view_doc_btn = QPushButton(layoutWidget)
        view_doc_btn.setObjectName(u"view_doc_btn")
        view_doc_btn.setMaximumSize(QSize(190, 16777215))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(9)
        font6.setUnderline(True)
        view_doc_btn.setFont(font6)
        view_doc_btn.setStyleSheet(u"color: #007E85; border: none;")

        doc_layout.addWidget(view_doc_btn)


        verticalLayout_2.addLayout(doc_layout)

        date_req_layout = QHBoxLayout()
        date_req_layout.setObjectName(u"date_req_layout")
        date_req_label = QLabel(layoutWidget)
        date_req_label.setObjectName(u"date_req_label")
        date_req_label.setFont(font4)
        date_req_label.setStyleSheet(u"border: none;")
        date_req_label.setWordWrap(True)
        date_req_label.setText("Date of request: ")
        date_req_layout.addWidget(date_req_label)

        date_req_display = QLabel(layoutWidget)
        date_req_display.setObjectName(u"date_req_display")
        date_req_display.setMinimumSize(QSize(390, 0))
        date_req_display.setFont(font5)
        date_req_display.setStyleSheet(u"border: none;")
        date_req_display.setScaledContents(False)
        date_req_display.setWordWrap(True)
        date_req_display.setText(clinic_data.get("clinic_dor", "Unknown"))
        date_req_layout.addWidget(date_req_display)


        verticalLayout_2.addLayout(date_req_layout)

        #if status is pending display btn
        reject_clinic_btn = QPushButton(request_detail_outer)
        reject_clinic_btn.setObjectName(u"reject_clinic_btn")
        reject_clinic_btn.setGeometry(QRect(550, 790, 181, 41))
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        reject_clinic_btn.setFont(font7)
        reject_clinic_btn.setStyleSheet(u"background-color: #E73030; border-radius: 16px; color: white;\\n border: 1px solid gray;")
        reject_clinic_btn.setText("Reject Clinic")
        
        approve_clinic_btn = QPushButton(request_detail_outer)
        approve_clinic_btn.setObjectName(u"approve_clinic_btn")
        approve_clinic_btn.setGeometry(QRect(340, 790, 181, 41))
        approve_clinic_btn.setFont(font7)
        approve_clinic_btn.setStyleSheet(u"background-color: #528265; border-radius: 16px; color: white;\\n border: 1px solid gray;")
        approve_clinic_btn.setText("Approve Clinic")
        
        status = clinic_data.get("clinic_status")
        if status == "pending":
                # Display the reject and approve buttons
                reject_clinic_btn.show()
                approve_clinic_btn.show()
        else:
                # Hide the reject and approve buttons
                reject_clinic_btn.hide()
                approve_clinic_btn.hide()

        
        return request_detail_outer

    def create_popup_widget(self, clinic_data):
        self.hide_clinic_details_frame()
        self.clinic_details_frame = self.create_clinic_details_frame(clinic_data)
        self.clinic_details_frame.setVisible(True)

    def search_clinics(self):
        search_text = self.search_clinic.text().strip().lower()
        if search_text:
                self.hide_clinic_details_frame()
                self.populate_clinic_info(search_text)
                self.hide_clinic_details_frame()
                
        else:
                self.hide_clinic_details_frame()
                self.populate_clinic_info()
                self.hide_clinic_details_frame()

    def clear_search(self):
        self.search_clinic.clear()
        self.hide_clinic_details_frame()

        # Remove all widgets from the layout
        while self.vLayout.count():
                widget = self.vLayout.takeAt(0).widget()
                if widget:
                        widget.deleteLater()
        self.hide_clinic_details_frame()
        self.populate_clinic_info()
        self.hide_clinic_details_frame()


    def hide_clinic_details_frame(self):
        if self.clinic_details_frame:
            self.clinic_details_frame.setVisible(False)

    def load_states(self):
        states = [
            "All",
            "Johor",
            "Kedah",
            "Kelantan",
            "Kuala Lumpur",
            "Labuan",
            "Melaka",
            "Negeri Sembilan",
            "Pahang",
            "Perak",
            "Perlis",
            "Penang",
            "Putrajaya",
            "Sabah",
            "Sarawak",
            "Selangor",
            "Terengganu"
        ]
        self.filter.addItems(states)

    def updateSelectedState(self, index):
        selected_text = self.filter.itemText(index)

        if index == 0:
                self.selected_state = ""
        else:
                self.selected_state = selected_text
        self.hide_clinic_details_frame()
        self.populate_clinic_info()
        self.hide_clinic_details_frame()










