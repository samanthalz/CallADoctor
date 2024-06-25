from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class CA_add_docWidget(QWidget):
    home_navigation_btn_clicked = pyqtSignal()
    doctors_navigation_btn_clicked = pyqtSignal()
    patients_navigation_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    settings_navigation_btn_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        Form.setStyleSheet(u"background-color: \"#B6D0E2\" ")
        self.background = QWidget(Form)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(150, 0, 1771, 1061))
        self.background.setStyleSheet(u"background-color: #F8F8F8;\\nborder-bottom-left-radius: 30px;\\nborder-top-left-radius: 30px;\\ntext-align: center;")
        self.doc_label = QLabel(self.background)
        self.doc_label.setObjectName(u"doc_label")
        self.doc_label.setGeometry(QRect(40, 40, 961, 61))
        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(22)
        self.doc_label.setFont(font)
        self.doc_label.setWordWrap(True)
        self.doc_img = QLabel(self.background)
        self.doc_img.setObjectName(u"doc_img")
        self.doc_img.setGeometry(QRect(120, 180, 200, 200))
        self.doc_img.setStyleSheet(u"border-radius: 100px; \n"
"background-color: #B6D0E2;  \n"
"color: white; \n"
"font-size: 16px;\n"
"text-align: center;")
        self.upload_img_btn = QPushButton(self.background)
        self.upload_img_btn.setObjectName(u"upload_img_btn")
        self.upload_img_btn.setGeometry(QRect(70, 420, 301, 51))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.upload_img_btn.setFont(font1)
        self.upload_img_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.add_btn = QPushButton(self.background)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(1400, 970, 301, 51))
        self.add_btn.setFont(font1)
        self.add_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.layoutWidget = QWidget(self.background)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(540, 202, 1181, 751))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_layout = QVBoxLayout()
        self.name_layout.setSpacing(10)
        self.name_layout.setObjectName(u"name_layout")
        self.name = QLabel(self.layoutWidget)
        self.name.setObjectName(u"name")
        self.name.setMaximumSize(QSize(16777215, 23))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(12)
        self.name.setFont(font2)

        self.name_layout.addWidget(self.name)

        self.name_input = QLineEdit(self.layoutWidget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMinimumSize(QSize(500, 40))
        self.name_input.setMaximumSize(QSize(16777215, 40))
        self.name_input.setBaseSize(QSize(0, 0))
        self.name_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.name_layout.addWidget(self.name_input)


        self.horizontalLayout.addLayout(self.name_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.services_layout = QVBoxLayout()
        self.services_layout.setSpacing(10)
        self.services_layout.setObjectName(u"services_layout")
        self.specialization_label = QLabel(self.layoutWidget)
        self.specialization_label.setObjectName(u"specialization_label")
        self.specialization_label.setMaximumSize(QSize(16777215, 23))
        self.specialization_label.setFont(font2)

        self.services_layout.addWidget(self.specialization_label)

        self.services_input = QLineEdit(self.layoutWidget)
        self.services_input.setObjectName(u"services_input")
        self.services_input.setMinimumSize(QSize(500, 40))
        self.services_input.setMaximumSize(QSize(16777215, 40))
        self.services_input.setBaseSize(QSize(0, 0))
        self.services_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.services_layout.addWidget(self.services_input)


        self.horizontalLayout_2.addLayout(self.services_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.add_layout = QVBoxLayout()
        self.add_layout.setSpacing(10)
        self.add_layout.setObjectName(u"add_layout")
        self.address_label = QLabel(self.layoutWidget)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMinimumSize(QSize(0, 23))
        self.address_label.setMaximumSize(QSize(16777215, 23))
        self.address_label.setFont(font2)

        self.add_layout.addWidget(self.address_label)

        self.address_input = QLineEdit(self.layoutWidget)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setMinimumSize(QSize(500, 140))
        self.address_input.setMaximumSize(QSize(16777215, 140))
        self.address_input.setBaseSize(QSize(0, 0))
        self.address_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-position: left center; \n"
"border: 1px solid gray;\n"
"border-radius: 0px; \n"
"")

        self.add_layout.addWidget(self.address_input)


        self.horizontalLayout_5.addLayout(self.add_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.phone_layout = QVBoxLayout()
        self.phone_layout.setSpacing(10)
        self.phone_layout.setObjectName(u"phone_layout")
        self.phone_label = QLabel(self.layoutWidget)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setMaximumSize(QSize(16777215, 23))
        self.phone_label.setFont(font2)

        self.phone_layout.addWidget(self.phone_label)

        self.phone_input = QLineEdit(self.layoutWidget)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setMinimumSize(QSize(500, 40))
        self.phone_input.setMaximumSize(QSize(16777215, 40))
        self.phone_input.setBaseSize(QSize(0, 0))
        self.phone_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.phone_layout.addWidget(self.phone_input)


        self.horizontalLayout_3.addLayout(self.phone_layout)

        self.email_layout = QVBoxLayout()
        self.email_layout.setSpacing(10)
        self.email_layout.setObjectName(u"email_layout")
        self.email_label = QLabel(self.layoutWidget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setMaximumSize(QSize(16777215, 23))
        self.email_label.setFont(font2)

        self.email_layout.addWidget(self.email_label)

        self.email_input = QLineEdit(self.layoutWidget)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setMinimumSize(QSize(500, 40))
        self.email_input.setMaximumSize(QSize(16777215, 40))
        self.email_input.setBaseSize(QSize(0, 0))
        self.email_input.setStyleSheet(u" padding: 60px; color: Black;\n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"background-size: 20px 20px; \n"
"border: 1px solid gray;\n"
"")

        self.email_layout.addWidget(self.email_input)


        self.horizontalLayout_3.addLayout(self.email_layout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.back_btn = QPushButton(self.background)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(1060, 970, 301, 51))
        self.back_btn.setFont(font1)
        self.back_btn.setStyleSheet(u"background-color: #B6D0E2; border-radius: 16px; padding: 60px; color: white;\\n border: 1px solid gray;")
        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 120, 87, 851))
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

        self.patients_navigation = QToolButton(self.layoutWidget_2)
        self.patients_navigation.setObjectName(u"patients_navigation")
        self.patients_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.patients_navigation.sizePolicy().hasHeightForWidth())
        self.patients_navigation.setSizePolicy(sizePolicy)
        self.patients_navigation.setMinimumSize(QSize(85, 96))
        self.patients_navigation.setMaximumSize(QSize(85, 96))
        self.patients_navigation.setFont(font3)
        self.patients_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patients_navigation.setIcon(icon2)
        self.patients_navigation.setIconSize(QSize(70, 70))
        self.patients_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.patients_navigation.clicked.connect(self.emitPatientsBtn)

        self.verticalLayout.addWidget(self.patients_navigation)

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

        self.settings_navigation.clicked.connect(self.emitSettingsBtn)

        self.verticalLayout.addWidget(self.settings_navigation)

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
        self.doc_label.setText(QCoreApplication.translate("Form", u"Add Doctor", None))
        self.doc_img.setText("")
        self.upload_img_btn.setText(QCoreApplication.translate("Form", u"Upload Image", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.name.setText(QCoreApplication.translate("Form", u"Doctor Name", None))
        self.specialization_label.setText(QCoreApplication.translate("Form", u"Specialization", None))
        self.address_label.setText(QCoreApplication.translate("Form", u"Address", None))
        self.phone_label.setText(QCoreApplication.translate("Form", u"Phone number", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"Email address", None))
        self.back_btn.setText(QCoreApplication.translate("Form", u"Back", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.doctors_navigation.setText(QCoreApplication.translate("Form", u"Doctors", None))
        self.patients_navigation.setText(QCoreApplication.translate("Form", u"Patients", None))
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




