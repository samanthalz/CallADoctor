from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from connection import db


class CAProfileSettingsWidget(QWidget):
    home_navigation_btn_clicked = pyqtSignal()
    doctors_navigation_btn_clicked = pyqtSignal()
    patients_navigation_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    settings_navigation_btn_clicked = pyqtSignal()
    change_pass_btn_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ca_id = 0
        self.setupUi(self)

    def set_user_id(self, ca_id):
        self.ca_id = ca_id
        # print(f"ca id is {self.ca_id}")
        self.get_user_credentials(self.ca_id)

    def get_user_credentials(self, ca_id):
        ca_name = ""  # default
        clinic_admin = db.child("clinic_admin").get().val()
        
        # Debug: Print the fetched clinic_admin data
        #print("Clinic Admin Data:", clinic_admin)
        
        if clinic_admin is not None:
            for i, ca_info in clinic_admin.items():
                if ca_info.get('firebase_uid') == ca_id:
                    ca_name = ca_info.get('ca_id')
                    break
        
        self.user_id_display.setText(ca_name)


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
        self.profile_btn.setGeometry(QRect(100, 25, 131, 31))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(10)
        self.profile_btn.setFont(font1)
        self.profile_btn.setStyleSheet(u"border: none")
        
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

        self.user_id = QLabel(self.layoutWidget)
        self.user_id.setObjectName(u"user_id")
        self.user_id.setMaximumSize(QSize(514, 23))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(12)
        self.user_id.setFont(font2)

        self.name_layout.addWidget(self.user_id)

        self.user_id_display = QLabel(self.layoutWidget)
        self.user_id_display.setObjectName(u"user_id_display")
        self.user_id_display.setMinimumSize(QSize(514, 40))
        self.user_id_display.setMaximumSize(QSize(514, 40))
        self.user_id_display.setFont(font1)
        self.user_id_display.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")

        self.name_layout.addWidget(self.user_id_display)


        self.verticalLayout_2.addLayout(self.name_layout)

        # ============================
        #   RIGHT SIDE - UPDATE PASSWORD BUTTON
        # ============================
        self.layoutWidget_3 = QWidget(self.whitebg)
        self.layoutWidget_3.setGeometry(QRect(1130, 270, 548, 211))

        self.btn_layout = QVBoxLayout(self.layoutWidget_3)
        self.btn_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_layout.setSpacing(50)

        # UPDATE PASSWORD BUTTON
        self.update_password_btn = QPushButton(self.layoutWidget_3)
        self.update_password_btn.setMinimumSize(QSize(546, 0))
        self.update_password_btn.setFont(QFont("Consolas", 14))
        self.update_password_btn.setStyleSheet(
            "border-radius: 10; background-color: transparent; color: black"
        )
        self.update_password_btn.setText("Update Password                     >")
        self.update_password_btn.clicked.connect(self.emitChangePassBtn)

        self.btn_layout.addWidget(self.update_password_btn)


        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 90, 87, 851))
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
        font3 = QFont()
        font3.setFamily(u"Source Sans Pro Semibold")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.home_navigation.setFont(font3)
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
        self.doctors_navigation.setFont(font3)
        self.doctors_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.doctors_navigation.setIcon(icon1)
        self.doctors_navigation.setIconSize(QSize(70, 70))
        self.doctors_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.doctors_navigation.clicked.connect(self.emitDoctorsBtn)

        self.verticalLayout.addWidget(self.doctors_navigation)

        self.patients_navigation_2 = QToolButton(self.layoutWidget_2)
        self.patients_navigation_2.setObjectName(u"patients_navigation_2")
        self.patients_navigation_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.patients_navigation_2.sizePolicy().hasHeightForWidth())
        self.patients_navigation_2.setSizePolicy(sizePolicy)
        self.patients_navigation_2.setMinimumSize(QSize(85, 96))
        self.patients_navigation_2.setMaximumSize(QSize(85, 96))
        self.patients_navigation_2.setFont(font3)
        self.patients_navigation_2.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patients_navigation_2.setIcon(icon2)
        self.patients_navigation_2.setIconSize(QSize(70, 70))
        self.patients_navigation_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        self.patients_navigation_2.clicked.connect(self.emitPatientsBtn)

        self.verticalLayout.addWidget(self.patients_navigation_2)

        self.settings_navigation = QToolButton(self.layoutWidget_2)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setMinimumSize(QSize(85, 96))
        self.settings_navigation.setMaximumSize(QSize(85, 96))
        self.settings_navigation.setFont(font3)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon3)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.settings_navigation)

        
        self.settings_navigation.clicked.connect(self.emitSettingsBtn)

        self.logout_navigation = QToolButton(self.layoutWidget_2)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setMinimumSize(QSize(85, 96))
        self.logout_navigation.setMaximumSize(QSize(85, 96))
        self.logout_navigation.setFont(font3)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        
        
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)

        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon4)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.settings_label.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Clinic", None))
        self.profile_icon_2.setText("")
        self.user_id.setText(QCoreApplication.translate("Form", u"User ID", None))
        
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.doctors_navigation.setText(QCoreApplication.translate("Form", u"Doctors", None))
        self.patients_navigation_2.setText(QCoreApplication.translate("Form", u"Patients", None))
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
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
    
    @pyqtSlot()
    def emitSettingsBtn(self):
        # Emit the custom signal
        self.settings_navigation_btn_clicked.emit()

    @pyqtSlot()
    def emitPatientsBtn(self):
        self.patients_navigation_btn_clicked.emit()  

    @pyqtSlot()
    def emitChangePassBtn(self):
        # Emit the custom signal
        self.change_pass_btn_clicked.emit()


# # # If run directly from this page
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = CAProfileSettingsWidget()
    ui.setupUi(Form)
    ui.set_user_id("ABCClinic")
    Form.show()
    sys.exit(app.exec_())