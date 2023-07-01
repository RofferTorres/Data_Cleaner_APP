# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_toolzHthLW.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"\n"
"#MenuBtn{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color:\n"
"}\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #222429;\n"
"	color: #eee;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #eee;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"	border: 1px solid #343434;\n"
"	color: #eee;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"	background-color: #303030;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, "
                        "y2:1, stop:0 rgba(89, 89, 89, 255),stop:1 rgba(66, 66, 66, 255));\n"
"	border: 1px solid #000;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #fff;\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #91c9f7;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBar-----*/\n"
"QToolBar\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"	border-top: none;\n"
"	border-bottom: 1px solid #343434;\n"
"	border-left: 1px solid #34343"
                        "4;\n"
"	border-right: 1px solid #343434;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton {\n"
"	text-align: center;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #30353d;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #3573f0;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"	background-color: #3573f0;\n"
"}\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(121, 121, 121, 255),stop:1 rgba(98, 98, 98, 255));\n"
"	color: #eee;\n"
"	border: 2px solid #30353d;\n"
"	border-radius: 4px;\n"
"	padding: 2px;\n"
"	margin-left: 5px\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	background-color: #8b8b8b;\n"
"	\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"	background-color: #353534;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"	background-color: #353534;\n"
"	border: 1px solid gray;\n"
"}\n"
"\n"
"\n"
"/*-----QDockWidget-----*/\n"
""
                        "QDockWidget\n"
"{\n"
"	color: #eee;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QDockWidget > QWidget\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"	border: 1px solid #646564;\n"
"	border-top: none;\n"
"}\n"
"\n"
"\n"
"QDockWidget::title \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(77, 77, 77, 255),stop:0.451923 rgba(64, 64, 64, 255),stop:1 rgba(41, 41, 41, 255));\n"
"	border: 1px solid #646564;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::close-button\n"
"{\n"
"	max-width: 14px;\n"
"	max-height: 14px;\n"
"	margin-top:1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::float-button\n"
"{\n"
"	max-width: 14px;\n"
"	max-height: 14px;\n"
"	margin-top:1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDockWidget::close-button:hover\n"
"{\n"
"	border: none;\n"
"	background-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
""
                        "QDockWidget::float-button:hover\n"
"{\n"
"	border: none;\n"
"	background-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #363636;\n"
"	color : #eee;\n"
"	border: 1px solid #343434;\n"
"	border-radius : 2px;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDoubleSpinBox-----*/\n"
"QSpinBox,\n"
"QDoubleSpinBox \n"
"{\n"
"    background-color: #363636;\n"
"	color : #eee;\n"
"	border: 1px solid #343434;\n"
"	padding: 2px;\n"
"    border-radius : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, \n"
"QDoubleSpinBox::up-button\n"
"{\n"
"	border-top-right-radius:2px;\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, \n"
"QDoubleSpinBox::up-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, \n"
"QDoubleSpinBox::up-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px"
                        ";\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button, \n"
"QDoubleSpinBox::down-button\n"
"{\n"
"	border-bottom-right-radius:2px;\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:hover, \n"
"QDoubleSpinBox::down-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:pressed, \n"
"QDoubleSpinBox::down-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop"
                        ":0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"    border : none;\n"
"    color: white;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"	border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate \n"
"{\n"
"    background-color: #4a4b4d;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"    border: 1px solid #6a6ea9;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"    background-color: #b7b9be;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"    background-color: #b7b9be;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover "
                        "{\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: -2px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(150, 150, 150, 255),stop:1 rgba(107, 107, 107, 255));\n"
"	border-radius: 6px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 17px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #3d3d3d;\n"
"    background-color: #3d3d3d;\n"
"    width: 17px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
""
                        "{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 15px;\n"
"    margin: 16px 0px 16px -2px;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(150, 150, 150, 255),stop:1 rgba(107, 107, 107, 255));\n"
"	border-radius: 6px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #3d3d3d;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
""
                        "\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: 1px solid #3d3d3d;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"	color: #eee;\n"
"	border: 1px solid #343434;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSizeGrip-----*/\n"
"QSizeGrip \n"
"{\n"
"	background-"
                        "color: image(\"./ressources/sizegrip.png\"); /*To replace*/\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"")
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.centralwidget)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setStyleSheet(u"background-color: rgb(48, 53, 61);")
        self.horizontalLayout_2 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftHeaderSection = QFrame(self.headerContainer)
        self.leftHeaderSection.setObjectName(u"leftHeaderSection")
        self.leftHeaderSection.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Arial Narrow"])
        font1.setPointSize(12)
        self.leftHeaderSection.setFont(font1)
        self.leftHeaderSection.setFrameShape(QFrame.NoFrame)
        self.leftHeaderSection.setFrameShadow(QFrame.Raised)
        self.leftHeaderSection.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.leftHeaderSection)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MenuBtn_2 = QPushButton(self.leftHeaderSection)
        self.MenuBtn_2.setObjectName(u"MenuBtn_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuBtn_2.sizePolicy().hasHeightForWidth())
        self.MenuBtn_2.setSizePolicy(sizePolicy)
        self.MenuBtn_2.setMinimumSize(QSize(0, 36))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        self.MenuBtn_2.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuBtn_2.setIcon(icon)
        self.MenuBtn_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.MenuBtn_2)


        self.horizontalLayout_2.addWidget(self.leftHeaderSection, 0, Qt.AlignLeft)

        self.centralHeaderSection = QFrame(self.headerContainer)
        self.centralHeaderSection.setObjectName(u"centralHeaderSection")
        self.centralHeaderSection.setFrameShape(QFrame.NoFrame)
        self.centralHeaderSection.setFrameShadow(QFrame.Plain)
        self.centralHeaderSection.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.centralHeaderSection)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.windowsMainTitle_2 = QLabel(self.centralHeaderSection)
        self.windowsMainTitle_2.setObjectName(u"windowsMainTitle_2")
        font3 = QFont()
        font3.setPointSize(11)
        self.windowsMainTitle_2.setFont(font3)
        self.windowsMainTitle_2.setFrameShape(QFrame.NoFrame)
        self.windowsMainTitle_2.setAlignment(Qt.AlignCenter)
        self.windowsMainTitle_2.setMargin(9)

        self.verticalLayout.addWidget(self.windowsMainTitle_2)


        self.horizontalLayout_2.addWidget(self.centralHeaderSection)

        self.systemBtns = QFrame(self.headerContainer)
        self.systemBtns.setObjectName(u"systemBtns")
        self.systemBtns.setFrameShape(QFrame.NoFrame)
        self.systemBtns.setFrameShadow(QFrame.Raised)
        self.systemBtns.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.systemBtns)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 6, 5, 6)
        self.closeBtn = QPushButton(self.systemBtns)
        self.closeBtn.setObjectName(u"closeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/macos-close-30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/icons/macos-close-30.png", QSize(), QIcon.Normal, QIcon.On)
        icon1.addFile(u":/icons/icons/hover-macos-close-30.png", QSize(), QIcon.Active, QIcon.On)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setIconSize(QSize(15, 15))
        self.closeBtn.setCheckable(True)
        self.closeBtn.setChecked(False)
        self.closeBtn.setAutoRepeat(False)
        self.closeBtn.setAutoRepeatDelay(10)

        self.horizontalLayout_6.addWidget(self.closeBtn)

        self.minimizeBtn = QPushButton(self.systemBtns)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/macos-minimize-30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icons/macos-minimize-30.png", QSize(), QIcon.Normal, QIcon.On)
        icon2.addFile(u":/icons/icons/hover-macos-minimize-30.png", QSize(), QIcon.Active, QIcon.On)
        self.minimizeBtn.setIcon(icon2)
        self.minimizeBtn.setIconSize(QSize(16, 16))
        self.minimizeBtn.setCheckable(True)
        self.minimizeBtn.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.systemBtns)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/macos-full-screen-30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icons/macos-full-screen-30.png", QSize(), QIcon.Normal, QIcon.On)
        icon3.addFile(u":/icons/icons/hover-macos-full-screen-30.png", QSize(), QIcon.Active, QIcon.On)
        self.restoreBtn.setIcon(icon3)
        self.restoreBtn.setIconSize(QSize(16, 16))
        self.restoreBtn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.restoreBtn)


        self.horizontalLayout_2.addWidget(self.systemBtns, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.headerContainer)

        self.lineHeader = QFrame(self.centralwidget)
        self.lineHeader.setObjectName(u"lineHeader")
        self.lineHeader.setFrameShadow(QFrame.Sunken)
        self.lineHeader.setLineWidth(2)
        self.lineHeader.setFrameShape(QFrame.HLine)

        self.verticalLayout_11.addWidget(self.lineHeader)

        self.centralContainer = QWidget(self.centralwidget)
        self.centralContainer.setObjectName(u"centralContainer")
        self.horizontalLayout = QHBoxLayout(self.centralContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralContainer)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.leftMenuContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 0, 0, 0)
        self.leftMenuSubContainer_2 = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer_2.setObjectName(u"leftMenuSubContainer_2")
        self.verticalLayout_7 = QVBoxLayout(self.leftMenuSubContainer_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 2, 0)
        self.frame_5 = QFrame(self.leftMenuSubContainer_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFont(font2)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.homeBtn_2 = QPushButton(self.frame_5)
        self.homeBtn_2.setObjectName(u"homeBtn_2")
        self.homeBtn_2.setMinimumSize(QSize(0, 28))
        self.homeBtn_2.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn_2.setIcon(icon4)
        self.homeBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.homeBtn_2)

        self.settingBtn_2 = QPushButton(self.frame_5)
        self.settingBtn_2.setObjectName(u"settingBtn_2")
        self.settingBtn_2.setMinimumSize(QSize(0, 28))
        self.settingBtn_2.setFont(font2)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn_2.setIcon(icon5)
        self.settingBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.settingBtn_2)

        self.previewBtn_2 = QPushButton(self.frame_5)
        self.previewBtn_2.setObjectName(u"previewBtn_2")
        self.previewBtn_2.setMinimumSize(QSize(0, 28))
        self.previewBtn_2.setFont(font2)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/table.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previewBtn_2.setIcon(icon6)
        self.previewBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.previewBtn_2)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.frame_6 = QFrame(self.leftMenuSubContainer_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.themeBtn_2 = QPushButton(self.frame_6)
        self.themeBtn_2.setObjectName(u"themeBtn_2")
        self.themeBtn_2.setMinimumSize(QSize(0, 28))
        self.themeBtn_2.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/sun.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.themeBtn_2.setIcon(icon7)
        self.themeBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.themeBtn_2)

        self.infoBtn_2 = QPushButton(self.frame_6)
        self.infoBtn_2.setObjectName(u"infoBtn_2")
        self.infoBtn_2.setMinimumSize(QSize(0, 28))
        self.infoBtn_2.setFont(font2)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn_2.setIcon(icon8)
        self.infoBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.infoBtn_2)

        self.helpBtn_2 = QPushButton(self.frame_6)
        self.helpBtn_2.setObjectName(u"helpBtn_2")
        self.helpBtn_2.setMinimumSize(QSize(0, 28))
        self.helpBtn_2.setFont(font2)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn_2.setIcon(icon9)
        self.helpBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.helpBtn_2)


        self.verticalLayout_7.addWidget(self.frame_6, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.leftMenuSubContainer_2)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.lineVertical = QFrame(self.centralContainer)
        self.lineVertical.setObjectName(u"lineVertical")
        self.lineVertical.setFrameShadow(QFrame.Raised)
        self.lineVertical.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.lineVertical)

        self.mainBodyContainer = QWidget(self.centralContainer)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.mainBodyContainer.setMinimumSize(QSize(560, 0))

        self.horizontalLayout.addWidget(self.mainBodyContainer)


        self.verticalLayout_11.addWidget(self.centralContainer)

        self.lineFooter = QFrame(self.centralwidget)
        self.lineFooter.setObjectName(u"lineFooter")
        self.lineFooter.setAutoFillBackground(False)
        self.lineFooter.setStyleSheet(u"color: rgb(48, 53, 61);")
        self.lineFooter.setFrameShadow(QFrame.Sunken)
        self.lineFooter.setLineWidth(2)
        self.lineFooter.setFrameShape(QFrame.HLine)

        self.verticalLayout_11.addWidget(self.lineFooter)

        self.footerContainer = QWidget(self.centralwidget)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 1, -1, 4)
        self.labelFooterLeft = QLabel(self.footerContainer)
        self.labelFooterLeft.setObjectName(u"labelFooterLeft")
        font4 = QFont()
        font4.setPointSize(9)
        self.labelFooterLeft.setFont(font4)

        self.horizontalLayout_3.addWidget(self.labelFooterLeft, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.labelFooterCenter = QLabel(self.footerContainer)
        self.labelFooterCenter.setObjectName(u"labelFooterCenter")
        self.labelFooterCenter.setFont(font4)

        self.horizontalLayout_3.addWidget(self.labelFooterCenter, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.labelFooterRight = QLabel(self.footerContainer)
        self.labelFooterRight.setObjectName(u"labelFooterRight")
        self.labelFooterRight.setFont(font4)

        self.horizontalLayout_3.addWidget(self.labelFooterRight, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.footerContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data Cleaner Tool v0.1a", None))
#if QT_CONFIG(tooltip)
        self.MenuBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.MenuBtn_2.setText("")
        self.windowsMainTitle_2.setText(QCoreApplication.translate("MainWindow", u"Data Cleaner Tool v0.1a", None))
        self.closeBtn.setText("")
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.settingBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Advance options", None))
#endif // QT_CONFIG(tooltip)
        self.settingBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.previewBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Preview", None))
#endif // QT_CONFIG(tooltip)
        self.previewBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.themeBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Change theme", None))
#endif // QT_CONFIG(tooltip)
        self.themeBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.infoBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"More information", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.helpBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn_2.setText("")
        self.labelFooterLeft.setText(QCoreApplication.translate("MainWindow", u"Percorso Esempio: C:.....  >  output_file", None))
        self.labelFooterCenter.setText(QCoreApplication.translate("MainWindow", u"ENCODE: UTF-8", None))
        self.labelFooterRight.setText(QCoreApplication.translate("MainWindow", u"Status o notifiche ", None))
    # retranslateUi

