from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal,pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from connection import db, auth
from datetime import datetime
from User.ui_privacy_consent_dialog import PrivacyConsentDialog
from security.audit_logger import log_event



class LoginWidget(QWidget):
    login_successful = pyqtSignal(int,str)  

    user_id = pyqtSignal(str)
    apply_btn_clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        self.bg = QFrame(Form)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(0, 0, 1920, 1080))
        self.bg.setMinimumSize(QSize(1920, 1080))
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.widget_2 = QWidget(self.bg)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 1350, 1080))
        self.widget_2.setMinimumSize(QSize(0, 1080))
        self.widget_2.setStyleSheet(u"background-color: white;")
        self.loginwidget = QWidget(self.widget_2)
        self.loginwidget.setObjectName(u"loginwidget")
        self.loginwidget.setGeometry(QRect(160, 200, 701, 721))
        self.layoutWidget = QWidget(self.loginwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(102, 72, 506, 428))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logintext = QLabel(self.layoutWidget)
        self.logintext.setObjectName(u"logintext")
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.logintext.setFont(font)
        self.logintext.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.logintext)

        self.verticalSpacer_13 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.ic_layout = QVBoxLayout()
        self.ic_layout.setSpacing(10)
        self.ic_layout.setObjectName(u"ic_layout")
        self.ic = QLabel(self.layoutWidget)
        self.ic.setObjectName(u"ic")
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(12)
        self.ic.setFont(font1)

        self.ic_layout.addWidget(self.ic)

        self.ic_input = QLineEdit(self.layoutWidget)
        self.ic_input.setObjectName(u"ic_input")
        self.ic_input.setMinimumSize(QSize(500, 40))
        self.ic_input.setBaseSize(QSize(0, 0))

        self.ic_layout.addWidget(self.ic_input)


        self.verticalLayout_14.addLayout(self.ic_layout)

        # --- Password layout (main vertical container) ---
        self.password_layout = QVBoxLayout()
        self.password_layout.setObjectName(u"password_layout")

        # --- Password label ---
        self.password = QLabel(self.layoutWidget)
        self.password.setObjectName(u"password")
        self.password.setFont(font1)
        self.password_layout.addWidget(self.password)

        # --- Password input field ---
        self.password_input = QLineEdit(self.layoutWidget)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(0, 40))

        # --- Add eye icon as action inside QLineEdit ---
        self.toggle_action = QAction(QIcon("CAD/Images/icon/eye.png"), "Show/Hide Password", self.password_input)
        self.toggle_action.setCheckable(True)
        self.password_input.addAction(self.toggle_action, QLineEdit.TrailingPosition)

        # --- Connect action to toggle function ---
        self.toggle_action.toggled.connect(self.toggle_password_visibility)

        # --- Add input to layout ---
        self.password_layout.addWidget(self.password_input)

        # --- Add to parent layout ---
        self.verticalLayout_14.addLayout(self.password_layout)
        self.verticalLayout.addLayout(self.verticalLayout_14)

        self.forgetpassword = QHBoxLayout()
        self.forgetpassword.setObjectName(u"forgetpassword")
        self.horizontalSpacer_9 = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.forgetpassword.addItem(self.horizontalSpacer_9)

        self.forgetpassbutton = QPushButton(self.layoutWidget)
        self.forgetpassbutton.setObjectName(u"forgetpassbutton")
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(9)
        self.forgetpassbutton.setFont(font2)
        self.forgetpassbutton.setStyleSheet(u"QPushButton { border: none; }")

        self.forgetpassword.addWidget(self.forgetpassbutton)


        self.verticalLayout.addLayout(self.forgetpassword)

        self.verticalSpacer_16 = QSpacerItem(498, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_16)

        self.loginbutton = QPushButton(self.layoutWidget)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setMinimumSize(QSize(0, 60))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(14)
        self.loginbutton.setFont(font3)
        self.loginbutton.setStyleSheet(u"border-radius: 15px; color: white; background-color: \"#B6D0E2\";")
        self.loginbutton.clicked.connect(self.validateLogin)

        self.verticalLayout.addWidget(self.loginbutton)

        self.registerbutton = QPushButton(self.loginwidget)
        self.registerbutton.setObjectName(u"registerbutton")
        self.registerbutton.setGeometry(QRect(200, 550, 331, 28))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(10)
        self.registerbutton.setFont(font4)
        self.registerbutton.setStyleSheet(u"border: none")

        
        self.apply_clinic_btn = QPushButton(self.loginwidget)
        self.apply_clinic_btn.setObjectName(u"apply_clinic_btn")
        self.apply_clinic_btn.setGeometry(QRect(110, 610, 521, 28))
        self.apply_clinic_btn.setFont(font4)
        self.apply_clinic_btn.setStyleSheet(u"border: none")
        self.apply_clinic_btn.clicked.connect(self.emitApplyClinicBtn)
        
        self.widget_3 = QWidget(self.bg)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(1348, 0, 579, 1080))
        self.widget_3.setMinimumSize(QSize(0, 1080))
        self.widget_3.setStyleSheet(u"background-color: \"#B6D0E2\";")
        self.imageframe = QFrame(self.bg)
        self.imageframe.setObjectName(u"imageframe")
        self.imageframe.setGeometry(QRect(1040, 110, 641, 841))
        self.imageframe.setFrameShape(QFrame.StyledPanel)
        self.imageframe.setFrameShadow(QFrame.Raised)
        self.imageframe.setLineWidth(0)
        self.image = QLabel(self.imageframe)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(0, 0, 641, 891))
        self.image.setPixmap(QPixmap(u"CAD/Images/Stethoscope.jpg"))
        self.image.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logintext.setText(QCoreApplication.translate("Form", u"Login", None))
        self.ic.setText(QCoreApplication.translate("Form", u"IC/ID Number", None))
        self.password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.forgetpassbutton.setText(QCoreApplication.translate("Form", u"Forgot Password", None))
#if QT_CONFIG(tooltip)
        self.loginbutton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.loginbutton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.registerbutton.setText(QCoreApplication.translate("Form", u"Don't have an account? Register here.", None))
        self.apply_clinic_btn.setText(QCoreApplication.translate("Form", u"Want to include your clinic in our system? Click here.", None))
        self.image.setText("")
    # retranslateUi

    def toggle_password_visibility(self, checked):
        if checked:
            self.password_input.setEchoMode(QLineEdit.Normal)  # show password
            self.toggle_action.setIcon(QIcon("CAD/Images/icon/hidden.png"))  # change icon
        else:
            self.password_input.setEchoMode(QLineEdit.Password)  # hide password
            self.toggle_action.setIcon(QIcon("CAD/Images/icon/eye.png"))
    
    
    def record_failed_attempt(self, user_ic):
        attempts_ref = db.child('login_attempts').child(user_ic)
        attempts = attempts_ref.get().val() or {}

        count = attempts.get('count', 0) + 1  # Always increment on failure
        last_attempt = datetime.now().timestamp()

        # Update this user's record and include their IC
        db.child('login_attempts').child(user_ic).update({
            'count': count,
            'last_attempt': last_attempt
        })
        return count, last_attempt


    def can_attempt_login(self, user_ic):
        if not user_ic:
            return True, 0

        attempts_ref = db.child('login_attempts').child(user_ic)
        attempts = attempts_ref.get().val() or {}

        count = attempts.get('count', 0)
        last_attempt = attempts.get('last_attempt', 0)
        now = datetime.now().timestamp()

        if count < 3:
            return True, 0  # First 3 attempts are always allowed

        # Exponential backoff after 3 failed attempts
        wait_time = 10 * 2 ** (count - 3)

        if now - last_attempt < wait_time:
            remaining = wait_time - (now - last_attempt)
            return False, remaining
        else:
            return True, 0
        
    def _load_policy_text(self) -> str:
        """Get current policy text from Firebase; fallback if missing."""
        try:
            text = db.child("privacy_policy").get().val()
            return text or "Privacy Policy not available."
        except Exception:
            return "Privacy Policy not available."

    def _ensure_privacy_consent(self, uid: str) -> bool:
        """
         If user hasn't accepted privacy policy, show a blocking dialog.
        Store consent at: /privacy_consent/{uid} = {accepted: True, ts: <server timestamp>}
        Returns True if accepted; False if user cancels.
        """
        try:
            consent = db.child("privacy_consent").child(uid).get().val()
        except Exception:
            consent = None

        if consent and consent.get("accepted"):
            return True

        dlg = PrivacyConsentDialog(policy_text=self._load_policy_text(), parent=self)
        if dlg.exec_():  # checkbox + Continue
            try:
                db.child("privacy_consent").child(uid).set(
                    {"accepted": True, "ts": {".sv": "timestamp"}}
                )
            except Exception:
                pass
            return True

        QMessageBox.warning(self, "Notice", "You must accept the Privacy Policy to continue.")
        return False
    


    def validateLogin(self):

        ic = self.ic_input.text().strip()
        ic = ic.replace('.', '_').replace('@', '_')
        password = self.password_input.text().strip()
        
        #  Basic IC format validation
        if not ic or not password:
            self.showMessageBox('Error', 'IC/ID number and password cannot be empty.')
            return

        # Check if user can attempt login
        can_login, wait = self.can_attempt_login(ic) 
        if not can_login:
            self.showMessageBox('Wait', f'Too many failed attempts. Please wait {int(wait)} seconds before retrying.')
            return

        # Before validating credentials, check Firebase 'login_attempts/{ic}'
        if not ic or not password:
            self.showMessageBox('Error', 'IC/ID number and password cannot be empty.')
            return

        # ===== PATIENT LOGIN =====
        try:
            # Look up the IC in Realtime DB to get the email
            patients = db.child('patients').get()
            user_email = None
            patient_data = None

            if patients.each():
                for patient in patients.each():
                    data = patient.val()
                    if data.get('patient_ic') == ic:
                        user_email = data.get('patient_email')
                        patient_data = data
                        break
                    
            # If IC not found in patients DB (Verification)
            if not user_email:
                self.showMessageBox('Error', 'No account found with this IC number.')
                return
        
            if user_email:
                try:
                    user = auth.sign_in_with_email_and_password(user_email, password)
                    
                    # Refresh token and check verification
                    refreshed = auth.refresh(user['refreshToken'])
                    id_token = refreshed['idToken']
                    user_info = auth.get_account_info(id_token)
                    verified = user_info['users'][0].get('emailVerified', False)

                    if not verified:
                        reply = QMessageBox.question(
                            self,
                            "Email Not Verified",
                            f"Your email ({user_email}) is not verified.\nWould you like to resend the verification link?",
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No
                        )

                        if reply == QMessageBox.Yes:
                            try:
                                auth.send_email_verification(user['idToken'])
                                QMessageBox.information(
                                    self,
                                    "Verification Email Sent",
                                    "A new verification link has been sent to your email.\nPlease verify your account before logging in."
                                )
                            except Exception as e:
                                QMessageBox.warning(
                                    self,
                                    "Error",
                                    f"Failed to resend verification email.\nDetails: {str(e)}"
                                )
                        else:
                            QMessageBox.information(
                                self,
                                "Verification Required",
                                "Please verify your email before logging in."
                            )
                        return

                    # Login success → reset failed attempts
                    db.child("login_attempts").child(ic).remove()
                    firebase_uid = user['localId']
                    rights = patient_data.get('rights', 0)

                    # Require privacy consent BEFORE showing success / emitting signals
                    if not self._ensure_privacy_consent(firebase_uid):
                        return
                    
                    # audit log for successful login (patient branch) ===
                    role_map = {0: "patient", 1: "doctor", 2: "clinic_admin", 4: "super_admin"}
                    role = role_map.get(rights, "patient")

                    log_event(
                        uid=firebase_uid,
                        role=role,
                        action="LOGIN_SUCCESS",
                        meta={"via": "password"}
                    )


                    self.showMessageBox('Info', 'Patient login successful')
                    self.login_successful.emit(rights,firebase_uid)
                    self.user_id.emit(ic)
                    return

                except Exception as e:
                    count, last = self.record_failed_attempt(ic)
                    self.showMessageBox(
                        'Invalid Login',
                        f'Invalid IC/ID or password. Attempt {count}.' # Reset failed login attempts in Firebase after successful login
                    )
                    return

        except Exception as e:
            self.showMessageBox('Error', f"Error fetching patient data: {e}")

        # ===== DOCTOR LOGIN =====
        try:
            doctors = db.child('doctors').get()
            if doctors.each():
                for doctor in doctors.each():
                    data = doctor.val()
                    if data.get('user_id') == ic and data.get('password') == password:
                        rights = data.get('rights', 1)
                        firebase_uid = ic

                        if not self._ensure_privacy_consent(firebase_uid):
                            return
                        
                        # audit log for successful login  ===
                        role_map = {0: "patient", 1: "doctor", 2: "clinic_admin", 4: "super_admin"}
                        role = role_map.get(rights, "patient")

                        log_event(
                            uid=firebase_uid,
                            role=role,
                            action="LOGIN_SUCCESS",
                            meta={"via": "password"}
                        )

                        self.showMessageBox('Info', 'Doctor login successful')
                        self.login_successful.emit(rights,firebase_uid)
                        self.user_id.emit(ic)
                        return
        except Exception as e:
            self.showMessageBox('Error', f"Error fetching doctor data: {e}")

        # ===== PROJECT ADMIN LOGIN =====
        try:
            pa_admins = db.child('project_admin').get()
            if pa_admins.each():
                for admin in pa_admins.each():
                    data = admin.val()
                    if data.get('pa_id') == ic and data.get('pa_pass') == password:
                        rights = data.get('rights', 4)
                        firebase_uid = ic

                        if not self._ensure_privacy_consent(firebase_uid):
                            return
                        
                        # audit log for successful login===
                        role_map = {0: "patient", 1: "doctor", 2: "clinic_admin", 4: "super_admin"}
                        role = role_map.get(rights, "patient")

                        log_event(
                            uid=firebase_uid,
                            role=role,
                            action="LOGIN_SUCCESS",
                            meta={"via": "password"}
                        )
                        
                        self.showMessageBox('Info', 'Admin login successful')
                        self.login_successful.emit(rights,firebase_uid)
                        self.user_id.emit(ic)
                        return
        except Exception as e:
            self.showMessageBox('Error', f"Error fetching project admin data: {e}")

        # ===== CLINIC ADMIN LOGIN =====
        try:
            ca_admins = db.child('clinic_admin').get()
            if ca_admins.each():
                for admin in ca_admins.each():
                    data = admin.val()
                    if data.get('ca_id') == ic and data.get('ca_pass') == password:
                        rights = data.get('rights', 2)
                        firebase_uid = ic           

                        if not self._ensure_privacy_consent(firebase_uid):
                            return
                        
                         # audit log for successful login===
                        role_map = {0: "patient", 1: "doctor", 2: "clinic_admin", 4: "super_admin"}
                        role = role_map.get(rights, "patient")

                        log_event(
                            uid=firebase_uid,
                            role=role,
                            action="LOGIN_SUCCESS",
                            meta={"via": "password"}
                        )


                        self.showMessageBox('Info', 'Clinic Admin login successful')
                        self.login_successful.emit(rights,firebase_uid)
                        self.user_id.emit(ic)
                        return
        except Exception as e:
            self.showMessageBox('Error', f"Error fetching clinic admin data: {e}")

        # ===== DEFAULT =====
        self.showMessageBox('Error', 'Invalid IC/ID number or password.')


    def showMessageBox(self, title, message, success=False):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    @pyqtSlot()
    def emitApplyClinicBtn(self):
        # Emit the custom signal
        self.apply_btn_clicked.emit()


