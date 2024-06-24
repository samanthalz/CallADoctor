from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,QMouseEvent,
    QRadialGradient)
from PyQt5.QtWidgets import *
from datetime import datetime
import pyrebase
from connection import db



class FeedbackInboxWidget(QWidget):
    clinic_btn_clicked = pyqtSignal()
    home_btn_clicked = pyqtSignal()
    logout_btn_clicked = pyqtSignal()
    profile_btn_clicked = pyqtSignal()
        
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fb_data_list = []
        self.setupUi(self)
        self.fetch_fb_data()
        self.fb_details_frame = None
        
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        
        Form.setAutoFillBackground(True)
        p = Form.palette()
        p.setColor(Form.backgroundRole(), QColor('#B6D0E2'))
        Form.setPalette(p)
        
        self.background = QWidget(Form)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(150, 0, 1771, 1061))
        self.background.setStyleSheet(u"background-color: #F8F8F8;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-left-radius: 30px;\n"
"text-align: center;")
        self.user_frame = QFrame(self.background)
        self.user_frame.setObjectName(u"user_frame")
        self.user_frame.setGeometry(QRect(1480, 30, 251, 80))
        self.user_frame.setStyleSheet(u"border-radius: 20px; border: 2px solid #808080")
        self.user_frame.setFrameShape(QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QFrame.Raised)
        self.profile_icon = QLabel(self.user_frame)
        self.profile_icon.setObjectName(u"profile_icon")
        self.profile_icon.setGeometry(QRect(10, 10, 60, 60))
        self.profile_icon.setStyleSheet(u"border: none")
        self.profile_icon.setPixmap(QPixmap(u"CAD/Images/icon/profile_icon.png"))
        self.profile_icon.setScaledContents(True)
        self.profile_btn = QPushButton(self.user_frame)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setGeometry(QRect(120, 25, 71, 31))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(16)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet(u"border: none")
        self.profile_btn.clicked.connect(self.emitSettingsBtn)
        self.feedback_label = QLabel(self.background)
        self.feedback_label.setObjectName(u"feedback_label")
        self.feedback_label.setGeometry(QRect(40, 170, 961, 61))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(22)
        self.feedback_label.setFont(font1)
        self.feedback_label.setWordWrap(True)
        self.search = QLineEdit(self.background)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(40, 40, 681, 71))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(11)
        self.search.setFont(font2)
        self.search.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 60px; color: Black;\n"
" background-image: url(\"C:/Users/Samantha Law/Documents/INTI/CAD/CallADoctor/CAD/Images/icon/search_icon.png\"); \n"
"background-repeat: no-repeat; \n"
"background-position: left center; \n"
"border: 1px solid gray;\n"
"")
        self.search.setClearButtonEnabled(False)
        
        self.clear_btn = QPushButton(self.background)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(760, 50, 140, 51))
        font11 = QFont()
        font11.setFamily(u"Consolas")
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setWeight(50)
        self.clear_btn.setFont(font11)
        self.clear_btn.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 10px; color: black; border: 1px solid gray;")
        self.clear_btn.clicked.connect(self.clear_search)
        
        self.search_btn = QPushButton(self.background)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(930, 50, 140, 51))
        self.search_btn.setFont(font11)
        self.search_btn.setStyleSheet(u"background-color: #f0f0f0; border-radius: 16px; padding: 10px; color: black; border: 1px solid gray;")
        self.search_btn.clicked.connect(self.search_names)
        
        self.scrollArea = QScrollArea(self.background)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(30, 250, 891, 781))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 821, 731))
        
        self.vLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.vLayout.setSpacing(10)
        self.vLayout.setObjectName(u"vlayout")
        self.vLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setLayout(self.vLayout)
        
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 141, 891))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(31, 20, 87, 851))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_navigation = QToolButton(self.layoutWidget_2)
        self.home_navigation.setObjectName(u"home_navigation")
        self.home_navigation.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_navigation.sizePolicy().hasHeightForWidth())
        self.home_navigation.setSizePolicy(sizePolicy)
        self.home_navigation.setMinimumSize(QSize(85, 96))
        self.home_navigation.setMaximumSize(QSize(85, 96))
        font7 = QFont()
        font7.setFamily(u"Source Sans Pro Semibold")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.home_navigation.setFont(font7)
        self.home_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon = QIcon()
        icon.addFile(u"CAD/Images/nav_images/home_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_navigation.setIcon(icon)
        self.home_navigation.setIconSize(QSize(70, 70))
        self.home_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.home_navigation.clicked.connect(self.emitHomeBtn)
        self.verticalLayout.addWidget(self.home_navigation)

        self.clinic_navigation = QToolButton(self.layoutWidget_2)
        self.clinic_navigation.setObjectName(u"clinic_navigation")
        self.clinic_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.clinic_navigation.sizePolicy().hasHeightForWidth())
        self.clinic_navigation.setSizePolicy(sizePolicy)
        self.clinic_navigation.setMinimumSize(QSize(85, 96))
        self.clinic_navigation.setMaximumSize(QSize(85, 96))
        self.clinic_navigation.setFont(font7)
        self.clinic_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"CAD/Images/nav_images/services_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clinic_navigation.setIcon(icon1)
        self.clinic_navigation.setIconSize(QSize(70, 70))
        self.clinic_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.clinic_navigation.clicked.connect(self.emitClinicBtn)
        self.verticalLayout.addWidget(self.clinic_navigation)

        self.feedback_navigation = QToolButton(self.layoutWidget_2)
        self.feedback_navigation.setObjectName(u"feedback_navigation")
        self.feedback_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.feedback_navigation.sizePolicy().hasHeightForWidth())
        self.feedback_navigation.setSizePolicy(sizePolicy)
        self.feedback_navigation.setMinimumSize(QSize(85, 96))
        self.feedback_navigation.setMaximumSize(QSize(85, 96))
        self.feedback_navigation.setFont(font7)
        self.feedback_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"CAD/Images/nav_images/feedback_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.feedback_navigation.setIcon(icon2)
        self.feedback_navigation.setIconSize(QSize(70, 70))
        self.feedback_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout.addWidget(self.feedback_navigation)

        self.settings_navigation = QToolButton(self.layoutWidget_2)
        self.settings_navigation.setObjectName(u"settings_navigation")
        self.settings_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.settings_navigation.sizePolicy().hasHeightForWidth())
        self.settings_navigation.setSizePolicy(sizePolicy)
        self.settings_navigation.setMinimumSize(QSize(85, 96))
        self.settings_navigation.setMaximumSize(QSize(85, 96))
        self.settings_navigation.setFont(font7)
        self.settings_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"CAD/Images/nav_images/settings_page_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_navigation.setIcon(icon3)
        self.settings_navigation.setIconSize(QSize(70, 70))
        self.settings_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settings_navigation.clicked.connect(self.emitSettingsBtn)
        self.verticalLayout.addWidget(self.settings_navigation)

        self.logout_navigation = QToolButton(self.layoutWidget_2)
        self.logout_navigation.setObjectName(u"logout_navigation")
        self.logout_navigation.setEnabled(True)
        sizePolicy.setHeightForWidth(self.logout_navigation.sizePolicy().hasHeightForWidth())
        self.logout_navigation.setSizePolicy(sizePolicy)
        self.logout_navigation.setMinimumSize(QSize(85, 96))
        self.logout_navigation.setMaximumSize(QSize(85, 96))
        self.logout_navigation.setFont(font7)
        self.logout_navigation.setStyleSheet(u"border: none; \n"
"color: white;")
        icon4 = QIcon()
        icon4.addFile(u"CAD/Images/nav_images/logout_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_navigation.setIcon(icon4)
        self.logout_navigation.setIconSize(QSize(70, 70))
        self.logout_navigation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.logout_navigation.clicked.connect(self.emitLogoutBtn)
        self.verticalLayout.addWidget(self.logout_navigation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.profile_icon.setText("")
        self.profile_btn.setText(QCoreApplication.translate("Form", u"Admin", None))
        self.feedback_label.setText(QCoreApplication.translate("Form", u"Feedbacks Inbox", None))
        self.search.setText("")
        self.search.setPlaceholderText(QCoreApplication.translate("Form", u"Search User's Name", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.search_btn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.home_navigation.setText(QCoreApplication.translate("Form", u"   Home   ", None))
        self.clinic_navigation.setText(QCoreApplication.translate("Form", u"Clinics", None))
        self.feedback_navigation.setText(QCoreApplication.translate("Form", u"Feedback", None))
        self.settings_navigation.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.logout_navigation.setText(QCoreApplication.translate("Form", u"Logout", None))
    # retranslateUi

    @pyqtSlot()
    def emitLogoutBtn(self):
        # Emit the custom signal
        self.logout_btn_clicked.emit()
        
    @pyqtSlot()
    def emitClinicBtn(self):
        self.clinic_btn_clicked.emit()
        
    @pyqtSlot()
    def emitSettingsBtn(self):
        # Emit the custom signal
        self.profile_btn_clicked.emit()
        
    @pyqtSlot()
    def emitHomeBtn(self):
        # Emit the custom signal
        self.home_btn_clicked.emit()
        
    def fetch_fb_data(self):
        db = self.initialize_db()
        try:
            feedbacks = db.child("feedback").get()
            
            if feedbacks.each():
                self.fb_data_list = []
                
                # Iterate through each feedback entry
                for fb in feedbacks.each():
                    feedback_data = fb.val()
                    user_id = feedback_data.get("user_id")
                    
                    # Fetch the patient name using the user_id
                    patient_name = db.child("patients").child(user_id).child("patient_name").get().val()
                    patient_email = db.child("patients").child(user_id).child("patient_email").get().val()
                    
                    # Add the patient name to the feedback data
                    feedback_data["patient_name"] = patient_name
                    feedback_data["patient_email"] = patient_name
                    
                    # Add the feedback data with patient name to the list
                    self.fb_data_list.append(feedback_data)
                
                # Populate the feedback information on the UI
                self.populate_fb_info()
            else:
                print("No feedback data found.")
        except Exception as e:
            print(f"An error occurred while fetching data: {e}")

    def clear_layout(self):
        while self.vLayout.count():
                item = self.vLayout.takeAt(0) 
                widget = item.widget()
                if widget is not None:
                        widget.deleteLater()
                        
    def create_fb_list_frame(self, fb_data):
        fb_frame = QFrame(self.scrollAreaWidgetContents)
        fb_frame.setObjectName(u"fb_frame")
        fb_frame.setGeometry(QRect(60, 270, 801, 81))
        fb_frame.setMinimumSize(QSize(801, 81))
        fb_frame.setMaximumSize(QSize(801, 81))
        fb_frame.setFrameShape(QFrame.StyledPanel)
        fb_frame.setFrameShadow(QFrame.Raised)
        fb_frame.setStyleSheet(u"border: 1px solid gray; border-radius: 10px;")
        
        user_name_label = QLabel(fb_frame)
        user_name_label.setObjectName(u"user_name_label")
        user_name_label.setGeometry(QRect(90, 30, 431, 21))
        user_name_label.setMinimumSize(QSize(431, 0))
        user_name_label.setMaximumSize(QSize(431, 16777215))
        font4 = QFont()
        font4.setFamily(u"Cascadia Code")
        font4.setPointSize(10)
        user_name_label.setFont(font4)
        user_name_label.setStyleSheet(u"border : none;\n")
        user_name_label.setText(fb_data.get("patient_name", "Unknown"))
        
        user_name_label.mousePressEvent = lambda event, fb=fb_data: self.create_popup_widget(fb)
        
        user_logo_label = QLabel(fb_frame)
        user_logo_label.setObjectName(u"user_logo_label")
        user_logo_label.setGeometry(QRect(10, 10, 54, 54))
        font5 = QFont()
        font5.setFamily(u"Cascadia Code")
        font5.setPointSize(9)
        user_logo_label.setFont(font5)
        user_logo_label.setStyleSheet(u"background-color: #B6D0E2; \n"
        "border-radius: 25px; \n"
        "border: 2px solid #B6D0F7; \n"
        "min-width: 50px; \n"
        "min-height: 50px; \n"
        "max-width: 50px;\n"
        "max-height: 50px; ")
        user_logo_label.setAlignment(Qt.AlignCenter)
        
        
        date = QLabel(fb_frame)
        date.setObjectName(u"date")
        date.setGeometry(QRect(580, 30, 191, 21))
        date.setMinimumSize(QSize(191, 0))
        date.setMaximumSize(QSize(191, 16777215))
        date.setFont(font4)
        date.setLayoutDirection(Qt.LeftToRight)
        date.setStyleSheet(u"border : none;\n")
        date.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        #date.setText(fb_data.get("date", "Unknown"))
        
        # Fetch the date string from fb_data
        date_str = fb_data.get("date", "Unknown")

        # Check if the date is valid and not "Unknown"
        if date_str != "Unknown":
            # Parse the date string to a datetime object
            date_obj = datetime.strptime(date_str, "%y%m%d")
            
            # Format the datetime object to the desired string format
            formatted_date = date_obj.strftime("%d %B %Y")
        else:
            formatted_date = "Unknown"

        # Set the text to the formatted date
        date.setText(formatted_date)

        return fb_frame
        
    def parse_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%y%m%d")
        except ValueError:
            return datetime.min  # return the earliest possible date if parsing fails

    def populate_fb_info(self, search_query=None):
        self.clear_layout()

        visible_fb = []

        # Sort fb_data_list by date in descending order
        sorted_fb_data_list = sorted(self.fb_data_list, key=lambda x: self.parse_date(x.get("date", "000000")), reverse=True)

        for i, fb_data in enumerate(sorted_fb_data_list):
            if isinstance(fb_data, dict):
                user_name = fb_data.get("patient_name", "").lower()

                # Check search query if provided
                if not search_query or search_query.lower() in user_name:
                    fb_frame = self.create_fb_list_frame(fb_data)
                    if fb_frame:
                        visible_fb.append(fb_frame)

        # Add visible clinics to the layout
        for fb_frame in visible_fb:
            self.vLayout.addWidget(fb_frame)

        self.scrollAreaWidgetContents.setLayout(self.vLayout)
        self.vLayout.setAlignment(Qt.AlignTop)
        self.vLayout.update()
        self.scrollAreaWidgetContents.update()
   
    def create_fb_details_frame(self, fb_data):
        fb_outer_frame = QFrame(self.background)
        fb_outer_frame.setObjectName(u"fb_outer_frame")
        fb_outer_frame.setGeometry(QRect(979, 180, 751, 841))
        fb_outer_frame.setStyleSheet(u"border: 1px solid #dcdcdc; border-radius: 8px; margin: 5px;")
        fb_outer_frame.setFrameShape(QFrame.StyledPanel)
        fb_outer_frame.setFrameShadow(QFrame.Raised)
        fb_inner_frame = QFrame(fb_outer_frame)
        fb_inner_frame.setObjectName(u"fb_inner_frame")
        fb_inner_frame.setGeometry(QRect(20, 20, 711, 791))
        fb_inner_frame.setStyleSheet(u" border: none; background-color: transparent;")
        fb_inner_frame.setFrameShape(QFrame.StyledPanel)
        fb_inner_frame.setFrameShadow(QFrame.Raised)
        layoutWidget = QWidget(fb_inner_frame)
        layoutWidget.setObjectName(u"layoutWidget")
        layoutWidget.setGeometry(QRect(0, 140, 715, 651))
        verticalLayout_2 = QVBoxLayout(layoutWidget)
        verticalLayout_2.setObjectName(u"verticalLayout_2")
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        subject_layout = QVBoxLayout()
        subject_layout.setObjectName(u"subject_layout")
        subject_label = QLabel(layoutWidget)
        subject_label.setObjectName(u"subject_label")
        subject_label.setMinimumSize(QSize(711, 0))
        subject_label.setMaximumSize(QSize(711, 16777215))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        subject_label.setFont(font6)
        subject_label.setWordWrap(True)
        subject_label.setText("Subject")
        subject_layout.addWidget(subject_label)

        subject_display = QLabel(layoutWidget)
        subject_display.setObjectName(u"subject_display")
        subject_display.setMinimumSize(QSize(711, 60))
        subject_display.setMaximumSize(QSize(711, 60))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        subject_display.setFont(font6)
        subject_display.setStyleSheet(u"background-color: white; border: none; border-radius: 0; padding-left: 10px;")
        subject_display.setScaledContents(False)
        subject_display.setWordWrap(False)
        subject_display.setText(fb_data.get("subject", "Unknown"))
        subject_layout.addWidget(subject_display)


        verticalLayout_2.addLayout(subject_layout)

        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        verticalLayout_2.addItem(verticalSpacer)

        email_layout = QVBoxLayout()
        email_layout.setObjectName(u"email_layout")
        email_label = QLabel(layoutWidget)
        email_label.setObjectName(u"email_label")
        email_label.setMinimumSize(QSize(711, 0))
        email_label.setMaximumSize(QSize(711, 16777215))
        email_label.setFont(font6)
        email_label.setWordWrap(True)
        email_label.setText("Email")
        email_layout.addWidget(email_label)

        email_display = QLabel(layoutWidget)
        email_display.setObjectName(u"email_display")
        email_display.setMinimumSize(QSize(711, 60))
        email_display.setMaximumSize(QSize(711, 60))
        email_display.setFont(font6)
        email_display.setStyleSheet(u"background-color: white; border: none; border-radius: 0; padding-left: 10px;")
        email_display.setText(fb_data.get("patient_email", "Unknown"))
        email_layout.addWidget(email_display)


        verticalLayout_2.addLayout(email_layout)

        verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        verticalLayout_2.addItem(verticalSpacer_2)

        feeback_layout = QVBoxLayout()
        feeback_layout.setObjectName(u"feeback_layout")
        feedback_label_2 = QLabel(layoutWidget)
        feedback_label_2.setObjectName(u"feedback_label_2")
        feedback_label_2.setMinimumSize(QSize(711, 0))
        feedback_label_2.setMaximumSize(QSize(711, 16777215))
        font6 = QFont()
        font6.setFamily(u"Consolas")
        font6.setPointSize(10)
        feedback_label_2.setFont(font6)
        feedback_label_2.setWordWrap(True)
        feedback_label_2.setText("Feedback")
        feeback_layout.addWidget(feedback_label_2)

        feedback_display = QLabel(layoutWidget)
        feedback_display.setObjectName(u"feedback_display")
        feedback_display.setMinimumSize(QSize(711, 270))
        feedback_display.setMaximumSize(QSize(711, 270))
        feedback_display.setFont(font6)
        feedback_display.setStyleSheet(u"background-color: white; border: none; border-radius: 0; padding-left: 10px;")
        feedback_display.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        feedback_display.setText(fb_data.get("content", "Unknown"))
        feeback_layout.addWidget(feedback_display)


        verticalLayout_2.addLayout(feeback_layout)

        user_logo = QLabel(fb_inner_frame)
        user_logo.setObjectName(u"user_logo")
        user_logo.setGeometry(QRect(10, 10, 64, 64))
        user_logo.setFont(font6)
        user_logo.setStyleSheet(u"background-color: #B6D0E2; "
        "border-radius: 25px;"
        "border: 2px solid #B6D0F7;"
        "min-width: 50px; "
        "min-height: 50px; "
        "max-width: 50px; "
        "max-height: 50px; ")
        user_logo.setAlignment(Qt.AlignCenter)
        user_name = QLabel(fb_inner_frame)
        user_name.setObjectName(u"user_name")
        user_name.setGeometry(QRect(100, 30, 301, 41))
        user_name.setFont(font6)
        user_name.setStyleSheet(u"border : none;\n")
        user_name.setText(fb_data.get("patient_name", "Unknown"))
        line = QFrame(fb_inner_frame)
        line.setObjectName(u"line")
        line.setGeometry(QRect(20, 100, 671, 3))
        line.setMinimumSize(QSize(357, 3))
        line.setMaximumSize(QSize(16777215, 3))
        line.setStyleSheet(u"background-color: #B6D0E2; border: none;")
        line.setFrameShape(QFrame.StyledPanel)
        line.setFrameShadow(QFrame.Raised)
        return fb_outer_frame
    
    def create_popup_widget(self, clinic_data):
        self.hide_fb_details_frame()
        self.fb_details_frame = self.create_fb_details_frame(clinic_data)
        self.fb_details_frame.setVisible(True)

    def search_names(self):
        
        search_text = self.search.text().strip().lower()
        if search_text:
                #print(f"search is {search_text}")
                self.hide_fb_details_frame()
                self.populate_fb_info(search_text)
                self.hide_fb_details_frame()
                
        else:
                self.hide_fb_details_frame()
                self.populate_fb_info()
                self.hide_fb_details_frame()

    def clear_search(self):
        self.search.clear()
        self.hide_fb_details_frame()
        self.populate_fb_info()
        self.hide_fb_details_frame()

    def hide_fb_details_frame(self):
        if self.fb_details_frame:
            self.fb_details_frame.setVisible(False)
        
    def initialize_db(self):
        return db 