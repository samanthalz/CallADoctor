from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class HomeWidget(QWidget):
        
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
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
"border-top-left-radius: 30px;")
        self.num_appt_frame = QFrame(self.background)
        self.num_appt_frame.setObjectName(u"num_appt_frame")
        self.num_appt_frame.setGeometry(QRect(50, 140, 1000, 230))
        self.num_appt_frame.setStyleSheet(u"border-radius: 10px;\n"
"    background-color: #B6D0E2;\n"
"    background-image: qlineargradient(\n"
"        spread: pad, \n"
"        x1: 0, y1: 0, \n"
"        x2: 0, y2: 1, \n"
"        stop: 0 #B6D0E2, \n"
"        stop: 1 #FFFFFF\n"
"    );")
        self.num_appt_frame.setFrameShape(QFrame.StyledPanel)
        self.num_appt_frame.setFrameShadow(QFrame.Raised)
        self.num_upcoming_appt_label = QLabel(self.num_appt_frame)
        self.num_upcoming_appt_label.setObjectName(u"num_upcoming_appt_label")
        self.num_upcoming_appt_label.setGeometry(QRect(20, 20, 951, 61))
        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(22)
        self.num_upcoming_appt_label.setFont(font)
        self.num_upcoming_appt_label.setWordWrap(True)
        self.num_appt_number_label = QLabel(self.num_appt_frame)
        self.num_appt_number_label.setObjectName(u"num_appt_number_label")
        self.num_appt_number_label.setGeometry(QRect(30, 100, 51, 71))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(48)
        self.num_appt_number_label.setFont(font1)
        self.appointment_frame = QFrame(self.background)
        self.appointment_frame.setObjectName(u"appointment_frame")
        self.appointment_frame.setGeometry(QRect(50, 410, 1000, 600))
        self.appointment_frame.setStyleSheet(u"border: 2px solid #F8F8F8;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.appointment_frame.setFrameShape(QFrame.StyledPanel)
        self.appointment_frame.setFrameShadow(QFrame.Raised)
        self.appointment_frame.setLineWidth(6)
        self.upcomin_appt_frame = QFrame(self.appointment_frame)
        self.upcomin_appt_frame.setObjectName(u"upcomin_appt_frame")
        self.upcomin_appt_frame.setGeometry(QRect(30, 30, 450, 531))
        self.upcomin_appt_frame.setStyleSheet(u"background-color : #ffffff;")
        self.upcomin_appt_frame.setFrameShape(QFrame.StyledPanel)
        self.upcomin_appt_frame.setFrameShadow(QFrame.Raised)
        self.upcoming_label = QLabel(self.upcomin_appt_frame)
        self.upcoming_label.setObjectName(u"upcoming_label")
        self.upcoming_label.setGeometry(QRect(30, 20, 101, 41))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(11)
        self.upcoming_label.setFont(font2)
        self.upcoming_label.setStyleSheet(u"border : none;\n"
"")
        self.clinicAppt_frame = QFrame(self.upcomin_appt_frame)
        self.clinicAppt_frame.setObjectName(u"clinicAppt_frame")
        self.clinicAppt_frame.setGeometry(QRect(20, 70, 401, 81))
        self.clinicAppt_frame.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame.setFrameShadow(QFrame.Raised)
        self.clinic_name_label = QLabel(self.clinicAppt_frame)
        self.clinic_name_label.setObjectName(u"clinic_name_label")
        self.clinic_name_label.setGeometry(QRect(90, 10, 121, 21))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)
        self.clinic_name_label.setFont(font3)
        self.clinic_name_label.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label = QLabel(self.clinicAppt_frame)
        self.clinic_logo_label.setObjectName(u"clinic_logo_label")
        self.clinic_logo_label.setGeometry(QRect(10, 10, 54, 54))
        font4 = QFont()
        font4.setFamily(u"Cascadia Code")
        font4.setPointSize(9)
        self.clinic_logo_label.setFont(font4)
        self.clinic_logo_label.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label.setAlignment(Qt.AlignCenter)
        self.toa_label = QLabel(self.clinicAppt_frame)
        self.toa_label.setObjectName(u"toa_label")
        self.toa_label.setGeometry(QRect(90, 30, 161, 21))
        self.toa_label.setFont(font3)
        self.toa_label.setStyleSheet(u"border : none;\n"
"color : #6ea0c4;\n"
"")
        self.date_time_frame = QFrame(self.clinicAppt_frame)
        self.date_time_frame.setObjectName(u"date_time_frame")
        self.date_time_frame.setGeometry(QRect(280, 20, 71, 41))
        self.date_time_frame.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #dbe7f0;")
        self.date_time_frame.setFrameShape(QFrame.StyledPanel)
        self.date_time_frame.setFrameShadow(QFrame.Raised)
        self.date_label = QLabel(self.date_time_frame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(10, 0, 47, 13))
        font5 = QFont()
        font5.setFamily(u"Cascadia Code")
        self.date_label.setFont(font5)
        self.date_label.setStyleSheet(u"border : none;\n"
"")
        self.time_label = QLabel(self.date_time_frame)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(10, 20, 47, 13))
        self.time_label.setFont(font5)
        self.time_label.setStyleSheet(u"border : none;\n"
"")
        self.clinicAppt_frame_2 = QFrame(self.upcomin_appt_frame)
        self.clinicAppt_frame_2.setObjectName(u"clinicAppt_frame_2")
        self.clinicAppt_frame_2.setGeometry(QRect(20, 170, 401, 81))
        self.clinicAppt_frame_2.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame_2.setFrameShadow(QFrame.Raised)
        self.clinic_name_label_2 = QLabel(self.clinicAppt_frame_2)
        self.clinic_name_label_2.setObjectName(u"clinic_name_label_2")
        self.clinic_name_label_2.setGeometry(QRect(90, 10, 121, 21))
        self.clinic_name_label_2.setFont(font3)
        self.clinic_name_label_2.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_2 = QLabel(self.clinicAppt_frame_2)
        self.clinic_logo_label_2.setObjectName(u"clinic_logo_label_2")
        self.clinic_logo_label_2.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_2.setFont(font4)
        self.clinic_logo_label_2.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_2.setAlignment(Qt.AlignCenter)
        self.toa_label_2 = QLabel(self.clinicAppt_frame_2)
        self.toa_label_2.setObjectName(u"toa_label_2")
        self.toa_label_2.setGeometry(QRect(90, 30, 161, 21))
        self.toa_label_2.setFont(font3)
        self.toa_label_2.setStyleSheet(u"border : none;\n"
"color : #6ea0c4;\n"
"")
        self.date_time_frame_2 = QFrame(self.clinicAppt_frame_2)
        self.date_time_frame_2.setObjectName(u"date_time_frame_2")
        self.date_time_frame_2.setGeometry(QRect(280, 20, 71, 41))
        self.date_time_frame_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #dbe7f0;")
        self.date_time_frame_2.setFrameShape(QFrame.StyledPanel)
        self.date_time_frame_2.setFrameShadow(QFrame.Raised)
        self.date_label_2 = QLabel(self.date_time_frame_2)
        self.date_label_2.setObjectName(u"date_label_2")
        self.date_label_2.setGeometry(QRect(10, 0, 47, 13))
        self.date_label_2.setFont(font5)
        self.date_label_2.setStyleSheet(u"border : none;\n"
"")
        self.time_label_2 = QLabel(self.date_time_frame_2)
        self.time_label_2.setObjectName(u"time_label_2")
        self.time_label_2.setGeometry(QRect(10, 20, 47, 13))
        self.time_label_2.setFont(font5)
        self.time_label_2.setStyleSheet(u"border : none;\n"
"")
        self.clinicAppt_frame_3 = QFrame(self.upcomin_appt_frame)
        self.clinicAppt_frame_3.setObjectName(u"clinicAppt_frame_3")
        self.clinicAppt_frame_3.setGeometry(QRect(20, 270, 401, 81))
        self.clinicAppt_frame_3.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame_3.setFrameShadow(QFrame.Raised)
        self.clinic_name_label_3 = QLabel(self.clinicAppt_frame_3)
        self.clinic_name_label_3.setObjectName(u"clinic_name_label_3")
        self.clinic_name_label_3.setGeometry(QRect(90, 10, 121, 21))
        self.clinic_name_label_3.setFont(font3)
        self.clinic_name_label_3.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_3 = QLabel(self.clinicAppt_frame_3)
        self.clinic_logo_label_3.setObjectName(u"clinic_logo_label_3")
        self.clinic_logo_label_3.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_3.setFont(font4)
        self.clinic_logo_label_3.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_3.setAlignment(Qt.AlignCenter)
        self.toa_label_3 = QLabel(self.clinicAppt_frame_3)
        self.toa_label_3.setObjectName(u"toa_label_3")
        self.toa_label_3.setGeometry(QRect(90, 30, 161, 21))
        self.toa_label_3.setFont(font3)
        self.toa_label_3.setStyleSheet(u"border : none;\n"
"color : #6ea0c4;\n"
"")
        self.date_time_frame_3 = QFrame(self.clinicAppt_frame_3)
        self.date_time_frame_3.setObjectName(u"date_time_frame_3")
        self.date_time_frame_3.setGeometry(QRect(280, 20, 71, 41))
        self.date_time_frame_3.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #dbe7f0;")
        self.date_time_frame_3.setFrameShape(QFrame.StyledPanel)
        self.date_time_frame_3.setFrameShadow(QFrame.Raised)
        self.date_label_3 = QLabel(self.date_time_frame_3)
        self.date_label_3.setObjectName(u"date_label_3")
        self.date_label_3.setGeometry(QRect(10, 0, 47, 13))
        self.date_label_3.setFont(font5)
        self.date_label_3.setStyleSheet(u"border : none;\n"
"")
        self.time_label_3 = QLabel(self.date_time_frame_3)
        self.time_label_3.setObjectName(u"time_label_3")
        self.time_label_3.setGeometry(QRect(10, 20, 47, 13))
        self.time_label_3.setFont(font5)
        self.time_label_3.setStyleSheet(u"border : none;\n"
"")
        self.upcomin_appt_frame_2 = QFrame(self.appointment_frame)
        self.upcomin_appt_frame_2.setObjectName(u"upcomin_appt_frame_2")
        self.upcomin_appt_frame_2.setGeometry(QRect(510, 30, 450, 531))
        self.upcomin_appt_frame_2.setStyleSheet(u"background-color : #ffffff;")
        self.upcomin_appt_frame_2.setFrameShape(QFrame.StyledPanel)
        self.upcomin_appt_frame_2.setFrameShadow(QFrame.Raised)
        self.upcoming_label_2 = QLabel(self.upcomin_appt_frame_2)
        self.upcoming_label_2.setObjectName(u"upcoming_label_2")
        self.upcoming_label_2.setGeometry(QRect(30, 20, 101, 41))
        self.upcoming_label_2.setFont(font2)
        self.upcoming_label_2.setStyleSheet(u"border : none;\n"
"")
        self.clinicAppt_frame_4 = QFrame(self.upcomin_appt_frame_2)
        self.clinicAppt_frame_4.setObjectName(u"clinicAppt_frame_4")
        self.clinicAppt_frame_4.setGeometry(QRect(20, 170, 401, 81))
        self.clinicAppt_frame_4.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame_4.setFrameShadow(QFrame.Raised)
        self.clinic_name_label_4 = QLabel(self.clinicAppt_frame_4)
        self.clinic_name_label_4.setObjectName(u"clinic_name_label_4")
        self.clinic_name_label_4.setGeometry(QRect(90, 10, 121, 21))
        self.clinic_name_label_4.setFont(font3)
        self.clinic_name_label_4.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_4 = QLabel(self.clinicAppt_frame_4)
        self.clinic_logo_label_4.setObjectName(u"clinic_logo_label_4")
        self.clinic_logo_label_4.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_4.setFont(font4)
        self.clinic_logo_label_4.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_4.setAlignment(Qt.AlignCenter)
        self.toa_label_4 = QLabel(self.clinicAppt_frame_4)
        self.toa_label_4.setObjectName(u"toa_label_4")
        self.toa_label_4.setGeometry(QRect(90, 30, 161, 21))
        self.toa_label_4.setFont(font3)
        self.toa_label_4.setStyleSheet(u"border : none;\n"
"color : #6ea0c4;\n"
"")
        self.date_time_frame_4 = QFrame(self.clinicAppt_frame_4)
        self.date_time_frame_4.setObjectName(u"date_time_frame_4")
        self.date_time_frame_4.setGeometry(QRect(280, 20, 71, 41))
        self.date_time_frame_4.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #dbe7f0;")
        self.date_time_frame_4.setFrameShape(QFrame.StyledPanel)
        self.date_time_frame_4.setFrameShadow(QFrame.Raised)
        self.date_label_4 = QLabel(self.date_time_frame_4)
        self.date_label_4.setObjectName(u"date_label_4")
        self.date_label_4.setGeometry(QRect(10, 0, 47, 13))
        self.date_label_4.setFont(font5)
        self.date_label_4.setStyleSheet(u"border : none;\n"
"")
        self.time_label_4 = QLabel(self.date_time_frame_4)
        self.time_label_4.setObjectName(u"time_label_4")
        self.time_label_4.setGeometry(QRect(10, 20, 47, 13))
        self.time_label_4.setFont(font5)
        self.time_label_4.setStyleSheet(u"border : none;\n"
"")
        self.clinicAppt_frame_5 = QFrame(self.upcomin_appt_frame_2)
        self.clinicAppt_frame_5.setObjectName(u"clinicAppt_frame_5")
        self.clinicAppt_frame_5.setGeometry(QRect(20, 270, 401, 81))
        self.clinicAppt_frame_5.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame_5.setFrameShadow(QFrame.Raised)
        self.clinic_name_label_5 = QLabel(self.clinicAppt_frame_5)
        self.clinic_name_label_5.setObjectName(u"clinic_name_label_5")
        self.clinic_name_label_5.setGeometry(QRect(90, 10, 121, 21))
        self.clinic_name_label_5.setFont(font3)
        self.clinic_name_label_5.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_5 = QLabel(self.clinicAppt_frame_5)
        self.clinic_logo_label_5.setObjectName(u"clinic_logo_label_5")
        self.clinic_logo_label_5.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_5.setFont(font4)
        self.clinic_logo_label_5.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_5.setAlignment(Qt.AlignCenter)
        self.toa_label_5 = QLabel(self.clinicAppt_frame_5)
        self.toa_label_5.setObjectName(u"toa_label_5")
        self.toa_label_5.setGeometry(QRect(90, 30, 161, 21))
        self.toa_label_5.setFont(font3)
        self.toa_label_5.setStyleSheet(u"border : none;\n"
"color : #6ea0c4;\n"
"")
        self.date_time_frame_5 = QFrame(self.clinicAppt_frame_5)
        self.date_time_frame_5.setObjectName(u"date_time_frame_5")
        self.date_time_frame_5.setGeometry(QRect(280, 20, 71, 41))
        self.date_time_frame_5.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #dbe7f0;")
        self.date_time_frame_5.setFrameShape(QFrame.StyledPanel)
        self.date_time_frame_5.setFrameShadow(QFrame.Raised)
        self.date_label_5 = QLabel(self.date_time_frame_5)
        self.date_label_5.setObjectName(u"date_label_5")
        self.date_label_5.setGeometry(QRect(10, 0, 47, 13))
        self.date_label_5.setFont(font5)
        self.date_label_5.setStyleSheet(u"border : none;\n"
"")
        self.time_label_5 = QLabel(self.date_time_frame_5)
        self.time_label_5.setObjectName(u"time_label_5")
        self.time_label_5.setGeometry(QRect(10, 20, 47, 13))
        self.time_label_5.setFont(font5)
        self.time_label_5.setStyleSheet(u"border : none;\n"
"")
        self.clinicAppt_frame_6 = QFrame(self.upcomin_appt_frame_2)
        self.clinicAppt_frame_6.setObjectName(u"clinicAppt_frame_6")
        self.clinicAppt_frame_6.setGeometry(QRect(20, 70, 401, 81))
        self.clinicAppt_frame_6.setFrameShape(QFrame.StyledPanel)
        self.clinicAppt_frame_6.setFrameShadow(QFrame.Raised)
        self.clinic_name_label_6 = QLabel(self.clinicAppt_frame_6)
        self.clinic_name_label_6.setObjectName(u"clinic_name_label_6")
        self.clinic_name_label_6.setGeometry(QRect(90, 10, 121, 21))
        self.clinic_name_label_6.setFont(font3)
        self.clinic_name_label_6.setStyleSheet(u"border : none;\n"
"")
        self.clinic_logo_label_6 = QLabel(self.clinicAppt_frame_6)
        self.clinic_logo_label_6.setObjectName(u"clinic_logo_label_6")
        self.clinic_logo_label_6.setGeometry(QRect(10, 10, 54, 54))
        self.clinic_logo_label_6.setFont(font4)
        self.clinic_logo_label_6.setStyleSheet(u"background-color: #B6D0E2; /* Fill color */\n"
"border-radius: 25px; /* Radius to make it round */\n"
"border: 2px solid #B6D0F7; /*  Border color and thickness */\n"
"min-width: 50px; /* Ensure the QLabel is a circle */\n"
"min-height: 50px; /* Ensure the QLabel is a circle */\n"
"max-width: 50px; /* Ensure the QLabel is a circle */\n"
"max-height: 50px; /* Ensure the QLabel is a circle */")
        self.clinic_logo_label_6.setAlignment(Qt.AlignCenter)
        self.toa_label_6 = QLabel(self.clinicAppt_frame_6)
        self.toa_label_6.setObjectName(u"toa_label_6")
        self.toa_label_6.setGeometry(QRect(90, 30, 161, 21))
        self.toa_label_6.setFont(font3)
        self.toa_label_6.setStyleSheet(u"border : none;\n"
"color : #6ea0c4;\n"
"")
        self.date_time_frame_6 = QFrame(self.clinicAppt_frame_6)
        self.date_time_frame_6.setObjectName(u"date_time_frame_6")
        self.date_time_frame_6.setGeometry(QRect(280, 20, 71, 41))
        self.date_time_frame_6.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #dbe7f0;")
        self.date_time_frame_6.setFrameShape(QFrame.StyledPanel)
        self.date_time_frame_6.setFrameShadow(QFrame.Raised)
        self.date_label_6 = QLabel(self.date_time_frame_6)
        self.date_label_6.setObjectName(u"date_label_6")
        self.date_label_6.setGeometry(QRect(10, 0, 47, 13))
        self.date_label_6.setFont(font5)
        self.date_label_6.setStyleSheet(u"border : none;\n"
"")
        self.time_label_6 = QLabel(self.date_time_frame_6)
        self.time_label_6.setObjectName(u"time_label_6")
        self.time_label_6.setGeometry(QRect(10, 20, 47, 13))
        self.time_label_6.setFont(font5)
        self.time_label_6.setStyleSheet(u"border : none;\n"
"")
        self.active_pres_frame = QFrame(self.background)
        self.active_pres_frame.setObjectName(u"active_pres_frame")
        self.active_pres_frame.setGeometry(QRect(1120, 170, 481, 831))
        self.active_pres_frame.setStyleSheet(u"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;")
        self.active_pres_frame.setFrameShape(QFrame.StyledPanel)
        self.active_pres_frame.setFrameShadow(QFrame.Raised)
        self.active_pres_label = QLabel(self.active_pres_frame)
        self.active_pres_label.setObjectName(u"active_pres_label")
        self.active_pres_label.setGeometry(QRect(20, 10, 451, 41))
        self.active_pres_label.setFont(font2)
        self.active_pres_label.setStyleSheet(u"border : none;\n"
"")
        self.active_pres1_frame = QFrame(self.active_pres_frame)
        self.active_pres1_frame.setObjectName(u"active_pres1_frame")
        self.active_pres1_frame.setGeometry(QRect(0, 50, 481, 71))
        self.active_pres1_frame.setStyleSheet(u"border : none;\n"
"border-radius : 0;\n"
"background-color : #FFFFFF;")
        self.active_pres1_frame.setFrameShape(QFrame.StyledPanel)
        self.active_pres1_frame.setFrameShadow(QFrame.Raised)
        self.medicineName_label = QLabel(self.active_pres1_frame)
        self.medicineName_label.setObjectName(u"medicineName_label")
        self.medicineName_label.setGeometry(QRect(60, 10, 241, 16))
        self.medicineName_label.setFont(font2)
        self.medicine_quantity_label = QLabel(self.active_pres1_frame)
        self.medicine_quantity_label.setObjectName(u"medicine_quantity_label")
        self.medicine_quantity_label.setGeometry(QRect(60, 30, 161, 21))
        self.medicine_quantity_label.setFont(font3)
        self.medicine_quantity_label.setStyleSheet(u"border : none;\n"
"color : #6ea0c4;\n"
"")
        self.active_pres1_frame_2 = QFrame(self.active_pres_frame)
        self.active_pres1_frame_2.setObjectName(u"active_pres1_frame_2")
        self.active_pres1_frame_2.setGeometry(QRect(0, 140, 481, 71))
        self.active_pres1_frame_2.setStyleSheet(u"border : none;\n"
"border-radius : 0;\n"
"background-color : #FFFFFF;")
        self.active_pres1_frame_2.setFrameShape(QFrame.StyledPanel)
        self.active_pres1_frame_2.setFrameShadow(QFrame.Raised)
        self.medicineName_label_2 = QLabel(self.active_pres1_frame_2)
        self.medicineName_label_2.setObjectName(u"medicineName_label_2")
        self.medicineName_label_2.setGeometry(QRect(60, 10, 241, 16))
        self.medicineName_label_2.setFont(font2)
        self.medicine_quantity_label_2 = QLabel(self.active_pres1_frame_2)
        self.medicine_quantity_label_2.setObjectName(u"medicine_quantity_label_2")
        self.medicine_quantity_label_2.setGeometry(QRect(60, 30, 161, 21))
        self.medicine_quantity_label_2.setFont(font3)
        self.medicine_quantity_label_2.setStyleSheet(u"border : none;\n"
"color : #6ea0c4;\n"
"")
        self.active_pres1_frame_3 = QFrame(self.active_pres_frame)
        self.active_pres1_frame_3.setObjectName(u"active_pres1_frame_3")
        self.active_pres1_frame_3.setGeometry(QRect(0, 230, 481, 71))
        self.active_pres1_frame_3.setStyleSheet(u"border : none;\n"
"border-radius : 0;\n"
"background-color : #FFFFFF;")
        self.active_pres1_frame_3.setFrameShape(QFrame.StyledPanel)
        self.active_pres1_frame_3.setFrameShadow(QFrame.Raised)
        self.medicineName_label_3 = QLabel(self.active_pres1_frame_3)
        self.medicineName_label_3.setObjectName(u"medicineName_label_3")
        self.medicineName_label_3.setGeometry(QRect(60, 10, 241, 16))
        self.medicineName_label_3.setFont(font2)
        self.medicine_quantity_label_3 = QLabel(self.active_pres1_frame_3)
        self.medicine_quantity_label_3.setObjectName(u"medicine_quantity_label_3")
        self.medicine_quantity_label_3.setGeometry(QRect(60, 30, 161, 21))
        self.medicine_quantity_label_3.setFont(font3)
        self.medicine_quantity_label_3.setStyleSheet(u"border : none;\n"
"color : #6ea0c4;\n"
"")
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
        self.profile_btn.setGeometry(QRect(120, 25, 71, 31))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(16)
        self.profile_btn.setFont(font6)
        self.profile_btn.setStyleSheet(u"border: none")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 19, 87, 871))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_navigation = QToolButton(self.widget)
        self.home_navigation.setObjectName(u"home_navigation")
        self.home_navigation.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        self.home_navigation.setMinimumSize(QSize(85, 96))
        self.home_navigation.setMaximumSize(QSize(85, 96))
        font7 = QFont()
        font7.setFamily(u"Source Sans Pro Semibold")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.home_navigation.setFont(font7)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.home_navigation)

        self.appointments_navigation = QToolButton(self.widget)
        self.appointments_navigation.setObjectName(u"appointments_navigation")
        self.appointments_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.appointments_navigation.sizePolicy().hasHeightForWidth())
        self.appointments_navigation.setSizePolicy(sizePolicy)
        self.appointments_navigation.setFont(font7)
        self.appointments_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/appointment_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appointments_navigation.setIcon(icon2)
        self.appointments_navigation.setIconSize(QSize(70, 70))
        self.appointments_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.appointments_navigation)

        self.services_navigation = QToolButton(self.widget)
        self.services_navigation.setObjectName(u"services_navigation")
        self.services_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.services_navigation.sizePolicy().hasHeightForWidth())
        self.services_navigation.setSizePolicy(sizePolicy)
        self.services_navigation.setFont(font7)
        self.services_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.services_navigation.setIcon(icon3)
        self.services_navigation.setIconSize(QSize(70, 70))
        self.services_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.services_navigation)

        self.settings_navigation = QToolButton(self.widget)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setFont(font7)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon4)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.widget)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setFont(font7)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon5 = QIcon()
        icon5.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon5)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.num_upcoming_appt_label.setText(QCoreApplication.translate("Form", u"Number of upcoming appointments :", None))
        self.num_appt_number_label.setText(QCoreApplication.translate("Form", u"2", None))
        self.upcoming_label.setText(QCoreApplication.translate("Form", u"Upcoming", None))
        self.clinic_name_label.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label.setText(QCoreApplication.translate("Form", u"A", None))
        self.toa_label.setText(QCoreApplication.translate("Form", u"Type of Appointment", None))
        self.date_label.setText(QCoreApplication.translate("Form", u"Date", None))
        self.time_label.setText(QCoreApplication.translate("Form", u"Time", None))
        self.clinic_name_label_2.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label_2.setText(QCoreApplication.translate("Form", u"A", None))
        self.toa_label_2.setText(QCoreApplication.translate("Form", u"Type of Appointment", None))
        self.date_label_2.setText(QCoreApplication.translate("Form", u"Date", None))
        self.time_label_2.setText(QCoreApplication.translate("Form", u"Time", None))
        self.clinic_name_label_3.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label_3.setText(QCoreApplication.translate("Form", u"A", None))
        self.toa_label_3.setText(QCoreApplication.translate("Form", u"Type of Appointment", None))
        self.date_label_3.setText(QCoreApplication.translate("Form", u"Date", None))
        self.time_label_3.setText(QCoreApplication.translate("Form", u"Time", None))
        self.upcoming_label_2.setText(QCoreApplication.translate("Form", u"Past", None))
        self.clinic_name_label_4.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label_4.setText(QCoreApplication.translate("Form", u"A", None))
        self.toa_label_4.setText(QCoreApplication.translate("Form", u"Type of Appointment", None))
        self.date_label_4.setText(QCoreApplication.translate("Form", u"Date", None))
        self.time_label_4.setText(QCoreApplication.translate("Form", u"Time", None))
        self.clinic_name_label_5.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label_5.setText(QCoreApplication.translate("Form", u"A", None))
        self.toa_label_5.setText(QCoreApplication.translate("Form", u"Type of Appointment", None))
        self.date_label_5.setText(QCoreApplication.translate("Form", u"Date", None))
        self.time_label_5.setText(QCoreApplication.translate("Form", u"Time", None))
        self.clinic_name_label_6.setText(QCoreApplication.translate("Form", u"Clinic Name", None))
        self.clinic_logo_label_6.setText(QCoreApplication.translate("Form", u"A", None))
        self.toa_label_6.setText(QCoreApplication.translate("Form", u"Type of Appointment", None))
        self.date_label_6.setText(QCoreApplication.translate("Form", u"Date", None))
        self.time_label_6.setText(QCoreApplication.translate("Form", u"Time", None))
        self.active_pres_label.setText(QCoreApplication.translate("Form", u"Active Prescriptions", None))
        self.medicineName_label.setText(QCoreApplication.translate("Form", u"Medicine Name", None))
        self.medicine_quantity_label.setText(QCoreApplication.translate("Form", u"Quantity", None))
        self.medicineName_label_2.setText(QCoreApplication.translate("Form", u"Medicine Name", None))
        self.medicine_quantity_label_2.setText(QCoreApplication.translate("Form", u"Quantity", None))
        self.medicineName_label_3.setText(QCoreApplication.translate("Form", u"Medicine Name", None))
        self.medicine_quantity_label_3.setText(QCoreApplication.translate("Form", u"Quantity", None))
        self.noti_icon.setText("")
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"User", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.appointments_navigation.setText(QCoreApplication.translate("Form", u"Schedule", None))
        self.services_navigation.setText(QCoreApplication.translate("Form", u"Services", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

