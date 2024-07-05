from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class CA_view_docWidget(QWidget):
    home_navigation_btn_clicked = pyqtSignal()
    doctors_navigation_btn_clicked = pyqtSignal()
    patients_navigation_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    settings_navigation_btn_clicked = pyqtSignal()
    add_doc_navigation_btn_clicked = pyqtSignal()
    remove_doc_navigation_btn_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.clinic_id = ""
        self.doc_data_list = []
        self.setupUi(self)
        self.fetch_doc_data()
        self.fetch_clinic_data()
        self.doctors_navigation = QToolButton(self)
        self.doctors_details_frame = None
        self.temp_doctors_name = ""
        self.temp_clinic_name = ""

        
    def setupUi(self, Form):
        """ self.view_patient_details_button = QPushButton(Form)
        self.view_patient_details_button.setObjectName("view_patient_details_button")
        self.view_patient_details_button.setText("View Patient Details")
        self.view_patient_details_button.clicked.connect(self.handle_view_patient_details) """
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

        """ def handle_view_patient_details(self):
        # Handle button click logic here
        print("View Patient Details button clicked")
    def on_view_patient_details_clicked(self):
        # Example method when button is clicked
        print("View Patient Details button clicked!") """
        
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
        font.setPointSize(10)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet(u"border: none")
        self.search_doctors = QLineEdit(self.background)
        self.search_doctors.setObjectName(u"search_doctors")
        self.search_doctors.setGeometry(QRect(40, 40, 831, 71))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(11)
        self.search_doctors.setFont(font1)
        self.search_doctors.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 60px; color: Black;\n"
" background-image: url(\"C:/Users/Samantha Law/Documents/INTI/CAD/CallADoctor/CAD/Images/icon/search_icon.png\"); \n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"

"border: 1px solid gray;\n"
"")

        self.profile_btn.clicked.connect(self.emitProfileBtn)

        self.search_doctors.setClearButtonEnabled(False)

       
        self.upcoming_label = QLabel(self.background)
        self.upcoming_label.setObjectName(u"upcoming_label")
        self.upcoming_label.setGeometry(QRect(50, 160, 341, 41))
        font8 = QFont()
        font8.setFamily(u"Cascadia Code")
        font8.setPointSize(16)
        self.upcoming_label.setFont(font8)
        self.upcoming_label.setStyleSheet(u"border : none;\n"
"")


        self.doc_detail_label = QLabel(self.background)
        self.doc_detail_label.setObjectName(u"doc_detail_label")
        self.doc_detail_label.setGeometry(QRect(990, 150, 571, 41))
        font9 = QFont()
        font9.setFamily(u"Consolas")
        font9.setPointSize(16)
        self.doc_detail_label.setFont(font9)
        self.doc_detail_label.setStyleSheet(u"border : none;\n"
"")
        self.add_doc_btn = QPushButton(self.background)
        self.add_doc_btn.setObjectName(u"add_doc_btn")
        self.add_doc_btn.setGeometry(QRect(60, 220, 801, 51))
        font10 = QFont()
        font10.setFamily(u"Consolas")
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setWeight(75)
        self.add_doc_btn.setFont(font10)
        self.add_doc_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white; border: 1px solid gray;")
       
        self.add_doc_btn.clicked.connect(self.emitAddDocBtn)
       
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
        font11 = QFont()
        font11.setFamily(u"Source Sans Pro Semibold")
        font11.setPointSize(10)
        font11.setBold(True)
        font11.setWeight(75)
        self.home_navigation.setFont(font11)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.home_navigation.clicked.connect(self.emitHomeBtn)

        self.verticalLayout.addWidget(self.home_navigation)

        self.doctors_navigation = QToolButton(self.layoutWidget_2)
        self.doctors_navigation.setObjectName(u"doctors_navigation")
        self.doctors_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.doctors_navigation.sizePolicy().hasHeightForWidth())
        self.doctors_navigation.setSizePolicy(sizePolicy)
        self.doctors_navigation.setMinimumSize(QSize(85, 96))
        self.doctors_navigation.setMaximumSize(QSize(85, 96))
        self.doctors_navigation.setFont(font11)
        self.doctors_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.doctors_navigation.setIcon(icon2)
        self.doctors_navigation.setIconSize(QSize(70, 70))
        self.doctors_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.doctors_navigation.clicked.connect(self.emitDoctorsBtn)

        self.verticalLayout.addWidget(self.doctors_navigation)

        self.patients_navigation = QToolButton(self.layoutWidget_2)
        self.patients_navigation.setObjectName(u"patients_navigation")
        self.patients_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.patients_navigation.sizePolicy().hasHeightForWidth())
        self.patients_navigation.setSizePolicy(sizePolicy)
        self.patients_navigation.setMinimumSize(QSize(85, 96))
        self.patients_navigation.setMaximumSize(QSize(85, 96))
        self.patients_navigation.setFont(font11)
        self.patients_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patients_navigation.setIcon(icon3)
        self.patients_navigation.setIconSize(QSize(70, 70))
        self.patients_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.patients_navigation.clicked.connect(self.emitPatientsBtn)

        self.verticalLayout.addWidget(self.patients_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget_2)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setMinimumSize(QSize(85, 96))
        self.settings_navigation.setMaximumSize(QSize(85, 96))
        self.settings_navigation.setFont(font11)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.settings_navigation.clicked.connect(self.emitSettingsBtn)

        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget_2)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setMinimumSize(QSize(85, 96))
        self.logout_navigation.setMaximumSize(QSize(85, 96))
        self.logout_navigation.setFont(font11)
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

    def on_doctors_navigation_btn_clicked(self):
        # Slot/function to handle doctors_navigation_btn clicked
        # Display QMessageBox or perform other actions
        QMessageBox.information(self, 'Info', 'View Doc button clicked.')

    def on_add_doc_navigation_btn_clicked(self):
        # Slot/function to handle add_doc_navigation_btn clicked
        # Display QMessageBox or perform other actions
        QMessageBox.information(self, 'Info', 'Add doctor button clicked.')


    def show_view_patient_details_message(self):
        QMessageBox.information(self, 'Info', 'View Patient Details button clicked.')

    def show_logout_message(self):
        QMessageBox.information(self, 'Info', 'Logout button clicked.')

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"clinic name", None))
        self.search_doctors.setPlaceholderText(QCoreApplication.translate("Form", u"Search doctors Name", None))
        

        self.upcoming_label.setText(QCoreApplication.translate("Form", u"Doctors List", None))
        self.doc_detail_label.setText(QCoreApplication.translate("Form", u"Doctor Details", None))
        self.add_doc_btn.setText(QCoreApplication.translate("Form", u"Add New Doctor", None))

        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.doctors_navigation.setText(QCoreApplication.translate("Form", u"doctorss", None))
        self.patients_navigation.setText(QCoreApplication.translate("Form", u"patients", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi


    def fetch_doc_data(self):
        db = self.initialize_db()  # Assuming this method initializes your Firebase connection
        try:
            clinics = db.child("clinic").get()
            
            if clinics.each():
                print(f"if clinic.each(): {clinics}")
                self.doc_data_list = []
                
                for clinic in clinics.each():
                    print(f"for clinic in clinics.each(): {clinic}")
                    clinic_data = clinic.val()
                    clinic_id = clinic.key()  # Assuming clinic ID is stored as the key
                    
                    if clinic_id == self.clinic_id:
                        print(f"if clinic_id == self.clinic_id: {clinic_id}")
                        doctors = clinic_data.get("doctors", {})
                        
                        for doctor_id, doctor_info in doctors.items():
                            print(f"for doctor_id, doctor_info in doctors.items(): {doctor_id}")
                            doctor_name = doctor_info.get("name", "Unknown")
                            
                            # Add fetched doctor data to the list
                            self.doc_data_list.append({"doctor_id": doctor_id, "doctor_name": doctor_name})
                        
                        break  # Assuming each clinic_id is unique and we only need to process the relevant clinic
                
                # Populate doctor information on the UI
                self.populate_doctor_info()
            else:
                print("No clinics data found.")
        
        except Exception as e:
            print(f"An error occurred while fetching data: {e}")


    def create_doctor_list_frame(self, doc_data):
        doc_frame = QFrame(self.background)
        doc_frame.setObjectName(u"doc_frame")
        doc_frame.setGeometry(QRect(60, 290, 801, 81))
        doc_frame.setFrameShape(QFrame.StyledPanel)
        doc_frame.setFrameShadow(QFrame.Raised)
        doc_name_label = QLabel(doc_frame)
        doc_name_label.setObjectName(u"doc_name_label")
        doc_name_label.setGeometry(QRect(90, 30, 121, 21))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(10)
        doc_name_label.setFont(font2)
        doc_name_label.setStyleSheet(u"border : none;\n"
"")
        doc_name_label = QLabel(doc_data["doctor_name"])
        doc_name_label.mousePressEvent = lambda event, doctors=doc_data: self.create_popup_widget(doctors)
        
        doc_logo_label = QLabel(doc_frame)
        doc_logo_label.setObjectName(u"doc_logo_label")
        doc_logo_label.setGeometry(QRect(10, 10, 54, 54))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(9)
        doc_logo_label.setFont(font3)
        doc_logo_label.setStyleSheet(u"background-color: #B6D0E2; \n"
"border-radius: 25px; \n"
"border: 2px solid #B6D0F7; \n"
"min-width: 50px; \n"
"min-height: 50px; \n"
"max-width: 50px;\n"
"max-height: 50px; ")
        doc_logo_label.setAlignment(Qt.AlignCenter)
    
        doc_img_path = doc_data.get("doc_img", "Path Not Found")
        if doc_img_path:
                pixmap = QPixmap(doc_img_path)
                doc_logo_label.setPixmap(pixmap.scaled(doc_logo_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        return doc_frame
    
    def clear_layout(self):
        while self.create_doctor_list_frame.count():
                item = self.create_doctor_list_frame.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.destroy()
            
    def populate_doctor_info(self, search_query=None):

        visible_doctors = []

        for doc_data in self.doc_data_list:
            if isinstance(doc_data, dict):
                doctor_name = doc_data.get("doctor_name", "").lower()

            # Check search query if provided
            if not search_query or search_query.lower() in doctor_name:
                doctor_frame = self.create_doctor_list_frame(doc_data)
                if doctor_frame:
                    visible_doctors.append(doctor_frame)

        # Add visible doctors to the layout in reverse order
        for doctor_frame in reversed(visible_doctors):
            self.verticalLayout_4.addWidget(doctor_frame)

        self.widget.setLayout(self.doctors_details_frame)
        self.doctors_details_frame.setAlignment(Qt.AlignTop)
        self.widget.update()
        self.doctors_details_frame.update()

  
         # Debug: Final update status
        print("Layout and widget updated.")

    def initialize_db(self):
        return db

    def set_user_id(self, user_id): 
        #self.clinic_id = user_id
        user_id = user_id.lower()
        clinics = db.child("clinic").get().val()
        for clinic_id, clinic_data in clinics.items():
                clinic_name = clinic_data.get("clinic_name")
                if clinic_name.lower().replace(" ", "") == user_id:
                      self.clinic_id = clinic_id
                      break
        self.fetch_doc_data()


    def create_doctors_details_frame(self, doc_data):
        request_detail_outer = QFrame(self.background)
        request_detail_outer.setObjectName(u"request_detail_outer")
        request_detail_outer.setGeometry(QRect(979, 200, 751, 841))
        request_detail_outer.setStyleSheet(u"background-color : #ffffff;")
        request_detail_outer.setFrameShape(QFrame.StyledPanel)
        request_detail_outer.setFrameShadow(QFrame.Raised)

        doctors_details_inner = QFrame(request_detail_outer)
        doctors_details_inner.setObjectName(u"doctors_details_inner")
        doctors_details_inner.setGeometry(QRect(20, 20, 711, 771))
        doctors_details_inner.setFrameShape(QFrame.StyledPanel)
        doctors_details_inner.setFrameShadow(QFrame.Raised)

        doc_name = QLabel(doctors_details_inner)
        doc_name.setObjectName(u"doc_name")
        doc_name.setGeometry(QRect(100, 30, 121, 21))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(10)
        doc_name.setFont(font2)
        doc_name.setStyleSheet(u"border : none;\n"
"")
        
        self.temp_doc_name = doc_data["doctor_name"]

        doc_logo = QLabel(doctors_details_inner)
        doc_logo.setObjectName(u"doc_logo")
        doc_logo.setGeometry(QRect(10, 10, 54, 54))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(9)
        doc_logo.setFont(font3)
        doc_logo.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        doc_logo.setAlignment(Qt.AlignCenter)

        doc_img_path = doc_data.get("doc_img", "")
        if doc_img_path:
                pixmap = QPixmap(doc_img_path)
                doc_logo.setPixmap(pixmap.scaled(doc_logo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        line = QFrame(doctors_details_inner)
        line.setObjectName(u"line")
        line.setGeometry(QRect(20, 100, 671, 3))
        line.setMinimumSize(QSize(357, 3))
        line.setMaximumSize(QSize(16777215, 3))
        line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        line.setFrameShape(QFrame.StyledPanel)
        line.setFrameShadow(QFrame.Raised)

        layoutWidget = QWidget(doctors_details_inner)
        layoutWidget.setObjectName(u"layoutWidget")
        layoutWidget.setGeometry(QRect(3, 123, 701, 641))

        verticalLayout_2 = QVBoxLayout(layoutWidget)
        verticalLayout_2.setObjectName(u"verticalLayout_2")
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        phone_layout = QHBoxLayout()
        phone_layout.setObjectName(u"phone_layout")
        phone_label = QLabel(layoutWidget)
        phone_label.setObjectName(u"phone_label")
        phone_label.setText("Phone Number: ")
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        phone_label.setFont(font4)
        phone_label.setStyleSheet(u"border: none;")
        phone_label.setLineWidth(0)

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
        phone_display.setText(doc_data.get("contact_number", "Unknown"))
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
        email_display.setText(doc_data.get("doctor_email", "Unknown"))
        email_layout.addWidget(email_display)


        verticalLayout_2.addLayout(email_layout)

        add_layout = QHBoxLayout()
        add_layout.setSpacing(135)
        add_layout.setObjectName(u"add_layout")
        add_label = QLabel(layoutWidget)
        add_label.setObjectName(u"add_label")
        add_label.setFont(font4)
        add_label.setStyleSheet(u"border: none;")
        add_label.setText("Doctor hours: ")
        add_layout.addWidget(add_label)

        add_display = QLabel(layoutWidget)
        add_display.setObjectName(u"add_display")
        add_display.setFont(font5)
        add_display.setStyleSheet(u"border: none;")
        add_display.setScaledContents(False)
        add_display.setWordWrap(True)
        add_display.setText(doc_data.get("doctor_hours", "Unknown"))
        add_layout.addWidget(add_display)


        verticalLayout_2.addLayout(add_layout)

        opening_hr_layout = QHBoxLayout()
        opening_hr_layout.setObjectName(u"opening_hr_layout")
        opening_hr_layout.setSizeConstraint(QLayout.SetFixedSize)
        specialization_label = QLabel(layoutWidget)
        specialization_label.setObjectName(u"specialization_label")
        specialization_label.setFont(font4)
        specialization_label.setStyleSheet(u"border: none;")
        specialization_label.setWordWrap(True)
        specialization_label.setText(" Specialization: ")
        opening_hr_layout.addWidget(specialization_label)

        specialization_display = QLabel(layoutWidget)
        specialization_display.setObjectName(u"specialization_display")
        specialization_display.setMinimumSize(QSize(390, 0))
        specialization_display.setFont(font5)
        specialization_display.setStyleSheet(u"border: none;")
        specialization_display.setScaledContents(False)
        specialization_display.setWordWrap(True)
        specialization_display.setText(doc_data.get("specialization", "Unknown"))
        opening_hr_layout.addWidget(specialization_display)


        verticalLayout_2.addLayout(opening_hr_layout)

        remove_doc_btn = QPushButton(request_detail_outer)
        remove_doc_btn.setObjectName(u"remove_doc_btn")
        remove_doc_btn.setGeometry(QRect(550, 790, 181, 41))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        remove_doc_btn.setFont(font6)
        remove_doc_btn.setStyleSheet(u"background-color: #E73030; border-radius: 16px; color: white; border: 1px solid gray;")
        remove_doc_btn.setText("Remove Doctor")
        remove_doc_btn.clicked.connect(self.emitRemoveDocBtn)   

        return request_detail_outer

    def create_popup_widget(self, doc_data):
        self.hide_doctors_details_frame()
        self.doctors_details_frame = self.create_doctors_details_frame(doc_data)
        self.doctors_details_frame.setVisible(True)

    def search_doctors(self):
        search_text = self.search_doctors.text().strip().lower()
        if search_text:
                self.hide_doctors_details_frame()
                self.populate_doctors_info(search_text)
                self.hide_doctors_details_frame()
                
        else:
                self.hide_doctors_details_frame()
                self.populate_doctors_info()
                self.hide_doctors_details_frame()
        
    def clear_search(self):
        self.search_doctors.clear()
        self.hide_doctors_details_frame()

         # Remove all widgets from the layout
        while self.vLayout.count():
                widget = self.vLayout.takeAt(0).widget()
                if widget:
                        widget.deleteLater()
        self.hide_clinic_details_frame()
        self.populate_clinic_info()
        self.hide_clinic_details_frame()


    def hide_doctors_details_frame(self):
        if self.doctors_details_frame:
            self.doctors_details_frame.setVisible(False)

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

    def remove_doc(self):
            clinic_name = self.temp_clinic_name
            clinic_id = None
            doctors_id = None

            if not self.clinic_data_list:
                    return None

            # Fetch the clinic data directly from the database
            try:
                    clinic_data_list = db.child("clinic").get().val()
            except Exception as e:
                    print(f"Failed to fetch clinic data: {e}")
                    return

            # Find the clinic ID by clinic name
            for cid, clinic_data in clinic_data_list.items():
                    if clinic_data.get("clinic_name") == clinic_name:
                            clinic_id = cid
                            break

            if clinic_id:
                    try:
                            db.child("clinic").child(clinic_id).remove()
                            
                            # Find and remove the associated doctor
                            doctors = db.child("doctors").get()
                            for doctors in doctors.each():
                                    doctors = doctors.val()
                                    if clinic_data.get("clinic_id").lower() == clinic_id.lower():
                                            doctors_id = doctors.key()
                                            db.child("doctors").child(doctors_id).remove()
                                            break
                                    
                            QMessageBox.information(self, "Success", "Doctor removed from the database.")

                            self.hide_doctors_details_frame()
                            
                            # Remove the doctor from doc_data_list
                            self.doc_data_list = [doctors for doctors in self.doc_data_list if doctors.get("doctor_name") != doctor_name]

                            # Refresh the clinic list after removal
                            self.populate_doctor_info()

                            # Hide the clinic details
                            self.hide_doctors_details_frame()

                    except Exception as e:
                            print(f"Failed to remove doctor: {e}")
                            QMessageBox.critical(self, "Error", f"Failed to remove doctor: {str(e)}")
            else:
                    QMessageBox.warning(self, "No Doctor Selected", "Please select a doctor to remove.")
        


    @pyqtSlot()
    def emitHomeBtn(self):
        self.home_navigation_btn_clicked.emit()

    @pyqtSlot()
    def emitDoctorsBtn(self):
        self.doctors_navigation_btn_clicked.emit()

    @pyqtSlot()
    def emitPatientsBtn(self):
        self.patients_navigation_btn_clicked.emit()    
        
    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
    
    @pyqtSlot()
    def emitSettingsBtn(self):
        # Emit the custom signal
        self.settings_navigation_btn_clicked.emit()

    @pyqtSlot()
    def emitProfileBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()

    @pyqtSlot()
    def emitAddDocBtn(self):
        # Emit the custom signal
        self.add_doc_navigation_btn_clicked.emit()

    @pyqtSlot()
    def emitRemoveDocBtn(self):
        # Emit the custom signal
        self.remove_doc_navigation_btn_clicked.emit()

