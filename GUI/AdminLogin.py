"""
Updated: 19 September 2021
TODO: Add Button Functionality
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(1331, 867)

        # Add Transparent Background, Only show the Widget and Not the GUI Frame
        LoginForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LoginForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            LoginForm.sizePolicy().hasHeightForWidth())
        LoginForm.setSizePolicy(sizePolicy)
        LoginForm.setToolTipDuration(0)
        self.LoginContainer = QtWidgets.QWidget(LoginForm)
        self.LoginContainer.setEnabled(True)
        self.LoginContainer.setGeometry(QtCore.QRect(29, 29, 1250, 800))
        self.LoginContainer.setStyleSheet("background-color: transparent;")
        self.LoginContainer.setObjectName("LoginContainer")
        self.LeftSide = QtWidgets.QLabel(self.LoginContainer)
        self.LeftSide.setGeometry(QtCore.QRect(49, 49, 541, 710))
        self.LeftSide.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4F46E5, stop:1#7C3AED);\n"
                                    "border-top-left-radius: 20px;\n"
                                    "border-bottom-left-radius: 20px;")
        self.LeftSide.setText("")
        self.LeftSide.setObjectName("LeftSide")
        self.login_details_container = QtWidgets.QLabel(self.LoginContainer)
        self.login_details_container.setGeometry(
            QtCore.QRect(420, 49, 791, 710))
        self.login_details_container.setToolTipDuration(0)
        self.login_details_container.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "border-top-right-radius: 20px;\n"
                                                   "border-bottom-right-radius: 20px;")
        self.login_details_container.setText("")
        self.login_details_container.setObjectName("login_details_container")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.LoginContainer)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(510, 90, 581, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.LoginTextContainerAdmin = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.LoginTextContainerAdmin.setContentsMargins(0, 0, 0, 0)
        self.LoginTextContainerAdmin.setSpacing(20)
        self.LoginTextContainerAdmin.setObjectName("LoginTextContainerAdmin")
        self.welcome_message_admin = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.welcome_message_admin.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.welcome_message_admin.sizePolicy().hasHeightForWidth())
        self.welcome_message_admin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_message_admin.setFont(font)
        self.welcome_message_admin.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.welcome_message_admin.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_message_admin.setObjectName("welcome_message_admin")
        self.LoginTextContainerAdmin.addWidget(self.welcome_message_admin)
        self.username_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.LoginTextContainerAdmin.addWidget(self.username_label)
        self.username_enter = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.username_enter.sizePolicy().hasHeightForWidth())
        self.username_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.username_enter.setFont(font)
        self.username_enter.setStyleSheet("QLineEdit {\n"
                                          "    border: 10px;\n"
                                          "    border-color: transparent;\n"
                                          "    padding: 0 8px;\n"
                                          "    background: rgba(229, 231, 235, 1);\n"
                                          "    font-size: 16px;\n"
                                          "    border-top-right-radius: 10px;\n"
                                          "    border-top-left-radius: 10px;\n"
                                          "    border-bottom-right-radius: 10px;\n"
                                          "    border-bottom-left-radius: 10px;\n"
                                          "}")
        self.username_enter.setObjectName("username_enter")
        self.LoginTextContainerAdmin.addWidget(self.username_enter)
        self.password_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.LoginTextContainerAdmin.addWidget(self.password_label)
        self.password_enter = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.password_enter.sizePolicy().hasHeightForWidth())
        self.password_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.password_enter.setFont(font)
        self.password_enter.setStyleSheet("QLineEdit {\n"
                                          "    border: 10px;\n"
                                          "    border-color: transparent;\n"
                                          "    padding: 0 8px;\n"
                                          "    background: rgba(229, 231, 235, 1);\n"
                                          "    font-size: 16px;\n"
                                          "    border-top-right-radius: 10px;\n"
                                          "    border-top-left-radius: 10px;\n"
                                          "    border-bottom-right-radius: 10px;\n"
                                          "    border-bottom-left-radius: 10px;\n"
                                          "}")
        self.password_enter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_enter.setObjectName("password_enter")
        self.LoginTextContainerAdmin.addWidget(self.password_enter)
        self.admin_key_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.admin_key_label.setFont(font)
        self.admin_key_label.setObjectName("admin_key_label")
        self.LoginTextContainerAdmin.addWidget(self.admin_key_label)
        self.Admin_key_password = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Admin_key_password.sizePolicy().hasHeightForWidth())
        self.Admin_key_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.Admin_key_password.setFont(font)
        self.Admin_key_password.setStyleSheet("QLineEdit {\n"
                                              "    border: 10px;\n"
                                              "    border-color: transparent;\n"
                                              "    padding: 0 8px;\n"
                                              "    background: rgba(229, 231, 235, 1);\n"
                                              "    font-size: 16px;\n"
                                              "    border-top-right-radius: 10px;\n"
                                              "    border-top-left-radius: 10px;\n"
                                              "    border-bottom-right-radius: 10px;\n"
                                              "    border-bottom-left-radius: 10px;\n"
                                              "}")
        self.Admin_key_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Admin_key_password.setObjectName("Admin_key_password")
        self.LoginTextContainerAdmin.addWidget(self.Admin_key_password)
        self.login_button = QtWidgets.QPushButton(self.LoginContainer)
        self.login_button.setGeometry(QtCore.QRect(650, 560, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.login_button.setFont(font)
        self.login_button.setToolTipDuration(0)
        self.login_button.setStyleSheet("QPushButton#login_button {\n"
                                        "    border-top-right-radius: 10px;\n"
                                        "    border-top-left-radius: 10px;\n"
                                        "    border-bottom-right-radius: 10px;\n"
                                        "    border-bottom-left-radius: 10px;\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 212, 191, 1), stop:1 rgba(6, 182, 212, 1));\n"
                                        "    font-size: 16px;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#login_button:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                        ", stop:1 #0E7490);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#login_button:pressed {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                        ", stop:1 #0E7490);\n"
                                        "    padding-left: 5px;\n"
                                        "    padding-top: 5px;\n"
                                        "}")
        self.login_button.setObjectName("login_button")
        self.label = QtWidgets.QLabel(self.LoginContainer)
        self.label.setGeometry(QtCore.QRect(640, 630, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.LoginContainer)
        self.pushButton.setGeometry(QtCore.QRect(830, 630, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    color: #6366F1;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    color: #4338CA;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")

        self.login_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=15, xOffset=0, yOffset=6))

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.welcome_message_admin.setText(
            _translate("LoginForm", "Welcome Back Admin!"))
        self.username_label.setText(_translate("LoginForm", "Username"))
        self.password_label.setText(_translate("LoginForm", "Password"))
        self.admin_key_label.setText(_translate("LoginForm", "Admin Key"))
        self.login_button.setText(_translate(
            "LoginForm", "Login && Initialise"))
        self.label.setText(_translate("LoginForm", "Not an Administrator?"))
        self.pushButton.setText(_translate("LoginForm", "Go Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())