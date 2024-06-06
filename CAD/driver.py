from PyQt5 import QtWidgets
from ui_login import LoginWindow
from User.forgotpw import ForgotPwWindow  # Assuming you have a ui_forgotpw file for ForgotPwWindow
import sys

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_window = LoginWindow()
        self.forgot_pw_window = ForgotPwWindow()
        
        self.login_window.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.showMaximized()
    sys.exit(app.exec_())
