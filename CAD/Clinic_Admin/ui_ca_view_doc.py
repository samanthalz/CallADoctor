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
        self.doctor_data_list = []
        self.clinic_data_list = []
        self.selected_status = ""
        self.setupUi(self)
        self.doctors_navigation = QToolButton(self)
        self.doctors_details_frame = None
        self.temp_doctors_name = ""
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
        self.profile_btn.clicked.connect(self.emitProfileBtn)


        self.search_doctor = QLineEdit(self.background)
        self.search_doctor.setObjectName(u"search_doctor")
        self.search_doctor.setGeometry(QRect(40, 40, 681, 71))
        self.search_doctor.setMinimumSize(QSize(681, 71))
        self.search_doctor.setMaximumSize(QSize(681, 71))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(11)
        self.search_doctor.setFont(font1)
        self.search_doctor.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 60px; color: Black;\n"
        " background-image: url(\"CAD/Images/icon/search_icon.png\"); \n"
        "background-repeat: no-repeat; \n"
        "background-position: left center; \n"
        "background-size: 20px 20px; \n"
        "border: 1px solid gray;\n")
        self.search_doctor.setClearButtonEnabled(False)
        
        self.filter = QComboBox(self.background)
        self.filter.setObjectName(u"filter")
        self.filter.setGeometry(QRect(520, 170, 340, 31))
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(12)
        self.filter.setFont(font7)
        self.filter.setStyleSheet(u"border: 1px solid gray;")
        self.filter.activated.connect(self.updateSelectedStatus)
        
        self.doc_label = QLabel(self.background)
        self.doc_label.setObjectName(u"doc_label")
        self.doc_label.setGeometry(QRect(50, 160, 341, 41))
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(16)
        self.doc_label.setFont(font8)
        self.doc_label.setStyleSheet(u"border : none;\n")
        self.doc_details_label = QLabel(self.background)
        self.doc_details_label.setObjectName(u"doc_details_label")
        self.doc_details_label.setGeometry(QRect(990, 150, 571, 41))
        font9 = QFont()
        font9.setFamily(u"Consolas")
        font9.setPointSize(16)
        self.doc_details_label.setFont(font9)
        self.doc_details_label.setStyleSheet(u"border : none;\n")
        
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
        self.search_btn.clicked.connect(self.search_patients)
        
        self.scrollArea = QScrollArea(self.background)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(50, 300, 811, 821))
        self.scrollArea.setMinimumSize(QSize(811, 821))
        self.scrollArea.setMaximumSize(QSize(811, 821))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 811, 821))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.vLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.vLayout.setSpacing(10)
        self.vLayout.setObjectName(u"vLayout")
        self.vLayout.setContentsMargins(0, 0, 0, 0)
       
        
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 50, 87, 851))
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
        icon = QIcon()
        icon.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.doctors_navigation.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patients_navigation.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon4)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)
        self.verticalLayout.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Clinic", None))
        self.search_doctor.setPlaceholderText(QCoreApplication.translate("Form", u"Search Doctor Name", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.doc_label.setText(QCoreApplication.translate("Form", u"Doctors List", None))
        self.doc_details_label.setText(QCoreApplication.translate("Form", u"Doctor Details", None))
        self.add_doc_btn.setText(QCoreApplication.translate("Form", u"Add New Doctor", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.doctors_navigation.setText(QCoreApplication.translate("Form", u"Doctors", None))
        self.patients_navigation.setText(QCoreApplication.translate("Form", u"Patients", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi
    
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
              
        self.load_status()
              
    def fetch_doc_data(self):
        # Clear list
        self.doctor_data_list = []
        db = self.initialize_db()
        #print(f"clinic is in ca doc is {self.clinic_id}")
        try:
                # Fetch the clinic data for the specific clinic_id
                clinic_data = db.child("clinic").child(self.clinic_id).get().val()
                
                if clinic_data:
                        doctors = clinic_data.get("doctors", {})
                        
                        for doctor_id, doctor_info in doctors.items():
                                # Add fetched doctor data to the list
                                #print(f"doc info is {doctor_info}")
                                self.doctor_data_list.append(doctor_info)

                        #print(f"ca list is {self.doctor_data_list}")
                        # Populate doctor information on the UI
                        self.populate_doctor_info()
                else:
                        print(f"No data found for clinic_id: {self.clinic_id}")
        
        except Exception as e:
                print(f"An error occurred while fetching data: {e}")


    def create_doctor_list_frame(self, doc_data):
        doc_frame_1 = QFrame(self.scrollAreaWidgetContents)
        doc_frame_1.setObjectName(u"doc_frame_1")
        doc_frame_1.setMinimumSize(QSize(801, 81))
        doc_frame_1.setMaximumSize(QSize(801, 81))
        doc_frame_1.setFrameShape(QFrame.StyledPanel)
        doc_frame_1.setFrameShadow(QFrame.Raised)
        doc_name_label_1 = QLabel(doc_frame_1)
        doc_name_label_1.setObjectName(u"doc_name_label_1")
        doc_name_label_1.setGeometry(QRect(130, 30, 600, 21))
        doc_name_label_1.setMinimumSize(QSize(600, 21))
        doc_name_label_1.setMaximumSize(QSize(600, 21))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(10)
        doc_name_label_1.setFont(font2)
        doc_name_label_1.setStyleSheet(u"border : none; color:black;")
        doc_name_label_1.setText(doc_data.get("doctor_name", "Unknown"))
        
        doc_name_label_1.mousePressEvent = lambda event, doctors=doc_data: self.create_popup_widget(doctors)
        
        doc_logo_label_1 = QLabel(doc_frame_1)
        doc_logo_label_1.setObjectName(u"doc_logo_label_1")
        doc_logo_label_1.setGeometry(QRect(10, 10, 80, 80))
        doc_logo_label_1.setMinimumSize(QSize(80, 80))
        doc_logo_label_1.setMaximumSize(QSize(80, 80))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(9)
        doc_logo_label_1.setFont(font3)
        doc_logo_label_1.setStyleSheet(u"background-color: transparent")
        doc_logo_label_1.setAlignment(Qt.AlignCenter)
        
        doc_img_path = doc_data.get("doctor_img", "Path Not Found")
        if doc_img_path:
                pixmap = QPixmap(doc_img_path)
                doc_logo_label_1.setPixmap(pixmap.scaled(doc_logo_label_1.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        return doc_frame_1

    def populate_doctor_info(self, search_query=None):
        self.clear_layout()

        visible_doctors = []

        for i, doctor_data in enumerate(self.doctor_data_list):
                if isinstance(doctor_data, dict):
                        doctor_name = doctor_data.get("doctor_name", "").lower()
                        speciality = doctor_data.get("specialization", "").lower()

                if self.selected_status and speciality.lower() != self.selected_status.lower():
                        continue

                # Check search query if provided
                if not search_query or search_query.lower() in doctor_name:
                    doctor_frame = self.create_doctor_list_frame(doctor_data)
                    if doctor_frame:
                            visible_doctors.append(doctor_frame)
                        
        #print(f"no of visible frames is {len(visible_doctors)}")
        # Add visible clinics to the layout in reverse order
        for patient_frame in reversed(visible_doctors):
                self.vLayout.addWidget(patient_frame)

        self.scrollAreaWidgetContents.setLayout(self.vLayout)
        self.vLayout.setAlignment(Qt.AlignTop)
        self.vLayout.update()
        self.scrollAreaWidgetContents.update()
        
    def clear_layout(self):
        while self.vLayout.count():
                item = self.vLayout.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.deleteLater()
                        
    def create_doctor_details_frame(self, doctor_data):
        doctor_details_outer = QFrame(self.background)
        doctor_details_outer.setObjectName(u"doctor_details_outer")
        doctor_details_outer.setGeometry(QRect(979, 200, 751, 841))
        doctor_details_outer.setStyleSheet(u"background-color : #ffffff;")
        doctor_details_outer.setFrameShape(QFrame.StyledPanel)
        doctor_details_outer.setFrameShadow(QFrame.Raised)
        doctor_details_inner = QFrame(doctor_details_outer)
        doctor_details_inner.setObjectName(u"doctor_details_inner")
        doctor_details_inner.setGeometry(QRect(20, 20, 711, 771))
        doctor_details_inner.setFrameShape(QFrame.StyledPanel)
        doctor_details_inner.setFrameShadow(QFrame.Raised)
        doc_name = QLabel(doctor_details_inner)
        doc_name.setObjectName(u"doc_name")
        doc_name.setGeometry(QRect(100, 30, 581, 21))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(10)
        doc_name.setFont(font2)
        doc_name.setStyleSheet(u"border : none;\n")
        doc_name.setText(doctor_data.get("doctor_name", "Unknown"))
        
        doc_logo = QLabel(doctor_details_inner)
        doc_logo.setObjectName(u"doc_logo")
        doc_logo.setGeometry(QRect(10, 10, 80, 80))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(9)
        doc_logo.setFont(font3)
        doc_logo.setStyleSheet(u"background-color: transparent;")
        doc_logo.setAlignment(Qt.AlignCenter)
        
        doc_img_path = doctor_data.get("doctor_img", "Path Not Found")
        if doc_img_path:
                pixmap = QPixmap(doc_img_path)
                doc_logo.setPixmap(pixmap.scaled(doc_logo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                
        line = QFrame(doctor_details_inner)
        line.setObjectName(u"line")
        line.setGeometry(QRect(20, 100, 671, 3))
        line.setMinimumSize(QSize(357, 3))
        line.setMaximumSize(QSize(16777215, 3))
        line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        line.setFrameShape(QFrame.StyledPanel)
        line.setFrameShadow(QFrame.Raised)
        layoutWidget = QWidget(doctor_details_inner)
        layoutWidget.setObjectName(u"layoutWidget")
        layoutWidget.setGeometry(QRect(3, 123, 710, 641))
        verticalLayout_2 = QVBoxLayout(layoutWidget)
        verticalLayout_2.setObjectName(u"verticalLayout_2")
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        phone_layout = QHBoxLayout()
        phone_layout.setObjectName(u"phone_layout")
        phone_label = QLabel(layoutWidget)
        phone_label.setObjectName(u"phone_label")
        phone_label.setMinimumSize(QSize(301, 153))
        phone_label.setMaximumSize(QSize(301, 153))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        phone_label.setFont(font4)
        phone_label.setStyleSheet(u"border: none;")
        phone_label.setLineWidth(0)
        phone_label.setText("Phone:")
        phone_layout.addWidget(phone_label)

        phone_display = QLabel(layoutWidget)
        phone_display.setObjectName(u"phone_display")
        phone_display.setMinimumSize(QSize(390, 153))
        phone_display.setMaximumSize(QSize(390, 153))
        font5 = QFont()
        font5.setFamily(u"Consolas")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setWeight(50)
        phone_display.setFont(font5)
        phone_display.setStyleSheet(u"border: none;")
        phone_display.setText(doctor_data.get("contact_number", "Unknown"))
        phone_layout.addWidget(phone_display)


        verticalLayout_2.addLayout(phone_layout)

        email_layout = QHBoxLayout()
        email_layout.setObjectName(u"email_layout")
        email_label = QLabel(layoutWidget)
        email_label.setObjectName(u"email_label")
        email_label.setMinimumSize(QSize(301, 153))
        email_label.setMaximumSize(QSize(301, 153))
        email_label.setFont(font4)
        email_label.setStyleSheet(u"border: none;")
        email_label.setText("Email:")
        email_layout.addWidget(email_label)

        email_display = QLabel(layoutWidget)
        email_display.setObjectName(u"email_display")
        email_display.setMinimumSize(QSize(390, 153))
        email_display.setMaximumSize(QSize(390, 153))
        email_display.setFont(font5)
        email_display.setStyleSheet(u"border: none;")
        email_display.setText(doctor_data.get("doctor_email", "Unknown"))
        email_layout.addWidget(email_display)


        verticalLayout_2.addLayout(email_layout)

        hour_layout = QHBoxLayout()
        hour_layout.setSpacing(6)
        hour_layout.setObjectName(u"hour_layout")
        hour_label = QLabel(layoutWidget)
        hour_label.setObjectName(u"hour_label")
        hour_label.setMinimumSize(QSize(301, 153))
        hour_label.setMaximumSize(QSize(301, 153))
        hour_label.setFont(font4)
        hour_label.setStyleSheet(u"border: none;")
        hour_label.setText("Doctor hours:")
        hour_layout.addWidget(hour_label)

        hour_display = QLabel(layoutWidget)
        hour_display.setObjectName(u"hour_display")
        hour_display.setMinimumSize(QSize(390, 153))
        hour_display.setMaximumSize(QSize(390, 153))
        hour_display.setFont(font5)
        hour_display.setStyleSheet(u"border: none;")
        hour_display.setScaledContents(False)
        hour_display.setWordWrap(True)
        hour_display.setText(doctor_data.get("doctor_hours", "Unknown"))
        hour_layout.addWidget(hour_display)


        verticalLayout_2.addLayout(hour_layout)

        speciality_layout = QHBoxLayout()
        speciality_layout.setObjectName(u"speciality_layout")
        speciality_layout.setSizeConstraint(QLayout.SetFixedSize)
        specialization_label = QLabel(layoutWidget)
        specialization_label.setObjectName(u"specialization_label")
        specialization_label.setMinimumSize(QSize(301, 153))
        specialization_label.setMaximumSize(QSize(301, 153))
        specialization_label.setFont(font4)
        specialization_label.setStyleSheet(u"border: none;")
        specialization_label.setWordWrap(True)
        specialization_label.setText("Specialization:")
        speciality_layout.addWidget(specialization_label)

        speciality_display = QLabel(layoutWidget)
        speciality_display.setObjectName(u"speciality_display")
        speciality_display.setMinimumSize(QSize(390, 153))
        speciality_display.setMaximumSize(QSize(390, 153))
        speciality_display.setFont(font5)
        speciality_display.setStyleSheet(u"border: none;")
        speciality_display.setScaledContents(False)
        speciality_display.setWordWrap(True)
        speciality_display.setText(doctor_data.get("specialization", "Unknown"))
        speciality_layout.addWidget(speciality_display)

        verticalLayout_2.addLayout(speciality_layout)

        remove_doc_btn = QPushButton(doctor_details_outer)
        remove_doc_btn.setObjectName(u"remove_doc_btn")
        remove_doc_btn.setGeometry(QRect(550, 750, 181, 41))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        remove_doc_btn.setFont(font6)
        remove_doc_btn.setStyleSheet(u"background-color: #E73030; border-radius: 16px; color: white; border: 1px solid gray;")
        remove_doc_btn.setText("Remove Doctor")
        remove_doc_btn.clicked.connect(self.remove_doc)

        return doctor_details_outer
        
                        
    def create_popup_widget(self, doctor_data):
        self.hide_doctor_details_frame()
        self.doctors_details_frame = self.create_doctor_details_frame(doctor_data)
        self.doctors_details_frame.setVisible(True)
        
    def hide_doctor_details_frame(self):
        if self.doctors_details_frame:
            self.doctors_details_frame.setVisible(False)
            
    def search_patients(self):
        search_text = self.search_doctor.text().strip().lower()
        if search_text:
                self.hide_doctor_details_frame()
                self.populate_doctor_info(search_text)
                self.hide_doctor_details_frame()
                
        else:
                self.hide_doctor_details_frame()
                self.populate_doctor_info()
                self.hide_doctor_details_frame()

    def clear_search(self):
        self.search_doctor.clear()
        self.hide_doctor_details_frame()

        # Remove all widgets from the layout
        while self.vLayout.count():
                widget = self.vLayout.takeAt(0).widget()
                if widget:
                        widget.deleteLater()
        self.hide_doctor_details_frame()
        self.populate_doctor_info()
        self.hide_doctor_details_frame()
        
    def load_status(self):
        self.initialize_db()
        specializations = set(["All"])  # Initialize with "All" and use a set to avoid duplicates
        
        # Fetch doctor data for the specific clinic_id
        db = self.initialize_db()
        
        try:
                clinic_data = db.child("clinic").child(self.clinic_id).get().val()
                
                if clinic_data:
                        doctors = clinic_data.get("doctors", {})
                        
                        for doctor_id, doctor_info in doctors.items():
                                specialization = doctor_info.get("specialization", "Unknown")
                                
                                # Ensure specialization is cleaned and split correctly
                                for spec in specialization.split(","):  # Split by comma if multiple specializations
                                        specializations.add(spec.strip())  # Add each specialization to the set
                
                        # Convert set to sorted list (optional)
                        status = sorted(list(specializations))
                        
                        # Add specializations to the filter widget
                        self.filter.addItems(status)
                        
                else:
                        print(f"No data found for clinic_id: {self.clinic_id}")
        
        except Exception as e:
                print(f"An error occurred while fetching data: {e}")

    def updateSelectedStatus(self, index):
        selected_text = self.filter.itemText(index)

        if index == 0:
                self.selected_status = ""
        else:
                self.selected_status = selected_text
        self.hide_doctor_details_frame()
        self.populate_doctor_info()
        self.hide_doctor_details_frame()
                        
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
                            #self.doc_data_list = [doctors for doctors in self.doc_data_list if doctors.get("doctor_name") != doctor_name]

                            # Refresh the clinic list after removal
                            self.populate_doctor_info()

                            # Hide the clinic details
                            self.hide_doctors_details_frame()

                    except Exception as e:
                            print(f"Failed to remove doctor: {e}")
                            QMessageBox.critical(self, "Error", f"Failed to remove doctor: {str(e)}")
            else:
                    QMessageBox.warning(self, "No Doctor Selected", "Please select a doctor to remove.")

    def fetch_clinic_data(self):
        db = self.initialize_db()
        try:
            clinics = db.child("clinic").get()
            
            if clinics.each():
                self.clinic_data_list = [clinic.val() for clinic in clinics.each()]
                #print("Fetched Clinics Data:", self.clinic_data_list)  # Debug: Print the fetched data
                #self.populate_clinic_info()
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

                            self.hide_doctor_details_frame()
                            
                            # Remove the doctor from doc_data_list
                            #self.doc_data_list = [doctors for doctors in self.doc_data_list if doctors.get("doctor_name") != doctor_name]

                            # Refresh the clinic list after removal
                            self.populate_doctor_info()

                    except Exception as e:
                            print(f"Failed to remove doctor: {e}")
                            QMessageBox.critical(self, "Error", f"Failed to remove doctor: {str(e)}")
            else:
                    QMessageBox.warning(self, "No Doctor Selected", "Please select a doctor to remove.")