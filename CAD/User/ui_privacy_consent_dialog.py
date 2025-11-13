from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextBrowser, QCheckBox, QPushButton

class PrivacyConsentDialog(QDialog):
    def __init__(self, policy_text: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Privacy Policy")
        self.resize(720, 520)

        layout = QVBoxLayout(self)

        self.viewer = QTextBrowser(self)
        self.viewer.setPlainText(policy_text)

        self.checkbox = QCheckBox("I have read and agree to the Privacy Policy", self)

        self.btn = QPushButton("Continue", self)
        self.btn.setEnabled(False)

        self.checkbox.stateChanged.connect(
            lambda _: self.btn.setEnabled(self.checkbox.isChecked())
        )
        self.btn.clicked.connect(self.accept)

        layout.addWidget(self.viewer)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.btn)
