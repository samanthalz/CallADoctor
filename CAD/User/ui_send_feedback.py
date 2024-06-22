from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QTextCharFormat)
from PyQt5.QtWidgets import *
from datetime import datetime, timedelta
from connection import db

class SendFeedbackWidget(QWidget):
    service_btn_clicked = pyqtSignal()
    cancel_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    schedule_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    redirect_profile = pyqtSignal()
    

    def __init__(self, parent=None):
        super().__init__(parent)
        self.patient_id = 0
        self.setupUi(self)
        
    
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        
        Form.setAutoFillBackground(True)
        p = Form.palette()
        p.setColor(Form.backgroundRole(), QColor('#B6D0E2'))
        Form.setPalette(p)
        
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.frame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(30, 19, 87, 871))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        font = QFont()
        font.setFamily(u"Source Sans Pro Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_navigation.setFont(font)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon = QIcon()
        icon.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.home_navigation.clicked.connect(self.emitHomeBtn)
        self.verticalLayout.addWidget(self.home_navigation)

        self.appointments_navigation = QToolButton(self.layoutWidget_4)
        self.appointments_navigation.setObjectName(u"appointments_navigation")
        self.appointments_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.appointments_navigation.sizePolicy().hasHeightForWidth())
        self.appointments_navigation.setSizePolicy(sizePolicy)
        self.appointments_navigation.setFont(font)
        self.appointments_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/appointment_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appointments_navigation.setIcon(icon1)
        self.appointments_navigation.setIconSize(QSize(70, 70))
        self.appointments_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.appointments_navigation.clicked.connect(self.emitScheduleBtn)
        self.verticalLayout.addWidget(self.appointments_navigation)

        self.services_navigation = QToolButton(self.layoutWidget_4)
        self.services_navigation.setObjectName(u"services_navigation")
        self.services_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.services_navigation.sizePolicy().hasHeightForWidth())
        self.services_navigation.setSizePolicy(sizePolicy)
        self.services_navigation.setFont(font)
        self.services_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_navigation.setIcon(icon2)
        self.services_navigation.setIconSize(QSize(70, 70))
        self.services_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.services_navigation.clicked.connect(self.emitServiceBtn)
        self.verticalLayout.addWidget(self.services_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget_4)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setFont(font)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon3)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settings_navigation.clicked.connect(self.emitProfileBtn)
        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget_4)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setFont(font)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon4)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)
        self.verticalLayout.addWidget(self.logout_navigation)

        self.whitebg = QWidget(Form)
        self.whitebg.setObjectName(u"whitebg")
        self.whitebg.setGeometry(QRect(150, 0, 1771, 1080))
        self.whitebg.setStyleSheet(u"background-color: #F8F8F8;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-left-radius: 30px;")
        self.fb_title = QLabel(self.whitebg)
        self.fb_title.setObjectName(u"fb_title")
        self.fb_title.setGeometry(QRect(60, 40, 481, 81))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(28)
        font1.setBold(True)
        font1.setWeight(75)
        self.fb_title.setFont(font1)
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
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(16)
        self.profile_btn.setFont(font2)
        self.profile_btn.setStyleSheet(u"border: none")
        self.cancel_btn = QPushButton(self.whitebg)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(440, 950, 321, 50))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        self.cancel_btn.setFont(font3)
        self.cancel_btn.setStyleSheet(u"background-color: \"#D3D3D3\"; border-radius: 10px;")
        self.cancel_btn.clicked.connect(self.emitCancelBtn)
        
        self.submit_btn = QPushButton(self.whitebg)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(850, 950, 321, 50))
        self.submit_btn.setFont(font3)
        self.submit_btn.setStyleSheet(u"background-color: \"#B6D0E2\"; border-radius: 10px;")
        self.submit_btn.clicked.connect(self.upload_data_to_db)
        
        self.widget = QWidget(self.whitebg)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 160, 1504, 731))
        self.form_layout = QVBoxLayout(self.widget)
        self.form_layout.setSpacing(50)
        self.form_layout.setObjectName(u"form_layout")
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.subject_layout = QVBoxLayout()
        self.subject_layout.setObjectName(u"subject_layout")
        self.subject_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.subject_label = QLabel(self.widget)
        self.subject_label.setObjectName(u"subject_label")
        self.subject_label.setMinimumSize(QSize(1500, 40))
        self.subject_label.setMaximumSize(QSize(1500, 16777215))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(18)
        self.subject_label.setFont(font4)
        self.subject_label.setWordWrap(True)

        self.subject_layout.addWidget(self.subject_label)

        self.subject_input = QLineEdit(self.widget)
        self.subject_input.setObjectName(u"subject_input")
        self.subject_input.setMinimumSize(QSize(1500, 60))
        self.subject_input.setMaximumSize(QSize(16777215, 16777215))
        self.subject_input.setFont(font3)
        self.subject_input.setStyleSheet(u"background-color: white; border: none; border-radius: 0; padding: 10px;")

        self.subject_layout.addWidget(self.subject_input)


        self.form_layout.addLayout(self.subject_layout)

        self.feedback_layout = QVBoxLayout()
        self.feedback_layout.setObjectName(u"feedback_layout")
        self.feedback_label = QLabel(self.widget)
        self.feedback_label.setObjectName(u"feedback_label")
        self.feedback_label.setMinimumSize(QSize(1500, 40))
        self.feedback_label.setMaximumSize(QSize(1500, 40))
        self.feedback_label.setFont(font4)
        self.feedback_label.setWordWrap(True)

        self.feedback_layout.addWidget(self.feedback_label)

        self.feedback_input = QTextEdit(self.widget)
        self.feedback_input.setObjectName(u"feedback_input")
        self.feedback_input.setMinimumSize(QSize(1500, 270))
        self.feedback_input.setMaximumSize(QSize(16777215, 16777215))
        self.feedback_input.setFont(font3)
        self.feedback_input.setStyleSheet(u"background-color: white; border: none; border-radius: 0; padding: 10px;")

        self.feedback_layout.addWidget(self.feedback_input)


        self.form_layout.addLayout(self.feedback_layout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Services", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
        self.fb_title.setText(QCoreApplication.translate("Form", u"Send Feedback", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.cancel_btn.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.submit_btn.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.subject_label.setText(QCoreApplication.translate("Form", u"Subject", None))
        self.subject_input.setText("")
        self.subject_input.setPlaceholderText(QCoreApplication.translate("Form", u"Type here...", None))
        self.feedback_label.setText(QCoreApplication.translate("Form", u"Feedback", None))
        self.feedback_input.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p></body></html>", None))
        self.feedback_input.setPlaceholderText(QCoreApplication.translate("Form", u"Type here...", None))
    # retranslateUi

    @pyqtSlot()
    def emitServiceBtn(self):
        # Emit the custom signal
        self.service_btn_clicked.emit()
        
    @pyqtSlot()
    def emitCancelBtn(self):
        # Emit the custom signal
        self.cancel_btn_clicked.emit()
        
    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
        
    @pyqtSlot()
    def emitProfileBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()
        
    @pyqtSlot()
    def emitScheduleBtn(self):
        # Emit the custom signal
        self.schedule_btn_clicked.emit()
        
    @pyqtSlot()
    def emitHomeBtn(self):
        # Emit the custom signal
        self.home_btn_clicked.emit()
        
    def set_user_id(self, user_id): 
        self.patient_id = user_id
        #print(f"set user id is {self.patient_id}")
        
    def fetch_patient_data(self):
        try:
                patient_data = db.child("patients").child(self.patient_id).get().val()
                if patient_data:
                        return patient_data
                else:
                        raise ValueError("No patient data found for the given ID.")
        except Exception as e:
                print(f"An error occurred while fetching patient data: {e}")
                return None
        
    def generate_new_fb_id(self):
        try:
            feedbacks = db.child("feedback").get()
            max_id = 0
            if feedbacks.each():
                for feedback in feedbacks.each():
                    #print(f"appt is {feedbacks}")
                    fb_id = feedback.key()
                    id_num = int(fb_id.replace("fb_", ""))
                    if id_num > max_id:
                        max_id = id_num
                        #print(f"current max id: {max_id}")
            new_id = max_id + 1
            return f"fb_{new_id}"
        except Exception as e:
            print(f"Error generating new feedback ID: {e}")
            return None
        
    def upload_data_to_db(self):
        subject = self.subject_input.text().strip()
        feedback = self.feedback_input.toPlainText().strip()
        new_fb_id = self.generate_new_fb_id()
        
        # Get the current date
        current_date = datetime.now()

        # Format the date as "yymmdd"
        formatted_date = current_date.strftime("%y%m%d")

        if not subject or not feedback:
            QMessageBox.warning(self, "Missing Data", "Please fill in all fields.")
            return

        try:
            db.child("feedback").child(new_fb_id).update({
                "subject": subject,
                "content": feedback,
                "date": formatted_date,
                "user_id": self.patient_id
            })
            # Display message box if appointment saved successfully
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setInformativeText("Feedback submitted successfully!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.buttonClicked.connect(self.redirect_to_profile)
            msgBox.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to submit feedback: {str(e)}")
            
    def redirect_to_profile(self, button):
        if button.text() == "OK":
            self.redirect_profile.emit()