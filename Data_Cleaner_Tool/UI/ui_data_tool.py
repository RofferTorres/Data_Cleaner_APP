# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_tooleZEwtC.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
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
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(False)
        self.mainWidget = QWidget(MainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.verticalLayout_11 = QVBoxLayout(self.mainWidget)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainWidget)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0.00568182, stop:0 rgba(54, 61, 70, 255), stop:0.502463 rgba(43, 46, 54, 255), stop:1 rgba(54, 61, 70, 255));")
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
        self.leftHeaderSection.setStyleSheet(u"background-color:transparent;")
        self.leftHeaderSection.setFrameShape(QFrame.NoFrame)
        self.leftHeaderSection.setFrameShadow(QFrame.Raised)
        self.leftHeaderSection.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.leftHeaderSection)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 0, 0, 0)
        self.MenuBtn = QPushButton(self.leftHeaderSection)
        self.MenuBtn.setObjectName(u"MenuBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuBtn.sizePolicy().hasHeightForWidth())
        self.MenuBtn.setSizePolicy(sizePolicy)
        self.MenuBtn.setMinimumSize(QSize(0, 36))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        self.MenuBtn.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuBtn.setIcon(icon)
        self.MenuBtn.setIconSize(QSize(32, 32))
        self.MenuBtn.setCheckable(True)
        self.MenuBtn.setChecked(True)

        self.horizontalLayout_5.addWidget(self.MenuBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.leftHeaderSection, 0, Qt.AlignLeft)

        self.centralHeaderSection = QFrame(self.headerContainer)
        self.centralHeaderSection.setObjectName(u"centralHeaderSection")
        self.centralHeaderSection.setStyleSheet(u"background-color:transparent;")
        self.centralHeaderSection.setFrameShape(QFrame.NoFrame)
        self.centralHeaderSection.setFrameShadow(QFrame.Plain)
        self.centralHeaderSection.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.centralHeaderSection)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.windowsMainTitle = QLabel(self.centralHeaderSection)
        self.windowsMainTitle.setObjectName(u"windowsMainTitle")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.windowsMainTitle.setFont(font3)
        self.windowsMainTitle.setFrameShape(QFrame.NoFrame)
        self.windowsMainTitle.setAlignment(Qt.AlignCenter)
        self.windowsMainTitle.setMargin(9)

        self.verticalLayout.addWidget(self.windowsMainTitle)


        self.horizontalLayout_2.addWidget(self.centralHeaderSection)

        self.systemBtns = QFrame(self.headerContainer)
        self.systemBtns.setObjectName(u"systemBtns")
        self.systemBtns.setStyleSheet(u"background-color:transparent;")
        self.systemBtns.setFrameShape(QFrame.NoFrame)
        self.systemBtns.setFrameShadow(QFrame.Raised)
        self.systemBtns.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.systemBtns)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 6, 5, 6)
        self.closeBtn = QPushButton(self.systemBtns)
        self.closeBtn.setObjectName(u"closeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/closeIconMacOS.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setIconSize(QSize(14, 14))
        self.closeBtn.setCheckable(True)
        self.closeBtn.setChecked(False)
        self.closeBtn.setAutoRepeat(False)
        self.closeBtn.setAutoRepeatDelay(10)

        self.horizontalLayout_6.addWidget(self.closeBtn)

        self.minimizeBtn = QPushButton(self.systemBtns)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/minimizeIconMacOS.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon2)
        self.minimizeBtn.setIconSize(QSize(14, 14))
        self.minimizeBtn.setCheckable(True)
        self.minimizeBtn.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.systemBtns)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/fullscreenIconMacOS.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon3)
        self.restoreBtn.setIconSize(QSize(14, 14))
        self.restoreBtn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.restoreBtn)


        self.horizontalLayout_2.addWidget(self.systemBtns, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.headerContainer)

        self.lineHeader = QFrame(self.mainWidget)
        self.lineHeader.setObjectName(u"lineHeader")
        self.lineHeader.setFrameShadow(QFrame.Sunken)
        self.lineHeader.setLineWidth(2)
        self.lineHeader.setFrameShape(QFrame.HLine)

        self.verticalLayout_11.addWidget(self.lineHeader)

        self.centralContainer = QWidget(self.mainWidget)
        self.centralContainer.setObjectName(u"centralContainer")
        self.horizontalLayout = QHBoxLayout(self.centralContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralContainer)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QSize(28, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.leftMenuContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setMaximumSize(QSize(16777215, 16777215))
        self.leftMenuSubContainer.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.leftMenuSubContainer)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        self.frame_5.setFont(font4)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_5)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy1)
        self.homeBtn.setMinimumSize(QSize(160, 28))
        self.homeBtn.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(13)
        self.homeBtn.setFont(font5)
        self.homeBtn.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon4)
        self.homeBtn.setIconSize(QSize(24, 24))
        self.homeBtn.setCheckable(False)
        self.homeBtn.setAutoDefault(False)

        self.verticalLayout_9.addWidget(self.homeBtn)

        self.editBtn = QPushButton(self.frame_5)
        self.editBtn.setObjectName(u"editBtn")
        sizePolicy1.setHeightForWidth(self.editBtn.sizePolicy().hasHeightForWidth())
        self.editBtn.setSizePolicy(sizePolicy1)
        self.editBtn.setMinimumSize(QSize(160, 28))
        self.editBtn.setMaximumSize(QSize(16777215, 16777215))
        self.editBtn.setFont(font5)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editBtn.setIcon(icon5)
        self.editBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.editBtn)

        self.previewBtn = QPushButton(self.frame_5)
        self.previewBtn.setObjectName(u"previewBtn")
        sizePolicy1.setHeightForWidth(self.previewBtn.sizePolicy().hasHeightForWidth())
        self.previewBtn.setSizePolicy(sizePolicy1)
        self.previewBtn.setMinimumSize(QSize(160, 28))
        self.previewBtn.setMaximumSize(QSize(16777215, 16777215))
        self.previewBtn.setFont(font5)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/table.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previewBtn.setIcon(icon6)
        self.previewBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.previewBtn)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.verticalSpacer = QSpacerItem(28, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.frame_6 = QFrame(self.leftMenuSubContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.settingBtn = QPushButton(self.frame_6)
        self.settingBtn.setObjectName(u"settingBtn")
        sizePolicy1.setHeightForWidth(self.settingBtn.sizePolicy().hasHeightForWidth())
        self.settingBtn.setSizePolicy(sizePolicy1)
        self.settingBtn.setMinimumSize(QSize(160, 28))
        self.settingBtn.setMaximumSize(QSize(16777215, 16777215))
        self.settingBtn.setFont(font5)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon7)
        self.settingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.settingBtn)

        self.infoBtn = QPushButton(self.frame_6)
        self.infoBtn.setObjectName(u"infoBtn")
        sizePolicy1.setHeightForWidth(self.infoBtn.sizePolicy().hasHeightForWidth())
        self.infoBtn.setSizePolicy(sizePolicy1)
        self.infoBtn.setMinimumSize(QSize(160, 28))
        self.infoBtn.setMaximumSize(QSize(16777215, 16777215))
        self.infoBtn.setFont(font5)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon8)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_6)
        self.helpBtn.setObjectName(u"helpBtn")
        sizePolicy1.setHeightForWidth(self.helpBtn.sizePolicy().hasHeightForWidth())
        self.helpBtn.setSizePolicy(sizePolicy1)
        self.helpBtn.setMinimumSize(QSize(160, 28))
        self.helpBtn.setMaximumSize(QSize(16777215, 16777215))
        self.helpBtn.setFont(font5)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon9)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.helpBtn)


        self.verticalLayout_7.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.leftMenuSubContainer)


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
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_2.setSpacing(45)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(45, 45, 45, 12)
        self.dropBoxFrame = QFrame(self.mainBodyContainer)
        self.dropBoxFrame.setObjectName(u"dropBoxFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(7)
        sizePolicy3.setHeightForWidth(self.dropBoxFrame.sizePolicy().hasHeightForWidth())
        self.dropBoxFrame.setSizePolicy(sizePolicy3)
        self.dropBoxFrame.setAcceptDrops(True)
        self.dropBoxFrame.setFrameShape(QFrame.StyledPanel)
        self.dropBoxFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.dropBoxFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(12, 45, -1, 45)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.uploadIcon = QLabel(self.dropBoxFrame)
        self.uploadIcon.setObjectName(u"uploadIcon")
        self.uploadIcon.setMinimumSize(QSize(88, 88))
        self.uploadIcon.setMaximumSize(QSize(88, 88))
        self.uploadIcon.setTextFormat(Qt.AutoText)
        self.uploadIcon.setPixmap(QPixmap(u":/icons/icons/uploadDocument.png"))
        self.uploadIcon.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.uploadIcon, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.dragLabel = QLabel(self.dropBoxFrame)
        self.dragLabel.setObjectName(u"dragLabel")
        font6 = QFont()
        font6.setFamilies([u"Tahoma"])
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setUnderline(False)
        self.dragLabel.setFont(font6)

        self.verticalLayout_3.addWidget(self.dragLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.browseFileLabel = QLabel(self.dropBoxFrame)
        self.browseFileLabel.setObjectName(u"browseFileLabel")
        font7 = QFont()
        font7.setFamilies([u"Tahoma"])
        font7.setPointSize(16)
        font7.setItalic(True)
        self.browseFileLabel.setFont(font7)

        self.verticalLayout_3.addWidget(self.browseFileLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.dropBoxFrame)

        self.basicSettingsFrame = QFrame(self.mainBodyContainer)
        self.basicSettingsFrame.setObjectName(u"basicSettingsFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(3)
        sizePolicy4.setHeightForWidth(self.basicSettingsFrame.sizePolicy().hasHeightForWidth())
        self.basicSettingsFrame.setSizePolicy(sizePolicy4)
        self.basicSettingsFrame.setStyleSheet(u"")
        self.basicSettingsFrame.setFrameShape(QFrame.NoFrame)
        self.basicSettingsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.basicSettingsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(60)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.basicSettingsFrame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(4)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy5)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        font8 = QFont()
        font8.setFamilies([u"Calibri"])
        font8.setPointSize(12)
        self.groupBox_2.setFont(font8)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 12)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        font9 = QFont()
        font9.setFamilies([u"Calibri"])
        font9.setPointSize(13)
        font9.setBold(True)
        self.label_2.setFont(font9)

        self.verticalLayout_5.addWidget(self.label_2)

        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        font10 = QFont()
        font10.setFamilies([u"Calibri"])
        font10.setPointSize(13)
        self.radioButton.setFont(font10)

        self.verticalLayout_5.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font10)

        self.verticalLayout_5.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font10)

        self.verticalLayout_5.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font10)

        self.verticalLayout_5.addWidget(self.radioButton_4)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 2, 1)

        self.groupBox_3 = QGroupBox(self.basicSettingsFrame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(5)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy6)
        self.groupBox_3.setFont(font8)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font9)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1, Qt.AlignLeft)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        font11 = QFont()
        font11.setFamilies([u"Calibri"])
        font11.setPointSize(12)
        font11.setItalic(True)
        self.lineEdit.setFont(font11)

        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font9)

        self.gridLayout_2.addWidget(self.checkBox, 5, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font9)

        self.gridLayout_2.addWidget(self.checkBox_2, 5, 1, 1, 1, Qt.AlignRight)


        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.basicSettingsFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font10)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icons/icons/minus-circle.svg", QSize(), QIcon.Active, QIcon.On)
        self.pushButton.setIcon(icon10)
        self.pushButton.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.basicSettingsFrame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy6.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy6)
        self.groupBox.setFont(font8)
        self.groupBox.setCheckable(False)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setSpacing(25)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font9)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setFont(font11)

        self.horizontalLayout_7.addWidget(self.lineEdit_2)


        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.basicSettingsFrame)


        self.horizontalLayout.addWidget(self.mainBodyContainer)


        self.verticalLayout_11.addWidget(self.centralContainer)

        self.lineFooter = QFrame(self.mainWidget)
        self.lineFooter.setObjectName(u"lineFooter")
        self.lineFooter.setAutoFillBackground(False)
        self.lineFooter.setStyleSheet(u"color: rgb(48, 53, 61);")
        self.lineFooter.setFrameShadow(QFrame.Sunken)
        self.lineFooter.setLineWidth(2)
        self.lineFooter.setFrameShape(QFrame.HLine)

        self.verticalLayout_11.addWidget(self.lineFooter)

        self.footerContainer = QWidget(self.mainWidget)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 1, -1, 4)
        self.labelFooterLeft = QLabel(self.footerContainer)
        self.labelFooterLeft.setObjectName(u"labelFooterLeft")
        font12 = QFont()
        font12.setFamilies([u"Calibri"])
        font12.setPointSize(10)
        self.labelFooterLeft.setFont(font12)

        self.horizontalLayout_3.addWidget(self.labelFooterLeft, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.labelFooterCenter = QLabel(self.footerContainer)
        self.labelFooterCenter.setObjectName(u"labelFooterCenter")
        self.labelFooterCenter.setFont(font12)

        self.horizontalLayout_3.addWidget(self.labelFooterCenter, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.labelFooterRight = QLabel(self.footerContainer)
        self.labelFooterRight.setObjectName(u"labelFooterRight")
        self.labelFooterRight.setFont(font12)

        self.horizontalLayout_3.addWidget(self.labelFooterRight, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.footerContainer)

        MainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data Cleaner Tool v0.1a", None))
#if QT_CONFIG(tooltip)
        self.MenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.MenuBtn.setText("")
        self.windowsMainTitle.setText(QCoreApplication.translate("MainWindow", u"Data Cleaner Tool v0.1a", None))
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Resize", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Pagina principale", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.editBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Advanced options", None))
#endif // QT_CONFIG(tooltip)
        self.editBtn.setText(QCoreApplication.translate("MainWindow", u"Opzioni avanzate", None))
#if QT_CONFIG(tooltip)
        self.previewBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Preview", None))
#endif // QT_CONFIG(tooltip)
        self.previewBtn.setText(QCoreApplication.translate("MainWindow", u"Tabella", None))
#if QT_CONFIG(tooltip)
        self.settingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Change theme", None))
#endif // QT_CONFIG(tooltip)
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Impostazioni", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More information", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Info", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Aiuto", None))
        self.uploadIcon.setText("")
        self.dragLabel.setText(QCoreApplication.translate("MainWindow", u"Trascina e rilascia un .CSV", None))
        self.browseFileLabel.setText(QCoreApplication.translate("MainWindow", u"Sfoglia sul tuo dispositivo", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"CSV file", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Delimitatore:", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"comma", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"semicolon", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"pipeline", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"tab", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"General", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Output filename:", None))
        self.lineEdit.setInputMask(QCoreApplication.translate("MainWindow", u"file_out.csv", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Skip righe vuote", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Trim tutte le colonne", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Opzioni base", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Excel file", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SheetName:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Sheet1", None))
        self.labelFooterLeft.setText(QCoreApplication.translate("MainWindow", u"Nessun file selezionato", None))
        self.labelFooterCenter.setText(QCoreApplication.translate("MainWindow", u"ENCODE: Default (UTF-8)", None))
        self.labelFooterRight.setText(QCoreApplication.translate("MainWindow", u"Status o notifiche ", None))
    # retranslateUi

