import unittest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication, QMessageBox
from User.ui_privacy_policy import PrivacyPolicyWidget  # Update the import path

class TestPrivacyPolicyWidget(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Create a QApplication instance

    def setUp(self):
        self.widget = PrivacyPolicyWidget()
        # Mock the signals
        self.widget.back_btn_clicked = MagicMock()

    def test_load_policy_from_db_success(self):
        # Mock the database call to return a fake privacy policy
        mock_db = MagicMock()
        mock_db.child.return_value.get.return_value.val.return_value = "This is a test privacy policy."

        with patch('User.ui_privacy_policy.db', new=mock_db):
            self.widget.load_policy_from_db()
            self.assertEqual(self.widget.textBrowser.toPlainText(), "This is a test privacy policy.")

    def test_load_policy_from_db_no_policy(self):
        # Mock the database call to return None
        mock_db = MagicMock()
        mock_db.child.return_value.get.return_value.val.return_value = None

        with patch('User.ui_privacy_policy.db', new=mock_db):
            self.widget.load_policy_from_db()
            self.assertEqual(self.widget.textBrowser.toPlainText(), "No policy found in the database.")

    def test_load_policy_from_db_exception(self):
        # Mock the database call to raise an exception
        mock_db = MagicMock()
        mock_db.child.return_value.get.side_effect = Exception("Database error")

        with patch('User.ui_privacy_policy.db', new=mock_db):
            with patch('PyQt5.QtWidgets.QMessageBox.critical') as mock_message_box:
                self.widget.load_policy_from_db()
                mock_message_box.assert_called_once_with(self.widget, "Database Error", "An error occurred while fetching terms: Database error")

    def test_back_button_signal(self):
        with patch.object(self.widget.back_btn_clicked, 'emit') as mock_emit:
            self.widget.back_button.click()
            mock_emit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
