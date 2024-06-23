import unittest
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QMessageBox
from PyQt5.QtCore import pyqtSignal
from unittest.mock import patch, MagicMock
from User.ui_tnc import TncWidget 

class TestTncWidget(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.widget = TncWidget()

    def tearDown(self):
        self.widget.close()

    def test_emitBackBtn(self):
        # Mock the back_btn_clicked signal
        mock_signal = MagicMock()
        self.widget.back_btn_clicked = mock_signal

        # Call the emitBackBtn method
        self.widget.emitBackBtn()

        # Verify that the back_btn_clicked signal was emitted
        mock_signal.emit.assert_called_once()

    def test_load_terms_from_db(self):
        # Mocking the database call and its response
        mock_db = MagicMock()
        mock_db.child.return_value.get.return_value.val.return_value = "Sample terms"

        # Patching the db object to use the mock_db
        with patch('User.ui_tnc.db', new=mock_db):
            # Call the load_terms_from_db method
            self.widget.load_terms_from_db()

            # Verify that the textBrowser contains the expected text
            self.assertEqual(self.widget.textBrowser.toPlainText(), "Sample terms")

    def test_load_terms_from_db_no_terms(self):
        # Mocking the database call to return None (no terms found)
        mock_db = MagicMock()
        mock_db.child.return_value.get.return_value.val.return_value = None

        # Patching the db object to use the mock_db
        with patch('User.ui_tnc.db', new=mock_db):
            # Call the load_terms_from_db method
            self.widget.load_terms_from_db()

            # Verify that the textBrowser contains the expected message
            self.assertEqual(self.widget.textBrowser.toPlainText(), "No terms found in the database.")

if __name__ == '__main__':
    unittest.main()
