from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QMessageBox

# Import custom widgets
from User.forgotpw import ForgotPwWidget
from User.forgotpw_newpw import ForgotPw_newpwWidget
from User.forgotpw_verification import ForgotPw_verificationWidget
from User.forgotpw_success import ForgotPw_successWidget
from User.ui_home import HomeWidget
from User.ui_profile_settings import ProfileSettingsWidget
from login import LoginWidget
from register import RegisterWidget
from User.ui_find_clinic import FindClinicWidget
from User.ui_view_doctor_profile import ViewDoctorProfileWidget
from User.ui_view_clinic_profile import ViewClinicProfileWidget
from User.ui_find_doctor import FindDoctorWidget
from User.ui_make_appt import MakeApptWidget
from User.ui_services import ServicesWidget
from User.ui_send_feedback import SendFeedbackWidget
from User.ui_privacy_policy import PrivacyPolicyWidget
from User.ui_privacy_register import PrivacyPolicyRegisterWidget
from User.ui_tnc import TncWidget
from User.ui_tnc_register import TncRegisterWidget
from User.change_pass_email import ChangePassEmailWidget
from User.change_pass_new import ChangePassNewWidget
from User.change_pass_verify import ChangePassVerifyWidget
from User.change_pass_success import ChangePassSuccessWidget
from User.ui_view_appt import ViewApptWidget

from Project_Admin.ui_pa_homepage import PAHomeWidget
from ui_register_clinic import RegisterClinicWidget
from Project_Admin.ui_feedback_inbox import FeedbackInboxWidget
from Project_Admin.ui_view_clinic import ViewClinicWidget
from Project_Admin.ui_edit_privacy_policy import EditPrivacyPolicyWidget
from Project_Admin.ui_edit_tnc import EditTncWidget
from Project_Admin.ui_pa_profile_settings import PAProfileSettingsWidget

from Doctor.ui_doc_profile_settings import DocProfileSettingsWidget
from Doctor.doc_patientsPage import PatientsPageWidget
from Doctor.doc_updatePrescription import UpdateRecordWidget
from Doctor.doc_homePage import Doc_HomeWidget

from Clinic_Admin.ui_ca_profile_settings import CAProfileSettingsWidget
from Clinic_Admin.ui_ca_homepage import CA_homepageWidget
from Clinic_Admin.ui_ca_patientsPage import CA_patientsPageWidget
from Clinic_Admin.ui_ca_view_doc import CA_view_docWidget
from Clinic_Admin.ui_ca_approve_reject import CA_approved_rejectWidget
from Clinic_Admin.ui_ca_add_doc import CA_add_docWidget


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #patient widgets
        self.loginWidget.forgetpassbutton.clicked.connect(self.showForgotPwWidget)
        self.loginWidget.registerbutton.clicked.connect(self.showRegisterWidget)
        self.loginWidget.login_successful.connect(self.handle_login_success)
        self.loginWidget.user_id.connect(self.set_user_id)
        self.loginWidget.apply_btn_clicked.connect(self.showRegisterClinicWidget)
        
        self.registerWidget.loginbutton.clicked.connect(self.showLoginWidget)
        self.registerWidget.registration_successful.connect(self.showLoginWidget)
        self.registerWidget.privacy_label_clicked.connect(self.showPrivacyPolicyRegisterWidget)
        self.registerWidget.tnc_label_clicked.connect(self.showTncRegisterWidget)
        
        self.registerClinicWidget.back_btn_clicked.connect(self.showLoginWidget)
        self.registerClinicWidget.red_to_login.connect(self.showLoginWidget)
        
        self.tncRegisterWidget.back_btn_clicked.connect(self.showRegisterWidget)
        self.privacyPolicyRegisterWidget.back_btn_clicked.connect(self.showRegisterWidget)
        
        self.tncWidget.back_btn_clicked.connect(self.showProfileSettingsWidget)
        self.privacyPolicyWidget.back_btn_clicked.connect(self.showProfileSettingsWidget)
 
        self.servicesWidget.fad_btn_clicked.connect(self.showFindDocWidget)
        self.servicesWidget.fac_btn_clicked.connect(self.showFindClinicWidget)
        self.servicesWidget.makeAppt_btn_clicked.connect(self.showMakeApptWidget)
        self.servicesWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.servicesWidget.profile_btn_clicked.connect(self.showProfileSettingsWidget)
        self.servicesWidget.home_btn_clicked.connect(self.showHomeWidget)
        self.servicesWidget.schedule_btn_clicked.connect(self.showViewApptWidget)
        
        self.homeWidget.service_btn_clicked.connect(self.showServicesWidget)
        self.homeWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.homeWidget.profile_btn_clicked.connect(self.showProfileSettingsWidget)
        self.homeWidget.appt_btn_clicked.connect(self.showViewApptWidget)
        
        self.findClinicWidget.service_btn_clicked.connect(self.showServicesWidget)
        self.findClinicWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.findClinicWidget.viewClinicProfileRequested.connect(self.showViewClinicProfileWidget)
        self.findClinicWidget.makeAppointmentRequested.connect(self.showPrefillMakeApptWidget)
        self.findClinicWidget.profile_btn_clicked.connect(self.showProfileSettingsWidget)
        self.findClinicWidget.home_btn_clicked.connect(self.showHomeWidget)
        self.findClinicWidget.schedule_btn_clicked.connect(self.showViewApptWidget)
        
        self.findDocWidget.service_btn_clicked.connect(self.showServicesWidget)
        self.findDocWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.findDocWidget.viewDoctorProfileRequested.connect(self.showViewDoctorProfileWidget)
        self.findDocWidget.makeAppointmentRequested.connect(self.showPrefillMakeApptWidget)
        self.findDocWidget.profile_btn_clicked.connect(self.showProfileSettingsWidget)
        self.findDocWidget.home_btn_clicked.connect(self.showHomeWidget)
        self.findDocWidget.schedule_btn_clicked.connect(self.showViewApptWidget)
        
        self.viewDoctorProfile.service_btn_clicked.connect(self.showServicesWidget)
        self.viewDoctorProfile.logout_btn_clicked.connect(self.showLogoutPopup)
        self.viewDoctorProfile.back_btn_clicked.connect(self.showFindDocWidget)
        self.viewDoctorProfile.makeAppointmentRequested.connect(self.showPrefillMakeApptWidget)
        self.viewDoctorProfile.profile_btn_clicked.connect(self.showProfileSettingsWidget)
        self.viewDoctorProfile.home_btn_clicked.connect(self.showHomeWidget)
        self.viewDoctorProfile.schedule_btn_clicked.connect(self.showViewApptWidget)
        
        self.viewClinicProfile.service_btn_clicked.connect(self.showServicesWidget)
        self.viewClinicProfile.logout_btn_clicked.connect(self.showLogoutPopup)
        self.viewClinicProfile.back_btn_clicked.connect(self.showFindClinicWidget)
        self.viewClinicProfile.makeAppointmentRequested.connect(self.showPrefillMakeApptWidget)
        self.viewClinicProfile.viewDocterRequested.connect(self.showPrefillFindDocWidget)
        self.viewClinicProfile.profile_btn_clicked.connect(self.showProfileSettingsWidget)
        self.viewClinicProfile.home_btn_clicked.connect(self.showHomeWidget)
        self.viewClinicProfile.schedule_btn_clicked.connect(self.showViewApptWidget)
        
        self.makeApptWidget.service_btn_clicked.connect(self.showServicesWidget)
        self.makeApptWidget.cancel_btn_clicked.connect(self.showServicesWidget)
        self.makeApptWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.makeApptWidget.profile_btn_clicked.connect(self.showProfileSettingsWidget)
        self.makeApptWidget.redirect_appt.connect(self.showViewApptWidget)
        self.makeApptWidget.schedule_btn_clicked.connect(self.showViewApptWidget)
        self.makeApptWidget.home_btn_clicked.connect(self.showHomeWidget)
        
        self.viewApptWidget.service_btn_clicked.connect(self.showServicesWidget)
        self.viewApptWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.viewApptWidget.profile_btn_clicked.connect(self.showProfileSettingsWidget)
        self.viewApptWidget.home_btn_clicked.connect(self.showHomeWidget)
        
        self.forgotPwWidget.continue_successful.connect(self.showForgotPw_verificationWidget)
        self.forgotPwWidget.back_successful.connect(self.showLoginWidget)       
        self.forgotPw_verificationWidget.continue_successful.connect(self.showForgotPw_newpwWidget)
        self.forgotPw_newpwWidget.update_successful.connect(self.showForgotPw_successWidget)
        self.forgotPw_successWidget.continue_btn_clicked.connect(self.showLoginWidget)
        self.forgotPwWidget.email_changed.connect(self.forgotPw_newpwWidget.set_email)
        
        self.profileSettingsWidget.feedback_btn_clicked.connect(self.showSendFeedbackWidget)
        self.profileSettingsWidget.home_btn_clicked.connect(self.showHomeWidget)
        self.profileSettingsWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.profileSettingsWidget.service_btn_clicked.connect(self.showServicesWidget)
        self.profileSettingsWidget.home_btn_clicked.connect(self.showHomeWidget)
        self.profileSettingsWidget.change_pass_btn_clicked.connect(self.showChangePassEmailWidget)
        self.profileSettingsWidget.schedule_btn_clicked.connect(self.showViewApptWidget)
        self.profileSettingsWidget.tnc_btn_clicked.connect(self.showTncWidget)
        self.profileSettingsWidget.privacy_btn_clicked.connect(self.showPrivacyPolicyWidget)
        
        self.changePassEmailWidget.back_successful.connect(self.showProfileSettingsWidget)
        self.changePassEmailWidget.continue_successful.connect(self.showChangePassVerifyWidget)
        self.changePassVerifyWidget.continue_successful.connect(self.showChangePassNew)
        self.changePassNewWidget.update_successful.connect(self.showChangePassSuccess)
        self.changePassSuccessWidget.continue_btn_clicked.connect(self.showProfileSettingsWidget)
        self.changePassEmailWidget.email_changed.connect(self.changePassNewWidget.set_email)
        
        self.sendFeedbackWidget.redirect_profile.connect(self.showProfileSettingsWidget)
        self.sendFeedbackWidget.cancel_btn_clicked.connect(self.showProfileSettingsWidget)
        self.sendFeedbackWidget.home_btn_clicked.connect(self.showHomeWidget)
        
        #project admin widgets
        self.paHomeWidget.clinic_btn_clicked.connect(self.showPAViewClinicWidget)
        self.paHomeWidget.feedback_btn_clicked.connect(self.showPAViewFeedBackInboxWidget)
        self.paHomeWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.paHomeWidget.profile_btn_clicked.connect(self.showPAProfileSettingsWidget)
        self.paHomeWidget.redirect_fb.connect(self.showPrefillPAFbWidget)
        
        self.paFeedbackInboxWidget.clinic_btn_clicked.connect(self.showPAViewClinicWidget)
        self.paFeedbackInboxWidget.home_btn_clicked.connect(self.showPAHomeWidget)
        self.paFeedbackInboxWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.paFeedbackInboxWidget.profile_btn_clicked.connect(self.showPAProfileSettingsWidget)
        
        self.paViewClinicWidget.feedback_btn_clicked.connect(self.showPAViewFeedBackInboxWidget)
        self.paViewClinicWidget.home_btn_clicked.connect(self.showPAHomeWidget)
        self.paViewClinicWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.paViewClinicWidget.profile_btn_clicked.connect(self.showPAProfileSettingsWidget)
        
        self.paProfileSettingsWidget.edit_policy_btn_clicked.connect(self.showPAEditPrivacyPolicyWidget)
        self.paProfileSettingsWidget.edit_tnc_btn_clicked.connect(self.showPAEditTncWidget)
        self.paProfileSettingsWidget.home_btn_clicked.connect(self.showPAHomeWidget)
        self.paProfileSettingsWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.paProfileSettingsWidget.clinic_btn_clicked.connect(self.showPAViewClinicWidget)
        self.paProfileSettingsWidget.feedback_btn_clicked.connect(self.showPAViewFeedBackInboxWidget)
        
        self.paEditPrivacyPolicyWidget.back_btn_clicked.connect(self.showPAProfileSettingsWidget)
        self.paEditPrivacyPolicyWidget.clinic_btn_clicked.connect(self.showPAViewClinicWidget)
        self.paEditPrivacyPolicyWidget.feedback_btn_clicked.connect(self.showPAViewFeedBackInboxWidget)
        self.paEditPrivacyPolicyWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.paEditPrivacyPolicyWidget.profile_btn_clicked.connect(self.showPAProfileSettingsWidget)
        
        self.paEditTncWidget.back_btn_clicked.connect(self.showPAProfileSettingsWidget)
        self.paEditTncWidget.clinic_btn_clicked.connect(self.showPAViewClinicWidget)
        self.paEditTncWidget.feedback_btn_clicked.connect(self.showPAViewFeedBackInboxWidget)
        self.paEditTncWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.paEditTncWidget.profile_btn_clicked.connect(self.showPAProfileSettingsWidget)

        # doctor signals connections
        self.docHomeWidget.home_btn_clicked.connect(self.showDocHomeWidget)
        self.docHomeWidget.patients_btn_clicked.connect(self.showDocPatientsWidget)
        self.docHomeWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.docHomeWidget.profile_btn_clicked.connect(self.showDocProfileSettingsWidget)

        self.docPatientsWidget.home_btn_clicked.connect(self.showDocHomeWidget)
        self.docPatientsWidget.patients_btn_clicked.connect(self.showDocPatientsWidget)
        self.docPatientsWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.docPatientsWidget.profile_btn_clicked.connect(self.showDocProfileSettingsWidget)
        self.docPatientsWidget.add_record_btn_click.connect(self.showDocUpdateRecordWidget)
        self.docPatientsWidget.patient_id_signal.connect(self.pass_pID_updateRecordWidget)

        self.docUpdateRecordWidget.home_btn_clicked.connect(self.showDocHomeWidget)
        self.docUpdateRecordWidget.patients_btn_clicked.connect(self.showDocPatientsWidget)
        self.docUpdateRecordWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.docUpdateRecordWidget.profile_btn_clicked.connect(self.showDocProfileSettingsWidget)
        self.docUpdateRecordWidget.redirect_doc_patients_page.connect(self.showDocPatientsWidget)
        
        self.docProfileSettingsWidget.home_btn_clicked.connect(self.showDocHomeWidget)
        self.docProfileSettingsWidget.patients_btn_clicked.connect(self.showDocPatientsWidget)
        self.docProfileSettingsWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.docProfileSettingsWidget.profile_btn_clicked.connect(self.showDocProfileSettingsWidget)
        
         #clinic admin widgets
        self.caHomeWidget.view_detail_btn_clicked.connect(self.showCAPatientsPageWidget)
        self.caHomeWidget.doctors_navigation_btn_clicked.connect(self.showCAViewDocWidget)
        self.caHomeWidget.settings_navigation_btn_clicked.connect(self.showCAProfileSettingsWidget)
        self.caHomeWidget.patients_navigation_btn_clicked.connect(self.showCAPatientsPageWidget)
        self.caHomeWidget.profile_btn_clicked.connect(self.showCAProfileSettingsWidget)
        self.caHomeWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.caHomeWidget.redirect_doc.connect(self.showPrefillCADocWidget)

        self.caViewDocWidget.home_navigation_btn_clicked.connect(self.showCAHomeWidget)
        self.caViewDocWidget.settings_navigation_btn_clicked.connect(self.showCAProfileSettingsWidget)
        self.caViewDocWidget.patients_navigation_btn_clicked.connect(self.showCAPatientsPageWidget)
        self.caViewDocWidget.profile_btn_clicked.connect(self.showCAProfileSettingsWidget)
        self.caViewDocWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.caViewDocWidget.add_doc_navigation_btn_clicked.connect(self.showCAAddDocWidget)

        self.caAddDocWidget.home_navigation_btn_clicked.connect(self.showCAHomeWidget)
        self.caAddDocWidget.doctors_navigation_btn_clicked.connect(self.showCAViewDocWidget)
        self.caAddDocWidget.settings_navigation_btn_clicked.connect(self.showCAProfileSettingsWidget)
        self.caAddDocWidget.patients_navigation_btn_clicked.connect(self.showCAPatientsPageWidget)
        self.caAddDocWidget.profile_btn_clicked.connect(self.showCAProfileSettingsWidget)
        self.caAddDocWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.caAddDocWidget.back_btn_clicked.connect(self.showCAViewDocWidget)
        self.caAddDocWidget.redirect_doc.connect(self.showCAViewDocWidget)
        
        self.caPatientsPageWidget.home_navigation_btn_clicked.connect(self.showCAHomeWidget)
        self.caPatientsPageWidget.doctors_navigation_btn_clicked.connect(self.showCAViewDocWidget)
        self.caPatientsPageWidget.settings_navigation_btn_clicked.connect(self.showCAProfileSettingsWidget)
        self.caPatientsPageWidget.profile_btn_clicked.connect(self.showCAProfileSettingsWidget)
        self.caPatientsPageWidget.logout_btn_clicked.connect(self.showLogoutPopup)
    
        self.caApproveRejectWidget.home_navigation_btn_clicked.connect(self.showCAHomeWidget)
        self.caApproveRejectWidget.doctors_navigation_btn_clicked.connect(self.showCAViewDocWidget)
        self.caApproveRejectWidget.patients_navigation_btn_clicked.connect(self.showCAPatientsPageWidget)
        self.caApproveRejectWidget.settings_navigation_btn_clicked.connect(self.showProfileSettingsWidget)
        self.caApproveRejectWidget.profile_btn_clicked.connect(self.showCAProfileSettingsWidget)
        self.caApproveRejectWidget.logout_btn_clicked.connect(self.showLogoutPopup)

        self.caProfileSettingsWidget.home_navigation_btn_clicked.connect(self.showCAHomeWidget)
        self.caProfileSettingsWidget.doctors_navigation_btn_clicked.connect(self.showCAViewDocWidget)
        self.caProfileSettingsWidget.patients_navigation_btn_clicked.connect(self.showCAPatientsPageWidget)
        self.caProfileSettingsWidget.settings_navigation_btn_clicked.connect(self.showCAProfileSettingsWidget)
        self.caProfileSettingsWidget.logout_btn_clicked.connect(self.showLogoutPopup)

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
        self.forgotPwWidget = ForgotPwWidget(self.centralwidget)
        self.forgotPw_verificationWidget = ForgotPw_verificationWidget()
        self.forgotPw_newpwWidget = ForgotPw_newpwWidget()
        self.forgotPw_successWidget = ForgotPw_successWidget()
        self.registerWidget = RegisterWidget()
        self.homeWidget = HomeWidget()
        self.findClinicWidget = FindClinicWidget()
        self.findDocWidget = FindDoctorWidget()
        self.makeApptWidget = MakeApptWidget()
        self.servicesWidget = ServicesWidget()
        self.viewDoctorProfile = ViewDoctorProfileWidget()
        self.viewClinicProfile = ViewClinicProfileWidget()
        self.profileSettingsWidget = ProfileSettingsWidget()
        self.sendFeedbackWidget = SendFeedbackWidget()
        self.privacyPolicyWidget = PrivacyPolicyWidget()
        self.privacyPolicyRegisterWidget = PrivacyPolicyRegisterWidget()
        self.tncWidget = TncWidget()
        self.tncRegisterWidget = TncRegisterWidget()
        self.changePassEmailWidget = ChangePassEmailWidget()
        self.changePassVerifyWidget = ChangePassVerifyWidget()
        self.changePassNewWidget = ChangePassNewWidget()
        self.changePassSuccessWidget = ChangePassSuccessWidget()
        self.viewApptWidget = ViewApptWidget()
        
        self.paHomeWidget = PAHomeWidget()
        self.registerClinicWidget = RegisterClinicWidget()
        self.paFeedbackInboxWidget = FeedbackInboxWidget()
        self.paViewClinicWidget = ViewClinicWidget()
        self.paEditPrivacyPolicyWidget = EditPrivacyPolicyWidget()
        self.paEditTncWidget = EditTncWidget()
        self.paProfileSettingsWidget = PAProfileSettingsWidget()

        self.caHomeWidget = CA_homepageWidget()
        self.caPatientsPageWidget = CA_patientsPageWidget()
        self.caApproveRejectWidget = CA_approved_rejectWidget()
        self.caViewDocWidget = CA_view_docWidget()
        self.caAddDocWidget = CA_add_docWidget()
        self.caProfileSettingsWidget = CAProfileSettingsWidget()

        # Doctor widgets
        self.docProfileSettingsWidget = DocProfileSettingsWidget()
        self.docPatientsWidget = PatientsPageWidget()
        self.docUpdateRecordWidget = UpdateRecordWidget()
        self.docHomeWidget = Doc_HomeWidget()
        
        
        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.addWidget(self.forgotPwWidget)
        self.stackedWidget.addWidget(self.forgotPw_newpwWidget)
        self.stackedWidget.addWidget(self.forgotPw_verificationWidget)
        self.stackedWidget.addWidget(self.forgotPw_successWidget)
        self.stackedWidget.addWidget(self.registerWidget)
        self.stackedWidget.addWidget(self.homeWidget)
        self.stackedWidget.addWidget(self.servicesWidget)
        self.stackedWidget.addWidget(self.findClinicWidget)
        self.stackedWidget.addWidget(self.findDocWidget)
        self.stackedWidget.addWidget(self.makeApptWidget)
        self.stackedWidget.addWidget(self.viewDoctorProfile)
        self.stackedWidget.addWidget(self.profileSettingsWidget)
        self.stackedWidget.addWidget(self.viewClinicProfile)
        self.stackedWidget.addWidget(self.paHomeWidget)
        self.stackedWidget.addWidget(self.paFeedbackInboxWidget)
        self.stackedWidget.addWidget(self.paViewClinicWidget)
        self.stackedWidget.addWidget(self.registerClinicWidget)
        self.stackedWidget.addWidget(self.sendFeedbackWidget)
        self.stackedWidget.addWidget(self.privacyPolicyWidget)
        self.stackedWidget.addWidget(self.privacyPolicyRegisterWidget)
        self.stackedWidget.addWidget(self.tncWidget)
        self.stackedWidget.addWidget(self.tncRegisterWidget)
        self.stackedWidget.addWidget(self.paEditPrivacyPolicyWidget)
        self.stackedWidget.addWidget(self.paEditTncWidget)
        self.stackedWidget.addWidget(self.paProfileSettingsWidget)
        self.stackedWidget.addWidget(self.docProfileSettingsWidget)
        self.stackedWidget.addWidget(self.caProfileSettingsWidget)
        self.stackedWidget.addWidget(self.caHomeWidget)
        self.stackedWidget.addWidget(self.caPatientsPageWidget)
        self.stackedWidget.addWidget(self.caApproveRejectWidget)
        self.stackedWidget.addWidget(self.caViewDocWidget)     
        self.stackedWidget.addWidget(self.caAddDocWidget)   
        self.stackedWidget.addWidget(self.changePassEmailWidget)  
        self.stackedWidget.addWidget(self.changePassNewWidget)  
        self.stackedWidget.addWidget(self.changePassSuccessWidget)  
        self.stackedWidget.addWidget(self.changePassVerifyWidget)  
        self.stackedWidget.addWidget(self.viewApptWidget)
        
        self.stackedWidget.addWidget(self.docPatientsWidget) 
        self.stackedWidget.addWidget(self.docUpdateRecordWidget) 
        self.stackedWidget.addWidget(self.docProfileSettingsWidget)
        self.stackedWidget.addWidget(self.docHomeWidget)


        self.stackedWidget.setCurrentWidget(self.loginWidget)
        

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow"))
        
        
    def handle_login_success(self, rights):

        if rights == 0:
            self.showHomeWidget()
        elif rights == 1: 
            self.showDocHomeWidget()
        elif rights == 2:
            self.showCAHomeWidget() # uncomment when update to show home widget for ca
            pass
        elif rights == 4:
            self.showPAHomeWidget()
            
    @pyqtSlot()
    def showViewApptWidget(self):
        self.stackedWidget.setCurrentWidget(self.viewApptWidget)
        self.viewApptWidget.fetch_appt_data()
        
    @pyqtSlot()
    def showForgotPwWidget(self):
        self.stackedWidget.setCurrentWidget(self.forgotPwWidget)
    
    
    @pyqtSlot()
    def showForgotPw_verificationWidget(self):
        self.stackedWidget.setCurrentWidget(self.forgotPw_verificationWidget)
        

    @pyqtSlot()
    def showForgotPw_newpwWidget(self):
        self.stackedWidget.setCurrentWidget(self.forgotPw_newpwWidget)

    @pyqtSlot()
    def showForgotPw_successWidget(self):
        self.stackedWidget.setCurrentWidget(self.forgotPw_successWidget)

    @pyqtSlot()
    def showRegisterWidget(self):
        self.stackedWidget.setCurrentWidget(self.registerWidget)
        
    @pyqtSlot()
    def showLoginWidget(self):
        self.loginWidget.ic_input.clear()
        self.loginWidget.password_input.clear()
        self.stackedWidget.setCurrentWidget(self.loginWidget)
        
    @pyqtSlot()
    def showPrivacyPolicyWidget(self):
        self.stackedWidget.setCurrentWidget(self.privacyPolicyWidget)
        
    @pyqtSlot()
    def showTncWidget(self):
        self.stackedWidget.setCurrentWidget(self.tncWidget)
        
    @pyqtSlot()
    def showPrivacyPolicyRegisterWidget(self):
        self.stackedWidget.setCurrentWidget(self.privacyPolicyRegisterWidget)
        self.privacyPolicyRegisterWidget.load_policy_from_db()
        
    @pyqtSlot()
    def showTncRegisterWidget(self):
        self.stackedWidget.setCurrentWidget(self.tncRegisterWidget)
        self.tncRegisterWidget.load_terms_from_db()

    @pyqtSlot()
    def showHomeWidget(self):
        self.stackedWidget.setCurrentWidget(self.homeWidget)
        
    @pyqtSlot()
    def showFindDocWidget(self):
        self.stackedWidget.setCurrentWidget(self.findDocWidget)
        self.findDocWidget.fetch_clinic_data()
    
    @pyqtSlot()
    def showNewPassword(self):
        self.stackedWidget.setCurrentWidget(self.forgotPw_newpwWidget)
        
    @pyqtSlot()
    def showChangePassEmailWidget(self):
        self.stackedWidget.setCurrentWidget(self.changePassEmailWidget)
        
    @pyqtSlot()
    def showChangePassVerifyWidget(self):
        self.stackedWidget.setCurrentWidget(self.changePassVerifyWidget)
        
    @pyqtSlot()
    def showChangePassNew(self):
        self.stackedWidget.setCurrentWidget(self.changePassNewWidget)
        
    @pyqtSlot()
    def showChangePassSuccess(self):
        self.stackedWidget.setCurrentWidget(self.changePassSuccessWidget)
                
    @pyqtSlot()
    def showFindClinicWidget(self):
        self.stackedWidget.setCurrentWidget(self.findClinicWidget)
        self.findClinicWidget.fetch_clinic_data()
        
    @pyqtSlot()
    def showMakeApptWidget(self):
        self.stackedWidget.setCurrentWidget(self.makeApptWidget)
        self.makeApptWidget.fetch_clinic_data()
        
        
    def showPrefillMakeApptWidget(self, clinic_name, doctor_name):
        self.stackedWidget.setCurrentWidget(self.makeApptWidget)
        self.makeApptWidget.prefill_appointment_form(clinic_name, doctor_name)
        
    def showPrefillFindDocWidget(self, clinic_name):
        self.stackedWidget.setCurrentWidget(self.findDocWidget)
        self.findDocWidget.prefill_clinic(clinic_name)
        
        
    @pyqtSlot()
    def showServicesWidget(self):
        self.stackedWidget.setCurrentWidget(self.servicesWidget)
        
    @pyqtSlot()
    def showPAViewClinicWidget(self):
        self.stackedWidget.setCurrentWidget(self.paViewClinicWidget)
        self.paViewClinicWidget.fetch_clinic_data()
        
    @pyqtSlot()
    def showPAViewFeedBackInboxWidget(self):
        self.stackedWidget.setCurrentWidget(self.paFeedbackInboxWidget)
        self.paFeedbackInboxWidget.fetch_fb_data()
        
    @pyqtSlot()
    def showPAHomeWidget(self):
        self.stackedWidget.setCurrentWidget(self.paHomeWidget)
        self.paHomeWidget.fetch_clinic_data()
        self.paHomeWidget.fetch_fb_data()
        self.paHomeWidget.calc_new_addition()
        
    @pyqtSlot()
    def showPAProfileSettingsWidget(self):
        self.stackedWidget.setCurrentWidget(self.paProfileSettingsWidget)
        self.paProfileSettingsWidget.set_default_texts()
        self.paProfileSettingsWidget.fetch_admin_data()
        
    @pyqtSlot()
    def showRegisterClinicWidget(self):
        self.stackedWidget.setCurrentWidget(self.registerClinicWidget)
        
    @pyqtSlot()
    def showProfileSettingsWidget(self):
        self.stackedWidget.setCurrentWidget(self.profileSettingsWidget)
        self.profileSettingsWidget.set_default_texts()
        self.profileSettingsWidget.fetch_patient_data()
        
    @pyqtSlot()
    def showSendFeedbackWidget(self):
        self.stackedWidget.setCurrentWidget(self.sendFeedbackWidget)
        self.sendFeedbackWidget.fetch_patient_data()
        
    @pyqtSlot()
    def showPAEditPrivacyPolicyWidget(self):
        self.stackedWidget.setCurrentWidget(self.paEditPrivacyPolicyWidget)
        self.paEditPrivacyPolicyWidget.set_default_text()
        
    @pyqtSlot()
    def showPAEditTncWidget(self):
        self.stackedWidget.setCurrentWidget(self.paEditTncWidget)
        self.paEditTncWidget.set_default_text()
        
    def showViewClinicProfileWidget(self, clinic_name, temp):
        #print(f"clinic name is {clinic_name} temp is {temp}")
        self.stackedWidget.setCurrentWidget(self.viewClinicProfile)
        self.viewClinicProfile.display_clinic_profile(clinic_name, temp)
        self.viewClinicProfile.fetch_clinic_info_from_db(clinic_name)
        
    def showPrefillPAFbWidget(self, fb_data):
        self.stackedWidget.setCurrentWidget(self.paFeedbackInboxWidget)
        self.paFeedbackInboxWidget.create_popup_widget(fb_data)
    
    #test   
    def showPrefillCADocWidget(self, doc_data):
        self.stackedWidget.setCurrentWidget(self.caViewDocWidget)
        self.caViewDocWidget.create_popup_widget(doc_data)

    def showViewDoctorProfileWidget(self, doc_id, clinic_name):
        self.stackedWidget.setCurrentWidget(self.viewDoctorProfile)
        self.viewDoctorProfile.display_doctor_profile(doc_id, clinic_name)
        self.viewDoctorProfile.fetch_doctor_info_from_db(doc_id, clinic_name)


    # Doctor widgets
    @pyqtSlot()
    def showDocPatientsWidget(self):
        self.docPatientsWidget.get_patient_data()
        self.docPatientsWidget.clear_patient_details()
        self.stackedWidget.setCurrentWidget(self.docPatientsWidget)

    @pyqtSlot()
    def showDocHomeWidget(self):
        self.stackedWidget.setCurrentWidget(self.docHomeWidget)
    
    @pyqtSlot()
    def showDocUpdateRecordWidget(self):
        self.stackedWidget.setCurrentWidget(self.docUpdateRecordWidget)

    @pyqtSlot()
    def showDocProfileSettingsWidget(self):
        self.stackedWidget.setCurrentWidget(self.docProfileSettingsWidget)


    def pass_pID_updateRecordWidget(self, patient_id):
        self.docUpdateRecordWidget.set_patient_id(patient_id)



    # clinic admin widgets
    @pyqtSlot()
    def showCAHomeWidget(self):
        self.stackedWidget.setCurrentWidget(self.caHomeWidget)
        self.caHomeWidget.fetch_patient_data()
        #self.caHomeWidget.admins_data()
        
    @pyqtSlot()
    def showCAPatientsPageWidget(self):
        self.stackedWidget.setCurrentWidget(self.caPatientsPageWidget)
        self.caPatientsPageWidget.fetch_patient_data()
        
    @pyqtSlot()
    def showCAAddDocWidget(self):
        self.stackedWidget.setCurrentWidget(self.caAddDocWidget)
        
    @pyqtSlot()
    def showCAApproveRejectWidget(self):
        self.stackedWidget.setCurrentWidget(self.caApproveRejectWidget)
        
    @pyqtSlot()
    def showCAViewDocWidget(self):
        self.stackedWidget.setCurrentWidget(self.caViewDocWidget)
        self.caViewDocWidget.fetch_doc_data()
        
    @pyqtSlot()
    def showCAProfileSettingsWidget(self):
        self.stackedWidget.setCurrentWidget(self.caProfileSettingsWidget)


    def set_user_id(self, user_id):  
        
        try:
            if user_id.isdigit(): 
                self.homeWidget.set_user_id(user_id)
                self.makeApptWidget.set_user_id(user_id)
                self.profileSettingsWidget.set_user_id(user_id)
                self.sendFeedbackWidget.set_user_id(user_id)
                self.paProfileSettingsWidget.set_user_id(user_id)
                self.viewApptWidget.set_user_id(user_id)
                
            else :  # doctor user id is a string
                self.docPatientsWidget.set_user_id(user_id)
                self.docHomeWidget.set_user_id(user_id)
                self.docProfileSettingsWidget.set_user_id(user_id)
                self.caHomeWidget.set_user_id(user_id)
                self.caProfileSettingsWidget.set_user_id(user_id)
                self.caAddDocWidget.set_user_id(user_id)
                self.caPatientsPageWidget.set_user_id(user_id)
                self.caViewDocWidget.set_user_id(user_id)

        except Exception as e:
            print(f"Error setting user id in widgets: {e}")
        
        
    def showLogoutPopup(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Logout")
        msg_box.setText("Are you sure you want to logout?")
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        reply = msg_box.exec_()  # Show the message box and get the button clicked

        # Handle the response immediately
        if reply == QMessageBox.Ok:
            self.showLoginWidget()  # Call the showLoginWidget method
        elif reply == QMessageBox.Cancel:
            msg_box.close()

        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWin = Ui_MainWindow()
    mainWin.showMaximized()
    sys.exit(app.exec_())
