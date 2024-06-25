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


class DocProfileSettingsWidget(QWidget):
    patients_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    
        
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user_id = 0
        self.setupUi(self)

    def set_user_id(self, user_id): 
        self.user_id = user_id
        self.get_user_credentials(self.user_id)

    def get_user_credentials(self, user_id):
        doctors = db.child("doctors").get.val()
        for i, doctor_info in doctors.items():
            if int(doctor_info.get("doctor_id")) == int(user_id):
                    doctor_name = doctor_info.get('doctor_name')
                    password = doctor_info.get('password')
                    break
            
        if doctor_name: 
            self.user_id_display.setText(doctor_name)
        if password : 
            self.pass_display.setText(password)
        
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
        font1.setPointSize(16)
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
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        self.user_id_display.setFont(font3)
        self.user_id_display.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")

        self.name_layout.addWidget(self.user_id_display)


        self.verticalLayout_2.addLayout(self.name_layout)

        self.pass_layout = QVBoxLayout()
        self.pass_layout.setObjectName(u"pass_layout")
        self.pas = QLabel(self.layoutWidget)
        self.pas.setObjectName(u"pas")
        self.pas.setMaximumSize(QSize(514, 23))
        self.pas.setFont(font2)

        self.pass_layout.addWidget(self.pas)

        self.pass_display = QLabel(self.layoutWidget)
        self.pass_display.setObjectName(u"pass_display")
        self.pass_display.setMinimumSize(QSize(514, 40))
        self.pass_display.setMaximumSize(QSize(514, 40))
        self.pass_display.setFont(font3)
        self.pass_display.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")

        self.pass_layout.addWidget(self.pass_display)


        self.verticalLayout_2.addLayout(self.pass_layout)



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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.settings_label.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Doctor", None))
        self.profile_icon_2.setText("")
        self.user_id.setText(QCoreApplication.translate("Form", u"User ID", None))
        self.user_id_display.setText("")
        self.pas.setText(QCoreApplication.translate("Form", u"Password", None))
        self.pass_display.setText("")

        self.home_navigation.setText(QCoreApplication.translate("Form", "   Home   "))
        self.patients_navigation.setText(QCoreApplication.translate("Form", "Patients"))
        self.settings_navigation.setText(QCoreApplication.translate("Form", "Settings"))
        self.logout_navigation.setText(QCoreApplication.translate("Form", "Logout"))
    # retranslateUi

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


# # # If run directly from this page
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = DocProfileSettingsWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
