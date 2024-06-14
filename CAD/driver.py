from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget

# Import your custom widgets
from User.forgotpw import ForgotPwWidget
from User.home_page_ui import HomeWidget
from login import LoginWidget
from register import RegisterWidget

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loginWidget.forgetpassbutton.clicked.connect(self.showForgotPwWidget)
        self.loginWidget.registerbutton.clicked.connect(self.showRegisterWidget)
        self.loginWidget.login_successful.connect(self.showHomeWidget)

        
        self.registerWidget.loginbutton.clicked.connect(self.showLoginWidget)
        self.registerWidget.registration_successful.connect(self.showLoginWidget)
        
        #this
        self.servicesWidget.fad_btn_clicked.connect(self.showFindDocWidget)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1920, 1080))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1920, 1080))
        self.stackedWidget.setMinimumSize(QSize(1920, 1080))
        MainWindow.setCentralWidget(self.centralwidget)

        self.loginWidget = LoginWidget()
        self.forgotPwWidget = ForgotPwWidget()
        self.registerWidget = RegisterWidget()
        self.homeWidget = HomeWidget()
         

        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.addWidget(self.forgotPwWidget)
        self.stackedWidget.addWidget(self.registerWidget)
        self.stackedWidget.addWidget(self.homeWidget)
        
        self.stackedWidget.setCurrentWidget(self.loginWidget)
        

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow"))
        
        
    @pyqtSlot()
    def showForgotPwWidget(self):
        self.stackedWidget.setCurrentWidget(self.forgotPwWidget)
        
    @pyqtSlot()
    def showRegisterWidget(self):
        self.stackedWidget.setCurrentWidget(self.registerWidget)
        
    @pyqtSlot()
    def showLoginWidget(self):
        self.stackedWidget.setCurrentWidget(self.loginWidget)

    @pyqtSlot()
    def showHomeWidget(self):
        self.stackedWidget.setCurrentWidget(self.homeWidget)
    
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWin = Ui_MainWindow()
    mainWin.showMaximized()
    sys.exit(app.exec_())
