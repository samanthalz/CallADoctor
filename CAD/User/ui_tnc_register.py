from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db

class TncRegisterWidget(QWidget):
    
    back_btn_clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        self.whitebg = QWidget(Form)
        self.whitebg.setObjectName(u"whitebg")
        self.whitebg.setGeometry(QRect(0, 0, 1921, 1080))
        self.whitebg.setStyleSheet(u"background-color: #F8F8F8;")
        self.tnc_label = QLabel(self.whitebg)
        self.tnc_label.setObjectName(u"tnc_label")
        self.tnc_label.setGeometry(QRect(60, 120, 481, 81))
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
        self.textBrowser = QTextBrowser(self.whitebg)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(65, 221, 1790, 800))
        self.textBrowser.setMaximumSize(QSize(1790, 800))
        self.textBrowser.setStyleSheet(u"border-radius: 0px; border: 1px solid #808080")
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(14)
        self.textBrowser.setFont(font2)
        self.load_terms_from_db()
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tnc_label.setText(QCoreApplication.translate("Form", u"Terms & Conditions", None))
        self.back_button.setText(QCoreApplication.translate("Form", u"< Back", None))
    # retranslateUi
    
    @pyqtSlot()
    def emitBackBtn(self):
        self.back_btn_clicked.emit()
        
    def load_terms_from_db(self):
        db = self.initialize_db()
        try:
            terms = db.child('terms').get().val()
            if terms:
                self.textBrowser.setText(terms)
            else:
                self.textBrowser.setText("No terms found in the database.")
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while fetching terms: {e}")

    def initialize_db(self):
        return db 
 