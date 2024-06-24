from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db


class CAProfileSettingsWidget(QWidget):
    logout_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    
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
        self.profile_icon.setPixmap(QPixmap(u"../Images/icon/profile_icon.png"))
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
        self.profile_icon_2.setPixmap(QPixmap(u"../Images/icon/profile_icon.png"))
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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.settings_label.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Admin", None))
        self.profile_icon_2.setText("")
        self.user_id.setText(QCoreApplication.translate("Form", u"User ID", None))
        self.user_id_display.setText("")
        self.pas.setText(QCoreApplication.translate("Form", u"Password", None))
        self.pass_display.setText("")
    # retranslateUi

