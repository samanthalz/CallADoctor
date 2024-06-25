import unittest
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox
from ui_ca_homepage import CA_homepageWidget  # Update to your actual import path

class TestCAHomepageWidget(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Create a QApplication instance

    def setUp(self):
        self.widget = CA_homepageWidget()

    def test_view_patient_details_button_clicked(self):
        with patch.object(QMessageBox, 'information') as mock_info:
            # Emit the clicked signal for the view_patient_details_button
            self.widget.view_patient_details_button.clicked.emit()
            # Check that QMessageBox.information was called with the expected arguments
            mock_info.assert_called_once_with(self.widget, 'Info', 'View Patient Details button clicked.')

    def test_logout_button_clicked(self):
        with patch.object(QMessageBox, 'information') as mock_info:
            # Emit the clicked signal for the logout_button
            self.widget.logout_button.clicked.emit()
            # Check that QMessageBox.information was called with the expected arguments
            mock_info.assert_called_once_with(self.widget, 'Info', 'Logout button clicked.')

if __name__ == '__main__':
    unittest.main()
