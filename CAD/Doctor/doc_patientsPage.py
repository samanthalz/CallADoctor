from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QRect, Qt
from PyQt5.QtGui import QColor

from connection import db
from datetime import date

class PatientsPageWidget(QWidget):
    patients_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    add_record_btn_click = pyqtSignal()
    patient_id_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.user_id = 0
        self.setupUi(self)
        # For tesing : 
        #self.set_user_id("Dr. John Doe")

    def set_user_id(self, user_id): 
        self.user_id = user_id
        # Assign values after user_id is initialized (moved to driver)
        #self.get_patient_data()

    def translate_date(self, date_str): # date_str = appt_data['date'] for appt_data in appt_info    ("240620")
        day = date_str[-2:]
        month = date_str[2:4]
        year = '20' + date_str[:2] 

        monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        month = monthList[int(month) - 1]

        date_str = day + " " + month + " " + year

        return date_str # returns in format 20 Jun 2024 (used for display)

    def clear_patient_details(self):
        self.selected_patient_name_label.setText("")
        self.prescription_display.setText("")
        self.diagnosis_display.setText("")
        self.age_display.setText("")
        self.gender_display.setText("") 

    def clear_verticalLayout_patient_list(self):
        while self.verticalLayout_patient_list.count():
                item = self.verticalLayout_patient_list.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.destroy()

    def get_patient_data(self):
        self.clear_verticalLayout_patient_list()
        today = date.today()
        current_date = today.strftime("%y%m%d")
        appointment_data = db.child("appointment").get().val()
        patient_data = db.child("patients").get().val()
        patient_frames = []
        
        if appointment_data:
            for appt_id, appt_info in appointment_data.items():
                if appt_info.get('doctor_id').lower() == self.user_id.lower() : 
                    if  int(appt_info.get('date')) >= int(current_date): # upcoming appointments
                        patient_id = appt_info['patient_id']
                        
                        for i, patient_info in patient_data.items():
                            if int(patient_info.get("patient_ic")) == int(patient_id):
                                patient_name = patient_info.get('patient_name')
                                break
                            
                        appt_date = appt_info['date']
                        appt_date = self.translate_date(appt_date)
                        appt_time = appt_info['time']
                        patient_frame = self.create_patient_frame(patient_name, appt_date, appt_time, patient_id)

                        if patient_frame:
                                patient_frames.append(patient_frame)

            # Add visible patients to the layout
            for patient_frame in patient_frames:
                self.verticalLayout_patient_list.addWidget(patient_frame)

        # Refresh the layout after adding all frames
        self.verticalLayout_patient_list.setAlignment(Qt.AlignTop)
        self.verticalLayout_patient_list.update()
        self.patient_list_frame.repaint()

    def set_patient_details(self, patient_id): # pass patient id of selected patient into the method
        try : 
                patient_data = db.child("patients").get().val()
                if patient_data: 
                    for id, patient_info in patient_data.items():
                        if int(id) == int(patient_id):
                            try : 
                                patient_age = patient_info['patient_age']
                                patient_name = patient_info['patient_name']

                                ic_last_char = id[-1]  # last character
                                if int(ic_last_char) % 2 == 0: # even number = female
                                        patient_gender = "Female"
                                elif int(ic_last_char) % 2 != 0: # odd number = male
                                        patient_gender = "Male"
                                else : 
                                        patient_gender = "Unspecified"
                            except Exception as e: 
                                self.showMessageBox('Error', f"Error fetching patient data: {e}") 
                        
                
                # get medical records : 
                today = date.today()
                current_date = today.strftime("%y%m%d")
                active_medication_list = []
                patient_diagnosis = ""

                medical_records = db.child("medical_records").get().val()
                if medical_records: 
                    for record_id, record_info in enumerate(medical_records):
                        if int(record_info['patient_id']) == int(patient_id):
                            if  int(record_info.get('end_date')) >= int(current_date): 
                                for medicine in record_info.get('medicine'):
                                    active_medication_list.append(medicine)
                                    patient_diagnosis = record_info.get('diagnosis')

        
                if not patient_diagnosis:
                        patient_diagnosis = "Unavailable"
                if not active_medication_list:
                        active_medication_list.append("No medication")


                # update text of selected patient:   
                self.selected_patient_name_label.setText(patient_name)
                self.prescription_display.setText(", ".join(active_medication_list))
                self.diagnosis_display.setText(patient_diagnosis)
                self.age_display.setText(str(patient_age))
                self.gender_display.setText(patient_gender) 

        except Exception as e:
            self.showMessageBox('Error', f"{e}") 
             

        return patient_name, active_medication_list, patient_diagnosis, patient_age, patient_gender 


    def create_patient_frame(self, patient_name, appt_date, appt_time, patient_id):
        # Patient list frame : 
        #self.patient_frame1 = QtWidgets.QFrame(self.patient_list_frame)
        # self.patient_frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.patient_frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.patient_frame1 = QtWidgets.QPushButton(self.patient_list_frame)
        self.patient_frame1.setFixedSize(801, 81) # set fixed size of frame
        self.patient_frame1.setStyleSheet("""
        QPushButton {
            border: 1px solid #dcdcdc;
            text-align: left;
        }
        QPushButton:hover {
            background-color: #f0f0f0;
        }
    """)
        self.patient_frame1.setObjectName("patient_frame_" + str(patient_id))
        self.patient_frame1.setProperty("identifier", patient_id)
        self.patient_name_label1 = QtWidgets.QLabel(self.patient_frame1)
        self.patient_name_label1.setGeometry(QtCore.QRect(90, 30, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.patient_name_label1.setFont(font)
        self.patient_name_label1.setStyleSheet("border : none;\n"
"")
        self.patient_name_label1.setObjectName("patient_name_label1")
        self.patient_profile_logo1 = QtWidgets.QLabel(self.patient_frame1)
        self.patient_profile_logo1.setGeometry(QtCore.QRect(10, 10, 54, 54))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.patient_profile_logo1.setFont(font)
        self.patient_profile_logo1.setStyleSheet("background-color: #B6D0E2; \n"
"border-radius: 25px; \n"
"border: 2px solid #B6D0F7; \n"
"min-width: 50px; \n"
"min-height: 50px; \n"
"max-width: 50px;\n"
"max-height: 50px; ")
        self.patient_profile_logo1.setAlignment(QtCore.Qt.AlignCenter)
        self.patient_profile_logo1.setObjectName("patient_profile_logo1")
        self.appt_time_label = QtWidgets.QLabel(self.patient_frame1)
        self.appt_time_label.setGeometry(QtCore.QRect(690, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.appt_time_label.setFont(font)
        self.appt_time_label.setStyleSheet("background-color: rgba(18, 137, 131, 0.15);\n"
"color: #128983; text-align: center;\n"
"")
        self.appt_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.appt_time_label.setObjectName("appt_time_label")
        self.appt_date_label = QtWidgets.QLabel(self.patient_frame1)
        self.appt_date_label.setGeometry(QtCore.QRect(580, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.appt_date_label.setFont(font)
        self.appt_date_label.setStyleSheet("background-color: rgba(18, 137, 131, 0.15);\n"
"color: #128983; text-align: center;\n"
"")
        self.appt_date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.appt_date_label.setObjectName("appt_date_label")

        self.patient_name_label1.setText(str(patient_name))
        self.patient_profile_logo1.setText("PN")
        self.appt_time_label.setText(appt_time)
        self.appt_date_label.setText(appt_date)

        # Connect the clicked signal to a slot method
        self.patient_frame1.clicked.connect(self.on_patient_frame_clicked)

        return self.patient_frame1
    
    def on_patient_frame_clicked(self):
        # Get the button that was clicked
        button = self.sender()
        identifier = button.property("identifier")
        self.set_patient_details(identifier) # update patient details on the right side
        self.update_prescription_button.clicked.connect(self.emitAddRecordBtn)
        self.patient_id_signal.emit(identifier)

                    

    def setupUi(self, Form):
        Form.setObjectName("Form")
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
"border-top-left-radius: 30px;")
        
        self.user_frame = QtWidgets.QFrame(self.background)
        self.user_frame.setGeometry(QtCore.QRect(1480, 30, 251, 80))
        self.user_frame.setStyleSheet("border-radius: 20px; border: 2px solid #808080")
        self.user_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_frame.setObjectName("user_frame")
        self.profile_icon = QtWidgets.QLabel(self.user_frame)
        self.profile_icon.setGeometry(QtCore.QRect(10, 10, 60, 60))
        self.profile_icon.setStyleSheet("border: none")
        self.profile_icon.setText("")
        self.profile_icon.setPixmap(QtGui.QPixmap("CAD/Images/icon/profile_icon.png"))
        self.profile_icon.setScaledContents(True)
        self.profile_icon.setObjectName("profile_icon")
        self.profile_btn = QtWidgets.QPushButton(self.user_frame)
        self.profile_btn.setGeometry(QtCore.QRect(100, 25, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet("border: none")
        self.profile_btn.setObjectName("profile_btn")
        
        self.patient_details_outer_frame = QtWidgets.QFrame(self.background)
        self.patient_details_outer_frame.setGeometry(QtCore.QRect(979, 200, 751, 841))
        self.patient_details_outer_frame.setStyleSheet("background-color : #ffffff;")
        self.patient_details_outer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.patient_details_outer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.patient_details_outer_frame.setObjectName("patient_details_outer_frame")
        self.clinic_details_inner = QtWidgets.QFrame(self.patient_details_outer_frame)
        self.clinic_details_inner.setGeometry(QtCore.QRect(20, 20, 711, 771))
        self.clinic_details_inner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.clinic_details_inner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.clinic_details_inner.setObjectName("clinic_details_inner")
        self.selected_patient_name_label = QtWidgets.QLabel(self.clinic_details_inner)
        self.selected_patient_name_label.setGeometry(QtCore.QRect(100, 30, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.selected_patient_name_label.setFont(font)
        self.selected_patient_name_label.setStyleSheet("border : none;\n"
"")
        self.selected_patient_name_label.setObjectName("selected_patient_name_label")
        self.selected_patient_profile_logo = QtWidgets.QLabel(self.clinic_details_inner)
        self.selected_patient_profile_logo.setGeometry(QtCore.QRect(10, 10, 54, 54))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(9)
        self.selected_patient_profile_logo.setFont(font)
        self.selected_patient_profile_logo.setStyleSheet("background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.selected_patient_profile_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_patient_profile_logo.setObjectName("selected_patient_profile_logo")
        self.line = QtWidgets.QFrame(self.clinic_details_inner)
        self.line.setGeometry(QtCore.QRect(20, 100, 671, 3))
        self.line.setMinimumSize(QtCore.QSize(357, 3))
        self.line.setMaximumSize(QtCore.QSize(16777215, 3))
        self.line.setStyleSheet("background-color: #B6D0E2; border: none;")
        self.line.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.clinic_details_inner)
        self.widget.setGeometry(QtCore.QRect(5, 125, 701, 621))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gender_layout = QtWidgets.QHBoxLayout()
        self.gender_layout.setObjectName("gender_layout")
        self.gender_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.gender_label.setFont(font)
        self.gender_label.setStyleSheet("border: none;")
        self.gender_label.setLineWidth(0)
        self.gender_label.setObjectName("gender_label")
        self.gender_layout.addWidget(self.gender_label)
        self.gender_display = QtWidgets.QLabel(self.widget)
        self.gender_display.setMinimumSize(QtCore.QSize(390, 102))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.gender_display.setFont(font)
        self.gender_display.setStyleSheet("border: none;")
        self.gender_display.setObjectName("gender_display")
        self.gender_layout.addWidget(self.gender_display)
        self.verticalLayout_2.addLayout(self.gender_layout)
        self.age_layout = QtWidgets.QHBoxLayout()
        self.age_layout.setObjectName("age_layout")
        self.age_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.age_label.setFont(font)
        self.age_label.setStyleSheet("border: none;")
        self.age_label.setObjectName("age_label")
        self.age_layout.addWidget(self.age_label)
        self.age_display = QtWidgets.QLabel(self.widget)
        self.age_display.setMinimumSize(QtCore.QSize(390, 102))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.age_display.setFont(font)
        self.age_display.setStyleSheet("border: none;")
        self.age_display.setObjectName("age_display")
        self.age_layout.addWidget(self.age_display)
        self.verticalLayout_2.addLayout(self.age_layout)
        self.diagnosis_layout = QtWidgets.QHBoxLayout()
        self.diagnosis_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.diagnosis_layout.setObjectName("diagnosis_layout")
        self.diagnosis_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.diagnosis_label.setFont(font)
        self.diagnosis_label.setStyleSheet("border: none;")
        self.diagnosis_label.setWordWrap(True)
        self.diagnosis_label.setObjectName("diagnosis_label")
        self.diagnosis_layout.addWidget(self.diagnosis_label)
        self.diagnosis_display = QtWidgets.QLabel(self.widget)
        self.diagnosis_display.setMinimumSize(QtCore.QSize(390, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.diagnosis_display.setFont(font)
        self.diagnosis_display.setStyleSheet("border: none;")
        self.diagnosis_display.setScaledContents(False)
        self.diagnosis_display.setWordWrap(True)
        self.diagnosis_display.setObjectName("diagnosis_display")
        self.diagnosis_layout.addWidget(self.diagnosis_display)
        self.verticalLayout_2.addLayout(self.diagnosis_layout)
        self.prescription_layout = QtWidgets.QHBoxLayout()
        self.prescription_layout.setObjectName("prescription_layout")
        self.prescription_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.prescription_label.setFont(font)
        self.prescription_label.setStyleSheet("border: none;")
        self.prescription_label.setWordWrap(True)
        self.prescription_label.setObjectName("prescription_label")
        self.prescription_layout.addWidget(self.prescription_label)
        self.prescription_display = QtWidgets.QLabel(self.widget)
        self.prescription_display.setMinimumSize(QtCore.QSize(390, 0))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.prescription_display.setFont(font)
        self.prescription_display.setStyleSheet("border: none;")
        self.prescription_display.setScaledContents(False)
        self.prescription_display.setWordWrap(True)
        self.prescription_display.setObjectName("prescription_display")
        self.prescription_layout.addWidget(self.prescription_display)
        self.verticalLayout_2.addLayout(self.prescription_layout)
        self.update_prescription_button = QtWidgets.QPushButton(self.patient_details_outer_frame)
        self.update_prescription_button.setGeometry(QtCore.QRect(550, 790, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.update_prescription_button.setFont(font)
        self.update_prescription_button.setStyleSheet("background-color: #B6D0E2; border-radius: 16px; color: black;\\n border: 1px solid gray;")
        self.update_prescription_button.setObjectName("update_prescription_button")
        self.update_prescription_button.clicked.connect(self.emitAddRecordBtn)
        self.patient_list_label = QtWidgets.QLabel(self.background)
        self.patient_list_label.setGeometry(QtCore.QRect(50, 160, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.patient_list_label.setFont(font)
        self.patient_list_label.setStyleSheet("border : none;\n"
"")
        self.patient_list_label.setObjectName("patient_list_label")
        self.patient_details_label = QtWidgets.QLabel(self.background)
        self.patient_details_label.setGeometry(QtCore.QRect(990, 150, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.patient_details_label.setFont(font)
        self.patient_details_label.setStyleSheet("border : none;\n"
"")
        self.patient_details_label.setObjectName("patient_details_label")
        
        self.patient_list_frame = QtWidgets.QFrame(self.background)
        self.patient_list_frame.setGeometry(QtCore.QRect(50, 230, 801, 801))
        self.patient_list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.patient_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.patient_list_frame.setObjectName("patient_list_frame")
        # Create a vertical layout and set it to the frame
        self.verticalLayout_patient_list = QVBoxLayout(self.patient_list_frame)
        self.patient_list_frame.setLayout(self.verticalLayout_patient_list)
        self.verticalLayout_patient_list.setContentsMargins(0, 0, 0, 0)  # Set the margins to zero
        self.verticalLayout_patient_list.setSpacing(10)  # Set spacing between items
        
        
        
        
#         self.patient_frame2 = QtWidgets.QFrame(self.patient_list_frame)
#         self.patient_frame2.setGeometry(QtCore.QRect(0, 130, 801, 81))
#         self.patient_frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.patient_frame2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.patient_frame2.setObjectName("patient_frame2")
#         self.patient_name_label2 = QtWidgets.QLabel(self.patient_frame2)
#         self.patient_name_label2.setGeometry(QtCore.QRect(90, 30, 121, 21))
#         font = QtGui.QFont()
#         font.setFamily("Cascadia Code")
#         font.setPointSize(10)
#         self.patient_name_label2.setFont(font)
#         self.patient_name_label2.setStyleSheet("border : none;\n"
# "")
#         self.patient_name_label2.setObjectName("patient_name_label2")
#         self.patient_profile_logo_2 = QtWidgets.QLabel(self.patient_frame2)
#         self.patient_profile_logo_2.setGeometry(QtCore.QRect(10, 10, 54, 54))
#         font = QtGui.QFont()
#         font.setFamily("Cascadia Code")
#         font.setPointSize(9)
#         self.patient_profile_logo_2.setFont(font)
#         self.patient_profile_logo_2.setStyleSheet("background-color: #B6D0E2; /* Fill color */\n"
# "border-radius: 25px; /* Radius to make it round */\n"
# "border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
# "min-width: 50px; /* Ensure the QLabel is a circle */\n"
# "min-height: 50px; /* Ensure the QLabel is a circle */\n"
# "max-width: 50px; /* Ensure the QLabel is a circle */\n"
# "max-height: 50px; /* Ensure the QLabel is a circle */")
#         self.patient_profile_logo_2.setAlignment(QtCore.Qt.AlignCenter)
#         self.patient_profile_logo_2.setObjectName("patient_profile_logo_2")
#         self.appt_date_label2 = QtWidgets.QLabel(self.patient_frame2)
#         self.appt_date_label2.setGeometry(QtCore.QRect(580, 20, 91, 41))
#         font = QtGui.QFont()
#         font.setFamily("Consolas")
#         font.setPointSize(10)
#         self.appt_date_label2.setFont(font)
#         self.appt_date_label2.setStyleSheet("background-color: rgba(18, 137, 131, 0.15);\n"
# "color: #128983; text-align: center;\n"
# "")
#         self.appt_date_label2.setAlignment(QtCore.Qt.AlignCenter)
#         self.appt_date_label2.setObjectName("appt_date_label2")
#         self.appt_time_label2 = QtWidgets.QLabel(self.patient_frame2)
#         self.appt_time_label2.setGeometry(QtCore.QRect(690, 20, 91, 41))
#         font = QtGui.QFont()
#         font.setFamily("Consolas")
#         font.setPointSize(10)
#         self.appt_time_label2.setFont(font)
#         self.appt_time_label2.setStyleSheet("background-color: rgba(18, 137, 131, 0.15);\n"
# "color: #128983; text-align: center;\n"
# "")
#         self.appt_time_label2.setAlignment(QtCore.Qt.AlignCenter)
#         self.appt_time_label2.setObjectName("appt_time_label2")


        # Nav bar layout : 
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.navigation_layout = QtWidgets.QWidget(self.frame)
        self.navigation_layout.setGeometry(QtCore.QRect(31, 20, 87, 851))
        self.navigation_layout.setObjectName("navigation_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.navigation_layout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        # Navigation buttons : 
        self.home_navigation = QtWidgets.QToolButton(self.navigation_layout)
        self.home_navigation.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        self.home_navigation.setMinimumSize(QtCore.QSize(85, 96))
        self.home_navigation.setMaximumSize(QtCore.QSize(85, 96))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_navigation.setFont(font)
        self.home_navigation.setStyleSheet("border: none; \n"
"color: white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("CAD/Images/nav_images/home_page_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QtCore.QSize(70, 70))
        self.home_navigation.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.home_navigation.setObjectName("home_navigation")
        self.home_navigation.clicked.connect(self.emitHomeBtn)
        self.verticalLayout.addWidget(self.home_navigation)
        
        self.patients_navigation = QtWidgets.QToolButton(self.navigation_layout)
        self.patients_navigation.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patients_navigation.sizePolicy().hasHeightForWidth())
        self.patients_navigation.setSizePolicy(sizePolicy)
        self.patients_navigation.setMinimumSize(QtCore.QSize(85, 96))
        self.patients_navigation.setMaximumSize(QtCore.QSize(85, 96))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.patients_navigation.setFont(font)
        self.patients_navigation.setStyleSheet("border: none; \n"
"color: white;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("CAD/Images/nav_images/services_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.patients_navigation.setIcon(icon3)
        self.patients_navigation.setIconSize(QtCore.QSize(70, 70))
        self.patients_navigation.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.patients_navigation.setObjectName("patients_navigation")
        self.patients_navigation.clicked.connect(self.emitPatientsBtn)
        self.verticalLayout.addWidget(self.patients_navigation)
        self.settings_navigation = QtWidgets.QToolButton(self.navigation_layout)
        self.settings_navigation.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setMinimumSize(QtCore.QSize(85, 96))
        self.settings_navigation.setMaximumSize(QtCore.QSize(85, 96))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.settings_navigation.setFont(font)
        self.settings_navigation.setStyleSheet("border: none; \n"
"color: white;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("CAD/Images/nav_images/settings_page_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QtCore.QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.settings_navigation.setObjectName("settings_navigation")
        self.settings_navigation.clicked.connect(self.emitProfileBtn)
        self.verticalLayout.addWidget(self.settings_navigation)
        self.logout_navigation = QtWidgets.QToolButton(self.navigation_layout)
        self.logout_navigation.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setMinimumSize(QtCore.QSize(85, 96))
        self.logout_navigation.setMaximumSize(QtCore.QSize(85, 96))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logout_navigation.setFont(font)
        self.logout_navigation.setStyleSheet("border: none; \n"
"color: white;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("CAD/Images/nav_images/logout_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QtCore.QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.logout_navigation.setObjectName("logout_navigation")
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)
        self.verticalLayout.addWidget(self.logout_navigation)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.profile_btn.setText(_translate("Form", "Doctor"))
        self.selected_patient_profile_logo.setText(_translate("Form", "A"))
        self.gender_label.setText(_translate("Form", "Gender: "))
        self.age_label.setText(_translate("Form", "Age: "))
        self.diagnosis_label.setText(_translate("Form", "Diagnosis : "))
        self.prescription_label.setText(_translate("Form", "Prescription : "))
        
        self.update_prescription_button.setText(_translate("Form", "Add record"))
        self.patient_list_label.setText(_translate("Form", "Patient List"))
        self.patient_details_label.setText(_translate("Form", "Patient Details"))



        self.home_navigation.setText(_translate("Form", "   Home   "))
        self.patients_navigation.setText(_translate("Form", "Patients"))
        self.settings_navigation.setText(_translate("Form", "Settings"))
        self.logout_navigation.setText(_translate("Form", "Logout"))


    def showMessageBox(self, title, message, success=False):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    @pyqtSlot()
    def emitHomeBtn(self):
        # Emit the custom signal
        self.home_btn_clicked.emit()     

    @pyqtSlot()
    def emitPatientsBtn(self):
        # Emit the custom signal
        self.patients_btn_clicked.emit()
        
    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
        
        
    @pyqtSlot()
    def emitProfileBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()

    @pyqtSlot()
    def emitAddRecordBtn(self):
        # Emit the custom signal
        self.add_record_btn_click.emit()

    


# If run file directly access this page
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = PatientsPageWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



