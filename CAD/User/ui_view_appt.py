from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,QMouseEvent,
    QRadialGradient)
from PyQt5.QtWidgets import *
import datetime
from connection import db


class ViewApptWidget(QWidget):
    service_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.appt_data_list = []
        self.selected_status = ""
        self.setupUi(self)
        self.fetch_appt_data()
        self.appt_details_frame = None
        self.temp_appt_id = ""
        
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
        font.setPointSize(16)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet(u"border: none")
        
        self.filter = QComboBox(self.background)
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.setObjectName(u"filter")
        self.filter.setGeometry(QRect(710, 170, 151, 31))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(12)
        self.filter.setFont(font4)
        self.filter.setStyleSheet(u"\n"
"border: 1px solid gray;")
        self.load_status()
        
        self.appt_list = QLabel(self.background)
        self.appt_list.setObjectName(u"appt_list")
        self.appt_list.setGeometry(QRect(50, 160, 341, 41))
        font5 = QFont()
        font5.setFamily(u"Cascadia Code")
        font5.setPointSize(16)
        self.appt_list.setFont(font5)
        self.appt_list.setStyleSheet(u"border : none;\n"
"")
        
        
        self.req_detail_label = QLabel(self.background)
        self.req_detail_label.setObjectName(u"req_detail_label")
        self.req_detail_label.setGeometry(QRect(990, 150, 571, 41))
        self.req_detail_label.setFont(font)
        self.req_detail_label.setStyleSheet(u"border : none;\n")
        
        self.scrollArea = QScrollArea(self.background)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(40, 230, 821, 731))
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
        self.layoutWidget_4 = QWidget(self.frame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(30, 19, 87, 871))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
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
        font8 = QFont()
        font8.setFamily(u"Source Sans Pro Semibold")
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setWeight(75)
        self.home_navigation.setFont(font8)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon = QIcon()
        icon.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.home_navigation)

        self.appointments_navigation = QToolButton(self.layoutWidget_4)
        self.appointments_navigation.setObjectName(u"appointments_navigation")
        self.appointments_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.appointments_navigation.sizePolicy().hasHeightForWidth())
        self.appointments_navigation.setSizePolicy(sizePolicy)
        self.appointments_navigation.setFont(font8)
        self.appointments_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/appointment_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appointments_navigation.setIcon(icon1)
        self.appointments_navigation.setIconSize(QSize(70, 70))
        self.appointments_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.appointments_navigation)

        self.services_navigation = QToolButton(self.layoutWidget_4)
        self.services_navigation.setObjectName(u"services_navigation")
        self.services_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.services_navigation.sizePolicy().hasHeightForWidth())
        self.services_navigation.setSizePolicy(sizePolicy)
        self.services_navigation.setFont(font8)
        self.services_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_navigation.setIcon(icon2)
        self.services_navigation.setIconSize(QSize(70, 70))
        self.services_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.services_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget_4)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setFont(font8)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon3)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget_4)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setFont(font8)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon4)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.appt_list.setText(QCoreApplication.translate("Form", u"Appointments List", None))
        self.req_detail_label.setText(QCoreApplication.translate("Form", u"Appointment Details", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Services", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
 
    @pyqtSlot()
    def emitSettingsBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()
        
    @pyqtSlot()
    def emitHomeBtn(self):
        # Emit the custom signal
        self.home_btn_clicked.emit()
        
    def initialize_db(self):
        return db 

    def fetch_appt_data(self):
        db = self.initialize_db()
        try:
                #print("Initializing database connection...")  # Debug statement
                appointments = db.child("appointment").get()
                #print(f"Fetched appointments from database: {appointments}")  # Debug statement

                if appointments.each():
                        self.appt_data_list = []
                        for appointment in appointments.each():
                                appt_id = appointment.key()
                                appt_data = appointment.val()
                                #print(f"Processing appointment ID: {appt_id}, Data: {appt_data}")  # Debug statement
                                appt_data["appt_id"] = appt_id
                                self.appt_data_list.append(appt_data)
                
                # Debug: Print the fetched data
                        print("Fetched appointments Data:", self.appt_data_list)  # Debug statement
                
                        self.populate_appt_info()
                else:
                        print("No appointments data found.")
        except Exception as e:
                print(f"An error occurred while fetching data: {e}")


            
            
    def clear_layout(self):
        while self.vLayout.count():
                item = self.vLayout.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.deleteLater()
                        
    def create_appt_list_frame(self, appt_data):
        appt_frame = QFrame(self.scrollAreaWidgetContents)
        appt_frame.setObjectName(u"clinic_frame")
        appt_frame.setGeometry(QRect(60, 240, 801, 81))
        appt_frame.setFrameShape(QFrame.StyledPanel)
        appt_frame.setFrameShadow(QFrame.Raised)
        appt_name_label = QLabel(appt_frame)
        appt_name_label.setObjectName(u"appt_name_label")
        appt_name_label.setGeometry(QRect(30, 30, 611, 21))
        appt_name_label.setText(f"{appt_data.get('clinic_name', 'Unknown')} - {appt_data.get('speciality', 'Unknown')}")
        
        #appt_name_label.mousePressEvent = lambda event, clinic=appt_data: self.create_popup_widget(clinic)
        
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        appt_name_label.setFont(font6)
        appt_name_label.setStyleSheet(u"border : none;\n")
        status = QLabel(appt_frame)
        status.setObjectName(u"status")
        status.setGeometry(QRect(690, 20, 91, 41))
        status.setFont(font6)
        status.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.15);color: #128983; text-align: center;\n")
        status.setAlignment(Qt.AlignCenter)
        return appt_frame

    def populate_appt_info(self):
        self.clear_layout()

        visible_appt = []
        db = self.initialize_db()  
        
        for i, appt_data in enumerate(self.appt_data_list):
                if isinstance(appt_data, dict):
                        clinic_id = appt_data.get("clinic_id", "")
                        doc_id = appt_data.get("doctor_id", "")

                        # Fetch clinic name using clinic_id
                        clinic_data = db.child("clinic").child(clinic_id).get().val()
                        clinic_name = clinic_data.get("clinic_name", "Unknown")
                        appt_data["clinic_name"] = clinic_name

                        # Fetch doctor name using doc_id
                        doc_data = db.child("doctors").child(doc_id).get().val()
                        doc_name = doc_data.get("doc_name", "Unknown")
                        appt_data["doc_name"] = doc_name

                        clinic_name_lower = clinic_name.lower()
                        status = appt_data.get("status", "").lower()

                        if self.selected_status and status.lower() != self.selected_status.lower():
                                continue

                       
                        appt_frame = self.create_appt_list_frame(appt_data)
                        if appt_frame:
                                visible_appt.append(appt_frame)

        # Add visible appointments to the layout in reverse order
        for appt_frame in reversed(visible_appt):
                self.vLayout.addWidget(appt_frame)

        self.scrollAreaWidgetContents.setLayout(self.vLayout)
        self.vLayout.setAlignment(Qt.AlignTop)
        self.vLayout.update()
        self.scrollAreaWidgetContents.update()


    def create_appt_details_frame(self, appt_data):
        request_detail_outer = QFrame(self.background)
        request_detail_outer.setObjectName(u"request_detail_outer")
        request_detail_outer.setGeometry(QRect(979, 200, 751, 831))
        request_detail_outer.setStyleSheet(u"background-color : #ffffff;")
        request_detail_outer.setFrameShape(QFrame.StyledPanel)
        request_detail_outer.setFrameShadow(QFrame.Raised)
        appt_details_inner = QFrame(request_detail_outer)
        appt_details_inner.setObjectName(u"appt_details_inner")
        appt_details_inner.setGeometry(QRect(20, 20, 711, 741))
        appt_details_inner.setFrameShape(QFrame.StyledPanel)
        appt_details_inner.setFrameShadow(QFrame.Raised)
        layoutWidget = QWidget(appt_details_inner)
        layoutWidget.setObjectName(u"layoutWidget")
        layoutWidget.setGeometry(QRect(3, 3, 701, 731))
        verticalLayout_2 = QVBoxLayout(layoutWidget)
        verticalLayout_2.setObjectName(u"verticalLayout_2")
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        date_layout = QHBoxLayout()
        date_layout.setObjectName(u"date_layout")
        date_label = QLabel(layoutWidget)
        date_label.setObjectName(u"date_label")
        date_label.setMaximumSize(QSize(301, 145))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        date_label.setFont(font1)
        date_label.setStyleSheet(u"border: none;")
        date_label.setLineWidth(0)
        date_label.setText("Date:")
        
        date_layout.addWidget(date_label)

        date_display = QLabel(layoutWidget)
        date_display.setObjectName(u"date_display")
        date_display.setMinimumSize(QSize(390, 102))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        date_display.setFont(font2)
        date_display.setStyleSheet(u"border: none;")
        date_display.setText(appt_data.get("clinic_name", "Unknown"))
        date_layout.addWidget(date_display)


        verticalLayout_2.addLayout(date_layout)

        time_layout = QHBoxLayout()
        time_layout.setObjectName(u"time_layout")
        time_label = QLabel(layoutWidget)
        time_label.setObjectName(u"time_label")
        time_label.setMaximumSize(QSize(301, 145))
        time_label.setFont(font1)
        time_label.setStyleSheet(u"border: none;")
        time_label.setText("Time:")
        time_layout.addWidget(time_label)

        time_display = QLabel(layoutWidget)
        time_display.setObjectName(u"time_display")
        time_display.setMinimumSize(QSize(390, 145))
        time_display.setMaximumSize(QSize(390, 145))
        time_display.setFont(font2)
        time_display.setStyleSheet(u"border: none;")
        time_display.setText(appt_data.get("time", "Unknown"))
        time_layout.addWidget(time_display)


        verticalLayout_2.addLayout(time_layout)

        clinic_layout = QHBoxLayout()
        clinic_layout.setSpacing(6)
        clinic_layout.setObjectName(u"clinic_layout")
        clinic_label = QLabel(layoutWidget)
        clinic_label.setObjectName(u"clinic_label")
        clinic_label.setMaximumSize(QSize(301, 145))
        clinic_label.setFont(font1)
        clinic_label.setStyleSheet(u"border: none;")
        clinic_label.setText("Clinic:")
        clinic_layout.addWidget(clinic_label)

        clinic_display = QLabel(layoutWidget)
        clinic_display.setObjectName(u"clinic_display")
        clinic_display.setMinimumSize(QSize(0, 145))
        clinic_display.setMaximumSize(QSize(390, 145))
        clinic_display.setFont(font2)
        clinic_display.setStyleSheet(u"border: none;")
        clinic_display.setScaledContents(False)
        clinic_display.setWordWrap(True)
        clinic_display.setText(appt_data.get("clinic_name", "Unknown"))

        clinic_layout.addWidget(clinic_display)


        verticalLayout_2.addLayout(clinic_layout)

        doc_spec_layout = QHBoxLayout()
        doc_spec_layout.setObjectName(u"doc_spec_layout")
        doc_spec_layout.setSizeConstraint(QLayout.SetFixedSize)
        doc_spec_label = QLabel(layoutWidget)
        doc_spec_label.setObjectName(u"doc_spec_label")
        doc_spec_label.setMaximumSize(QSize(301, 145))
        doc_spec_label.setFont(font1)
        doc_spec_label.setStyleSheet(u"border: none;")
        doc_spec_label.setWordWrap(True)
        doc_spec_label.setText("Doctor & Speciality")
        doc_spec_layout.addWidget(doc_spec_label)

        doc_spec_display = QLabel(layoutWidget)
        doc_spec_display.setObjectName(u"doc_spec_display")
        doc_spec_display.setMinimumSize(QSize(390, 145))
        doc_spec_display.setMaximumSize(QSize(390, 145))
        doc_spec_display.setFont(font2)
        doc_spec_display.setStyleSheet(u"border: none;")
        doc_spec_display.setScaledContents(False)
        doc_spec_display.setWordWrap(True)
        doc_spec_display.setText(f"{appt_data.get('clinic_name', 'Unknown')} - {appt_data.get('speciality', 'Unknown')}")

        doc_spec_layout.addWidget(doc_spec_display)


        verticalLayout_2.addLayout(doc_spec_layout)

        med_con_layout = QHBoxLayout()
        med_con_layout.setObjectName(u"med_con_layout")
        med_con_label = QLabel(layoutWidget)
        med_con_label.setObjectName(u"med_con_label")
        med_con_label.setMaximumSize(QSize(301, 145))
        med_con_label.setFont(font1)
        med_con_label.setStyleSheet(u"border: none;")
        med_con_label.setWordWrap(True)
        med_con_label.setText("Medical Concerns:")
        med_con_layout.addWidget(med_con_label)

        med_con_display = QLabel(layoutWidget)
        med_con_display.setObjectName(u"med_con_display")
        med_con_display.setMinimumSize(QSize(390, 145))
        med_con_display.setMaximumSize(QSize(390, 145))
        med_con_display.setFont(font2)
        med_con_display.setStyleSheet(u"border: none;")
        med_con_display.setScaledContents(False)
        med_con_display.setWordWrap(True)
        med_con_display.setText(appt_data.get("med_concern", "Unknown"))

        med_con_layout.addWidget(med_con_display)
        verticalLayout_2.addLayout(med_con_layout)
        
        cancel_btn = QPushButton(request_detail_outer)
        cancel_btn.setObjectName(u"cancel_btn")
        cancel_btn.setGeometry(QRect(500, 770, 221, 41))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        cancel_btn.setFont(font3)
        cancel_btn.setStyleSheet(u"background-color: #E73030; border-radius: 16px; color: white;\\n border: 1px solid gray;")
        cancel_btn.setText("Cancel Appointment")

        status = appt_data.get("status")
        
        if status == "pending":
                cancel_btn.show()
        else:
                cancel_btn.hide()

        self.temp_appt_id = appt_data["appt_id"]
        
        return request_detail_outer
        
    def create_popup_widget(self, appt_data):
        self.hide_appt_details_frame()
        self.clinic_appt_frame = self.create_appt_details_frame(appt_data)
        self.clinic_appt_frame.setVisible(True)
        
    def hide_appt_details_frame(self):
        if self.clinic_appt_frame:
            self.clinic_appt_frame.setVisible(False)
            
    def load_status(self):
        status = [
            "All",
            "Pending",
            "Approved",
            "Rejected"
        ]
        self.filter.addItems(status)   
        
    def updateSelectedStatus(self, index):
        selected_text = self.filter.itemText(index)

        if index == 0:
                self.selected_status = ""
        else:
                self.selected_status = selected_text
        self.hide_appt_details_frame()
        self.populate_appt_info()
        self.hide_appt_details_frame()
        
    def cancel_appt(self):
        appt_id = self.temp_appt_id
        appt_data = None

        if not self.appt_data_list:
                return None

        # Fetch the appointment data directly from the database
        try:
                appt_data_list = db.child("appointment").get().val()
        except Exception as e:
                print(f"Failed to fetch appointment data: {e}")
                return

        # Find the appointment data by appointment ID
        for aid, data in appt_data_list.items():
                if aid == appt_id:
                        appt_data = data
                        break

        if appt_data:
                try:
                        # Check if the current date is at least 3 days before the appointment date
                        current_date = datetime.datetime.now().date()
                        appt_date_str = appt_data.get("appt_date", "")
                        appt_date = datetime.datetime.strptime(appt_date_str, "%y%m%d").date()

                        if (appt_date - current_date).days >= 3:
                                # Remove the appointment from the database
                                db.child("appointment").child(appt_id).remove()

                                QMessageBox.information(self, "Success", "Appointment canceled and removed from the database.")
                                
                                # Remove the canceled appointment from appt_data_list
                                self.appt_data_list = [appt for appt in self.appt_data_list if appt.get("appt_id") != appt_id]

                                # Refresh the appointment list after removal
                                self.populate_appt_info()

                                # Hide the appointment details
                                self.hide_appt_details_frame()

                        else:
                                QMessageBox.warning(self, "Cannot Cancel Appointment", "You can only cancel appointments at least 3 days in advance.")
                        
                except Exception as e:
                        print(f"Failed to remove appointment: {e}")
                        QMessageBox.critical(self, "Error", f"Failed to cancel appointment: {str(e)}")
        else:
                QMessageBox.warning(self, "No Appointment Selected", "Please select an appointment to cancel.")
