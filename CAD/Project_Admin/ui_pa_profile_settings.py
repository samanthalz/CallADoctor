from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class PAProfileSettingsWidget(QWidget):
    feedback_btn_clicked = pyqtSignal()
    clinic_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    edit_policy_btn_clicked = pyqtSignal()
    edit_tnc_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
        
    def __init__(self, parent=None):
        super().__init__(parent)
        self.admin_id = 0
        self.setupUi(self)
        
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
        self.whitebg.setStyleSheet(u"background-color: #F8F8F8;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-left-radius: 30px;")
        self.settings_label = QLabel(self.whitebg)
        self.settings_label.setObjectName(u"settings_label")
        self.settings_label.setGeometry(QRect(60, 40, 481, 81))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.settings_label.setFont(font)
        self.updateFrame = QFrame(self.whitebg)
        self.updateFrame.setObjectName(u"updateFrame")
        self.updateFrame.setGeometry(QRect(180, 160, 741, 461))
        self.layoutWidget = QWidget(self.updateFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 41, 518, 391))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.name_layout = QVBoxLayout()
        self.name_layout.setSpacing(10)
        self.name_layout.setObjectName(u"name_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(175, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.profile_icon_2 = QLabel(self.layoutWidget)
        self.profile_icon_2.setObjectName(u"profile_icon_2")
        self.profile_icon_2.setMinimumSize(QSize(150, 150))
        self.profile_icon_2.setMaximumSize(QSize(150, 150))
        self.profile_icon_2.setStyleSheet(u"border: none")
        self.profile_icon_2.setPixmap(QPixmap(u"CAD/Images/icon/profile_icon.png"))
        self.profile_icon_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.profile_icon_2)

        self.horizontalSpacer_2 = QSpacerItem(175, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.name_layout.addLayout(self.horizontalLayout)

        self.user_id_label = QLabel(self.layoutWidget)
        self.user_id_label.setObjectName(u"user_id_label")
        self.user_id_label.setMaximumSize(QSize(514, 23))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(12)
        self.user_id_label.setFont(font1)

        self.name_layout.addWidget(self.user_id_label)

        self.user_id_display = QLabel(self.layoutWidget)
        self.user_id_display.setObjectName(u"user_id_display")
        self.user_id_display.setMinimumSize(QSize(514, 40))
        self.user_id_display.setMaximumSize(QSize(514, 40))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(10)
        self.user_id_display.setFont(font2)
        self.user_id_display.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")

        self.name_layout.addWidget(self.user_id_display)


        self.verticalLayout_2.addLayout(self.name_layout)

        self.pass_layout = QVBoxLayout()
        self.pass_layout.setObjectName(u"pass_layout")
        self.pas = QLabel(self.layoutWidget)
        self.pas.setObjectName(u"pas")
        self.pas.setMaximumSize(QSize(514, 23))
        self.pas.setFont(font1)

        self.pass_layout.addWidget(self.pas)

        self.pass_display = QLabel(self.layoutWidget)
        self.pass_display.setObjectName(u"pass_display")
        self.pass_display.setMinimumSize(QSize(514, 40))
        self.pass_display.setMaximumSize(QSize(514, 40))
        self.pass_display.setFont(font2)
        self.pass_display.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")

        self.pass_layout.addWidget(self.pass_display)


        self.verticalLayout_2.addLayout(self.pass_layout)

        self.layoutWidget_2 = QWidget(self.whitebg)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(1130, 270, 548, 211))
        self.btn_layout = QVBoxLayout(self.layoutWidget_2)
        self.btn_layout.setSpacing(50)
        self.btn_layout.setObjectName(u"btn_layout")
        self.btn_layout.setContentsMargins(0, 0, 0, 0)
        self.edit_policy_btn = QPushButton(self.layoutWidget_2)
        self.edit_policy_btn.setObjectName(u"edit_policy_btn")
        self.edit_policy_btn.setMinimumSize(QSize(546, 0))
        self.edit_policy_btn.setMaximumSize(QSize(546, 16777215))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(14)
        self.edit_policy_btn.setFont(font3)
        self.edit_policy_btn.setStyleSheet(u"border-radius: 10; background-color: transparent; color: black")
        self.edit_policy_btn.clicked.connect(self.emitEditPolicy)
        
        self.btn_layout.addWidget(self.edit_policy_btn)

        self.edit_tnc_btn = QPushButton(self.layoutWidget_2)
        self.edit_tnc_btn.setObjectName(u"edit_tnc_btn")
        self.edit_tnc_btn.setMinimumSize(QSize(546, 0))
        self.edit_tnc_btn.setMaximumSize(QSize(546, 16777215))
        self.edit_tnc_btn.setFont(font3)
        self.edit_tnc_btn.setStyleSheet(u"border-radius: 10; background-color: transparent; color: black")
        self.edit_tnc_btn.clicked.connect(self.emitEditTnc)
        
        self.btn_layout.addWidget(self.edit_tnc_btn)

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
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(16)
        self.profile_btn.setFont(font4)
        self.profile_btn.setStyleSheet(u"border: none")
        self.profile_btn.clicked.connect(self.emitSettingsBtn)
        
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.frame)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(31, 20, 87, 851))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_navigation = QToolButton(self.layoutWidget_3)
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
        icon = QIcon()
        icon.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.home_navigation.clicked.connect(self.emitHomeBtn)
        self.verticalLayout.addWidget(self.home_navigation)

        self.clinic_navigation = QToolButton(self.layoutWidget_3)
        self.clinic_navigation.setObjectName(u"clinic_navigation")
        self.clinic_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.clinic_navigation.sizePolicy().hasHeightForWidth())
        self.clinic_navigation.setSizePolicy(sizePolicy)
        self.clinic_navigation.setMinimumSize(QSize(85, 96))
        self.clinic_navigation.setMaximumSize(QSize(85, 96))
        self.clinic_navigation.setFont(font5)
        self.clinic_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clinic_navigation.setIcon(icon1)
        self.clinic_navigation.setIconSize(QSize(70, 70))
        self.clinic_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.clinic_navigation.clicked.connect(self.emitClinicBtn)
        self.verticalLayout.addWidget(self.clinic_navigation)

        self.feedback_navigation = QToolButton(self.layoutWidget_3)
        self.feedback_navigation.setObjectName(u"feedback_navigation")
        self.feedback_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.feedback_navigation.sizePolicy().hasHeightForWidth())
        self.feedback_navigation.setSizePolicy(sizePolicy)
        self.feedback_navigation.setMinimumSize(QSize(85, 96))
        self.feedback_navigation.setMaximumSize(QSize(85, 96))
        self.feedback_navigation.setFont(font5)
        self.feedback_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.feedback_navigation.setIcon(icon2)
        self.feedback_navigation.setIconSize(QSize(70, 70))
        self.feedback_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.feedback_navigation.clicked.connect(self.emitFeedbackBtn)
        self.verticalLayout.addWidget(self.feedback_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget_3)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setMinimumSize(QSize(85, 96))
        self.settings_navigation.setMaximumSize(QSize(85, 96))
        self.settings_navigation.setFont(font5)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon3)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settings_navigation.clicked.connect(self.emitSettingsBtn)
        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget_3)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setMinimumSize(QSize(85, 96))
        self.logout_navigation.setMaximumSize(QSize(85, 96))
        self.logout_navigation.setFont(font5)
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
        self.settings_label.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.profile_icon_2.setText("")
        self.user_id_label.setText(QCoreApplication.translate("Form", u"User ID", None))
        self.user_id_display.setText("")
        self.pas.setText(QCoreApplication.translate("Form", u"Password", None))
        self.pass_display.setText("")
        self.edit_policy_btn.setText(QCoreApplication.translate("Form", u"Edit Privacy policy                  >", None))
        self.edit_tnc_btn.setText(QCoreApplication.translate("Form", u"Edit Terms and Conditions            >", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Admin", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.clinic_navigation.setText(QCoreApplication.translate("Form", u"Clinics", None))
        self.feedback_navigation.setText(QCoreApplication.translate("Form", u"Feedback", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi
    
    
    @pyqtSlot()
    def emitEditPolicy(self):
        # Emit the custom signal
        self.edit_policy_btn_clicked.emit()
        
    @pyqtSlot()
    def emitEditTnc(self):
        # Emit the custom signal
        self.edit_tnc_btn_clicked.emit()
        
    @pyqtSlot()
    def emitHomeBtn(self):
        # Emit the custom signal
        self.home_btn_clicked.emit()
        
    @pyqtSlot()
    def emitClinicBtn(self):
        self.clinic_btn_clicked.emit()
        
    @pyqtSlot()
    def emitFeedbackBtn(self):
        self.feedback_btn_clicked.emit()
        
    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
        
    @pyqtSlot()
    def emitSettingsBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()

    def set_user_id(self, user_id):
        try:
                if user_id is not None:
                        self.admin_id = user_id
                        #print(f"set user id is {self.admin_id}")
                else:
                        print("Error: Invalid user_id (None)")
        except Exception as e:
                print(f"Error setting user id: {e}")
        
    def fetch_admin_data(self):
        db = self.initialize_db()
        try:
                admin_data = db.child("project_admin").child(self.admin_id).get().val()
                if admin_data:
                        return admin_data
                else:
                        raise ValueError("No admin data found for the given ID.")
        except Exception as e:
                print(f"An error occurred while fetching patient data: {e}")
                return None
        
    def set_default_texts(self):
        db = self.initialize_db()
        #print(f"id is {self.admin_id}")
        if self.admin_id:
            admin_data = self.fetch_admin_data()
            
            if admin_data:
                self.user_id_display.setText(admin_data.get("pa_id", ""))
                self.pass_display.setText(admin_data.get("pa_pass", ""))
        else:
                print("error")
         
    def initialize_db(self):
        return db       