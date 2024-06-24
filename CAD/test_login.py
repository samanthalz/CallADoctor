import unittest
from unittest.mock import MagicMock, patch, call
from PyQt5.QtWidgets import QApplication, QLineEdit
from login import LoginWidget  # Update this path to the actual import path

class TestLoginWidget(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Create a QApplication instance

    def setUp(self):
        self.widget = LoginWidget()
        self.widget.login_successful = MagicMock()
        self.widget.user_id = MagicMock()

    def test_validateLogin_empty_fields(self):
        self.widget.ic_input = QLineEdit('')
        self.widget.password_input = QLineEdit('')

        with patch.object(self.widget, 'showMessageBox') as mock_message_box:
            self.widget.validateLogin()
            mock_message_box.assert_called_once_with('Error', 'IC/ID number and password cannot be empty.')

    def test_validateLogin_patient_success(self):
        mock_db = MagicMock()
        mock_db.child.return_value.get.return_value.each.return_value = [
            MagicMock(val=lambda: {'patient_ic': '123456789123', 'patient_pass': 'amy12345', 'rights': 1})
        ]

        self.widget.ic_input = QLineEdit('123456789123')
        self.widget.password_input = QLineEdit('amy12345')

        with patch('login.db', new=mock_db):
            with patch.object(self.widget, 'showMessageBox') as mock_message_box:
                self.widget.validateLogin()
                mock_message_box.assert_called_once_with('Info', 'Patient login successful')
                self.widget.login_successful.emit.assert_called_once_with(1)
                self.widget.user_id.emit.assert_called_once_with('123456789123')

    def test_validateLogin_admin_success(self):
        mock_db = MagicMock()
        mock_db.child.return_value.get.return_value.each.return_value = [
            MagicMock(val=lambda: {'pa_id': '112233445566', 'pa_pass': '44444444', 'rights': 4})
        ]

        self.widget.ic_input = QLineEdit('112233445566')
        self.widget.password_input = QLineEdit('44444444')

        with patch('login.db', new=mock_db):
            with patch.object(self.widget, 'showMessageBox') as mock_message_box:
                self.widget.validateLogin()

                # Check that showMessageBox was called at least once with the expected parameters
                mock_message_box.assert_any_call('Info', 'Admin login successful')
                self.widget.login_successful.emit.assert_called_once_with(4)
                self.widget.user_id.emit.assert_called_once_with('112233445566')


    def test_validateLogin_invalid_credentials(self):
        mock_db = MagicMock()
        mock_db.child.return_value.get.return_value.each.return_value = []

        self.widget.ic_input = QLineEdit('invalid_ic')
        self.widget.password_input = QLineEdit('invalid_password')

        with patch('login.db', new=mock_db):
            with patch.object(self.widget, 'showMessageBox') as mock_message_box:
                self.widget.validateLogin()
                mock_message_box.assert_called_once_with('Error', 'Invalid IC/ID number or password.')

    def test_validateLogin_exception(self):
        mock_db = MagicMock()
        mock_db.child.return_value.get.side_effect = Exception("Database error")

        self.widget.ic_input = QLineEdit('123456789123')
        self.widget.password_input = QLineEdit('amy12345')

        with patch('login.db', new=mock_db):  
            with patch.object(self.widget, 'showMessageBox') as mock_message_box:
                self.widget.validateLogin()
                expected_calls = [
                    call('Error', 'Error fetching patient data: Database error'),
                    call('Error', 'Error fetching admin data: Database error'),
                    call('Error', 'Invalid IC/ID number or password.')
                ]
                mock_message_box.assert_has_calls(expected_calls)
                
if __name__ == '__main__':
    unittest.main()
