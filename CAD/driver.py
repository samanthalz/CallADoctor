from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget

# Import your custom widgets
from User.forgotpw import ForgotPwWidget
from User.forgotpw_newpw import ForgotPw_newpwWidget
from User.forgotpw_verification import ForgotPw_verificationWidget
from User.ui_home import HomeWidget
from login import LoginWidget
from register import RegisterWidget
from User.ui_find_clinic import FindClinicWidget
from User.ui_find_clinic_copy import ViewClinicWidget
from User.ui_view_doctor_profile import ViewDoctorProfileWidget
from User.ui_view_clinic_profile import ViewClinicProfileWidget
from User.ui_find_doctor import FindDoctorWidget
from User.ui_make_appt import MakeApptWidget
from User.ui_services import ServicesWidget
from Project_Admin.ui_pa_homepage import PAHomeWidget
from Project_Admin.ui_add_clinic import AddClinicWidget
from Project_Admin.ui_feedback_inbox import FeedbackInboxWidget
#from Project_Admin.ui_view_clinic import ViewClinicWidget
from Project_Admin.ui_view_feedback import ViewFeedbackWidget

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loginWidget.forgetpassbutton.clicked.connect(self.showForgotPwWidget)
        self.loginWidget.registerbutton.clicked.connect(self.showRegisterWidget)
        self.loginWidget.login_successful.connect(self.handle_login_success)
        self.loginWidget.user_id.connect(self.set_user_id)

        
        self.registerWidget.loginbutton.clicked.connect(self.showLoginWidget)
        self.registerWidget.registration_successful.connect(self.showLoginWidget)
 
        self.servicesWidget.fad_btn_clicked.connect(self.showFindDocWidget)
        self.servicesWidget.fac_btn_clicked.connect(self.showFindClinicWidget)
        self.servicesWidget.makeAppt_btn_clicked.connect(self.showMakeApptWidget)
        
        self.homeWidget.service_btn_clicked.connect(self.showServicesWidget)
        
        self.findClinicWidget.service_btn_clicked.connect(self.showServicesWidget)
        
        self.findDocWidget.service_btn_clicked.connect(self.showServicesWidget)
        
        self.makeApptWidget.service_btn_clicked.connect(self.showServicesWidget)

        self.forgotPw_verificationWidget.continue_successful.connect(self.showNewPassword)
        
        self.paHomeWidget.clinic_btn_clicked.connect(self.showPAViewClinicWidget)
        self.paHomeWidget.feedback_btn_clicked.connect(self.showPAViewFeedBackInboxWidget)
        
        self.paFeedbackInboxWidget.clinic_btn_clicked.connect(self.showPAViewClinicWidget)
        self.paFeedbackInboxWidget.home_btn_clicked.connect(self.showPAHomeWidget)
        
        self.paViewClinicWidget.feedback_btn_clicked.connect(self.showPAViewFeedBackInboxWidget)
        self.paViewClinicWidget.home_btn_clicked.connect(self.showPAHomeWidget)
        

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
        self.forgotPw_verificationWidget = ForgotPw_verificationWidget()
        self.forgotPw_newpwWidget = ForgotPw_newpwWidget()
        self.registerWidget = RegisterWidget()
        self.homeWidget = HomeWidget()
        self.findClinicWidget = FindClinicWidget()
        self.findDocWidget = FindDoctorWidget()
        self.makeApptWidget = MakeApptWidget()
        self.servicesWidget = ServicesWidget()
        self.paHomeWidget = PAHomeWidget()
        self.paAddClinicWidget = AddClinicWidget()
        self.paFeedbackInboxWidget = FeedbackInboxWidget()
        self.paViewClinicWidget = ViewClinicWidget()
        self.paViewFeedbackWidget = ViewFeedbackWidget()
         

        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.addWidget(self.forgotPwWidget)
        self.stackedWidget.addWidget(self.forgotPw_newpwWidget)
        self.stackedWidget.addWidget(self.forgotPw_verificationWidget)
        self.stackedWidget.addWidget(self.registerWidget)
        self.stackedWidget.addWidget(self.homeWidget)
        self.stackedWidget.addWidget(self.servicesWidget)
        self.stackedWidget.addWidget(self.findClinicWidget)
        self.stackedWidget.addWidget(self.findDocWidget)
        self.stackedWidget.addWidget(self.makeApptWidget)
        self.stackedWidget.addWidget(self.paHomeWidget)
        self.stackedWidget.addWidget(self.paViewClinicWidget)
        self.stackedWidget.addWidget(self.paFeedbackInboxWidget)
        self.stackedWidget.addWidget(self.paViewClinicWidget)
        self.stackedWidget.addWidget(self.paViewFeedbackWidget)
        
        self.stackedWidget.setCurrentWidget(self.loginWidget)
        

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow"))
        
        
    def handle_login_success(self, rights):
        if rights == 0:
            self.stackedWidget.setCurrentWidget(self.homeWidget)
        elif rights == 4:
            self.stackedWidget.setCurrentWidget(self.paHomeWidget)
            
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
        
    @pyqtSlot()
    def showFindDocWidget(self):
        self.stackedWidget.setCurrentWidget(self.findDocWidget)
    
    @pyqtSlot()
    def showNewPassword(self):
        self.stackedWidget.setCurrentWidget(self.forgotPw_newpwWidget)
        
    @pyqtSlot()
    def showFindClinicWidget(self):
        self.stackedWidget.setCurrentWidget(self.findClinicWidget)
        
    @pyqtSlot()
    def showMakeApptWidget(self):
        self.stackedWidget.setCurrentWidget(self.makeApptWidget)
        
    @pyqtSlot()
    def showServicesWidget(self):
        self.stackedWidget.setCurrentWidget(self.servicesWidget)
        
    @pyqtSlot()
    def showPAViewClinicWidget(self):
        self.stackedWidget.setCurrentWidget(self.paViewClinicWidget)
        
    @pyqtSlot()
    def showPAViewFeedBackInboxWidget(self):
        self.stackedWidget.setCurrentWidget(self.paFeedbackInboxWidget)
        
    @pyqtSlot()
    def showPAHomeWidget(self):
        self.stackedWidget.setCurrentWidget(self.paHomeWidget)

    
    def set_user_id(self, user_id):  
        self.homeWidget.set_user_id(user_id)

        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWin = Ui_MainWindow()
    mainWin.showMaximized()
    sys.exit(app.exec_())