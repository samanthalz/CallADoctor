from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, pyqtSlot, QDateTime, QTimer, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QMessageBox
from connection import db
from datetime import datetime
import uuid

from User.ui_home import HomeWidget
from User.ui_profile_settings import ProfileSettingsWidget
from login import LoginWidget
from register import RegisterWidget
from forgotpw import ForgotPwWidget
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
from security.session import Session
from User.ui_privacy_consent_dialog import PrivacyConsentDialog  
# add import
from security.audit_logger import log_event

RIGHTS_TO_ROLE = {
    0: "patient",
    1: "doctor",
    2: "clinic_admin",
    4: "super_admin"
}


class SessionManager(QObject):
    """Manages user session state and authentication"""

    session_expired = pyqtSignal()
    active_sessions = {}  

    def __init__(self):
        super().__init__()
        self.current_user_id = None
        self.current_user_rights = None
        self.is_authenticated = False
        self.login_time = None
        self.session_timeout = 30 * 60 * 1000  # 30 minutes in milliseconds
        self.session_timer = QTimer()
        self.session_timer.timeout.connect(self._on_session_timeout)

    def start_session(self, user_id, rights):
        """Start a new user session, preventing multiple sessions"""
        # Check DB if user is already logged in
        active_session = db.child("active_sessions").child(user_id).get().val()
        if active_session:
            print(f"[INFO] Login attempt blocked: user {user_id} already has an active session.")
            
            QMessageBox.warning(
                None,
                "Already Logged In",
                "This account is already logged in on another device.\nPlease log out first."
            )
            # Do NOT start session or timer
            self.is_authenticated = False
            return False

        # No active session → start new session
        self.current_user_id = user_id
        self.current_user_rights = rights
        self.is_authenticated = True
        self.login_time = QDateTime.currentDateTime()
        self.session_id = str(uuid.uuid4())
        self.session_timer.start(self.session_timeout)

        # Update DB
        db.child("active_sessions").child(user_id).update({
            "session_id": self.session_id,
            "last_active": datetime.now().timestamp()
        })
        print(f"[INFO] Session started for user {user_id}")
        return True


    def end_session(self):
        """End current user session"""
        if self.current_user_id:
            try:
                db.child("active_sessions").child(self.current_user_id).remove()
            except Exception as e:
                print(f"[ERROR] Failed to remove session from DB: {e}")

        self.current_user_id = None
        self.current_user_rights = None
        self.is_authenticated = False
        self.login_time = None
        self.session_timer.stop()


    def extend_session(self):
        """Extend the session timeout"""
        if self.is_authenticated:
            self.session_timer.start(self.session_timeout)

    def _on_session_timeout(self):
        # Only end session if it's actually authenticated
        if not self.is_authenticated or not self.current_user_id:
            return

        print(f"[INFO] Session timeout for user {self.current_user_id}")
        self.end_session()
        self.session_expired.emit()


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.session_manager = SessionManager()
        self.session_manager.session_expired.connect(self.handle_session_expired) 
        self.previous_widget = None
        self.current_widget = None
        self.setupUi(self)
        self.setupConnections()
        
    def setupConnections(self):
        # Patient widgets connections
        self.loginWidget.forgetpassbutton.clicked.connect(self.showForgotPwWidget)
        self.loginWidget.registerbutton.clicked.connect(self.showRegisterWidget)
        self.loginWidget.login_successful.connect(self.handle_login_success)
        #self.loginWidget.user_id.connect(self.set_user_id)
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
        
        self.forgotPwWidget.continue_successful.connect(self.showLoginWidget)
        self.forgotPwWidget.back_successful.connect(self.handleBackFromForgotPw)       
        
        self.profileSettingsWidget.feedback_btn_clicked.connect(self.showSendFeedbackWidget)
        self.profileSettingsWidget.home_btn_clicked.connect(self.showHomeWidget)
        self.profileSettingsWidget.logout_btn_clicked.connect(self.showLogoutPopup)
        self.profileSettingsWidget.service_btn_clicked.connect(self.showServicesWidget)
        self.profileSettingsWidget.home_btn_clicked.connect(self.showHomeWidget)
        self.profileSettingsWidget.change_pass_btn_clicked.connect(self.showForgotPwWidget)
        self.profileSettingsWidget.schedule_btn_clicked.connect(self.showViewApptWidget)
        self.profileSettingsWidget.tnc_btn_clicked.connect(self.showTncWidget)
        self.profileSettingsWidget.privacy_btn_clicked.connect(self.showPrivacyPolicyWidget)
        
        
        self.sendFeedbackWidget.redirect_profile.connect(self.showProfileSettingsWidget)
        self.sendFeedbackWidget.cancel_btn_clicked.connect(self.showProfileSettingsWidget)
        self.sendFeedbackWidget.home_btn_clicked.connect(self.showHomeWidget)
        
        # Project admin widgets
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

        # Doctor signals connections
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
        self.docProfileSettingsWidget.change_pass_btn_clicked.connect(self.showForgotPwWidget)
        
        # Clinic admin widgets
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
        self.caProfileSettingsWidget.change_pass_btn_clicked.connect(self.showForgotPwWidget)

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

        # Initialize all widgets 
        self.loginWidget = LoginWidget()
        self.forgotPwWidget = ForgotPwWidget(self.centralwidget)
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
        
        # Add all widgets to stacked widget 
        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.addWidget(self.forgotPwWidget)
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
        self.stackedWidget.addWidget(self.viewApptWidget)
        
        self.stackedWidget.addWidget(self.docPatientsWidget) 
        self.stackedWidget.addWidget(self.docUpdateRecordWidget) 

        self.stackedWidget.addWidget(self.docHomeWidget)

        self.stackedWidget.setCurrentWidget(self.loginWidget)
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow"))
        
    def handle_login_success(self, rights, user_id):
        """Handle successful login with rights and user_id"""
        if rights is not None and user_id is not None:
            session_started = self.session_manager.start_session(user_id, rights)
            if not session_started:
                # User is already logged in 
                return

            self.set_user_id(user_id)


        # new: map rights -> role and set global session
            role = RIGHTS_TO_ROLE.get(rights, "patient")

            clinic_id = None

            Session.set(uid=user_id, role=role, clinic_id=clinic_id)
            


            if rights == 0:
                self.showHomeWidget()
            elif rights == 1: 
                self.showDocHomeWidget()
            elif rights == 2:
                self.showCAHomeWidget()
            elif rights == 4:
                self.showPAHomeWidget()

    @pyqtSlot()
    def showViewApptWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.viewApptWidget)
            self.viewApptWidget.fetch_appt_data()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showForgotPwWidget(self):
        self.previous_widget = self.current_widget  # remember where user was
        self.stackedWidget.setCurrentWidget(self.forgotPwWidget)

    def handleBackFromForgotPw(self):
        if self.previous_widget:
            self.stackedWidget.setCurrentWidget(self.previous_widget)
            self.current_widget = self.previous_widget
        else:
            # fallback if no previous widget known
            self.showLoginWidget()

    @pyqtSlot()
    def showRegisterWidget(self):
        self.stackedWidget.setCurrentWidget(self.registerWidget)
        
    @pyqtSlot()
    def showLoginWidget(self):
        """Show login widget and clear any existing session"""
        self.session_manager.end_session()
        self.loginWidget.ic_input.clear()
        self.loginWidget.password_input.clear()
        self.current_widget = self.loginWidget
        self.stackedWidget.setCurrentWidget(self.loginWidget)
        
    @pyqtSlot()
    def showPrivacyPolicyWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.privacyPolicyWidget)
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showTncWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.tncWidget)
            self.session_manager.extend_session()
        
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
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.homeWidget)
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showFindDocWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.findDocWidget)
            self.findDocWidget.fetch_clinic_data()
            self.session_manager.extend_session()
    
        
                
    @pyqtSlot()
    def showFindClinicWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.findClinicWidget)
            self.findClinicWidget.fetch_clinic_data()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showMakeApptWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.makeApptWidget)
            self.makeApptWidget.fetch_clinic_data()
            self.session_manager.extend_session()
        
    def showPrefillMakeApptWidget(self, clinic_name, doctor_name):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.makeApptWidget)
            self.makeApptWidget.prefill_appointment_form(clinic_name, doctor_name)
            self.session_manager.extend_session()
        
    def showPrefillFindDocWidget(self, clinic_name):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.findDocWidget)
            self.findDocWidget.prefill_clinic(clinic_name)
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showServicesWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.servicesWidget)
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showPAViewClinicWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.paViewClinicWidget)
            self.paViewClinicWidget.fetch_clinic_data()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showPAViewFeedBackInboxWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.paFeedbackInboxWidget)
            self.paFeedbackInboxWidget.fetch_fb_data()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showPAHomeWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.paHomeWidget)
            self.paHomeWidget.fetch_clinic_data()
            self.paHomeWidget.fetch_fb_data()
            self.paHomeWidget.calc_new_addition()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showPAProfileSettingsWidget(self):
        if self._check_authentication():
            self.current_widget = self.paProfileSettingsWidget
            self.stackedWidget.setCurrentWidget(self.paProfileSettingsWidget)
            self.paProfileSettingsWidget.set_default_texts()
            self.paProfileSettingsWidget.fetch_admin_data()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showRegisterClinicWidget(self):
        self.stackedWidget.setCurrentWidget(self.registerClinicWidget)
        
    @pyqtSlot()
    def showProfileSettingsWidget(self):
        if self._check_authentication():
            self.current_widget = self.profileSettingsWidget
            self.stackedWidget.setCurrentWidget(self.profileSettingsWidget)
            self.profileSettingsWidget.set_default_texts()
            self.profileSettingsWidget.fetch_patient_data()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showSendFeedbackWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.sendFeedbackWidget)
            self.sendFeedbackWidget.fetch_patient_data()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showPAEditPrivacyPolicyWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.paEditPrivacyPolicyWidget)
            self.paEditPrivacyPolicyWidget.set_default_text()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showPAEditTncWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.paEditTncWidget)
            self.paEditTncWidget.set_default_text()
            self.session_manager.extend_session()
        
    def showViewClinicProfileWidget(self, clinic_name, temp):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.viewClinicProfile)
            self.viewClinicProfile.display_clinic_profile(clinic_name, temp)
            self.viewClinicProfile.fetch_clinic_info_from_db(clinic_name)
            self.session_manager.extend_session()
        
    def showPrefillPAFbWidget(self, fb_data):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.paFeedbackInboxWidget)
            self.paFeedbackInboxWidget.create_popup_widget(fb_data)
            self.session_manager.extend_session()
    
    def showPrefillCADocWidget(self, doc_data):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.caViewDocWidget)
            self.caViewDocWidget.create_popup_widget(doc_data)
            self.session_manager.extend_session()

    def showViewDoctorProfileWidget(self, doc_id, clinic_name):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.viewDoctorProfile)
            self.viewDoctorProfile.display_doctor_profile(doc_id, clinic_name)
            self.viewDoctorProfile.fetch_doctor_info_from_db(doc_id, clinic_name)
            self.session_manager.extend_session()

    # Doctor widgets
    @pyqtSlot()
    def showDocPatientsWidget(self):
        if self._check_authentication():
            self.docPatientsWidget.get_patient_data()
            self.docPatientsWidget.clear_patient_details()
            self.stackedWidget.setCurrentWidget(self.docPatientsWidget)
            self.session_manager.extend_session()

    @pyqtSlot()
    def showDocHomeWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.docHomeWidget)
            self.session_manager.extend_session()
    
    @pyqtSlot()
    def showDocUpdateRecordWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.docUpdateRecordWidget)
            self.session_manager.extend_session()

    @pyqtSlot()
    def showDocProfileSettingsWidget(self):
        if self._check_authentication():
            self.current_widget = self.docProfileSettingsWidget
            self.stackedWidget.setCurrentWidget(self.docProfileSettingsWidget)
            self.session_manager.extend_session()

    def pass_pID_updateRecordWidget(self, patient_id):
        if self._check_authentication():
            self.docUpdateRecordWidget.set_patient_id(patient_id)
            self.session_manager.extend_session()

    # Clinic admin widgets
    @pyqtSlot()
    def showCAHomeWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.caHomeWidget)
            self.caHomeWidget.fetch_patient_data()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showCAPatientsPageWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.caPatientsPageWidget)
            self.caPatientsPageWidget.fetch_patient_data()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showCAAddDocWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.caAddDocWidget)
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showCAApproveRejectWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.caApproveRejectWidget)
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showCAViewDocWidget(self):
        if self._check_authentication():
            self.stackedWidget.setCurrentWidget(self.caViewDocWidget)
            self.caViewDocWidget.fetch_doc_data()
            self.session_manager.extend_session()
        
    @pyqtSlot()
    def showCAProfileSettingsWidget(self):
        if self._check_authentication():
            self.current_widget = self.caProfileSettingsWidget
            self.stackedWidget.setCurrentWidget(self.caProfileSettingsWidget)
            self.session_manager.extend_session()

    def set_user_id(self, user_id):  
        try:
            self.homeWidget.set_user_id(user_id)
            self.makeApptWidget.set_user_id(user_id)
            self.profileSettingsWidget.set_user_id(user_id)
            self.sendFeedbackWidget.set_user_id(user_id)
            self.paProfileSettingsWidget.set_user_id(user_id)
            self.viewApptWidget.set_user_id(user_id)

            self.docPatientsWidget.set_user_id(str(user_id))
            self.docHomeWidget.set_user_id(str(user_id))
            self.docProfileSettingsWidget.set_user_id(str(user_id))
            self.caHomeWidget.set_user_id(str(user_id))
            self.caProfileSettingsWidget.set_user_id(str(user_id))
            self.caAddDocWidget.set_user_id(str(user_id))
            self.caPatientsPageWidget.set_user_id(str(user_id))
            self.caViewDocWidget.set_user_id(str(user_id))
        except Exception as e:
            print(f"Error setting user id in widgets: {e}")
        
    def _check_authentication(self):
        """Check if user is authenticated, if not redirect to login"""
        if not self.session_manager.is_authenticated:
            self.handle_session_expired()
            return False
        return True
        
    def handle_session_expired(self):
        # log session time out
        try:
            if Session.current:
                log_event(
                    uid=Session.current.uid,
                    role=Session.current.role,
                    action="SESSION_TIMEOUT"
                )
            else:
                print("[AUDIT] timeout log skipped: no active session")
        except Exception as e:
            print("[AUDIT] timeout log failed:", e)

        """Handle when session automatically expires"""
        # Show message and redirect to login
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Session Expired")
        msg_box.setText("Your session has expired due to inactivity. Please login again.")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.buttonClicked.connect(self.showLoginWidget)  # Redirect after OK
        msg_box.exec_()
        
    def showLogoutPopup(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Logout")
        msg_box.setText("Are you sure you want to logout?")
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        reply = msg_box.exec_()

        if reply == QMessageBox.Ok:
            # log out and session timeout
            try:
                log_event(uid=Session.uid, role=Session.role, action="LOGOUT")
            except Exception as e:
                print("[AUDIT] logout log failed:", e)

            # End session 
            try:
                self.session_manager.end_session()
                print("[INFO] Session ended successfully.")
            except Exception as e:
                print(f"[ERROR] Failed to end session: {e}")

            # Clear any other user data or cached info
            try:
                if hasattr(self, "current_user"):
                    self.current_user = None
                if hasattr(self, "user_data"):
                    self.user_data = {}
                if hasattr(self, "user_role"):
                    self.user_role = None
            except Exception as e:
                print(f"[WARNING] Failed to clear user data: {e}")

            # Redirect to login page
            self.showLoginWidget()
        elif reply == QMessageBox.Cancel:
            msg_box.close()

        # Clear any stored session data or tokens
        # Redirect to login page and reset session timer
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWin = Ui_MainWindow()
    mainWin.showMaximized()
    sys.exit(app.exec_())