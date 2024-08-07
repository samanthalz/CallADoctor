from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QRect
from PyQt5.QtGui import QColor

from connection import db
from datetime import date


class UpdateRecordWidget(QWidget):
    patients_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    redirect_doc_patients_page = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.patient_id = 0
        self.setupUi(self)

    def set_patient_id(self, patient_id):
        self.patient_id = patient_id
        self.get_patient_records(patient_id)

    def get_patient_records(self, patient_id): 
        today = date.today()
        current_date = today.strftime("%y%m%d")
        active_medication_list = []

        patient_data = db.child("patients").get().val()
        if patient_data: 
            for id, patient_info in patient_data.items():
                if int(id) == int(patient_id):
                    patient_name = patient_info['patient_name']

        medical_records = db.child("medical_records").get().val()
        if medical_records: 
            for record_id, record_info in enumerate(medical_records):
                if int(record_info.get('patient_id')) == int(patient_id):
                    if  int(record_info.get('end_date')) >= int(current_date): 
                        for medicine in record_info.get('medicine'):
                            active_medication_list.append(medicine)
                        patient_diagnosis = record_info.get('diagnosis')
                
            if not patient_diagnosis:
                patient_diagnosis = "Unavailable"
            if not active_medication_list:
                active_medication_list.append("No medication")

        # update text of selected patient:   
        self.name_display.setText(patient_name)
        self.name_display.setAlignment(Qt.AlignLeft)
        self.diagnosis_input.setText(patient_diagnosis)
        self.medication_input.setText(", ".join(active_medication_list))

    def generate_new_record_id(self):
        try:
            medical_records = db.child("medical_records").get().val()
            max_id = 0
            if medical_records: 
                for record_id, record_info in enumerate(medical_records):
                    id_num = int(record_id.replace("fb_", ""))
                    if id_num > max_id:
                        max_id = id_num
            new_id = max_id + 1
            return f"record_{new_id}"
        except Exception as e:
            print(f"Error generating new record ID: {e}")
            return None

    def set_medical_records(self):  # method to call when the submit button is clicked
        diagnosis = self.diagnosis_input.text().strip()
        medication_string = self.medication_input.toPlainText().strip()
        medication_list = medication_string.split(",")

        if not diagnosis or not medication_string:
            QMessageBox.warning(self, "Missing Data", "Please fill in all fields.")
            return
        
        medical_records = db.child("medical_records").get().val()
        if medical_records: 
            for record_id, record_info in enumerate(medical_records):
                if int(record_info.get('patient_id')) == int(self.patient_id): # existing record exists
                    record_exists = True
                    existing_record_id = record_id
                    break

        if not record_exists : # if existing record does not exist 
            record_id = self.generate_new_record_id()  
        else : 
            record_id = existing_record_id

        try:
            db.child("medical_records").child(record_id).update({
                        "diagnosis": diagnosis,
                        "medicine": medication_list,
                        "patient_id": self.patient_id
                })
            # Display message box if recrod saved successfully
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Prescription updated successfully!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.buttonClicked.connect(self.redirect_to_patients)
            msgBox.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to upload prescription: {str(e)}")
        
    


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


        # Nav frame & Layout 
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


        self.whitebg = QtWidgets.QWidget(Form)
        self.whitebg.setGeometry(QtCore.QRect(150, 0, 1771, 1080))
        self.whitebg.setStyleSheet("background-color: #F8F8F8;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-left-radius: 30px;")
        self.whitebg.setObjectName("whitebg")
        self.update_title = QtWidgets.QLabel(self.whitebg)
        self.update_title.setGeometry(QtCore.QRect(60, 40, 600, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.update_title.setFont(font)
        self.update_title.setObjectName("update_title")
        self.user_frame = QtWidgets.QFrame(self.whitebg)
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
        self.profile_btn.setGeometry(QtCore.QRect(120, 25, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet("border: none")
        self.profile_btn.setObjectName("profile_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.whitebg)
        self.cancel_btn.setGeometry(QtCore.QRect(440, 950, 321, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color: \"#D3D3D3\"; border-radius: 10px;")
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.redirect_to_patients)
        self.submit_btn = QtWidgets.QPushButton(self.whitebg)
        self.submit_btn.setGeometry(QtCore.QRect(850, 950, 321, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.submit_btn.setFont(font)
        self.submit_btn.setStyleSheet("background-color: \"#B6D0E2\"; border-radius: 10px;")
        self.submit_btn.setObjectName("submit_btn")
        self.submit_btn.clicked.connect(self.set_medical_records)
        self.layoutWidget = QtWidgets.QWidget(self.whitebg)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 260, 1504, 631))
        self.layoutWidget.setObjectName("layoutWidget")
        self.form_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setSpacing(50)
        self.form_layout.setObjectName("form_layout")
        self.diagnosis_layout = QtWidgets.QVBoxLayout()
        self.diagnosis_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.diagnosis_layout.setObjectName("diagnosis_layout")
        self.diagnosis_label = QtWidgets.QLabel(self.layoutWidget)
        self.diagnosis_label.setMinimumSize(QtCore.QSize(1500, 40))
        self.diagnosis_label.setMaximumSize(QtCore.QSize(1500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.diagnosis_label.setFont(font)
        self.diagnosis_label.setWordWrap(True)
        self.diagnosis_label.setObjectName("diagnosis_label")
        self.diagnosis_layout.addWidget(self.diagnosis_label)
        self.diagnosis_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.diagnosis_input.setMinimumSize(QtCore.QSize(1500, 60))
        self.diagnosis_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.diagnosis_input.setFont(font)
        self.diagnosis_input.setStyleSheet("background-color: white; border: none; border-radius: 0; padding: 10px;")
        self.diagnosis_input.setText("")
        self.diagnosis_input.setObjectName("diagnosis_input")
        self.diagnosis_layout.addWidget(self.diagnosis_input)
        self.form_layout.addLayout(self.diagnosis_layout)
        self.medication_layout = QtWidgets.QVBoxLayout()
        self.medication_layout.setObjectName("medication_layout")
        self.medication_label = QtWidgets.QLabel(self.layoutWidget)
        self.medication_label.setMinimumSize(QtCore.QSize(1500, 40))
        self.medication_label.setMaximumSize(QtCore.QSize(1500, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.medication_label.setFont(font)
        self.medication_label.setWordWrap(True)
        self.medication_label.setObjectName("medication_label")
        self.medication_layout.addWidget(self.medication_label)
        self.medication_input = QtWidgets.QTextEdit(self.layoutWidget)
        self.medication_input.setMinimumSize(QtCore.QSize(1500, 270))
        self.medication_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.medication_input.setFont(font)
        self.medication_input.setStyleSheet("background-color: white; border: none; border-radius: 0; padding: 10px;")
        self.medication_input.setObjectName("medication_input")
        self.medication_layout.addWidget(self.medication_input)
        self.form_layout.addLayout(self.medication_layout)
        self.widget = QtWidgets.QWidget(self.whitebg)
        self.widget.setGeometry(QtCore.QRect(62, 122, 1538, 39))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.patient_name_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.patient_name_label.setFont(font)
        self.patient_name_label.setObjectName("patient_name_label")
        self.horizontalLayout.addWidget(self.patient_name_label)
        self.name_display = QtWidgets.QLabel(self.widget)
        self.name_display.setAlignment(Qt.AlignLeft)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.name_display.setFont(font)
        self.name_display.setObjectName("name_display")
        self.horizontalLayout.addWidget(self.name_display)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.home_navigation.setText(_translate("Form", "   Home   "))
        self.patients_navigation.setText(_translate("Form", "Patients"))
        self.settings_navigation.setText(_translate("Form", "Settings"))
        self.logout_navigation.setText(_translate("Form", "Logout"))
        self.update_title.setText(_translate("Form", "Update Medical Records"))
        self.profile_btn.setText(_translate("Form", "Doctor"))
        self.cancel_btn.setText(_translate("Form", "Cancel"))
        self.submit_btn.setText(_translate("Form", "Submit"))
        self.diagnosis_label.setText(_translate("Form", "Diagnosis"))
        self.medication_label.setText(_translate("Form", "Medication"))
        self.medication_input.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>"))
        self.patient_name_label.setText(_translate("Form", "Patient Name : "))


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

    def redirect_to_patients(self, button = None):
        if button : 
            if button.text() == "OK":
                self.redirect_doc_patients_page.emit()
        else : 
            self.redirect_doc_patients_page.emit()
        

        

    
        

# If run file directly access this page
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UpdateRecordWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
