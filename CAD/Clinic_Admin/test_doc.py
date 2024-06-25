import pytest
import sys
import time
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QComboBox, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtGui import QPixmap
from connection import db  # Assuming db is needed for testing

from ui_ca_view_doc import CA_view_docWidget  # Assuming CA_view_docWidget is in CA_view_docWidget.py

@pytest.fixture
def ca_view_doc_widget(qtbot):
    # Setup function to initialize QApplication and CA_view_docWidget
    app = QApplication(sys.argv)
    widget = CA_view_docWidget()
    qtbot.addWidget(widget)
    yield widget
    widget.close()
    sys.exit(app.exec_())

def test_view_patient_details_button(ca_view_doc_widget, qtbot):
    # Test if view_patient_details_button click emits the correct signal
    with qtbot.waitSignal(ca_view_doc_widget.view_patient_details_button.clicked):
        ca_view_doc_widget.view_patient_details_button.click()

def test_search_clinic_widget(ca_view_doc_widget, qtbot):
    # Test search clinic widget functionalities
    search_text = "Test Clinic"
    qtbot.keyClicks(ca_view_doc_widget.search_clinic, search_text)
    assert ca_view_doc_widget.search_clinic.text() == search_text

def test_add_doc_button(ca_view_doc_widget, qtbot):
    # Test if add_doc_btn click emits the correct signal
    with qtbot.waitSignal(ca_view_doc_widget.add_doc_btn.clicked):
        ca_view_doc_widget.add_doc_btn.click()

def test_remove_doc_button(ca_view_doc_widget, qtbot):
    # Test if remove_doc_btn click emits the correct signal
    with qtbot.waitSignal(ca_view_doc_widget.remove_doc_btn.clicked):
        ca_view_doc_widget.remove_doc_btn.click()

def test_navigation_buttons(ca_view_doc_widget, qtbot):
    # Test navigation buttons (home, doctors, patients, settings, logout)
    buttons = [
        (ca_view_doc_widget.home_navigation, ca_view_doc_widget.home_navigation_btn_clicked),
        (ca_view_doc_widget.doctors_navigation, ca_view_doc_widget.doctors_navigation_btn_clicked),
        (ca_view_doc_widget.patients_navigation, ca_view_doc_widget.patients_navigation_btn_clicked),
        (ca_view_doc_widget.settings_navigation, ca_view_doc_widget.settings_navigation_btn_clicked),
        (ca_view_doc_widget.logout_navigation, ca_view_doc_widget.logout_btn_clicked)
    ]
    for button, signal in buttons:
        with qtbot.waitSignal(signal):
            button.click()

if __name__ == "__main__":
    pytest.main()
