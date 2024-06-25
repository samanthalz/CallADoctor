from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class CA_homepageWidget(QWidget):
    login_successful = pyqtSignal(int)
    user_id = pyqtSignal(str)
    apply_btn_clicked = pyqtSignal()
    open_ca_homepage = pyqtSignal()
    view_detail_btn_clicked = pyqtSignal()
    doctors_navigation_btn_clicked = pyqtSignal()
    patients_navigation_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    settings_navigation_btn_clicked = pyqtSignal()
    redirect_fb = pyqtSignal(dict)

    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(2307, 1082)
        Form.setStyleSheet(u"background-color: \"#B6D0E2\" ")
        self.background = QWidget(Form)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(150, 0, 1771, 1061))
        self.background.setStyleSheet(u"background-color: #F8F8F8;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-left-radius: 30px;\n"
"text-align: center;")
        self.feedback_frame = QFrame(self.background)
        self.feedback_frame.setObjectName(u"feedback_frame")
        self.feedback_frame.setGeometry(QRect(1090, 180, 481, 831))
        self.feedback_frame.setStyleSheet(u"border: 2px solid #FFFFFF;\n"
"border-radius: 16px;\n"
"background-color: white")
        self.feedback_frame.setFrameShape(QFrame.StyledPanel)
        self.feedback_frame.setFrameShadow(QFrame.Raised)
        self.upcomin_appt_frame_2 = QFrame(self.feedback_frame)
        self.upcomin_appt_frame_2.setObjectName(u"upcomin_appt_frame_2")
        self.upcomin_appt_frame_2.setGeometry(QRect(20, 20, 450, 551))
        self.upcomin_appt_frame_2.setStyleSheet(u"background-color : #ffffff;")
        self.upcomin_appt_frame_2.setFrameShape(QFrame.StyledPanel)
        self.upcomin_appt_frame_2.setFrameShadow(QFrame.Raised)
        self.upcoming_label_2 = QLabel(self.upcomin_appt_frame_2)
        self.upcoming_label_2.setObjectName(u"upcoming_label_2")
        self.upcoming_label_2.setGeometry(QRect(30, 20, 211, 41))
        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(11)
        self.upcoming_label_2.setFont(font)
        self.upcoming_label_2.setStyleSheet(u"border : none;\n"
"")
        self.clinicReq_frame_6 = QFrame(self.upcomin_appt_frame_2)
        self.clinicReq_frame_6.setObjectName(u"clinicReq_frame_6")
        self.clinicReq_frame_6.setGeometry(QRect(20, 70, 401, 81))
        self.clinicReq_frame_6.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame_6.setFrameShadow(QFrame.Raised)
        self.doc_name_label_6 = QLabel(self.clinicReq_frame_6)
        self.doc_name_label_6.setObjectName(u"doc_name_label_6")
        self.doc_name_label_6.setGeometry(QRect(90, 30, 121, 21))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(10)
        self.doc_name_label_6.setFont(font1)
        self.doc_name_label_6.setStyleSheet(u"border : none;\n"
"")
        self.doc_logo_label_2 = QLabel(self.clinicReq_frame_6)
        self.doc_logo_label_2.setObjectName(u"doc_logo_label_2")
        self.doc_logo_label_2.setGeometry(QRect(10, 10, 54, 54))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(9)
        self.doc_logo_label_2.setFont(font2)
        self.doc_logo_label_2.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.doc_logo_label_2.setAlignment(Qt.AlignCenter)
        self.patient_visit_reason_label_6 = QLabel(self.clinicReq_frame_6)
        self.patient_visit_reason_label_6.setObjectName(u"patient_visit_reason_label_6")
        self.patient_visit_reason_label_6.setGeometry(QRect(90, 60, 55, 16))
        self.patient_visit_reason_label_6.setStyleSheet(u"color: #128983")
        self.clinicReq_frame_7 = QFrame(self.upcomin_appt_frame_2)
        self.clinicReq_frame_7.setObjectName(u"clinicReq_frame_7")
        self.clinicReq_frame_7.setGeometry(QRect(20, 170, 401, 81))
        self.clinicReq_frame_7.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame_7.setFrameShadow(QFrame.Raised)
        self.doc_name_label_7 = QLabel(self.clinicReq_frame_7)
        self.doc_name_label_7.setObjectName(u"doc_name_label_7")
        self.doc_name_label_7.setGeometry(QRect(90, 30, 151, 21))
        self.doc_name_label_7.setFont(font1)
        self.doc_name_label_7.setStyleSheet(u"border : none;\n"
"")
        self.clinic_name_label = QLabel(self.clinicReq_frame_7)
        self.clinic_name_label.setObjectName(u"clinic_name_label")
        self.clinic_name_label.setGeometry(QRect(90, 60, 55, 16))
        self.clinic_name_label.setStyleSheet(u"color: #128983")
        self.doc_logo_label_3 = QLabel(self.clinicReq_frame_7)
        self.doc_logo_label_3.setObjectName(u"doc_logo_label_3")
        self.doc_logo_label_3.setGeometry(QRect(10, 10, 54, 54))
        self.doc_logo_label_3.setFont(font2)
        self.doc_logo_label_3.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.doc_logo_label_3.setAlignment(Qt.AlignCenter)
        self.comboBox_2 = QComboBox(self.upcomin_appt_frame_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(290, 30, 131, 31))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        self.comboBox_2.setFont(font3)
        self.clinicReq_frame_8 = QFrame(self.upcomin_appt_frame_2)
        self.clinicReq_frame_8.setObjectName(u"clinicReq_frame_8")
        self.clinicReq_frame_8.setGeometry(QRect(20, 270, 401, 81))
        self.clinicReq_frame_8.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame_8.setFrameShadow(QFrame.Raised)
        self.doc_name_label_8 = QLabel(self.clinicReq_frame_8)
        self.doc_name_label_8.setObjectName(u"doc_name_label_8")
        self.doc_name_label_8.setGeometry(QRect(90, 30, 151, 21))
        self.doc_name_label_8.setFont(font1)
        self.doc_name_label_8.setStyleSheet(u"border : none;\n"
"")
        self.doc_logo_label_7 = QLabel(self.clinicReq_frame_8)
        self.doc_logo_label_7.setObjectName(u"doc_logo_label_7")
        self.doc_logo_label_7.setGeometry(QRect(10, 10, 54, 54))
        self.doc_logo_label_7.setFont(font2)
        self.doc_logo_label_7.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.doc_logo_label_7.setAlignment(Qt.AlignCenter)
        self.patient_visit_reason_label_8 = QLabel(self.clinicReq_frame_8)
        self.patient_visit_reason_label_8.setObjectName(u"patient_visit_reason_label_8")
        self.patient_visit_reason_label_8.setGeometry(QRect(90, 60, 55, 16))
        self.patient_visit_reason_label_8.setStyleSheet(u"color: #128983")
        self.clinicReq_frame_9 = QFrame(self.upcomin_appt_frame_2)
        self.clinicReq_frame_9.setObjectName(u"clinicReq_frame_9")
        self.clinicReq_frame_9.setGeometry(QRect(20, 370, 401, 81))
        self.clinicReq_frame_9.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame_9.setFrameShadow(QFrame.Raised)
        self.patient_name_label_9 = QLabel(self.clinicReq_frame_9)
        self.patient_name_label_9.setObjectName(u"patient_name_label_9")
        self.patient_name_label_9.setGeometry(QRect(90, 30, 151, 21))
        self.patient_name_label_9.setFont(font1)
        self.patient_name_label_9.setStyleSheet(u"border : none;\n"
"")
        self.doc_logo_label_8 = QLabel(self.clinicReq_frame_9)
        self.doc_logo_label_8.setObjectName(u"doc_logo_label_8")
        self.doc_logo_label_8.setGeometry(QRect(10, 10, 54, 54))
        self.doc_logo_label_8.setFont(font2)
        self.doc_logo_label_8.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.doc_logo_label_8.setAlignment(Qt.AlignCenter)
        self.patient_visit_reason_label_9 = QLabel(self.clinicReq_frame_9)
        self.patient_visit_reason_label_9.setObjectName(u"patient_visit_reason_label_9")
        self.patient_visit_reason_label_9.setGeometry(QRect(90, 60, 55, 16))
        self.patient_visit_reason_label_9.setStyleSheet(u"color: #128983")
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
        self.profile_btn.setGeometry(QRect(110, 25, 111, 31))
        self.profile_btn.setFont(font3)
        self.profile_btn.setStyleSheet(u"border: none")

        self.profile_btn.clicked.connect(self.emitProfileBtn)

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
        self.visit_for_today_label = QLabel(self.clinic_req_frame)
        self.visit_for_today_label.setObjectName(u"visit_for_today_label")
        self.visit_for_today_label.setGeometry(QRect(20, 20, 961, 61))
        font4 = QFont()
        font4.setFamily(u"Cascadia Code")
        font4.setPointSize(22)
        self.visit_for_today_label.setFont(font4)
        self.visit_for_today_label.setWordWrap(True)
        self.clinic_req__label = QLabel(self.clinic_req_frame)
        self.clinic_req__label.setObjectName(u"clinic_req__label")
        self.clinic_req__label.setGeometry(QRect(30, 100, 141, 71))
        font5 = QFont()
        font5.setFamily(u"Cascadia Code")
        font5.setPointSize(48)
        self.clinic_req__label.setFont(font5)
        self.details_frame = QFrame(self.background)
        self.details_frame.setObjectName(u"details_frame")
        self.details_frame.setGeometry(QRect(50, 420, 1000, 600))
        self.details_frame.setStyleSheet(u"border: 2px solid #F8F8F8;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.details_frame.setFrameShape(QFrame.StyledPanel)
        self.details_frame.setFrameShadow(QFrame.Raised)
        self.details_frame.setLineWidth(6)
        self.upcomin_appt_frame = QFrame(self.details_frame)
        self.upcomin_appt_frame.setObjectName(u"upcomin_appt_frame")
        self.upcomin_appt_frame.setGeometry(QRect(30, 30, 450, 551))
        self.upcomin_appt_frame.setStyleSheet(u"background-color : #ffffff;")
        self.upcomin_appt_frame.setFrameShape(QFrame.StyledPanel)
        self.upcomin_appt_frame.setFrameShadow(QFrame.Raised)
        self.upcoming_label = QLabel(self.upcomin_appt_frame)
        self.upcoming_label.setObjectName(u"upcoming_label")
        self.upcoming_label.setGeometry(QRect(30, 20, 211, 41))
        self.upcoming_label.setFont(font)
        self.upcoming_label.setStyleSheet(u"border : none;\n"
"")
        self.clinicReq_frame = QFrame(self.upcomin_appt_frame)
        self.clinicReq_frame.setObjectName(u"clinicReq_frame")
        self.clinicReq_frame.setGeometry(QRect(20, 70, 401, 81))
        self.clinicReq_frame.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame.setFrameShadow(QFrame.Raised)
        self.patient_name_label = QLabel(self.clinicReq_frame)
        self.patient_name_label.setObjectName(u"patient_name_label")
        self.patient_name_label.setGeometry(QRect(90, 30, 121, 21))
        self.patient_name_label.setFont(font1)
        self.patient_name_label.setStyleSheet(u"border : none;\n"
"")
        self.patient_logo_label = QLabel(self.clinicReq_frame)
        self.patient_logo_label.setObjectName(u"patient_logo_label")
        self.patient_logo_label.setGeometry(QRect(10, 10, 54, 54))
        self.patient_logo_label.setFont(font2)
        self.patient_logo_label.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.patient_logo_label.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.clinicReq_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 91, 41))
        self.label.setFont(font3)
        self.label.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.10);\n"
"color: #128983; text-align: center;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.patient_visit_reason_label = QLabel(self.clinicReq_frame)
        self.patient_visit_reason_label.setObjectName(u"patient_visit_reason_label")
        self.patient_visit_reason_label.setGeometry(QRect(90, 60, 55, 16))
        self.patient_visit_reason_label.setStyleSheet(u"color: #128983")
        self.clinicReq_frame_2 = QFrame(self.upcomin_appt_frame)
        self.clinicReq_frame_2.setObjectName(u"clinicReq_frame_2")
        self.clinicReq_frame_2.setGeometry(QRect(20, 170, 401, 81))
        self.clinicReq_frame_2.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame_2.setFrameShadow(QFrame.Raised)
        self.patient_name_label_2 = QLabel(self.clinicReq_frame_2)
        self.patient_name_label_2.setObjectName(u"patient_name_label_2")
        self.patient_name_label_2.setGeometry(QRect(90, 30, 151, 21))
        self.patient_name_label_2.setFont(font1)
        self.patient_name_label_2.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_2 = QLabel(self.clinicReq_frame_2)
        self.clinic_logo_label_2.setObjectName(u"clinic_logo_label_2")
        self.clinic_logo_label_2.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_2.setFont(font2)
        self.clinic_logo_label_2.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_2.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.clinicReq_frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 20, 91, 41))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.10);\n"
"color: #128983; text-align: center;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.patient_visit_reason_label_2 = QLabel(self.clinicReq_frame_2)
        self.patient_visit_reason_label_2.setObjectName(u"patient_visit_reason_label_2")
        self.patient_visit_reason_label_2.setGeometry(QRect(90, 60, 121, 16))
        self.patient_visit_reason_label_2.setStyleSheet(u"color: #128983")
        self.comboBox = QComboBox(self.upcomin_appt_frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(290, 30, 131, 31))
        self.comboBox.setFont(font3)
        self.clinicReq_frame_3 = QFrame(self.upcomin_appt_frame)
        self.clinicReq_frame_3.setObjectName(u"clinicReq_frame_3")
        self.clinicReq_frame_3.setGeometry(QRect(20, 270, 401, 81))
        self.clinicReq_frame_3.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame_3.setFrameShadow(QFrame.Raised)
        self.patient_name_label_3 = QLabel(self.clinicReq_frame_3)
        self.patient_name_label_3.setObjectName(u"patient_name_label_3")
        self.patient_name_label_3.setGeometry(QRect(90, 30, 151, 21))
        self.patient_name_label_3.setFont(font1)
        self.patient_name_label_3.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_3 = QLabel(self.clinicReq_frame_3)
        self.clinic_logo_label_3.setObjectName(u"clinic_logo_label_3")
        self.clinic_logo_label_3.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_3.setFont(font2)
        self.clinic_logo_label_3.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_3.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.clinicReq_frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 20, 91, 41))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.10);\n"
"color: #128983; text-align: center;\n"
"\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.patient_visit_reason_label_3 = QLabel(self.clinicReq_frame_3)
        self.patient_visit_reason_label_3.setObjectName(u"patient_visit_reason_label_3")
        self.patient_visit_reason_label_3.setGeometry(QRect(90, 60, 121, 16))
        self.patient_visit_reason_label_3.setStyleSheet(u"color: #128983")
        self.clinicReq_frame_4 = QFrame(self.upcomin_appt_frame)
        self.clinicReq_frame_4.setObjectName(u"clinicReq_frame_4")
        self.clinicReq_frame_4.setGeometry(QRect(20, 370, 401, 81))
        self.clinicReq_frame_4.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame_4.setFrameShadow(QFrame.Raised)
        self.patient_name_label_4 = QLabel(self.clinicReq_frame_4)
        self.patient_name_label_4.setObjectName(u"patient_name_label_4")
        self.patient_name_label_4.setGeometry(QRect(90, 30, 151, 21))
        self.patient_name_label_4.setFont(font1)
        self.patient_name_label_4.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_4 = QLabel(self.clinicReq_frame_4)
        self.clinic_logo_label_4.setObjectName(u"clinic_logo_label_4")
        self.clinic_logo_label_4.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_4.setFont(font2)
        self.clinic_logo_label_4.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_4.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.clinicReq_frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 20, 91, 41))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.10);\n"
"color: #128983; text-align: center;\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.patient_visit_reason_label_4 = QLabel(self.clinicReq_frame_4)
        self.patient_visit_reason_label_4.setObjectName(u"patient_visit_reason_label_4")
        self.patient_visit_reason_label_4.setGeometry(QRect(90, 60, 55, 16))
        self.patient_visit_reason_label_4.setStyleSheet(u"color: #128983")
        self.clinicReq_frame_5 = QFrame(self.upcomin_appt_frame)
        self.clinicReq_frame_5.setObjectName(u"clinicReq_frame_5")
        self.clinicReq_frame_5.setGeometry(QRect(20, 470, 401, 81))
        self.clinicReq_frame_5.setFrameShape(QFrame.StyledPanel)
        self.clinicReq_frame_5.setFrameShadow(QFrame.Raised)
        self.patient_name_label_5 = QLabel(self.clinicReq_frame_5)
        self.patient_name_label_5.setObjectName(u"patient_name_label_5")
        self.patient_name_label_5.setGeometry(QRect(90, 30, 151, 21))
        self.patient_name_label_5.setFont(font1)
        self.patient_name_label_5.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_5 = QLabel(self.clinicReq_frame_5)
        self.clinic_logo_label_5.setObjectName(u"clinic_logo_label_5")
        self.clinic_logo_label_5.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_5.setFont(font2)
        self.clinic_logo_label_5.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_5.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.clinicReq_frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 20, 91, 41))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"background-color: rgba(18, 137, 131, 0.10);\n"
"color: #128983; text-align: center;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.patient_visit_reason_label_5 = QLabel(self.clinicReq_frame_5)
        self.patient_visit_reason_label_5.setObjectName(u"patient_visit_reason_label_5")
        self.patient_visit_reason_label_5.setGeometry(QRect(80, 60, 91, 16))
        self.patient_visit_reason_label_5.setStyleSheet(u"color: #128983")
        self.request_detail_outer = QFrame(self.details_frame)
        self.request_detail_outer.setObjectName(u"request_detail_outer")
        self.request_detail_outer.setGeometry(QRect(510, 30, 450, 551))
        self.request_detail_outer.setStyleSheet(u"background-color : #ffffff;")
        self.request_detail_outer.setFrameShape(QFrame.StyledPanel)
        self.request_detail_outer.setFrameShadow(QFrame.Raised)
        self.req_detail_label = QLabel(self.request_detail_outer)
        self.req_detail_label.setObjectName(u"req_detail_label")
        self.req_detail_label.setGeometry(QRect(30, 20, 381, 41))
        self.req_detail_label.setFont(font)
        self.req_detail_label.setStyleSheet(u"border : none;\n"
"")
        self.clinic_details_inner = QFrame(self.request_detail_outer)
        self.clinic_details_inner.setObjectName(u"clinic_details_inner")
        self.clinic_details_inner.setGeometry(QRect(20, 70, 411, 421))
        self.clinic_details_inner.setFrameShape(QFrame.StyledPanel)
        self.clinic_details_inner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.clinic_details_inner)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.patient_logo = QLabel(self.clinic_details_inner)
        self.patient_logo.setObjectName(u"patient_logo")
        self.patient_logo.setFont(font2)
        self.patient_logo.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.patient_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.patient_logo)

        self.patient_name = QLabel(self.clinic_details_inner)
        self.patient_name.setObjectName(u"patient_name")
        self.patient_name.setFont(font1)
        self.patient_name.setStyleSheet(u"border : none;\n"
"")

        self.verticalLayout_2.addWidget(self.patient_name)

        self.line = QFrame(self.clinic_details_inner)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(357, 3))
        self.line.setMaximumSize(QSize(16777215, 3))
        self.line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        self.line.setFrameShape(QFrame.StyledPanel)
        self.line.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.line)

        self.splitter = QSplitter(self.clinic_details_inner)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.phone_label = QLabel(self.splitter)
        self.phone_label.setObjectName(u"phone_label")
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.phone_label.setFont(font6)
        self.phone_label.setStyleSheet(u"border: none;")
        self.phone_label.setLineWidth(0)
        self.splitter.addWidget(self.phone_label)
        self.add_display_2 = QLabel(self.splitter)
        self.add_display_2.setObjectName(u"add_display_2")
        font7 = QFont()
        font7.setFamily(u"Consolas")
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setWeight(50)
        self.add_display_2.setFont(font7)
        self.add_display_2.setStyleSheet(u"border: none;")
        self.add_display_2.setScaledContents(False)
        self.add_display_2.setWordWrap(True)
        self.splitter.addWidget(self.add_display_2)

        self.verticalLayout_2.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.clinic_details_inner)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.diagnosis_label = QLabel(self.splitter_2)
        self.diagnosis_label.setObjectName(u"diagnosis_label")
        self.diagnosis_label.setFont(font6)
        self.diagnosis_label.setStyleSheet(u"border: none;")
        self.splitter_2.addWidget(self.diagnosis_label)
        self.add_display = QLabel(self.splitter_2)
        self.add_display.setObjectName(u"add_display")
        self.add_display.setFont(font7)
        self.add_display.setStyleSheet(u"border: none;")
        self.add_display.setScaledContents(False)
        self.add_display.setWordWrap(True)
        self.splitter_2.addWidget(self.add_display)

        self.verticalLayout_2.addWidget(self.splitter_2)

        self.splitter_3 = QSplitter(self.clinic_details_inner)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.date_text = QLabel(self.splitter_3)
        self.date_text.setObjectName(u"date_text")
        self.date_text.setFont(font6)
        self.date_text.setStyleSheet(u"border: none;")
        self.date_text.setWordWrap(True)
        self.splitter_3.addWidget(self.date_text)
        self.hour_display = QLabel(self.splitter_3)
        self.hour_display.setObjectName(u"hour_display")
        self.hour_display.setFont(font7)
        self.hour_display.setStyleSheet(u"border: none;")
        self.hour_display.setScaledContents(False)
        self.hour_display.setWordWrap(True)
        self.splitter_3.addWidget(self.hour_display)

        self.verticalLayout_2.addWidget(self.splitter_3)

        self.view_detail_btn = QPushButton(self.request_detail_outer)
        self.view_detail_btn.setObjectName(u"view_detail_btn")
        self.view_detail_btn.setGeometry(QRect(320, 510, 93, 28))
        font8 = QFont()
        font8.setFamily(u"Consolas")
        font8.setPointSize(9)
        font8.setUnderline(True)
        self.view_detail_btn.setFont(font8)
        self.view_detail_btn.setStyleSheet(u"color: #007E85; border: none;")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(31, 20, 87, 851))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_navigation = QToolButton(self.layoutWidget)
        self.home_navigation.setObjectName(u"home_navigation")
        self.home_navigation.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        self.home_navigation.setMinimumSize(QSize(85, 96))
        self.home_navigation.setMaximumSize(QSize(85, 96))
        font9 = QFont()
        font9.setFamily(u"Source Sans Pro Semibold")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        self.home_navigation.setFont(font9)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.view_detail_btn_clicked.connect(self.emitViewDetailBtn)

        self.verticalLayout.addWidget(self.home_navigation)

        self.doctors_navigation = QToolButton(self.layoutWidget)
        self.doctors_navigation.setObjectName(u"doctors_navigation")
        self.doctors_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.doctors_navigation.sizePolicy().hasHeightForWidth())
        self.doctors_navigation.setSizePolicy(sizePolicy)
        self.doctors_navigation.setMinimumSize(QSize(85, 96))
        self.doctors_navigation.setMaximumSize(QSize(85, 96))
        self.doctors_navigation.setFont(font9)
        self.doctors_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.doctors_navigation.setIcon(icon2)
        self.doctors_navigation.setIconSize(QSize(70, 70))
        self.doctors_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.doctors_navigation_btn_clicked.connect(self.emitDoctorsBtn)

        self.verticalLayout.addWidget(self.doctors_navigation)

        self.patients_navigation = QToolButton(self.layoutWidget)
        self.patients_navigation.setObjectName(u"patients_navigation")
        self.patients_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.patients_navigation.sizePolicy().hasHeightForWidth())
        self.patients_navigation.setSizePolicy(sizePolicy)
        self.patients_navigation.setMinimumSize(QSize(85, 96))
        self.patients_navigation.setMaximumSize(QSize(85, 96))
        self.patients_navigation.setFont(font9)
        self.patients_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patients_navigation.setIcon(icon3)
        self.patients_navigation.setIconSize(QSize(70, 70))
        self.patients_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.patients_navigation_btn_clicked.connect(self.emitPatientsBtn)

        self.verticalLayout.addWidget(self.patients_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setMinimumSize(QSize(85, 96))
        self.settings_navigation.setMaximumSize(QSize(85, 96))
        self.settings_navigation.setFont(font9)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.settings_navigation_btn_clicked.connect(self.emitSettingsBtn)

        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setMinimumSize(QSize(85, 96))
        self.logout_navigation.setMaximumSize(QSize(85, 96))
        self.logout_navigation.setFont(font9)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon5 = QIcon()
        icon5.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.logout_navigation)

        self.logout_btn_clicked.connect(self.emitLogoutBtn)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.upcoming_label_2.setText(QCoreApplication.translate("Form", u"Doctor List", None))
        self.doc_name_label_6.setText(QCoreApplication.translate("Form", u"Dr Name", None))
        self.doc_logo_label_2.setText(QCoreApplication.translate("Form", u"A", None))
        self.patient_visit_reason_label_6.setText(QCoreApplication.translate("Form", u"Clinic A", None))
        self.doc_name_label_7.setText(QCoreApplication.translate("Form", u"Dr Name", None))
        self.clinic_name_label.setText(QCoreApplication.translate("Form", u"Clinic A", None))
        self.doc_logo_label_3.setText(QCoreApplication.translate("Form", u"DR", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Recent", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Oldest", None))

        self.doc_name_label_8.setText(QCoreApplication.translate("Form", u"Dr Name", None))
        self.doc_logo_label_7.setText(QCoreApplication.translate("Form", u"DR", None))
        self.patient_visit_reason_label_8.setText(QCoreApplication.translate("Form", u"Clinic A", None))
        self.patient_name_label_9.setText(QCoreApplication.translate("Form", u"Dr Name", None))
        self.doc_logo_label_8.setText(QCoreApplication.translate("Form", u"DR", None))
        self.patient_visit_reason_label_9.setText(QCoreApplication.translate("Form", u"Clinic A", None))
        self.noti_icon.setText("")
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Clinic name", None))
        self.visit_for_today_label.setText(QCoreApplication.translate("Form", u"Visits for today:", None))
        self.clinic_req__label.setText(QCoreApplication.translate("Form", u"10", None))
        self.upcoming_label.setText(QCoreApplication.translate("Form", u"Patient List", None))
        self.patient_name_label.setText(QCoreApplication.translate("Form", u"A", None))
        self.patient_logo_label.setText(QCoreApplication.translate("Form", u"A", None))
        self.label.setText(QCoreApplication.translate("Form", u"Time", None))
        self.patient_visit_reason_label.setText(QCoreApplication.translate("Form", u"Report", None))
        self.patient_name_label_2.setText(QCoreApplication.translate("Form", u"Patient Name", None))
        self.clinic_logo_label_2.setText(QCoreApplication.translate("Form", u"PN", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Time", None))
        self.patient_visit_reason_label_2.setText(QCoreApplication.translate("Form", u"Weekly visit", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Recent", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Oldest", None))

        self.patient_name_label_3.setText(QCoreApplication.translate("Form", u"Patient Name", None))
        self.clinic_logo_label_3.setText(QCoreApplication.translate("Form", u"PN", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Time", None))
        self.patient_visit_reason_label_3.setText(QCoreApplication.translate("Form", u"Routine Checkup", None))
        self.patient_name_label_4.setText(QCoreApplication.translate("Form", u"Patient Name", None))
        self.clinic_logo_label_4.setText(QCoreApplication.translate("Form", u"PN", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Time", None))
        self.patient_visit_reason_label_4.setText(QCoreApplication.translate("Form", u"Report", None))
        self.patient_name_label_5.setText(QCoreApplication.translate("Form", u"Patient Name", None))
        self.clinic_logo_label_5.setText(QCoreApplication.translate("Form", u"PN", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Time", None))
        self.patient_visit_reason_label_5.setText(QCoreApplication.translate("Form", u"Weekly Visit", None))
        self.req_detail_label.setText(QCoreApplication.translate("Form", u"Consultation Details", None))
        self.patient_logo.setText(QCoreApplication.translate("Form", u"A", None))
        self.patient_name.setText(QCoreApplication.translate("Form", u"Patient Name", None))
        self.phone_label.setText(QCoreApplication.translate("Form", u"Last Checked:", None))
        self.add_display_2.setText(QCoreApplication.translate("Form", u"Dr name", None))
        self.diagnosis_label.setText(QCoreApplication.translate("Form", u"Dianogsis:", None))
        self.add_display.setText(QCoreApplication.translate("Form", u"diagnosis", None))
        self.date_text.setText(QCoreApplication.translate("Form", u"Date:", None))
        self.hour_display.setText(QCoreApplication.translate("Form", u"date", None))
        self.view_detail_btn.setText(QCoreApplication.translate("Form", u"View More", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.doctors_navigation.setText(QCoreApplication.translate("Form", u"Doctors", None))
        self.patients_navigation.setText(QCoreApplication.translate("Form", u"Patients", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

    @pyqtSlot()
    def emitDoctorsBtn(self):
        self.doctors_navigation_btn_clicked.emit()
        
    @pyqtSlot()
    def emitViewDetailBtn(self):
        self.view_detail_btn_clicked.emit()

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

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWin = CA_homepageWidget()
    mainWin.showMaximized()
    sys.exit(app.exec_())
