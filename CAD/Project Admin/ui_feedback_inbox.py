from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *



class FeedbackInboxWidget(QWidget):
    clinic_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
        
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
        self.profile_btn.setGeometry(QRect(120, 25, 71, 31))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(16)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet(u"border: none")
        self.feedback_label = QLabel(self.background)
        self.feedback_label.setObjectName(u"feedback_label")
        self.feedback_label.setGeometry(QRect(40, 170, 961, 61))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(22)
        self.feedback_label.setFont(font1)
        self.feedback_label.setWordWrap(True)
        self.lineEdit = QLineEdit(self.background)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 50, 831, 71))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(11)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 60px; color: Black;\n"
" background-image: url(\"C:/Users/Samantha Law/Documents/INTI/CAD/CallADoctor/CAD/Images/icon/search_icon.png\"); \n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"border: 1px solid gray;\n"
"")
        self.lineEdit.setClearButtonEnabled(False)
        self.fb_outer_frame = QFrame(self.background)
        self.fb_outer_frame.setObjectName(u"fb_outer_frame")
        self.fb_outer_frame.setGeometry(QRect(40, 260, 1681, 81))
        self.fb_outer_frame.setMinimumSize(QSize(0, 62))
        self.fb_outer_frame.setMaximumSize(QSize(16777215, 16777215))
        self.fb_outer_frame.setStyleSheet(u"background-color: #f0f0f0;  border: 1px solid #dcdcdc; border-radius: 8px; margin: 5px;")
        self.fb_outer_frame.setFrameShape(QFrame.StyledPanel)
        self.fb_outer_frame.setFrameShadow(QFrame.Raised)
        self.fb_outer_frame.setLineWidth(0)
        self.fb_inner_frame = QFrame(self.fb_outer_frame)
        self.fb_inner_frame.setObjectName(u"fb_inner_frame")
        self.fb_inner_frame.setGeometry(QRect(0, 0, 1681, 81))
        self.fb_inner_frame.setMinimumSize(QSize(0, 62))
        self.fb_inner_frame.setMaximumSize(QSize(16777215, 16777215))
        self.fb_inner_frame.setStyleSheet(u"border: none;")
        self.fb_inner_frame.setFrameShape(QFrame.StyledPanel)
        self.fb_inner_frame.setFrameShadow(QFrame.Raised)
        self.fb_inner_frame.setLineWidth(0)
        self.widget = QWidget(self.fb_inner_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 10, 1631, 57))
        self.feedback_info_layout = QHBoxLayout(self.widget)
        self.feedback_info_layout.setSpacing(0)
        self.feedback_info_layout.setObjectName(u"feedback_info_layout")
        self.feedback_info_layout.setContentsMargins(0, 0, 0, 0)
        self.name = QLabel(self.widget)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(421, 0))
        self.name.setMaximumSize(QSize(421, 16777215))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(12)
        self.name.setFont(font3)
        self.name.setStyleSheet(u"border:none;")

        self.feedback_info_layout.addWidget(self.name)

        self.subject = QLabel(self.widget)
        self.subject.setObjectName(u"subject")
        self.subject.setMinimumSize(QSize(871, 0))
        self.subject.setMaximumSize(QSize(871, 16777215))
        self.subject.setFont(font3)
        self.subject.setStyleSheet(u"border:none;")

        self.feedback_info_layout.addWidget(self.subject)

        self.date = QLabel(self.widget)
        self.date.setObjectName(u"date")
        self.date.setMinimumSize(QSize(131, 0))
        self.date.setMaximumSize(QSize(131, 16777215))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(10)
        self.date.setFont(font4)
        self.date.setStyleSheet(u"border:none;")

        self.feedback_info_layout.addWidget(self.date)

        self.time = QLabel(self.widget)
        self.time.setObjectName(u"time")
        self.time.setMinimumSize(QSize(131, 0))
        self.time.setMaximumSize(QSize(131, 16777215))
        self.time.setFont(font4)
        self.time.setStyleSheet(u"border:none;")

        self.feedback_info_layout.addWidget(self.time)

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
        font5 = QFont()
        font5.setFamily(u"Source Sans Pro Semibold")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.home_navigation.setFont(font5)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon1)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.home_navigation.clicked.connect(self.emitHomeBtn)
        self.verticalLayout.addWidget(self.home_navigation)

        self.clinic_navigation = QToolButton(self.layoutWidget_2)
        self.clinic_navigation.setObjectName(u"clinic_navigation")
        self.clinic_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.clinic_navigation.sizePolicy().hasHeightForWidth())
        self.clinic_navigation.setSizePolicy(sizePolicy)
        self.clinic_navigation.setMinimumSize(QSize(85, 96))
        self.clinic_navigation.setMaximumSize(QSize(85, 96))
        self.clinic_navigation.setFont(font5)
        self.clinic_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clinic_navigation.setIcon(icon2)
        self.clinic_navigation.setIconSize(QSize(70, 70))
        self.clinic_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.clinic_navigation.clicked.connect(self.emitClinicBtn)
        self.verticalLayout.addWidget(self.clinic_navigation)

        self.feedback_navigation = QToolButton(self.layoutWidget_2)
        self.feedback_navigation.setObjectName(u"feedback_navigation")
        self.feedback_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.feedback_navigation.sizePolicy().hasHeightForWidth())
        self.feedback_navigation.setSizePolicy(sizePolicy)
        self.feedback_navigation.setMinimumSize(QSize(85, 96))
        self.feedback_navigation.setMaximumSize(QSize(85, 96))
        self.feedback_navigation.setFont(font5)
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
        self.settings_navigation.setFont(font5)
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
        self.logout_navigation.setFont(font5)
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
        self.feedback_label.setText(QCoreApplication.translate("Form", u"Feedbacks Inbox", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.name.setText(QCoreApplication.translate("Form", u"Name", None))
        self.subject.setText(QCoreApplication.translate("Form", u"Subject: ", None))
        self.date.setText(QCoreApplication.translate("Form", u"Date", None))
        self.time.setText(QCoreApplication.translate("Form", u"Time", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.clinic_navigation.setText(QCoreApplication.translate("Form", u"Clinics", None))
        self.feedback_navigation.setText(QCoreApplication.translate("Form", u"Feedback", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi
    
    @pyqtSlot()
    def emitClinicBtn(self):
        self.clinic_btn_clicked.emit()
        
    @pyqtSlot()
    def emitHomeBtn(self):
        self.home_btn_clicked.emit()
        
    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()

