from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db

class FindDoctorWidget(QWidget):
    service_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    viewDoctorProfileRequested = pyqtSignal(str, str) 
    makeAppointmentRequested = pyqtSignal(str, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clinic_data_list = []
        self.selected_clinic = ""
        self.selected_specialization = ""
        self.selected_doctor = ""
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
        self.fad_title = QLabel(self.whitebg)
        self.fad_title.setObjectName(u"fad_title")
        self.fad_title.setGeometry(QRect(60, 40, 481, 81))
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
        self.scrollAreaWidgetContents.setLayout(self.gridLayout)
        
        self.layoutWidget2 = QWidget(self.whitebg)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(81, 141, 1641, 48))
        self.seopdown_layout = QHBoxLayout(self.layoutWidget2)
        self.seopdown_layout.setSpacing(80)
        self.seopdown_layout.setObjectName(u"seopdown_layout")
        self.seopdown_layout.setContentsMargins(0, 0, 0, 0)
        
        
        self.clinic_dropdown = QComboBox(self.layoutWidget2)
        self.clinic_dropdown.setEditable(False)
        self.clinic_dropdown.setObjectName(u"clinic_dropdown")
        self.clinic_dropdown.setMinimumSize(QSize(321, 41))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(11)
        self.clinic_dropdown.setFont(font2)
        self.clinic_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
        "border-radius: 5px; \n"
        "background-color: #FFFFFF; \n"
        "padding: 10px; \n"
        "font-family: Consolas;\n"
        "font-size: 11pt;")
        self.clinic_dropdown.setIconSize(QSize(50, 50))
        self.clinic_dropdown.setFrame(True)
        self.clinic_dropdown.currentIndexChanged.connect(self.updateSelectedClinic)
        self.seopdown_layout.addWidget(self.clinic_dropdown)
        
        self.load_clinics()
        
        self.speciality_dropdown = QComboBox(self.layoutWidget2)
        self.speciality_dropdown.setObjectName(u"speciality_dropdown")
        self.speciality_dropdown.setMinimumSize(QSize(321, 41))
        self.speciality_dropdown.setFont(font2)
        self.speciality_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
        "border-radius: 5px; \n"
        "background-color: #FFFFFF; \n"
        "padding: 10px; \n"
        "font-family: Consolas;\n"
        "font-size: 11pt;")
        self.speciality_dropdown.setEditable(False)
        self.speciality_dropdown.setIconSize(QSize(50, 50))
        self.speciality_dropdown.setFrame(True)
        self.speciality_dropdown.currentIndexChanged.connect(self.updateSelectedSpecialization)
        self.seopdown_layout.addWidget(self.speciality_dropdown)
        
        self.load_specializations()

        self.doc_dropdown = QComboBox(self.layoutWidget2)
        self.doc_dropdown.setObjectName(u"doc_dropdown")
        self.doc_dropdown.setMinimumSize(QSize(321, 41))
        self.doc_dropdown.setFont(font2)
        self.doc_dropdown.setStyleSheet(u"border: 1px solid #000000;\n"
        "border-radius: 5px; \n"
        "background-color: #FFFFFF; \n"
        "padding: 10px; \n"
        "font-family: Consolas;\n"
        "font-size: 11pt;")
        self.doc_dropdown.setEditable(False)
        self.doc_dropdown.setIconSize(QSize(50, 50))
        self.doc_dropdown.setFrame(True)
        self.doc_dropdown.currentIndexChanged.connect(self.updateSelectedDoctor)
        self.seopdown_layout.addWidget(self.doc_dropdown)
        
        self.load_doctors()

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
        self.services_navigation.clicked.connect(self.emitServiceBtn)

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
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)
        self.verticalLayout_2.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.noti_icon.setText("")
        self.fad_title.setText(QCoreApplication.translate("Form", u"Find A Doctor", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
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
        
    def fetch_clinic_data(self):
        try:
            clinics = db.child("clinic").get()
            
            if clinics.each():
                self.clinic_data_list = [clinic.val() for clinic in clinics.each()]
                #print("Fetched Clinics Data:", self.clinic_data_list)  # Debug: Print the fetched data
                self.populate_doc_info()
            else:
                print("No clinics data found.")
        except Exception as e:
            print(f"An error occurred while fetching data: {e}")
            
    def clear_layout(self):
        while self.gridLayout.count():
                item = self.gridLayout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                        widget.deleteLater()
        
    def populate_doc_info(self):
        # Clear existing items from the layout
        self.clear_layout()
        
        visible_doctors = []
        
        for clinic in self.clinic_data_list:
            if isinstance(clinic, dict):
                clinic_name = clinic.get("clinic_name", "")
                doctors = clinic.get("doctors", {})
                
                for doc_id, doctor in doctors.items():
                    doctor_name = doctor.get("doctor_name", "")
                    specialization = doctor.get("specialization", "")
                    #print(f"Clinic: {clinic_name}, Doctor: {doctor_name}, Specialization: {specialization}")

                    # Check the selected clinic
                    if self.selected_clinic and clinic_name.lower() != self.selected_clinic.lower():
                        #print(f"Skipping doctor {doctor_name} in clinic {clinic_name} due to clinic name.")
                        continue

                    # Check the selected specialization
                    if self.selected_specialization and specialization.lower() != self.selected_specialization.lower():
                        #print(f"Skipping doctor {doctor_name} in clinic {clinic_name} due to specialization.")
                        continue

                    # Check the selected doctor
                    if self.selected_doctor and doctor_name.lower() != self.selected_doctor.lower():
                        #print(f"Skipping doctor {doctor_name} due to doctor name.")
                        continue

                    #print(f"Adding doctor {doctor_name} in clinic {clinic_name} to layout.")
                    doctor_outer = self.create_doctor_frame(clinic, doctor)
                    if doctor_outer:
                        visible_doctors.append(doctor_outer)

        # Add visible doctors to the layout
        for i, doctor_outer in enumerate(visible_doctors):
            row = i // 3
            col = i % 3
            self.gridLayout.addWidget(doctor_outer, row, col)

        # Refresh the layout after adding all frames
        self.gridLayout.update()
        self.scrollAreaWidgetContents.update()

    def load_clinics(self):
        try:
                clinics_data = db.child("clinic").get()
                clinic_names = [clinic.val().get("clinic_name", "") for clinic in clinics_data.each()]
                clinic_names = sorted(set(clinic_names))  # Sort and remove duplicates
                clinic_names.insert(0, "Search or Select a Clinic")  
                self.clinic_dropdown.addItems(clinic_names)
        except Exception as e:
                print(f"An error occurred while loading clinics: {e}")

    def load_specializations(self):
        try:
                doctors_data = db.child("clinic").get()
                specializations = []

                for clinic in doctors_data.each():
                        doctors = clinic.val().get("doctors", {})
                        for doctor_id, doctor_info in doctors.items():
                                if "specialization" in doctor_info:
                                        specialization = doctor_info["specialization"]
                                        specializations.append(specialization)
                                else:
                                        print("specialization not found")
                                        
                        
                # Sort and remove duplicates
                specializations = sorted(set(specializations))
                specializations.insert(0, "Search or Select a Specialization")  
                #print(f"final sorted specialixation {specialization}")
                self.speciality_dropdown.addItems(specializations)
        except Exception as e:
                print(f"An error occurred while loading specializations: {e}")
                
    def load_doctors(self):
        try:
                doctors_data = db.child("clinic").get()
                doctor_names = []

                for clinic in doctors_data.each():
                        doctors = clinic.val().get("doctors", {})
                        for doctor_id, doctor in doctors.items():
                                doctor_name = doctor.get("doctor_name", "")
                                if doctor_name:
                                        doctor_names.append(doctor_name)
                
                # Sort and remove duplicates
                doctor_names = sorted(set(doctor_names))
                doctor_names.insert(0, "Search or Select a Doctor")  
                self.doc_dropdown.addItems(doctor_names)
        except Exception as e:
                print(f"An error occurred while loading doctors: {e}")
          
    def updateSelectedClinic(self, index):
        #print("Activated signal received.")
        selected_text = self.clinic_dropdown.itemText(index)
        #print("Selected clinic text:", selected_text)

        if index == 0:
            self.selected_clinic = ""
        else:
            self.selected_clinic = selected_text

        #print("Updated selected clinic:", self.selected_clinic)
        self.populate_doc_info()

    def updateSelectedSpecialization(self, index):
        #print("Activated signal received.")
        selected_text = self.speciality_dropdown.itemText(index)
        #print("Selected specialization text:", selected_text)

        if index == 0:
            self.selected_specialization = ""
        else:
            self.selected_specialization = selected_text

        #print("Updated selected specialization:", self.selected_specialization)
        self.populate_doc_info()
        
    def updateSelectedDoctor(self, index):
        #print("Activated signal received.")
        selected_text = self.doc_dropdown.itemText(index)
        #print("Selected doctor text:", selected_text)

        if index == 0:
                self.selected_doctor = ""
        else:
                self.selected_doctor = selected_text

        #print("Updated selected doctor:", self.selected_doctor)
        self.populate_doc_info()

    def create_doctor_frame(self, clinic, doctor):
        doc_info_outer = QFrame()
        doc_info_outer.setObjectName(u"doc_info_outer")
        doc_info_outer.setGeometry(QRect(0, 0, 388, 535))
        doc_info_outer.setStyleSheet(u"border: 1px solid black; \n""border-radius: 24px; ")
        doc_info_outer.setFrameShape(QFrame.StyledPanel)
        doc_info_outer.setFrameShadow(QFrame.Raised)
        doc_info_outer.setMinimumSize(QSize(388, 535))
        doc_info_outer.setMaximumSize(QSize(388, 535))
        
        doc_info_inner = QFrame(doc_info_outer)
        doc_info_inner.setObjectName(u"doc_info_inner")
        doc_info_inner.setGeometry(QRect(0, 0, 388, 535))
        doc_info_inner.setStyleSheet(u"border: none; background-color: transparent;")
        doc_info_inner.setFrameShape(QFrame.StyledPanel)
        doc_info_inner.setFrameShadow(QFrame.Raised)
        
        layoutWidget = QWidget(doc_info_inner)
        layoutWidget.setObjectName(u"layoutWidget")
        layoutWidget.setGeometry(QRect(1, 480, 396, 55))
        
        btnlayout = QHBoxLayout(layoutWidget)
        btnlayout.setObjectName(u"btnlayout")
        btnlayout.setContentsMargins(0, 0, 0, 0)
        
        
        view_profile_btn = QPushButton(layoutWidget)
        view_profile_btn.setObjectName("view_profile_btn")
        view_profile_btn.setMinimumSize(QSize(193, 55))
        view_profile_btn.setStyleSheet("border-radius: 0 0 24pt 0; background-color: #B6D0E2; border: none;")
        view_profile_btn.setText("View Profile")
        font = QFont("Consolas", 10)
        view_profile_btn.setFont(font)
        view_profile_btn.setProperty("doctor_name", doctor.get("doctor_name", "Unknown"))
        view_profile_btn.clicked.connect(self.on_view_profile_button_clicked)


        btnlayout.addWidget(view_profile_btn)

        make_appt_btn = QPushButton(layoutWidget)
        make_appt_btn.setObjectName(u"make_appt_btn")
        make_appt_btn.setMinimumSize(QSize(193, 55))
        make_appt_btn.setStyleSheet(u"border-radius: 0 0 24pt 0; background-color: #B6D0E2; border: none;")
        make_appt_btn.setText("Make Appointment")
        font = QFont("Consolas", 10)
        make_appt_btn.setFont(font)
        make_appt_btn.clicked.connect(self.on_make_appointment_button_clicked)
        make_appt_btn.setProperty("clinic_name", clinic.get("clinic_name", "Unknown")) 
        make_appt_btn.setProperty("doctor_name", doctor.get("doctor_name", "Unknown"))
        
        btnlayout.addWidget(make_appt_btn)

        layoutWidget1 = QWidget(doc_info_inner)
        layoutWidget1.setObjectName(u"layoutWidget1")
        layoutWidget1.setGeometry(QRect(30, 30, 326, 451))
        
        verticalLayout = QVBoxLayout(layoutWidget1)
        verticalLayout.setObjectName(u"verticalLayout")
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        doc_img = QLabel(layoutWidget1)
        doc_img.setObjectName(u"doc_img")
        doc_img.setMinimumSize(QSize(324, 160))
        doc_img.setStyleSheet(u"border: none;")
        doc_img.setAlignment(Qt.AlignCenter)
        
        doc_img_path = doctor.get("doctor_img", "")
        if doc_img_path:
                pixmap = QPixmap(doc_img_path)
                doc_img.setPixmap(pixmap.scaled(doc_img.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        verticalLayout.addWidget(doc_img)
        verticalSpacer_3 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Fixed)
        verticalLayout.addItem(verticalSpacer_3)

        doc_name = QLabel(layoutWidget1)
        doc_name.setObjectName(u"doc_name")
        doc_name.setStyleSheet(u"text-align: center; border: none;")
        doc_name.setText(doctor.get("doctor_name", "Unknown"))
        font = QFont("Consolas", 12, QFont.Bold)
        doc_name.setFont(font)

        verticalLayout.addWidget(doc_name)

        doc_speciality = QLabel(layoutWidget1)
        doc_speciality.setObjectName(u"doc_speciality")
        doc_speciality.setStyleSheet(u"text-align: center; border: none;")
        doc_speciality.setText(doctor.get("specialization", "Unknown"))
        font = QFont("Consolas", 12, QFont.Bold)
        doc_speciality.setFont(font)

        verticalLayout.addWidget(doc_speciality)
        verticalSpacer = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(verticalSpacer)

        line = QFrame(layoutWidget1)
        line.setObjectName(u"line")
        line.setMinimumSize(QSize(324, 3))
        line.setMaximumSize(QSize(324, 3))
        line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        verticalLayout.addWidget(line)

        clinic_name = QLabel(layoutWidget1)
        clinic_name.setObjectName(u"clinic_name")
        clinic_name.setStyleSheet(u"text-align: center; border: none;")
        clinic_name.setText(clinic.get("clinic_name", "Unknown"))
        font = QFont("Consolas", 12, QFont.Bold)
        clinic_name.setFont(font)

        verticalLayout.addWidget(clinic_name)
        verticalSpacer_2 = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalLayout.addItem(verticalSpacer_2)
        
        return doc_info_outer

    @pyqtSlot()
    def on_view_profile_button_clicked(self):
        button = self.sender()  # Get the button that was clicked
        doctor_name = button.property("doctor_name")  # Retrieve the doctor name from the button's property
        
        # Find the corresponding clinic and doctor info using the doctor name
        clinic_name = ""
        doctor_id = ""
        for clinic in self.clinic_data_list:
            if isinstance(clinic, dict):
                doctors = clinic.get("doctors", {})
                for doc_id, doctor in doctors.items():
                    if doctor.get("doctor_name") == doctor_name:
                        clinic_name = clinic.get("clinic_name", "")
                        doctor_id = doc_id
                        break
                if clinic_name and doctor_id:
                    break
        
        print(f"Doctor ID: {doctor_id}, Clinic Name: {clinic_name}")
        if doctor_id and clinic_name:
            self.viewDoctorProfileRequested.emit(doctor_id, clinic_name)
            
            
    def on_make_appointment_button_clicked(self):
        button = self.sender()  # Get the button that was clicked
        clinic_name = button.property("clinic_name")  # Retrieve the clinic ID from the button's property
        doctor_name = button.property("doctor_name")  # Retrieve the doctor name from the button's property
        if clinic_name and doctor_name:
            self.makeAppointmentRequested.emit(clinic_name, doctor_name)
            
    def prefill_clinic(self, clinic_name):
        # Pre-fill the clinic dropdown
        clinic_index = self.clinic_dropdown.findText(clinic_name)
        if clinic_index != -1:
            self.clinic_dropdown.setCurrentIndex(clinic_index)

                