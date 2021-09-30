import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1914, 1077)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setEnabled(True)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Btn_Toggle.setSizeIncrement(QtCore.QSize(0, 0))
        self.Btn_Toggle.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_Toggle.setStyleSheet("image: url(:/menuBurger/icons8-menu-48.png);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border: 0px solid;\n"
                                      "background-color: rgb(35, 35, 25);\n"
                                      "padding-left: 25px;")
        self.Btn_Toggle.setText("")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.title = QtWidgets.QLabel(self.frame_top)
        self.title.setGeometry(QtCore.QRect(640, 10, 641, 51))
        self.title.setMaximumSize(QtCore.QSize(641, 16777215))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: #C7D2FE;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                           "padding:1px;")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_left_menu)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(20)
        self.btn_page_1.setFont(font)
        self.btn_page_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_1.setStyleSheet("QPushButton {\n"
                                      "    image: url(:/SideBar/icons8-shop-48.png);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "    padding-right: 0px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    \n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2DD4BF, stop:1 #0EA5E9);\n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_3.addWidget(self.btn_page_1)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_left_menu)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(20)
        self.btn_page_2.setFont(font)
        self.btn_page_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_2.setStyleSheet("QPushButton {\n"
                                      "    image: url(:/SideBar/icons8-shopping-cart-48.png);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "    padding-right: 0px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2DD4BF, stop:1 #0EA5E9);\n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_3.addWidget(self.btn_page_2)
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_left_menu)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(20)
        self.btn_page_3.setFont(font)
        self.btn_page_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_3.setStyleSheet("QPushButton {\n"
                                      "    \n"
                                      "    image: url(:/SideBar/icons8-computer-support-48.png);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "    padding-right: 0px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2DD4BF, stop:1 #0EA5E9);\n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.btn_page_3.setObjectName("btn_page_3")
        self.verticalLayout_3.addWidget(self.btn_page_3)
        self.btn_page_4 = QtWidgets.QPushButton(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_page_4.sizePolicy().hasHeightForWidth())
        self.btn_page_4.setSizePolicy(sizePolicy)
        self.btn_page_4.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(20)
        self.btn_page_4.setFont(font)
        self.btn_page_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_4.setStyleSheet("QPushButton {\n"
                                      "    image: url(:/SideBar/icons8-exit-48.png);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "    padding-right: 0px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2DD4BF, stop:1 #0EA5E9);\n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.btn_page_4.setObjectName("btn_page_4")
        self.verticalLayout_3.addWidget(self.btn_page_4)
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_3.addWidget(self.frame_top_menus)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSizeConstraint(
            QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.product_table = QtWidgets.QTableWidget(self.page_1)
        self.product_table.setGeometry(QtCore.QRect(20, 325, 1761, 561))
        self.product_table.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.product_table.setFont(font)
        self.product_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.product_table.setAutoFillBackground(False)
        self.product_table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "alternate-background-color: rgb(241, 245, 249);\n"
                                         "font: 10pt \"8514oem\";\n"
                                         "")
        self.product_table.setFrameShape(QtWidgets.QFrame.Box)
        self.product_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.product_table.setLineWidth(10)
        self.product_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.product_table.setAlternatingRowColors(True)
        self.product_table.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.product_table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.product_table.setIconSize(QtCore.QSize(0, 0))
        self.product_table.setTextElideMode(QtCore.Qt.ElideLeft)
        self.product_table.setRowCount(7)
        self.product_table.setColumnCount(6)
        self.product_table.setObjectName("product_table")
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table.setItem(6, 5, item)
        self.product_table.horizontalHeader().setCascadingSectionResizes(False)
        self.product_table.horizontalHeader().setDefaultSectionSize(270)
        self.product_table.horizontalHeader().setMinimumSectionSize(26)
        self.product_table.horizontalHeader().setStretchLastSection(True)
        self.product_table.verticalHeader().setDefaultSectionSize(87)
        self.product_table.verticalHeader().setSortIndicatorShown(True)
        self.product_table.verticalHeader().setStretchLastSection(False)
        self.submit_query = QtWidgets.QPushButton(self.page_1)
        self.submit_query.setGeometry(QtCore.QRect(1470, 250, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.submit_query.setFont(font)
        self.submit_query.setToolTipDuration(0)
        self.submit_query.setStyleSheet("QPushButton {\n"
                                        "    border-top-right-radius: 10px;\n"
                                        "    border-top-left-radius: 10px;\n"
                                        "    border-bottom-right-radius: 10px;\n"
                                        "    border-bottom-left-radius: 10px;\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 212, 191, 1), stop:1 rgba(6, 182, 212, 1));\n"
                                        "    font: 22px;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                        ", stop:1 #0E7490);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                        ", stop:1 #0E7490);\n"
                                        "    padding-left: 5px;\n"
                                        "    padding-top: 5px;\n"
                                        "}")
        self.submit_query.setObjectName("submit_query")
        self.Categories_label = QtWidgets.QLineEdit(self.page_1)
        self.Categories_label.setGeometry(QtCore.QRect(20, 10, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Categories_label.setFont(font)
        self.Categories_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgba(255, 255, 255, 0);")
        self.Categories_label.setFrame(False)
        self.Categories_label.setObjectName("Categories_label")
        self.category_comboBox = QtWidgets.QComboBox(self.page_1)
        self.category_comboBox.setGeometry(QtCore.QRect(20, 37, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.category_comboBox.sizePolicy().hasHeightForWidth())
        self.category_comboBox.setSizePolicy(sizePolicy)
        self.category_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.category_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.category_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.category_comboBox.setFont(font)
        self.category_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.category_comboBox.setStyleSheet("QComboBox {\n"
                                             "    border: 1px solid gray;\n"
                                             "    border-radius: 10px;\n"
                                             "    padding: 1px 18px 1px 3px;\n"
                                             "    min-width: 6em;\n"
                                             "    font: 16pt \"8514oem\";\n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             "    \n"
                                             "    color: rgb(0, 0, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox:on { /* shift the text when the popup opens */\n"
                                             "    padding-top: 3px;\n"
                                             "    padding-left: 4px;\n"
                                             "    background: white;\n"
                                             "    border-radius: 10px;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox::drop-down {\n"
                                             "    subcontrol-origin: padding;\n"
                                             "    subcontrol-position: top right;\n"
                                             "    width: 15px;\n"
                                             "    background-color:white;\n"
                                             "    border-left-width: 1px;\n"
                                             "    border-left-color: darkgray;\n"
                                             "    border-left-style: solid; /* just a single line */\n"
                                             "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                             "    border-bottom-right-radius: 3px;\n"
                                             "    border-radius: 10px;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                             "    top: 1px;\n"
                                             "    left: 1px;\n"
                                             "}\n"
                                             "QListView\n"
                                             "{\n"
                                             "background-color : #334155;\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "}")
        self.category_comboBox.setEditable(False)
        self.category_comboBox.setFrame(True)
        self.category_comboBox.setObjectName("category_comboBox")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.gradient_backdrop = QtWidgets.QLabel(self.page_1)
        self.gradient_backdrop.setGeometry(QtCore.QRect(10, 0, 1781, 311))
        self.gradient_backdrop.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4F46E5, stop:1 #6D28D9);\n"
                                             "border-radius: 20px;")
        self.gradient_backdrop.setText("")
        self.gradient_backdrop.setObjectName("gradient_backdrop")
        self.Model_label = QtWidgets.QLineEdit(self.page_1)
        self.Model_label.setGeometry(QtCore.QRect(20, 110, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Model_label.setFont(font)
        self.Model_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgba(255, 255, 255, 0);")
        self.Model_label.setFrame(False)
        self.Model_label.setObjectName("Model_label")
        self.Price_label = QtWidgets.QLineEdit(self.page_1)
        self.Price_label.setGeometry(QtCore.QRect(20, 210, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Price_label.setFont(font)
        self.Price_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgba(255, 255, 255, 0);")
        self.Price_label.setFrame(False)
        self.Price_label.setObjectName("Price_label")
        self.model_comboBox = QtWidgets.QComboBox(self.page_1)
        self.model_comboBox.setGeometry(QtCore.QRect(20, 140, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.model_comboBox.sizePolicy().hasHeightForWidth())
        self.model_comboBox.setSizePolicy(sizePolicy)
        self.model_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.model_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.model_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.model_comboBox.setFont(font)
        self.model_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.model_comboBox.setStyleSheet("QComboBox {\n"
                                          "    border: 1px solid gray;\n"
                                          "    border-radius: 10px;\n"
                                          "    padding: 1px 18px 1px 3px;\n"
                                          "    min-width: 6em;\n"
                                          "    font: 16pt \"8514oem\";\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          "    \n"
                                          "    color: rgb(0, 0, 0);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:on { /* shift the text when the popup opens */\n"
                                          "    padding-top: 3px;\n"
                                          "    padding-left: 4px;\n"
                                          "    background: white;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::drop-down {\n"
                                          "    subcontrol-origin: padding;\n"
                                          "    subcontrol-position: top right;\n"
                                          "    width: 15px;\n"
                                          "    background-color:white;\n"
                                          "    border-left-width: 1px;\n"
                                          "    border-left-color: darkgray;\n"
                                          "    border-left-style: solid; /* just a single line */\n"
                                          "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                          "    border-bottom-right-radius: 3px;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                          "    top: 1px;\n"
                                          "    left: 1px;\n"
                                          "}\n"
                                          "QListView\n"
                                          "{\n"
                                          "background-color : #334155;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "}")
        self.model_comboBox.setEditable(False)
        self.model_comboBox.setFrame(True)
        self.model_comboBox.setObjectName("model_comboBox")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.price_comboBox = QtWidgets.QComboBox(self.page_1)
        self.price_comboBox.setGeometry(QtCore.QRect(20, 240, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.price_comboBox.sizePolicy().hasHeightForWidth())
        self.price_comboBox.setSizePolicy(sizePolicy)
        self.price_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.price_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.price_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price_comboBox.setFont(font)
        self.price_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.price_comboBox.setStyleSheet("QComboBox {\n"
                                          "    border: 1px solid gray;\n"
                                          "    border-radius: 10px;\n"
                                          "    padding: 1px 18px 1px 3px;\n"
                                          "    min-width: 6em;\n"
                                          "    font: 16pt \"8514oem\";\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          "    \n"
                                          "    color: rgb(0, 0, 0);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:on { /* shift the text when the popup opens */\n"
                                          "    padding-top: 3px;\n"
                                          "    padding-left: 4px;\n"
                                          "    background: white;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::drop-down {\n"
                                          "    subcontrol-origin: padding;\n"
                                          "    subcontrol-position: top right;\n"
                                          "    width: 15px;\n"
                                          "    background-color:white;\n"
                                          "    border-left-width: 1px;\n"
                                          "    border-left-color: darkgray;\n"
                                          "    border-left-style: solid; /* just a single line */\n"
                                          "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                          "    border-bottom-right-radius: 3px;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                          "    top: 1px;\n"
                                          "    left: 1px;\n"
                                          "}\n"
                                          "QListView\n"
                                          "{\n"
                                          "background-color : #334155;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "}")
        self.price_comboBox.setEditable(False)
        self.price_comboBox.setFrame(True)
        self.price_comboBox.setObjectName("price_comboBox")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.factory_comboBox = QtWidgets.QComboBox(self.page_1)
        self.factory_comboBox.setGeometry(QtCore.QRect(630, 140, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.factory_comboBox.sizePolicy().hasHeightForWidth())
        self.factory_comboBox.setSizePolicy(sizePolicy)
        self.factory_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.factory_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.factory_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.factory_comboBox.setFont(font)
        self.factory_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.factory_comboBox.setStyleSheet("QComboBox {\n"
                                            "    border: 1px solid gray;\n"
                                            "    border-radius: 10px;\n"
                                            "    padding: 1px 18px 1px 3px;\n"
                                            "    min-width: 6em;\n"
                                            "    font: 16pt \"8514oem\";\n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            "    \n"
                                            "    color: rgb(0, 0, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox:on { /* shift the text when the popup opens */\n"
                                            "    padding-top: 3px;\n"
                                            "    padding-left: 4px;\n"
                                            "    background: white;\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox::drop-down {\n"
                                            "    subcontrol-origin: padding;\n"
                                            "    subcontrol-position: top right;\n"
                                            "    width: 15px;\n"
                                            "    background-color:white;\n"
                                            "    border-left-width: 1px;\n"
                                            "    border-left-color: darkgray;\n"
                                            "    border-left-style: solid; /* just a single line */\n"
                                            "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                            "    border-bottom-right-radius: 3px;\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                            "    top: 1px;\n"
                                            "    left: 1px;\n"
                                            "}\n"
                                            "QListView\n"
                                            "{\n"
                                            "background-color : #334155;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "}")
        self.factory_comboBox.setEditable(False)
        self.factory_comboBox.setFrame(True)
        self.factory_comboBox.setObjectName("factory_comboBox")
        self.factory_comboBox.addItem("")
        self.factory_comboBox.addItem("")
        self.factory_comboBox.addItem("")
        self.Factory_label = QtWidgets.QLineEdit(self.page_1)
        self.Factory_label.setGeometry(QtCore.QRect(630, 110, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Factory_label.setFont(font)
        self.Factory_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(255, 255, 255, 0);")
        self.Factory_label.setFrame(False)
        self.Factory_label.setObjectName("Factory_label")
        self.production_year_label = QtWidgets.QLineEdit(self.page_1)
        self.production_year_label.setGeometry(QtCore.QRect(630, 210, 191, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.production_year_label.setFont(font)
        self.production_year_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "background-color: rgba(255, 255, 255, 0);")
        self.production_year_label.setFrame(False)
        self.production_year_label.setObjectName("production_year_label")
        self.colour_comboBox = QtWidgets.QComboBox(self.page_1)
        self.colour_comboBox.setGeometry(QtCore.QRect(630, 37, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.colour_comboBox.sizePolicy().hasHeightForWidth())
        self.colour_comboBox.setSizePolicy(sizePolicy)
        self.colour_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.colour_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.colour_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.colour_comboBox.setFont(font)
        self.colour_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.colour_comboBox.setStyleSheet("QComboBox {\n"
                                           "    border: 1px solid gray;\n"
                                           "    border-radius: 10px;\n"
                                           "    padding: 1px 18px 1px 3px;\n"
                                           "    min-width: 6em;\n"
                                           "    font: 16pt \"8514oem\";\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    \n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox:on { /* shift the text when the popup opens */\n"
                                           "    padding-top: 3px;\n"
                                           "    padding-left: 4px;\n"
                                           "    background: white;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox::drop-down {\n"
                                           "    subcontrol-origin: padding;\n"
                                           "    subcontrol-position: top right;\n"
                                           "    width: 15px;\n"
                                           "    background-color:white;\n"
                                           "    border-left-width: 1px;\n"
                                           "    border-left-color: darkgray;\n"
                                           "    border-left-style: solid; /* just a single line */\n"
                                           "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                           "    border-bottom-right-radius: 3px;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                           "    top: 1px;\n"
                                           "    left: 1px;\n"
                                           "}\n"
                                           "QListView\n"
                                           "{\n"
                                           "background-color : #334155;\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "}")
        self.colour_comboBox.setEditable(False)
        self.colour_comboBox.setFrame(True)
        self.colour_comboBox.setObjectName("colour_comboBox")
        self.colour_comboBox.addItem("")
        self.colour_comboBox.addItem("")
        self.colour_comboBox.addItem("")
        self.colour_comboBox.addItem("")
        self.colour_comboBox.addItem("")
        self.Colour_label = QtWidgets.QLineEdit(self.page_1)
        self.Colour_label.setGeometry(QtCore.QRect(630, 10, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Colour_label.setFont(font)
        self.Colour_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(255, 255, 255, 0);")
        self.Colour_label.setFrame(False)
        self.Colour_label.setObjectName("Colour_label")
        self.production_year_comboBox = QtWidgets.QComboBox(self.page_1)
        self.production_year_comboBox.setGeometry(
            QtCore.QRect(630, 240, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.production_year_comboBox.sizePolicy().hasHeightForWidth())
        self.production_year_comboBox.setSizePolicy(sizePolicy)
        self.production_year_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.production_year_comboBox.setMaximumSize(
            QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.production_year_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.production_year_comboBox.setFont(font)
        self.production_year_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.production_year_comboBox.setStyleSheet("QComboBox {\n"
                                                    "    border: 1px solid gray;\n"
                                                    "    border-radius: 10px;\n"
                                                    "    padding: 1px 18px 1px 3px;\n"
                                                    "    min-width: 6em;\n"
                                                    "    font: 16pt \"8514oem\";\n"
                                                    "    background-color: rgb(255, 255, 255);\n"
                                                    "    \n"
                                                    "    color: rgb(0, 0, 0);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QComboBox:on { /* shift the text when the popup opens */\n"
                                                    "    padding-top: 3px;\n"
                                                    "    padding-left: 4px;\n"
                                                    "    background: white;\n"
                                                    "    border-radius: 10px;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QComboBox::drop-down {\n"
                                                    "    subcontrol-origin: padding;\n"
                                                    "    subcontrol-position: top right;\n"
                                                    "    width: 15px;\n"
                                                    "    background-color:white;\n"
                                                    "    border-left-width: 1px;\n"
                                                    "    border-left-color: darkgray;\n"
                                                    "    border-left-style: solid; /* just a single line */\n"
                                                    "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                                    "    border-bottom-right-radius: 3px;\n"
                                                    "    border-radius: 10px;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                                    "    top: 1px;\n"
                                                    "    left: 1px;\n"
                                                    "}\n"
                                                    "QListView\n"
                                                    "{\n"
                                                    "background-color : #334155;\n"
                                                    "color: rgb(255, 255, 255);\n"
                                                    "}")
        self.production_year_comboBox.setEditable(False)
        self.production_year_comboBox.setFrame(True)
        self.production_year_comboBox.setObjectName("production_year_comboBox")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.Power_supply_label = QtWidgets.QLineEdit(self.page_1)
        self.Power_supply_label.setGeometry(QtCore.QRect(1250, 10, 151, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Power_supply_label.setFont(font)
        self.Power_supply_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "background-color: rgba(255, 255, 255, 0);")
        self.Power_supply_label.setFrame(False)
        self.Power_supply_label.setObjectName("Power_supply_label")
        self.power_supply_comboBox = QtWidgets.QComboBox(self.page_1)
        self.power_supply_comboBox.setGeometry(QtCore.QRect(1250, 37, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.power_supply_comboBox.sizePolicy().hasHeightForWidth())
        self.power_supply_comboBox.setSizePolicy(sizePolicy)
        self.power_supply_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.power_supply_comboBox.setMaximumSize(
            QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.power_supply_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.power_supply_comboBox.setFont(font)
        self.power_supply_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.power_supply_comboBox.setStyleSheet("QComboBox {\n"
                                                 "    border: 1px solid gray;\n"
                                                 "    border-radius: 10px;\n"
                                                 "    padding: 1px 18px 1px 3px;\n"
                                                 "    min-width: 6em;\n"
                                                 "    font: 16pt \"8514oem\";\n"
                                                 "    background-color: rgb(255, 255, 255);\n"
                                                 "    \n"
                                                 "    color: rgb(0, 0, 0);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox:on { /* shift the text when the popup opens */\n"
                                                 "    padding-top: 3px;\n"
                                                 "    padding-left: 4px;\n"
                                                 "    background: white;\n"
                                                 "    border-radius: 10px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox::drop-down {\n"
                                                 "    subcontrol-origin: padding;\n"
                                                 "    subcontrol-position: top right;\n"
                                                 "    width: 15px;\n"
                                                 "    background-color:white;\n"
                                                 "    border-left-width: 1px;\n"
                                                 "    border-left-color: darkgray;\n"
                                                 "    border-left-style: solid; /* just a single line */\n"
                                                 "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                                 "    border-bottom-right-radius: 3px;\n"
                                                 "    border-radius: 10px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                                 "    top: 1px;\n"
                                                 "    left: 1px;\n"
                                                 "}\n"
                                                 "QListView\n"
                                                 "{\n"
                                                 "background-color : #334155;\n"
                                                 "color: rgb(255, 255, 255);\n"
                                                 "}")
        self.power_supply_comboBox.setEditable(False)
        self.power_supply_comboBox.setFrame(True)
        self.power_supply_comboBox.setObjectName("power_supply_comboBox")
        self.power_supply_comboBox.addItem("")
        self.power_supply_comboBox.addItem("")
        self.Warranty_label = QtWidgets.QLineEdit(self.page_1)
        self.Warranty_label.setGeometry(QtCore.QRect(1250, 113, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Warranty_label.setFont(font)
        self.Warranty_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color: rgba(255, 255, 255, 0);")
        self.Warranty_label.setFrame(False)
        self.Warranty_label.setObjectName("Warranty_label")
        self.warranty_comboBox = QtWidgets.QComboBox(self.page_1)
        self.warranty_comboBox.setGeometry(QtCore.QRect(1250, 140, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.warranty_comboBox.sizePolicy().hasHeightForWidth())
        self.warranty_comboBox.setSizePolicy(sizePolicy)
        self.warranty_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.warranty_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.warranty_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.warranty_comboBox.setFont(font)
        self.warranty_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.warranty_comboBox.setStyleSheet("QComboBox {\n"
                                             "    border: 1px solid gray;\n"
                                             "    border-radius: 10px;\n"
                                             "    padding: 1px 18px 1px 3px;\n"
                                             "    min-width: 6em;\n"
                                             "    font: 16pt \"8514oem\";\n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             "    \n"
                                             "    color: rgb(0, 0, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox:on { /* shift the text when the popup opens */\n"
                                             "    padding-top: 3px;\n"
                                             "    padding-left: 4px;\n"
                                             "    background: white;\n"
                                             "    border-radius: 10px;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox::drop-down {\n"
                                             "    subcontrol-origin: padding;\n"
                                             "    subcontrol-position: top right;\n"
                                             "    width: 15px;\n"
                                             "    background-color:white;\n"
                                             "    border-left-width: 1px;\n"
                                             "    border-left-color: darkgray;\n"
                                             "    border-left-style: solid; /* just a single line */\n"
                                             "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                             "    border-bottom-right-radius: 3px;\n"
                                             "    border-radius: 10px;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                             "    top: 1px;\n"
                                             "    left: 1px;\n"
                                             "}\n"
                                             "QListView\n"
                                             "{\n"
                                             "background-color : #334155;\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "}")
        self.warranty_comboBox.setEditable(False)
        self.warranty_comboBox.setFrame(True)
        self.warranty_comboBox.setObjectName("warranty_comboBox")
        self.warranty_comboBox.addItem("")
        self.warranty_comboBox.addItem("")
        self.warranty_comboBox.addItem("")
        self.warranty_comboBox.addItem("")
        self.gradient_backdrop.raise_()
        self.product_table.raise_()
        self.submit_query.raise_()
        self.Categories_label.raise_()
        self.category_comboBox.raise_()
        self.Model_label.raise_()
        self.Price_label.raise_()
        self.model_comboBox.raise_()
        self.price_comboBox.raise_()
        self.factory_comboBox.raise_()
        self.Factory_label.raise_()
        self.production_year_label.raise_()
        self.colour_comboBox.raise_()
        self.Colour_label.raise_()
        self.production_year_comboBox.raise_()
        self.Power_supply_label.raise_()
        self.power_supply_comboBox.raise_()
        self.Warranty_label.raise_()
        self.warranty_comboBox.raise_()
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.item_table = QtWidgets.QTableWidget(self.page_2)
        self.item_table.setGeometry(QtCore.QRect(20, 215, 1761, 671))
        self.item_table.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.item_table.setFont(font)
        self.item_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_table.setAutoFillBackground(False)
        self.item_table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "alternate-background-color: rgb(241, 245, 249);\n"
                                      "font: 10pt \"8514oem\";\n"
                                      "")
        self.item_table.setFrameShape(QtWidgets.QFrame.Box)
        self.item_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.item_table.setLineWidth(10)
        self.item_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.item_table.setAlternatingRowColors(True)
        self.item_table.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.item_table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.item_table.setIconSize(QtCore.QSize(0, 0))
        self.item_table.setTextElideMode(QtCore.Qt.ElideLeft)
        self.item_table.setRowCount(1)
        self.item_table.setColumnCount(11)
        self.item_table.setObjectName("item_table")
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setItem(0, 3, item)
        self.item_table.horizontalHeader().setCascadingSectionResizes(False)
        self.item_table.horizontalHeader().setDefaultSectionSize(168)
        self.item_table.horizontalHeader().setMinimumSectionSize(26)
        self.item_table.horizontalHeader().setSortIndicatorShown(True)
        self.item_table.horizontalHeader().setStretchLastSection(False)
        self.item_table.verticalHeader().setDefaultSectionSize(81)
        self.item_table.verticalHeader().setSortIndicatorShown(True)
        self.item_table.verticalHeader().setStretchLastSection(False)
        self.fetch_orders_button = QtWidgets.QPushButton(self.page_2)
        self.fetch_orders_button.setGeometry(QtCore.QRect(20, 130, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fetch_orders_button.setFont(font)
        self.fetch_orders_button.setToolTipDuration(0)
        self.fetch_orders_button.setStyleSheet("QPushButton {\n"
                                               "    border-top-right-radius: 10px;\n"
                                               "    border-top-left-radius: 10px;\n"
                                               "    border-bottom-right-radius: 10px;\n"
                                               "    border-bottom-left-radius: 10px;\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #F59E0B, stop:1#E11D48);\n"
                                               "    font: 22px;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #B45309\n"
                                               ", stop:1 #9F1239);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #B45309\n"
                                               ", stop:1 #9F1239);\n"
                                               "    padding-left: 5px;\n"
                                               "    padding-top: 5px;\n"
                                               "}")
        self.fetch_orders_button.setObjectName("fetch_orders_button")
        self.my_purchases_label = QtWidgets.QLabel(self.page_2)
        self.my_purchases_label.setGeometry(QtCore.QRect(670, 0, 411, 91))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(25)
        self.my_purchases_label.setFont(font)
        self.my_purchases_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "image: url(:/SideBar/icons8-shopping-cart-48.png);\n"
                                              "padding-right:50px;")
        self.my_purchases_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.my_purchases_label.setObjectName("my_purchases_label")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.my_requests_label = QtWidgets.QLabel(self.page_3)
        self.my_requests_label.setGeometry(QtCore.QRect(670, 0, 411, 91))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(25)
        self.my_requests_label.setFont(font)
        self.my_requests_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "image: url(:/SideBar/icons8-computer-support-48.png);\n"
                                             "padding-right:50px;")
        self.my_requests_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.my_requests_label.setObjectName("my_requests_label")
        self.requests_table = QtWidgets.QTableWidget(self.page_3)
        self.requests_table.setGeometry(QtCore.QRect(20, 215, 1761, 671))
        self.requests_table.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.requests_table.setFont(font)
        self.requests_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.requests_table.setAutoFillBackground(False)
        self.requests_table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "alternate-background-color: rgb(241, 245, 249);\n"
                                          "font: 10pt \"8514oem\";\n"
                                          "")
        self.requests_table.setFrameShape(QtWidgets.QFrame.Box)
        self.requests_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.requests_table.setLineWidth(10)
        self.requests_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.requests_table.setAlternatingRowColors(True)
        self.requests_table.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.requests_table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.requests_table.setIconSize(QtCore.QSize(0, 0))
        self.requests_table.setTextElideMode(QtCore.Qt.ElideLeft)
        self.requests_table.setRowCount(1)
        self.requests_table.setColumnCount(6)
        self.requests_table.setObjectName("requests_table")
        item = QtWidgets.QTableWidgetItem()
        self.requests_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.requests_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.requests_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.requests_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.requests_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.requests_table.setHorizontalHeaderItem(5, item)
        self.requests_table.horizontalHeader().setCascadingSectionResizes(False)
        self.requests_table.horizontalHeader().setDefaultSectionSize(282)
        self.requests_table.horizontalHeader().setMinimumSectionSize(26)
        self.requests_table.horizontalHeader().setSortIndicatorShown(True)
        self.requests_table.horizontalHeader().setStretchLastSection(False)
        self.requests_table.verticalHeader().setDefaultSectionSize(81)
        self.requests_table.verticalHeader().setSortIndicatorShown(True)
        self.requests_table.verticalHeader().setStretchLastSection(False)
        self.view_requests_button = QtWidgets.QPushButton(self.page_3)
        self.view_requests_button.setGeometry(QtCore.QRect(20, 130, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.view_requests_button.setFont(font)
        self.view_requests_button.setToolTipDuration(0)
        self.view_requests_button.setStyleSheet("QPushButton {\n"
                                                "    border-top-right-radius: 10px;\n"
                                                "    border-top-left-radius: 10px;\n"
                                                "    border-bottom-right-radius: 10px;\n"
                                                "    border-bottom-left-radius: 10px;\n"
                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #6366F1, stop:1#7C3AED);\n"
                                                "    font: 22px;\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3730A3\n"
                                                ", stop:1 #5B21B6);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3730A3\n"
                                                ", stop:1 #5B21B6);\n"
                                                "    padding-left: 5px;\n"
                                                "    padding-top: 5px;\n"
                                                "}")
        self.view_requests_button.setObjectName("view_requests_button")
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Lights & Locks"))
        self.btn_page_1.setText(_translate(
            "MainWindow", "                 Shop"))
        self.btn_page_2.setText(_translate(
            "MainWindow", "                  Purchases"))
        self.btn_page_3.setText(_translate(
            "MainWindow", "                 Requests"))
        self.btn_page_4.setText(_translate(
            "MainWindow", "                 Exit"))
        self.product_table.setSortingEnabled(True)
        item = self.product_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Categories"))
        item = self.product_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Model"))
        item = self.product_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Warranty"))
        item = self.product_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.product_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Inverntory Level"))
        item = self.product_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Purchase Now"))
        __sortingEnabled = self.product_table.isSortingEnabled()
        self.product_table.setSortingEnabled(False)
        self.product_table.setSortingEnabled(__sortingEnabled)
        self.submit_query.setText(_translate("MainWindow", "Submit"))
        self.Categories_label.setText(_translate("MainWindow", "Categories"))
        self.category_comboBox.setCurrentText(
            _translate("MainWindow", "Locks"))
        self.category_comboBox.setItemText(
            0, _translate("MainWindow", "Locks"))
        self.category_comboBox.setItemText(
            1, _translate("MainWindow", "Lights"))
        self.Model_label.setText(_translate("MainWindow", "Models"))
        self.Price_label.setText(_translate("MainWindow", "Price"))
        self.model_comboBox.setCurrentText(_translate("MainWindow", "Light1"))
        self.model_comboBox.setItemText(0, _translate("MainWindow", "Light1"))
        self.model_comboBox.setItemText(1, _translate("MainWindow", "Light2"))
        self.model_comboBox.setItemText(
            2, _translate("MainWindow", "SmartHome1"))
        self.model_comboBox.setItemText(3, _translate("MainWindow", "Safe1"))
        self.model_comboBox.setItemText(4, _translate("MainWindow", "Safe2"))
        self.price_comboBox.setCurrentText(_translate("MainWindow", "$50"))
        self.price_comboBox.setItemText(0, _translate("MainWindow", "$50"))
        self.price_comboBox.setItemText(1, _translate("MainWindow", "$60"))
        self.price_comboBox.setItemText(2, _translate("MainWindow", "$100"))
        self.price_comboBox.setItemText(3, _translate("MainWindow", "$120"))
        self.price_comboBox.setItemText(4, _translate("MainWindow", "$125"))
        self.price_comboBox.setItemText(5, _translate("MainWindow", "$200"))
        self.factory_comboBox.setCurrentText(_translate("MainWindow", "China"))
        self.factory_comboBox.setItemText(0, _translate("MainWindow", "China"))
        self.factory_comboBox.setItemText(
            1, _translate("MainWindow", "Malaysia"))
        self.factory_comboBox.setItemText(
            2, _translate("MainWindow", "Philippines"))
        self.Factory_label.setText(_translate("MainWindow", "Factory"))
        self.production_year_label.setText(
            _translate("MainWindow", "Production year"))
        self.colour_comboBox.setCurrentText(_translate("MainWindow", "Blue"))
        self.colour_comboBox.setItemText(0, _translate("MainWindow", "Blue"))
        self.colour_comboBox.setItemText(1, _translate("MainWindow", "Black"))
        self.colour_comboBox.setItemText(2, _translate("MainWindow", "Green"))
        self.colour_comboBox.setItemText(3, _translate("MainWindow", "Yellow"))
        self.colour_comboBox.setItemText(4, _translate("MainWindow", "White"))
        self.Colour_label.setText(_translate("MainWindow", "Colour"))
        self.production_year_comboBox.setCurrentText(
            _translate("MainWindow", "2014"))
        self.production_year_comboBox.setItemText(
            0, _translate("MainWindow", "2014"))
        self.production_year_comboBox.setItemText(
            1, _translate("MainWindow", "2015"))
        self.production_year_comboBox.setItemText(
            2, _translate("MainWindow", "2016"))
        self.production_year_comboBox.setItemText(
            3, _translate("MainWindow", "2017"))
        self.production_year_comboBox.setItemText(
            4, _translate("MainWindow", "2019"))
        self.production_year_comboBox.setItemText(
            5, _translate("MainWindow", "2020"))
        self.Power_supply_label.setText(
            _translate("MainWindow", "Power Supply"))
        self.power_supply_comboBox.setCurrentText(
            _translate("MainWindow", "Battery"))
        self.power_supply_comboBox.setItemText(
            0, _translate("MainWindow", "Battery"))
        self.power_supply_comboBox.setItemText(
            1, _translate("MainWindow", "USB"))
        self.Warranty_label.setText(_translate("MainWindow", "Warranty"))
        self.warranty_comboBox.setCurrentText(_translate("MainWindow", "6"))
        self.warranty_comboBox.setItemText(0, _translate("MainWindow", "6"))
        self.warranty_comboBox.setItemText(1, _translate("MainWindow", "8"))
        self.warranty_comboBox.setItemText(2, _translate("MainWindow", "10"))
        self.warranty_comboBox.setItemText(3, _translate("MainWindow", "12"))
        self.item_table.setSortingEnabled(True)
        item = self.item_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item ID"))
        item = self.item_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Request Now"))
        item = self.item_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.item_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Purchase Date"))
        item = self.item_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Warranty End"))
        item = self.item_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Warranty"))
        item = self.item_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Color"))
        item = self.item_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Category"))
        item = self.item_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Factory"))
        item = self.item_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Model"))
        item = self.item_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Power Supply"))
        __sortingEnabled = self.item_table.isSortingEnabled()
        self.item_table.setSortingEnabled(False)
        self.item_table.setSortingEnabled(__sortingEnabled)
        self.fetch_orders_button.setText(
            _translate("MainWindow", "Fetch Purchases"))
        self.my_purchases_label.setText(
            _translate("MainWindow", "My Purchases"))
        self.my_requests_label.setText(_translate("MainWindow", "My Requests"))
        self.requests_table.setSortingEnabled(True)
        item = self.requests_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item ID"))
        item = self.requests_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Admin ID"))
        item = self.requests_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Request Date"))
        item = self.requests_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        item = self.requests_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cancel"))
        item = self.requests_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Pay Service Fee"))
        self.view_requests_button.setText(
            _translate("MainWindow", "View Requests"))
