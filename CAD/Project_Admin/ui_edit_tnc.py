from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,QMouseEvent,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class EditTncWidget(QWidget):
    home_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    back_btn_clicked = pyqtSignal()
        
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
        
        self.whitebg = QWidget(Form)
        self.whitebg.setObjectName(u"whitebg")
        self.whitebg.setGeometry(QRect(150, 0, 1771, 1080))
        self.whitebg.setStyleSheet(u"background-color: #F8F8F8;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-left-radius: 30px;")
        self.tnc_label = QLabel(self.whitebg)
        self.tnc_label.setObjectName(u"tnc_label")
        self.tnc_label.setGeometry(QRect(60, 120, 901, 81))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.tnc_label.setFont(font)
        self.back_button = QPushButton(self.whitebg)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setEnabled(True)
        self.back_button.setGeometry(QRect(60, 40, 181, 61))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.back_button.setFont(font1)
        self.back_button.setAutoFillBackground(False)
        self.back_button.setStyleSheet(u"background-color: rgba(182, 208, 226,0.8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.back_button.setIconSize(QSize(70, 70))
        self.back_button.clicked.connect(self.emitBackBtn)
        
        self.textEdit = QTextEdit(self.whitebg)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(65, 221, 1661, 800))
        self.textEdit.setMaximumSize(QSize(16777215, 800))
        self.textEdit.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")
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
        font2 = QFont()
        font2.setFamily(u"Source Sans Pro Semibold")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.home_navigation.setFont(font2)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon = QIcon()
        icon.addFile(u"../Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.home_navigation)

        self.clinic_navigation = QToolButton(self.layoutWidget_2)
        self.clinic_navigation.setObjectName(u"clinic_navigation")
        self.clinic_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.clinic_navigation.sizePolicy().hasHeightForWidth())
        self.clinic_navigation.setSizePolicy(sizePolicy)
        self.clinic_navigation.setMinimumSize(QSize(85, 96))
        self.clinic_navigation.setMaximumSize(QSize(85, 96))
        self.clinic_navigation.setFont(font2)
        self.clinic_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"../Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clinic_navigation.setIcon(icon1)
        self.clinic_navigation.setIconSize(QSize(70, 70))
        self.clinic_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.clinic_navigation)

        self.feedback_navigation = QToolButton(self.layoutWidget_2)
        self.feedback_navigation.setObjectName(u"feedback_navigation")
        self.feedback_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.feedback_navigation.sizePolicy().hasHeightForWidth())
        self.feedback_navigation.setSizePolicy(sizePolicy)
        self.feedback_navigation.setMinimumSize(QSize(85, 96))
        self.feedback_navigation.setMaximumSize(QSize(85, 96))
        self.feedback_navigation.setFont(font2)
        self.feedback_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"../Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.feedback_navigation.setIcon(icon2)
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
        self.settings_navigation.setFont(font2)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"../Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon3)
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
        self.logout_navigation.setFont(font2)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"../Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon4)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tnc_label.setText(QCoreApplication.translate("Form", u"Edit Terms & Conditions", None))
        self.back_button.setText(QCoreApplication.translate("Form", u"< Back", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.clinic_navigation.setText(QCoreApplication.translate("Form", u"Clinics", None))
        self.feedback_navigation.setText(QCoreApplication.translate("Form", u"Feedback", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi
    
    
    @pyqtSlot()
    def emitBackBtn(self):
        self.back_btn_clicked.emit()
        
        
