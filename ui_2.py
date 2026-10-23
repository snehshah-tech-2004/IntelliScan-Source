import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPalette

# ruff: noqa: E402,F401,F403,F405,F541,E722,F841,F821


def _resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Ui_SigmaControls_1(object):
    def setupUi(self, SigmaControls):
        SigmaControls.setObjectName("SigmaControls")
        SigmaControls.setEnabled(True)
        SigmaControls.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SigmaControls.sizePolicy().hasHeightForWidth())
        SigmaControls.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        SigmaControls.setFont(font)
        icon = QtGui.QIcon(_resource_path("SIGMA_ICON.svg"))
        SigmaControls.setWindowIcon(icon)
        SigmaControls.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:#F0E9D2;\n"
"font: 9pt \"Segoe UI\";")
        SigmaControls.setAnimated(True)
        SigmaControls.setDocumentMode(False)
        SigmaControls.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SigmaControls)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(460, 440, 1431, 531))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(
        "QTabBar::tab {"
        "color: black;"
        "font: 8.5pt \"Segoe UI\";"
        "font-weight: bold;"
        "}"
        
        "QTabBar::tab:selected {"
        "color: #00A0E3;"
        "}"
        )

        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.DATA = QtWidgets.QWidget()
        self.DATA.setAutoFillBackground(False)
        self.DATA.setStyleSheet("selection-background-color: rgb(170, 0, 255);")
        self.DATA.setObjectName("DATA")
        self.groupBox = QtWidgets.QGroupBox(self.DATA)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 1371, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(160, 30, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.lcdNumber_01 = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_01.setEnabled(True)
        self.lcdNumber_01.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_01.sizePolicy().hasHeightForWidth())
        self.lcdNumber_01.setSizePolicy(sizePolicy)
        self.lcdNumber_01.setAutoFillBackground(False)
        self.lcdNumber_01.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_01.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_01.setSmallDecimalPoint(True)
        self.lcdNumber_01.setDigitCount(6)
        self.lcdNumber_01.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_01.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_01.setProperty("value", 0.0)
        self.lcdNumber_01.setObjectName("lcdNumber_01")
        self.CH01Temp = QtWidgets.QLabel(self.widget)
        self.CH01Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH01Temp.sizePolicy().hasHeightForWidth())
        self.CH01Temp.setSizePolicy(sizePolicy)
        self.CH01Temp.setAutoFillBackground(False)
        self.CH01Temp.setText("")
        self.CH01Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH01Temp.setScaledContents(True)
        self.CH01Temp.setObjectName("CH01Temp")
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setGeometry(QtCore.QRect(160, 100, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.lcdNumber_02 = QtWidgets.QLCDNumber(self.widget_2)
        self.lcdNumber_02.setEnabled(False)
        self.lcdNumber_02.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_02.sizePolicy().hasHeightForWidth())
        self.lcdNumber_02.setSizePolicy(sizePolicy)
        self.lcdNumber_02.setAutoFillBackground(False)
        self.lcdNumber_02.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_02.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_02.setSmallDecimalPoint(True)
        self.lcdNumber_02.setDigitCount(6)
        self.lcdNumber_02.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_02.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_02.setProperty("value", 0.0)
        self.lcdNumber_02.setObjectName("lcdNumber_02")
        self.CH02Temp = QtWidgets.QLabel(self.widget_2)
        self.CH02Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH02Temp.sizePolicy().hasHeightForWidth())
        self.CH02Temp.setSizePolicy(sizePolicy)
        self.CH02Temp.setAutoFillBackground(False)
        self.CH02Temp.setText("")
        self.CH02Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH02Temp.setScaledContents(True)
        self.CH02Temp.setObjectName("CH02Temp")
        self.widget_3 = QtWidgets.QWidget(self.groupBox)
        self.widget_3.setGeometry(QtCore.QRect(160, 170, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.lcdNumber_03 = QtWidgets.QLCDNumber(self.widget_3)
        self.lcdNumber_03.setEnabled(False)
        self.lcdNumber_03.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_03.sizePolicy().hasHeightForWidth())
        self.lcdNumber_03.setSizePolicy(sizePolicy)
        self.lcdNumber_03.setAutoFillBackground(False)
        self.lcdNumber_03.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_03.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_03.setSmallDecimalPoint(True)
        self.lcdNumber_03.setDigitCount(6)
        self.lcdNumber_03.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_03.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_03.setProperty("value", 0.0)
        self.lcdNumber_03.setObjectName("lcdNumber_03")
        self.CH03Temp = QtWidgets.QLabel(self.widget_3)
        self.CH03Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH03Temp.sizePolicy().hasHeightForWidth())
        self.CH03Temp.setSizePolicy(sizePolicy)
        self.CH03Temp.setAutoFillBackground(False)
        self.CH03Temp.setText("")
        self.CH03Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH03Temp.setScaledContents(True)
        self.CH03Temp.setObjectName("CH03Temp")
        self.widget_4 = QtWidgets.QWidget(self.groupBox)
        self.widget_4.setGeometry(QtCore.QRect(160, 240, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.lcdNumber_04 = QtWidgets.QLCDNumber(self.widget_4)
        self.lcdNumber_04.setEnabled(False)
        self.lcdNumber_04.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_04.sizePolicy().hasHeightForWidth())
        self.lcdNumber_04.setSizePolicy(sizePolicy)
        self.lcdNumber_04.setAutoFillBackground(False)
        self.lcdNumber_04.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_04.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_04.setSmallDecimalPoint(True)
        self.lcdNumber_04.setDigitCount(6)
        self.lcdNumber_04.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_04.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_04.setProperty("value", 0.0)
        self.lcdNumber_04.setObjectName("lcdNumber_04")
        self.CH04Temp = QtWidgets.QLabel(self.widget_4)
        self.CH04Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH04Temp.sizePolicy().hasHeightForWidth())
        self.CH04Temp.setSizePolicy(sizePolicy)
        self.CH04Temp.setAutoFillBackground(False)
        self.CH04Temp.setText("")
        self.CH04Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH04Temp.setScaledContents(True)
        self.CH04Temp.setObjectName("CH04Temp")
        self.widget_5 = QtWidgets.QWidget(self.groupBox)
        self.widget_5.setGeometry(QtCore.QRect(160, 310, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.lcdNumber_05 = QtWidgets.QLCDNumber(self.widget_5)
        self.lcdNumber_05.setEnabled(False)
        self.lcdNumber_05.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_05.sizePolicy().hasHeightForWidth())
        self.lcdNumber_05.setSizePolicy(sizePolicy)
        self.lcdNumber_05.setAutoFillBackground(False)
        self.lcdNumber_05.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_05.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_05.setSmallDecimalPoint(True)
        self.lcdNumber_05.setDigitCount(6)
        self.lcdNumber_05.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_05.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_05.setProperty("value", 0.0)
        self.lcdNumber_05.setObjectName("lcdNumber_05")
        self.CH05Temp = QtWidgets.QLabel(self.widget_5)
        self.CH05Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH05Temp.sizePolicy().hasHeightForWidth())
        self.CH05Temp.setSizePolicy(sizePolicy)
        self.CH05Temp.setAutoFillBackground(False)
        self.CH05Temp.setText("")
        self.CH05Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH05Temp.setScaledContents(True)
        self.CH05Temp.setObjectName("CH05Temp")
        self.widget_6 = QtWidgets.QWidget(self.groupBox)
        self.widget_6.setGeometry(QtCore.QRect(160, 380, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.lcdNumber_06 = QtWidgets.QLCDNumber(self.widget_6)
        self.lcdNumber_06.setEnabled(False)
        self.lcdNumber_06.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_06.sizePolicy().hasHeightForWidth())
        self.lcdNumber_06.setSizePolicy(sizePolicy)
        self.lcdNumber_06.setAutoFillBackground(False)
        self.lcdNumber_06.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_06.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_06.setSmallDecimalPoint(True)
        self.lcdNumber_06.setDigitCount(6)
        self.lcdNumber_06.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_06.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_06.setProperty("value", 0.0)
        self.lcdNumber_06.setObjectName("lcdNumber_06")
        self.CH06Temp = QtWidgets.QLabel(self.widget_6)
        self.CH06Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH06Temp.sizePolicy().hasHeightForWidth())
        self.CH06Temp.setSizePolicy(sizePolicy)
        self.CH06Temp.setAutoFillBackground(False)
        self.CH06Temp.setText("")
        self.CH06Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH06Temp.setScaledContents(True)
        self.CH06Temp.setObjectName("CH06Temp")
        self.widget_7 = QtWidgets.QWidget(self.groupBox)
        self.widget_7.setGeometry(QtCore.QRect(500, 30, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.lcdNumber_07 = QtWidgets.QLCDNumber(self.widget_7)
        self.lcdNumber_07.setEnabled(False)
        self.lcdNumber_07.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_07.sizePolicy().hasHeightForWidth())
        self.lcdNumber_07.setSizePolicy(sizePolicy)
        self.lcdNumber_07.setAutoFillBackground(False)
        self.lcdNumber_07.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_07.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_07.setSmallDecimalPoint(True)
        self.lcdNumber_07.setDigitCount(6)
        self.lcdNumber_07.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_07.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_07.setProperty("value", 0.0)
        self.lcdNumber_07.setObjectName("lcdNumber_07")
        self.CH07Temp = QtWidgets.QLabel(self.widget_7)
        self.CH07Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH07Temp.sizePolicy().hasHeightForWidth())
        self.CH07Temp.setSizePolicy(sizePolicy)
        self.CH07Temp.setAutoFillBackground(False)
        self.CH07Temp.setText("")
        self.CH07Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH07Temp.setScaledContents(True)
        self.CH07Temp.setObjectName("CH07Temp")
        self.widget_8 = QtWidgets.QWidget(self.groupBox)
        self.widget_8.setGeometry(QtCore.QRect(500, 100, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.lcdNumber_08 = QtWidgets.QLCDNumber(self.widget_8)
        self.lcdNumber_08.setEnabled(False)
        self.lcdNumber_08.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_08.sizePolicy().hasHeightForWidth())
        self.lcdNumber_08.setSizePolicy(sizePolicy)
        self.lcdNumber_08.setAutoFillBackground(False)
        self.lcdNumber_08.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_08.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_08.setSmallDecimalPoint(True)
        self.lcdNumber_08.setDigitCount(6)
        self.lcdNumber_08.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_08.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_08.setProperty("value", 0.0)
        self.lcdNumber_08.setObjectName("lcdNumber_08")
        self.CH08Temp = QtWidgets.QLabel(self.widget_8)
        self.CH08Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH08Temp.sizePolicy().hasHeightForWidth())
        self.CH08Temp.setSizePolicy(sizePolicy)
        self.CH08Temp.setAutoFillBackground(False)
        self.CH08Temp.setText("")
        self.CH08Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH08Temp.setScaledContents(True)
        self.CH08Temp.setObjectName("CH08Temp")
        self.widget_9 = QtWidgets.QWidget(self.groupBox)
        self.widget_9.setGeometry(QtCore.QRect(500, 170, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setObjectName("widget_9")
        self.lcdNumber_09 = QtWidgets.QLCDNumber(self.widget_9)
        self.lcdNumber_09.setEnabled(False)
        self.lcdNumber_09.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_09.sizePolicy().hasHeightForWidth())
        self.lcdNumber_09.setSizePolicy(sizePolicy)
        self.lcdNumber_09.setAutoFillBackground(False)
        self.lcdNumber_09.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_09.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_09.setSmallDecimalPoint(True)
        self.lcdNumber_09.setDigitCount(6)
        self.lcdNumber_09.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_09.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_09.setProperty("value", 0.0)
        self.lcdNumber_09.setObjectName("lcdNumber_09")
        self.CH09Temp = QtWidgets.QLabel(self.widget_9)
        self.CH09Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH09Temp.sizePolicy().hasHeightForWidth())
        self.CH09Temp.setSizePolicy(sizePolicy)
        self.CH09Temp.setAutoFillBackground(False)
        self.CH09Temp.setText("")
        self.CH09Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH09Temp.setScaledContents(True)
        self.CH09Temp.setObjectName("CH09Temp")
        self.widget_10 = QtWidgets.QWidget(self.groupBox)
        self.widget_10.setGeometry(QtCore.QRect(500, 240, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setObjectName("widget_10")
        self.lcdNumber_10 = QtWidgets.QLCDNumber(self.widget_10)
        self.lcdNumber_10.setEnabled(False)
        self.lcdNumber_10.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_10.sizePolicy().hasHeightForWidth())
        self.lcdNumber_10.setSizePolicy(sizePolicy)
        self.lcdNumber_10.setAutoFillBackground(False)
        self.lcdNumber_10.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_10.setSmallDecimalPoint(True)
        self.lcdNumber_10.setDigitCount(6)
        self.lcdNumber_10.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_10.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_10.setProperty("value", 0.0)
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.CH10Temp = QtWidgets.QLabel(self.widget_10)
        self.CH10Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH10Temp.sizePolicy().hasHeightForWidth())
        self.CH10Temp.setSizePolicy(sizePolicy)
        self.CH10Temp.setAutoFillBackground(False)
        self.CH10Temp.setText("")
        self.CH10Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH10Temp.setScaledContents(True)
        self.CH10Temp.setObjectName("CH10Temp")
        self.widget_11 = QtWidgets.QWidget(self.groupBox)
        self.widget_11.setGeometry(QtCore.QRect(500, 310, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setObjectName("widget_11")
        self.lcdNumber_11 = QtWidgets.QLCDNumber(self.widget_11)
        self.lcdNumber_11.setEnabled(False)
        self.lcdNumber_11.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_11.sizePolicy().hasHeightForWidth())
        self.lcdNumber_11.setSizePolicy(sizePolicy)
        self.lcdNumber_11.setAutoFillBackground(False)
        self.lcdNumber_11.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_11.setSmallDecimalPoint(True)
        self.lcdNumber_11.setDigitCount(6)
        self.lcdNumber_11.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_11.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_11.setProperty("value", 0.0)
        self.lcdNumber_11.setObjectName("lcdNumber_11")
        self.CH11Temp = QtWidgets.QLabel(self.widget_11)
        self.CH11Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH11Temp.sizePolicy().hasHeightForWidth())
        self.CH11Temp.setSizePolicy(sizePolicy)
        self.CH11Temp.setAutoFillBackground(False)
        self.CH11Temp.setText("")
        self.CH11Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH11Temp.setScaledContents(True)
        self.CH11Temp.setObjectName("CH11Temp")
        self.widget_12 = QtWidgets.QWidget(self.groupBox)
        self.widget_12.setGeometry(QtCore.QRect(500, 380, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.widget_12.setObjectName("widget_12")
        self.lcdNumber_12 = QtWidgets.QLCDNumber(self.widget_12)
        self.lcdNumber_12.setEnabled(False)
        self.lcdNumber_12.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_12.sizePolicy().hasHeightForWidth())
        self.lcdNumber_12.setSizePolicy(sizePolicy)
        self.lcdNumber_12.setAutoFillBackground(False)
        self.lcdNumber_12.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_12.setSmallDecimalPoint(True)
        self.lcdNumber_12.setDigitCount(6)
        self.lcdNumber_12.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_12.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_12.setProperty("value", 0.0)
        self.lcdNumber_12.setObjectName("lcdNumber_12")
        self.CH12Temp = QtWidgets.QLabel(self.widget_12)
        self.CH12Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH12Temp.sizePolicy().hasHeightForWidth())
        self.CH12Temp.setSizePolicy(sizePolicy)
        self.CH12Temp.setAutoFillBackground(False)
        self.CH12Temp.setText("")
        self.CH12Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH12Temp.setScaledContents(True)
        self.CH12Temp.setObjectName("CH12Temp")
        self.widget_13 = QtWidgets.QWidget(self.groupBox)
        self.widget_13.setGeometry(QtCore.QRect(840, 30, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy)
        self.widget_13.setObjectName("widget_13")
        self.lcdNumber_13 = QtWidgets.QLCDNumber(self.widget_13)
        self.lcdNumber_13.setEnabled(False)
        self.lcdNumber_13.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_13.sizePolicy().hasHeightForWidth())
        self.lcdNumber_13.setSizePolicy(sizePolicy)
        self.lcdNumber_13.setAutoFillBackground(False)
        self.lcdNumber_13.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_13.setSmallDecimalPoint(True)
        self.lcdNumber_13.setDigitCount(6)
        self.lcdNumber_13.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_13.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_13.setProperty("value", 0.0)
        self.lcdNumber_13.setObjectName("lcdNumber_13")
        self.CH13Temp = QtWidgets.QLabel(self.widget_13)
        self.CH13Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH13Temp.sizePolicy().hasHeightForWidth())
        self.CH13Temp.setSizePolicy(sizePolicy)
        self.CH13Temp.setAutoFillBackground(False)
        self.CH13Temp.setText("")
        self.CH13Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH13Temp.setScaledContents(True)
        self.CH13Temp.setObjectName("CH13Temp")
        self.widget_14 = QtWidgets.QWidget(self.groupBox)
        self.widget_14.setGeometry(QtCore.QRect(840, 100, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.widget_14.setObjectName("widget_14")
        self.lcdNumber_14 = QtWidgets.QLCDNumber(self.widget_14)
        self.lcdNumber_14.setEnabled(False)
        self.lcdNumber_14.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_14.sizePolicy().hasHeightForWidth())
        self.lcdNumber_14.setSizePolicy(sizePolicy)
        self.lcdNumber_14.setAutoFillBackground(False)
        self.lcdNumber_14.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_14.setSmallDecimalPoint(True)
        self.lcdNumber_14.setDigitCount(6)
        self.lcdNumber_14.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_14.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_14.setProperty("value", 0.0)
        self.lcdNumber_14.setObjectName("lcdNumber_14")
        self.CH14Temp = QtWidgets.QLabel(self.widget_14)
        self.CH14Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH14Temp.sizePolicy().hasHeightForWidth())
        self.CH14Temp.setSizePolicy(sizePolicy)
        self.CH14Temp.setAutoFillBackground(False)
        self.CH14Temp.setText("")
        self.CH14Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH14Temp.setScaledContents(True)
        self.CH14Temp.setObjectName("CH14Temp")
        self.widget_15 = QtWidgets.QWidget(self.groupBox)
        self.widget_15.setGeometry(QtCore.QRect(840, 170, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.widget_15.setObjectName("widget_15")
        self.lcdNumber_15 = QtWidgets.QLCDNumber(self.widget_15)
        self.lcdNumber_15.setEnabled(False)
        self.lcdNumber_15.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_15.sizePolicy().hasHeightForWidth())
        self.lcdNumber_15.setSizePolicy(sizePolicy)
        self.lcdNumber_15.setAutoFillBackground(False)
        self.lcdNumber_15.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_15.setSmallDecimalPoint(True)
        self.lcdNumber_15.setDigitCount(6)
        self.lcdNumber_15.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_15.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_15.setProperty("value", 0.0)
        self.lcdNumber_15.setObjectName("lcdNumber_15")
        self.CH15Temp = QtWidgets.QLabel(self.widget_15)
        self.CH15Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH15Temp.sizePolicy().hasHeightForWidth())
        self.CH15Temp.setSizePolicy(sizePolicy)
        self.CH15Temp.setAutoFillBackground(False)
        self.CH15Temp.setText("")
        self.CH15Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH15Temp.setScaledContents(True)
        self.CH15Temp.setObjectName("CH15Temp")
        self.widget_16 = QtWidgets.QWidget(self.groupBox)
        self.widget_16.setGeometry(QtCore.QRect(840, 240, 181, 61))
        self.widget_16.setObjectName("widget_16")
        self.lcdNumber_64 = QtWidgets.QLCDNumber(self.widget_16)
        self.lcdNumber_64.setEnabled(False)
        self.lcdNumber_64.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_64.setAutoFillBackground(False)
        self.lcdNumber_64.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_64.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_64.setSmallDecimalPoint(True)
        self.lcdNumber_64.setDigitCount(6)
        self.lcdNumber_64.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_64.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_64.setProperty("value", 0.0)
        self.lcdNumber_64.setObjectName("lcdNumber_64")
        self.label_17 = QtWidgets.QLabel(self.widget_16)
        self.label_17.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_17.setAutoFillBackground(False)
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.widget_17 = QtWidgets.QWidget(self.widget_16)
        self.widget_17.setGeometry(QtCore.QRect(0, 0, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy)
        self.widget_17.setObjectName("widget_17")
        self.lcdNumber_16 = QtWidgets.QLCDNumber(self.widget_17)
        self.lcdNumber_16.setEnabled(False)
        self.lcdNumber_16.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_16.sizePolicy().hasHeightForWidth())
        self.lcdNumber_16.setSizePolicy(sizePolicy)
        self.lcdNumber_16.setAutoFillBackground(False)
        self.lcdNumber_16.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_16.setSmallDecimalPoint(True)
        self.lcdNumber_16.setDigitCount(6)
        self.lcdNumber_16.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_16.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_16.setProperty("value", 0.0)
        self.lcdNumber_16.setObjectName("lcdNumber_16")
        self.CH16Temp = QtWidgets.QLabel(self.widget_17)
        self.CH16Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH16Temp.sizePolicy().hasHeightForWidth())
        self.CH16Temp.setSizePolicy(sizePolicy)
        self.CH16Temp.setAutoFillBackground(False)
        self.CH16Temp.setText("")
        self.CH16Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH16Temp.setScaledContents(True)
        self.CH16Temp.setObjectName("CH16Temp")
        self.widget_18 = QtWidgets.QWidget(self.groupBox)
        self.widget_18.setGeometry(QtCore.QRect(840, 310, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy)
        self.widget_18.setObjectName("widget_18")
        self.lcdNumber_17 = QtWidgets.QLCDNumber(self.widget_18)
        self.lcdNumber_17.setEnabled(False)
        self.lcdNumber_17.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_17.sizePolicy().hasHeightForWidth())
        self.lcdNumber_17.setSizePolicy(sizePolicy)
        self.lcdNumber_17.setAutoFillBackground(False)
        self.lcdNumber_17.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_17.setSmallDecimalPoint(True)
        self.lcdNumber_17.setDigitCount(6)
        self.lcdNumber_17.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_17.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_17.setProperty("value", 0.0)
        self.lcdNumber_17.setObjectName("lcdNumber_17")
        self.CH17Temp = QtWidgets.QLabel(self.widget_18)
        self.CH17Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH17Temp.sizePolicy().hasHeightForWidth())
        self.CH17Temp.setSizePolicy(sizePolicy)
        self.CH17Temp.setAutoFillBackground(False)
        self.CH17Temp.setText("")
        self.CH17Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH17Temp.setScaledContents(True)
        self.CH17Temp.setObjectName("CH17Temp")
        self.widget_19 = QtWidgets.QWidget(self.groupBox)
        self.widget_19.setGeometry(QtCore.QRect(840, 380, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy)
        self.widget_19.setObjectName("widget_19")
        self.lcdNumber_18 = QtWidgets.QLCDNumber(self.widget_19)
        self.lcdNumber_18.setEnabled(False)
        self.lcdNumber_18.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_18.sizePolicy().hasHeightForWidth())
        self.lcdNumber_18.setSizePolicy(sizePolicy)
        self.lcdNumber_18.setAutoFillBackground(False)
        self.lcdNumber_18.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_18.setSmallDecimalPoint(True)
        self.lcdNumber_18.setDigitCount(6)
        self.lcdNumber_18.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_18.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_18.setProperty("value", 0.0)
        self.lcdNumber_18.setObjectName("lcdNumber_18")
        self.CH18Temp = QtWidgets.QLabel(self.widget_19)
        self.CH18Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH18Temp.sizePolicy().hasHeightForWidth())
        self.CH18Temp.setSizePolicy(sizePolicy)
        self.CH18Temp.setAutoFillBackground(False)
        self.CH18Temp.setText("")
        self.CH18Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH18Temp.setScaledContents(True)
        self.CH18Temp.setObjectName("CH18Temp")
        self.widget_20 = QtWidgets.QWidget(self.groupBox)
        self.widget_20.setGeometry(QtCore.QRect(2020, 350, 181, 61))
        self.widget_20.setObjectName("widget_20")
        self.lcdNumber_68 = QtWidgets.QLCDNumber(self.widget_20)
        self.lcdNumber_68.setEnabled(False)
        self.lcdNumber_68.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_68.setAutoFillBackground(False)
        self.lcdNumber_68.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_68.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_68.setSmallDecimalPoint(True)
        self.lcdNumber_68.setDigitCount(6)
        self.lcdNumber_68.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_68.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_68.setProperty("value", 0.0)
        self.lcdNumber_68.setObjectName("lcdNumber_68")
        self.label_21 = QtWidgets.QLabel(self.widget_20)
        self.label_21.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_21.setAutoFillBackground(False)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.widget_21 = QtWidgets.QWidget(self.groupBox)
        self.widget_21.setGeometry(QtCore.QRect(2020, 140, 181, 61))
        self.widget_21.setObjectName("widget_21")
        self.lcdNumber_69 = QtWidgets.QLCDNumber(self.widget_21)
        self.lcdNumber_69.setEnabled(False)
        self.lcdNumber_69.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_69.setAutoFillBackground(False)
        self.lcdNumber_69.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_69.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_69.setSmallDecimalPoint(True)
        self.lcdNumber_69.setDigitCount(6)
        self.lcdNumber_69.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_69.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_69.setProperty("value", 0.0)
        self.lcdNumber_69.setObjectName("lcdNumber_69")
        self.label_22 = QtWidgets.QLabel(self.widget_21)
        self.label_22.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_22.setAutoFillBackground(False)
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.widget_22 = QtWidgets.QWidget(self.groupBox)
        self.widget_22.setGeometry(QtCore.QRect(1180, 30, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy)
        self.widget_22.setObjectName("widget_22")
        self.lcdNumber_19 = QtWidgets.QLCDNumber(self.widget_22)
        self.lcdNumber_19.setEnabled(False)
        self.lcdNumber_19.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_19.sizePolicy().hasHeightForWidth())
        self.lcdNumber_19.setSizePolicy(sizePolicy)
        self.lcdNumber_19.setAutoFillBackground(False)
        self.lcdNumber_19.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_19.setSmallDecimalPoint(True)
        self.lcdNumber_19.setDigitCount(6)
        self.lcdNumber_19.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_19.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_19.setProperty("value", 0.0)
        self.lcdNumber_19.setObjectName("lcdNumber_19")
        self.CH19Temp = QtWidgets.QLabel(self.widget_22)
        self.CH19Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH19Temp.sizePolicy().hasHeightForWidth())
        self.CH19Temp.setSizePolicy(sizePolicy)
        self.CH19Temp.setAutoFillBackground(False)
        self.CH19Temp.setText("")
        self.CH19Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH19Temp.setScaledContents(True)
        self.CH19Temp.setObjectName("CH19Temp")
        self.widget_23 = QtWidgets.QWidget(self.groupBox)
        self.widget_23.setGeometry(QtCore.QRect(2020, 70, 181, 61))
        self.widget_23.setObjectName("widget_23")
        self.lcdNumber_71 = QtWidgets.QLCDNumber(self.widget_23)
        self.lcdNumber_71.setEnabled(False)
        self.lcdNumber_71.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_71.setAutoFillBackground(False)
        self.lcdNumber_71.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_71.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_71.setSmallDecimalPoint(True)
        self.lcdNumber_71.setDigitCount(6)
        self.lcdNumber_71.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_71.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_71.setProperty("value", 0.0)
        self.lcdNumber_71.setObjectName("lcdNumber_71")
        self.label_24 = QtWidgets.QLabel(self.widget_23)
        self.label_24.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_24.setAutoFillBackground(False)
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.widget_24 = QtWidgets.QWidget(self.groupBox)
        self.widget_24.setGeometry(QtCore.QRect(2020, 420, 181, 61))
        self.widget_24.setObjectName("widget_24")
        self.lcdNumber_72 = QtWidgets.QLCDNumber(self.widget_24)
        self.lcdNumber_72.setEnabled(False)
        self.lcdNumber_72.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_72.setAutoFillBackground(False)
        self.lcdNumber_72.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_72.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_72.setSmallDecimalPoint(True)
        self.lcdNumber_72.setDigitCount(6)
        self.lcdNumber_72.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_72.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_72.setProperty("value", 0.0)
        self.lcdNumber_72.setObjectName("lcdNumber_72")
        self.label_25 = QtWidgets.QLabel(self.widget_24)
        self.label_25.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_25.setAutoFillBackground(False)
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.widget_25 = QtWidgets.QWidget(self.groupBox)
        self.widget_25.setGeometry(QtCore.QRect(2020, 210, 181, 61))
        self.widget_25.setObjectName("widget_25")
        self.lcdNumber_73 = QtWidgets.QLCDNumber(self.widget_25)
        self.lcdNumber_73.setEnabled(False)
        self.lcdNumber_73.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_73.setAutoFillBackground(False)
        self.lcdNumber_73.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_73.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_73.setSmallDecimalPoint(True)
        self.lcdNumber_73.setDigitCount(6)
        self.lcdNumber_73.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_73.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_73.setProperty("value", 0.0)
        self.lcdNumber_73.setObjectName("lcdNumber_73")
        self.label_26 = QtWidgets.QLabel(self.widget_25)
        self.label_26.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_26.setAutoFillBackground(False)
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.widget_26 = QtWidgets.QWidget(self.groupBox)
        self.widget_26.setGeometry(QtCore.QRect(2020, 410, 181, 61))
        self.widget_26.setObjectName("widget_26")
        self.lcdNumber_74 = QtWidgets.QLCDNumber(self.widget_26)
        self.lcdNumber_74.setEnabled(False)
        self.lcdNumber_74.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_74.setAutoFillBackground(False)
        self.lcdNumber_74.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_74.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_74.setSmallDecimalPoint(True)
        self.lcdNumber_74.setDigitCount(6)
        self.lcdNumber_74.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_74.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_74.setProperty("value", 0.0)
        self.lcdNumber_74.setObjectName("lcdNumber_74")
        self.label_27 = QtWidgets.QLabel(self.widget_26)
        self.label_27.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_27.setAutoFillBackground(False)
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.widget_27 = QtWidgets.QWidget(self.groupBox)
        self.widget_27.setGeometry(QtCore.QRect(2020, 200, 181, 61))
        self.widget_27.setObjectName("widget_27")
        self.lcdNumber_75 = QtWidgets.QLCDNumber(self.widget_27)
        self.lcdNumber_75.setEnabled(False)
        self.lcdNumber_75.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_75.setAutoFillBackground(False)
        self.lcdNumber_75.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_75.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_75.setSmallDecimalPoint(True)
        self.lcdNumber_75.setDigitCount(6)
        self.lcdNumber_75.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_75.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_75.setProperty("value", 0.0)
        self.lcdNumber_75.setObjectName("lcdNumber_75")
        self.label_28 = QtWidgets.QLabel(self.widget_27)
        self.label_28.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_28.setAutoFillBackground(False)
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.widget_28 = QtWidgets.QWidget(self.groupBox)
        self.widget_28.setGeometry(QtCore.QRect(1180, 100, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy)
        self.widget_28.setObjectName("widget_28")
        self.lcdNumber_20 = QtWidgets.QLCDNumber(self.widget_28)
        self.lcdNumber_20.setEnabled(False)
        self.lcdNumber_20.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_20.sizePolicy().hasHeightForWidth())
        self.lcdNumber_20.setSizePolicy(sizePolicy)
        self.lcdNumber_20.setAutoFillBackground(False)
        self.lcdNumber_20.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_20.setSmallDecimalPoint(True)
        self.lcdNumber_20.setDigitCount(6)
        self.lcdNumber_20.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_20.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_20.setProperty("value", 0.0)
        self.lcdNumber_20.setObjectName("lcdNumber_20")
        self.CH20Temp = QtWidgets.QLabel(self.widget_28)
        self.CH20Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH20Temp.sizePolicy().hasHeightForWidth())
        self.CH20Temp.setSizePolicy(sizePolicy)
        self.CH20Temp.setAutoFillBackground(False)
        self.CH20Temp.setText("")
        self.CH20Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH20Temp.setScaledContents(True)
        self.CH20Temp.setObjectName("CH20Temp")
        self.widget_29 = QtWidgets.QWidget(self.groupBox)
        self.widget_29.setGeometry(QtCore.QRect(2020, 130, 181, 61))
        self.widget_29.setObjectName("widget_29")
        self.lcdNumber_77 = QtWidgets.QLCDNumber(self.widget_29)
        self.lcdNumber_77.setEnabled(False)
        self.lcdNumber_77.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_77.setAutoFillBackground(False)
        self.lcdNumber_77.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_77.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_77.setSmallDecimalPoint(True)
        self.lcdNumber_77.setDigitCount(6)
        self.lcdNumber_77.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_77.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_77.setProperty("value", 0.0)
        self.lcdNumber_77.setObjectName("lcdNumber_77")
        self.label_30 = QtWidgets.QLabel(self.widget_29)
        self.label_30.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_30.setAutoFillBackground(False)
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.widget_30 = QtWidgets.QWidget(self.groupBox)
        self.widget_30.setGeometry(QtCore.QRect(2020, 480, 181, 61))
        self.widget_30.setObjectName("widget_30")
        self.lcdNumber_78 = QtWidgets.QLCDNumber(self.widget_30)
        self.lcdNumber_78.setEnabled(False)
        self.lcdNumber_78.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_78.setAutoFillBackground(False)
        self.lcdNumber_78.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_78.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_78.setSmallDecimalPoint(True)
        self.lcdNumber_78.setDigitCount(6)
        self.lcdNumber_78.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_78.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_78.setProperty("value", 0.0)
        self.lcdNumber_78.setObjectName("lcdNumber_78")
        self.label_31 = QtWidgets.QLabel(self.widget_30)
        self.label_31.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_31.setAutoFillBackground(False)
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setObjectName("label_31")
        self.widget_31 = QtWidgets.QWidget(self.groupBox)
        self.widget_31.setGeometry(QtCore.QRect(2020, 270, 181, 61))
        self.widget_31.setObjectName("widget_31")
        self.lcdNumber_79 = QtWidgets.QLCDNumber(self.widget_31)
        self.lcdNumber_79.setEnabled(False)
        self.lcdNumber_79.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_79.setAutoFillBackground(False)
        self.lcdNumber_79.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_79.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_79.setSmallDecimalPoint(True)
        self.lcdNumber_79.setDigitCount(6)
        self.lcdNumber_79.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_79.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_79.setProperty("value", 0.0)
        self.lcdNumber_79.setObjectName("lcdNumber_79")
        self.label_32 = QtWidgets.QLabel(self.widget_31)
        self.label_32.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_32.setAutoFillBackground(False)
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.widget_32 = QtWidgets.QWidget(self.groupBox)
        self.widget_32.setGeometry(QtCore.QRect(2020, 480, 181, 61))
        self.widget_32.setObjectName("widget_32")
        self.lcdNumber_80 = QtWidgets.QLCDNumber(self.widget_32)
        self.lcdNumber_80.setEnabled(False)
        self.lcdNumber_80.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_80.setAutoFillBackground(False)
        self.lcdNumber_80.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_80.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_80.setSmallDecimalPoint(True)
        self.lcdNumber_80.setDigitCount(6)
        self.lcdNumber_80.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_80.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_80.setProperty("value", 0.0)
        self.lcdNumber_80.setObjectName("lcdNumber_80")
        self.label_33 = QtWidgets.QLabel(self.widget_32)
        self.label_33.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_33.setAutoFillBackground(False)
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.widget_33 = QtWidgets.QWidget(self.groupBox)
        self.widget_33.setGeometry(QtCore.QRect(2020, 270, 181, 61))
        self.widget_33.setObjectName("widget_33")
        self.lcdNumber_81 = QtWidgets.QLCDNumber(self.widget_33)
        self.lcdNumber_81.setEnabled(False)
        self.lcdNumber_81.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_81.setAutoFillBackground(False)
        self.lcdNumber_81.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_81.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_81.setSmallDecimalPoint(True)
        self.lcdNumber_81.setDigitCount(6)
        self.lcdNumber_81.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_81.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_81.setProperty("value", 0.0)
        self.lcdNumber_81.setObjectName("lcdNumber_81")
        self.label_34 = QtWidgets.QLabel(self.widget_33)
        self.label_34.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_34.setAutoFillBackground(False)
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.widget_34 = QtWidgets.QWidget(self.groupBox)
        self.widget_34.setGeometry(QtCore.QRect(1180, 170, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy)
        self.widget_34.setObjectName("widget_34")
        self.lcdNumber_21 = QtWidgets.QLCDNumber(self.widget_34)
        self.lcdNumber_21.setEnabled(False)
        self.lcdNumber_21.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_21.sizePolicy().hasHeightForWidth())
        self.lcdNumber_21.setSizePolicy(sizePolicy)
        self.lcdNumber_21.setAutoFillBackground(False)
        self.lcdNumber_21.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_21.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_21.setSmallDecimalPoint(True)
        self.lcdNumber_21.setDigitCount(6)
        self.lcdNumber_21.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_21.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_21.setProperty("value", 0.0)
        self.lcdNumber_21.setObjectName("lcdNumber_21")
        self.CH21Temp = QtWidgets.QLabel(self.widget_34)
        self.CH21Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH21Temp.sizePolicy().hasHeightForWidth())
        self.CH21Temp.setSizePolicy(sizePolicy)
        self.CH21Temp.setAutoFillBackground(False)
        self.CH21Temp.setText("")
        self.CH21Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH21Temp.setScaledContents(True)
        self.CH21Temp.setObjectName("CH21Temp")
        self.widget_35 = QtWidgets.QWidget(self.groupBox)
        self.widget_35.setGeometry(QtCore.QRect(2020, 200, 181, 61))
        self.widget_35.setObjectName("widget_35")
        self.lcdNumber_83 = QtWidgets.QLCDNumber(self.widget_35)
        self.lcdNumber_83.setEnabled(False)
        self.lcdNumber_83.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_83.setAutoFillBackground(False)
        self.lcdNumber_83.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_83.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_83.setSmallDecimalPoint(True)
        self.lcdNumber_83.setDigitCount(6)
        self.lcdNumber_83.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_83.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_83.setProperty("value", 0.0)
        self.lcdNumber_83.setObjectName("lcdNumber_83")
        self.label_36 = QtWidgets.QLabel(self.widget_35)
        self.label_36.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_36.setAutoFillBackground(False)
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setObjectName("label_36")
        self.widget_36 = QtWidgets.QWidget(self.groupBox)
        self.widget_36.setGeometry(QtCore.QRect(2020, 550, 181, 61))
        self.widget_36.setObjectName("widget_36")
        self.lcdNumber_84 = QtWidgets.QLCDNumber(self.widget_36)
        self.lcdNumber_84.setEnabled(False)
        self.lcdNumber_84.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_84.setAutoFillBackground(False)
        self.lcdNumber_84.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_84.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_84.setSmallDecimalPoint(True)
        self.lcdNumber_84.setDigitCount(6)
        self.lcdNumber_84.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_84.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_84.setProperty("value", 0.0)
        self.lcdNumber_84.setObjectName("lcdNumber_84")
        self.label_37 = QtWidgets.QLabel(self.widget_36)
        self.label_37.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_37.setAutoFillBackground(False)
        self.label_37.setText("")
        self.label_37.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setObjectName("label_37")
        self.widget_37 = QtWidgets.QWidget(self.groupBox)
        self.widget_37.setGeometry(QtCore.QRect(2020, 340, 181, 61))
        self.widget_37.setObjectName("widget_37")
        self.lcdNumber_85 = QtWidgets.QLCDNumber(self.widget_37)
        self.lcdNumber_85.setEnabled(False)
        self.lcdNumber_85.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_85.setAutoFillBackground(False)
        self.lcdNumber_85.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_85.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_85.setSmallDecimalPoint(True)
        self.lcdNumber_85.setDigitCount(6)
        self.lcdNumber_85.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_85.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_85.setProperty("value", 0.0)
        self.lcdNumber_85.setObjectName("lcdNumber_85")
        self.label_38 = QtWidgets.QLabel(self.widget_37)
        self.label_38.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_38.setAutoFillBackground(False)
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.widget_38 = QtWidgets.QWidget(self.groupBox)
        self.widget_38.setGeometry(QtCore.QRect(2020, 550, 181, 61))
        self.widget_38.setObjectName("widget_38")
        self.lcdNumber_86 = QtWidgets.QLCDNumber(self.widget_38)
        self.lcdNumber_86.setEnabled(False)
        self.lcdNumber_86.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_86.setAutoFillBackground(False)
        self.lcdNumber_86.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_86.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_86.setSmallDecimalPoint(True)
        self.lcdNumber_86.setDigitCount(6)
        self.lcdNumber_86.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_86.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_86.setProperty("value", 0.0)
        self.lcdNumber_86.setObjectName("lcdNumber_86")
        self.label_39 = QtWidgets.QLabel(self.widget_38)
        self.label_39.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_39.setAutoFillBackground(False)
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_39.setScaledContents(True)
        self.label_39.setObjectName("label_39")
        self.widget_39 = QtWidgets.QWidget(self.groupBox)
        self.widget_39.setGeometry(QtCore.QRect(2020, 340, 181, 61))
        self.widget_39.setObjectName("widget_39")
        self.lcdNumber_87 = QtWidgets.QLCDNumber(self.widget_39)
        self.lcdNumber_87.setEnabled(False)
        self.lcdNumber_87.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_87.setAutoFillBackground(False)
        self.lcdNumber_87.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_87.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_87.setSmallDecimalPoint(True)
        self.lcdNumber_87.setDigitCount(6)
        self.lcdNumber_87.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_87.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_87.setProperty("value", 0.0)
        self.lcdNumber_87.setObjectName("lcdNumber_87")
        self.label_40 = QtWidgets.QLabel(self.widget_39)
        self.label_40.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_40.setAutoFillBackground(False)
        self.label_40.setText("")
        self.label_40.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_40.setScaledContents(True)
        self.label_40.setObjectName("label_40")
        self.widget_40 = QtWidgets.QWidget(self.groupBox)
        self.widget_40.setGeometry(QtCore.QRect(1180, 240, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_40.sizePolicy().hasHeightForWidth())
        self.widget_40.setSizePolicy(sizePolicy)
        self.widget_40.setObjectName("widget_40")
        self.lcdNumber_22 = QtWidgets.QLCDNumber(self.widget_40)
        self.lcdNumber_22.setEnabled(False)
        self.lcdNumber_22.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_22.sizePolicy().hasHeightForWidth())
        self.lcdNumber_22.setSizePolicy(sizePolicy)
        self.lcdNumber_22.setAutoFillBackground(False)
        self.lcdNumber_22.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_22.setSmallDecimalPoint(True)
        self.lcdNumber_22.setDigitCount(6)
        self.lcdNumber_22.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_22.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_22.setProperty("value", 0.0)
        self.lcdNumber_22.setObjectName("lcdNumber_22")
        self.CH22Temp = QtWidgets.QLabel(self.widget_40)
        self.CH22Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH22Temp.sizePolicy().hasHeightForWidth())
        self.CH22Temp.setSizePolicy(sizePolicy)
        self.CH22Temp.setAutoFillBackground(False)
        self.CH22Temp.setText("")
        self.CH22Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH22Temp.setScaledContents(True)
        self.CH22Temp.setObjectName("CH22Temp")
        self.widget_41 = QtWidgets.QWidget(self.groupBox)
        self.widget_41.setGeometry(QtCore.QRect(2020, 270, 181, 61))
        self.widget_41.setObjectName("widget_41")
        self.lcdNumber_89 = QtWidgets.QLCDNumber(self.widget_41)
        self.lcdNumber_89.setEnabled(False)
        self.lcdNumber_89.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_89.setAutoFillBackground(False)
        self.lcdNumber_89.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_89.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_89.setSmallDecimalPoint(True)
        self.lcdNumber_89.setDigitCount(6)
        self.lcdNumber_89.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_89.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_89.setProperty("value", 0.0)
        self.lcdNumber_89.setObjectName("lcdNumber_89")
        self.label_42 = QtWidgets.QLabel(self.widget_41)
        self.label_42.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_42.setAutoFillBackground(False)
        self.label_42.setText("")
        self.label_42.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_42.setScaledContents(True)
        self.label_42.setObjectName("label_42")
        self.widget_42 = QtWidgets.QWidget(self.groupBox)
        self.widget_42.setGeometry(QtCore.QRect(2020, 620, 181, 61))
        self.widget_42.setObjectName("widget_42")
        self.lcdNumber_90 = QtWidgets.QLCDNumber(self.widget_42)
        self.lcdNumber_90.setEnabled(False)
        self.lcdNumber_90.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_90.setAutoFillBackground(False)
        self.lcdNumber_90.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_90.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_90.setSmallDecimalPoint(True)
        self.lcdNumber_90.setDigitCount(6)
        self.lcdNumber_90.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_90.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_90.setProperty("value", 0.0)
        self.lcdNumber_90.setObjectName("lcdNumber_90")
        self.label_43 = QtWidgets.QLabel(self.widget_42)
        self.label_43.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_43.setAutoFillBackground(False)
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_43.setScaledContents(True)
        self.label_43.setObjectName("label_43")
        self.widget_43 = QtWidgets.QWidget(self.groupBox)
        self.widget_43.setGeometry(QtCore.QRect(2020, 410, 181, 61))
        self.widget_43.setObjectName("widget_43")
        self.lcdNumber_91 = QtWidgets.QLCDNumber(self.widget_43)
        self.lcdNumber_91.setEnabled(False)
        self.lcdNumber_91.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_91.setAutoFillBackground(False)
        self.lcdNumber_91.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_91.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_91.setSmallDecimalPoint(True)
        self.lcdNumber_91.setDigitCount(6)
        self.lcdNumber_91.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_91.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_91.setProperty("value", 0.0)
        self.lcdNumber_91.setObjectName("lcdNumber_91")
        self.label_44 = QtWidgets.QLabel(self.widget_43)
        self.label_44.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_44.setAutoFillBackground(False)
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_44.setScaledContents(True)
        self.label_44.setObjectName("label_44")
        self.widget_44 = QtWidgets.QWidget(self.groupBox)
        self.widget_44.setGeometry(QtCore.QRect(2020, 620, 181, 61))
        self.widget_44.setObjectName("widget_44")
        self.lcdNumber_92 = QtWidgets.QLCDNumber(self.widget_44)
        self.lcdNumber_92.setEnabled(False)
        self.lcdNumber_92.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_92.setAutoFillBackground(False)
        self.lcdNumber_92.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_92.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_92.setSmallDecimalPoint(True)
        self.lcdNumber_92.setDigitCount(6)
        self.lcdNumber_92.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_92.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_92.setProperty("value", 0.0)
        self.lcdNumber_92.setObjectName("lcdNumber_92")
        self.label_45 = QtWidgets.QLabel(self.widget_44)
        self.label_45.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_45.setAutoFillBackground(False)
        self.label_45.setText("")
        self.label_45.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_45.setScaledContents(True)
        self.label_45.setObjectName("label_45")
        self.widget_45 = QtWidgets.QWidget(self.groupBox)
        self.widget_45.setGeometry(QtCore.QRect(2020, 410, 181, 61))
        self.widget_45.setObjectName("widget_45")
        self.lcdNumber_93 = QtWidgets.QLCDNumber(self.widget_45)
        self.lcdNumber_93.setEnabled(False)
        self.lcdNumber_93.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_93.setAutoFillBackground(False)
        self.lcdNumber_93.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_93.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_93.setSmallDecimalPoint(True)
        self.lcdNumber_93.setDigitCount(6)
        self.lcdNumber_93.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_93.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_93.setProperty("value", 0.0)
        self.lcdNumber_93.setObjectName("lcdNumber_93")
        self.label_46 = QtWidgets.QLabel(self.widget_45)
        self.label_46.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_46.setAutoFillBackground(False)
        self.label_46.setText("")
        self.label_46.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_46.setScaledContents(True)
        self.label_46.setObjectName("label_46")
        self.widget_46 = QtWidgets.QWidget(self.groupBox)
        self.widget_46.setGeometry(QtCore.QRect(1180, 310, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_46.sizePolicy().hasHeightForWidth())
        self.widget_46.setSizePolicy(sizePolicy)
        self.widget_46.setObjectName("widget_46")
        self.lcdNumber_23 = QtWidgets.QLCDNumber(self.widget_46)
        self.lcdNumber_23.setEnabled(False)
        self.lcdNumber_23.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_23.sizePolicy().hasHeightForWidth())
        self.lcdNumber_23.setSizePolicy(sizePolicy)
        self.lcdNumber_23.setAutoFillBackground(False)
        self.lcdNumber_23.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_23.setSmallDecimalPoint(True)
        self.lcdNumber_23.setDigitCount(6)
        self.lcdNumber_23.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_23.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_23.setProperty("value", 0.0)
        self.lcdNumber_23.setObjectName("lcdNumber_23")
        self.CH23Temp = QtWidgets.QLabel(self.widget_46)
        self.CH23Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH23Temp.sizePolicy().hasHeightForWidth())
        self.CH23Temp.setSizePolicy(sizePolicy)
        self.CH23Temp.setAutoFillBackground(False)
        self.CH23Temp.setText("")
        self.CH23Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH23Temp.setScaledContents(True)
        self.CH23Temp.setObjectName("CH23Temp")
        self.widget_47 = QtWidgets.QWidget(self.groupBox)
        self.widget_47.setGeometry(QtCore.QRect(2020, 340, 181, 61))
        self.widget_47.setObjectName("widget_47")
        self.lcdNumber_95 = QtWidgets.QLCDNumber(self.widget_47)
        self.lcdNumber_95.setEnabled(False)
        self.lcdNumber_95.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_95.setAutoFillBackground(False)
        self.lcdNumber_95.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_95.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_95.setSmallDecimalPoint(True)
        self.lcdNumber_95.setDigitCount(6)
        self.lcdNumber_95.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_95.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_95.setProperty("value", 0.0)
        self.lcdNumber_95.setObjectName("lcdNumber_95")
        self.label_48 = QtWidgets.QLabel(self.widget_47)
        self.label_48.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_48.setAutoFillBackground(False)
        self.label_48.setText("")
        self.label_48.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_48.setScaledContents(True)
        self.label_48.setObjectName("label_48")
        self.widget_48 = QtWidgets.QWidget(self.groupBox)
        self.widget_48.setGeometry(QtCore.QRect(2020, 690, 181, 61))
        self.widget_48.setObjectName("widget_48")
        self.lcdNumber_96 = QtWidgets.QLCDNumber(self.widget_48)
        self.lcdNumber_96.setEnabled(False)
        self.lcdNumber_96.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_96.setAutoFillBackground(False)
        self.lcdNumber_96.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_96.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_96.setSmallDecimalPoint(True)
        self.lcdNumber_96.setDigitCount(6)
        self.lcdNumber_96.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_96.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_96.setProperty("value", 0.0)
        self.lcdNumber_96.setObjectName("lcdNumber_96")
        self.label_49 = QtWidgets.QLabel(self.widget_48)
        self.label_49.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_49.setAutoFillBackground(False)
        self.label_49.setText("")
        self.label_49.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_49.setScaledContents(True)
        self.label_49.setObjectName("label_49")
        self.widget_49 = QtWidgets.QWidget(self.groupBox)
        self.widget_49.setGeometry(QtCore.QRect(2020, 480, 181, 61))
        self.widget_49.setObjectName("widget_49")
        self.lcdNumber_97 = QtWidgets.QLCDNumber(self.widget_49)
        self.lcdNumber_97.setEnabled(False)
        self.lcdNumber_97.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_97.setAutoFillBackground(False)
        self.lcdNumber_97.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_97.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_97.setSmallDecimalPoint(True)
        self.lcdNumber_97.setDigitCount(6)
        self.lcdNumber_97.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_97.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_97.setProperty("value", 0.0)
        self.lcdNumber_97.setObjectName("lcdNumber_97")
        self.label_50 = QtWidgets.QLabel(self.widget_49)
        self.label_50.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_50.setAutoFillBackground(False)
        self.label_50.setText("")
        self.label_50.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_50.setScaledContents(True)
        self.label_50.setObjectName("label_50")
        self.widget_50 = QtWidgets.QWidget(self.groupBox)
        self.widget_50.setGeometry(QtCore.QRect(2020, 690, 181, 61))
        self.widget_50.setObjectName("widget_50")
        self.lcdNumber_98 = QtWidgets.QLCDNumber(self.widget_50)
        self.lcdNumber_98.setEnabled(False)
        self.lcdNumber_98.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_98.setAutoFillBackground(False)
        self.lcdNumber_98.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_98.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_98.setSmallDecimalPoint(True)
        self.lcdNumber_98.setDigitCount(6)
        self.lcdNumber_98.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_98.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_98.setProperty("value", 0.0)
        self.lcdNumber_98.setObjectName("lcdNumber_98")
        self.label_51 = QtWidgets.QLabel(self.widget_50)
        self.label_51.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_51.setAutoFillBackground(False)
        self.label_51.setText("")
        self.label_51.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_51.setScaledContents(True)
        self.label_51.setObjectName("label_51")
        self.widget_51 = QtWidgets.QWidget(self.groupBox)
        self.widget_51.setGeometry(QtCore.QRect(2020, 480, 181, 61))
        self.widget_51.setObjectName("widget_51")
        self.lcdNumber_99 = QtWidgets.QLCDNumber(self.widget_51)
        self.lcdNumber_99.setEnabled(False)
        self.lcdNumber_99.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_99.setAutoFillBackground(False)
        self.lcdNumber_99.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_99.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_99.setSmallDecimalPoint(True)
        self.lcdNumber_99.setDigitCount(6)
        self.lcdNumber_99.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_99.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_99.setProperty("value", 0.0)
        self.lcdNumber_99.setObjectName("lcdNumber_99")
        self.label_52 = QtWidgets.QLabel(self.widget_51)
        self.label_52.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_52.setAutoFillBackground(False)
        self.label_52.setText("")
        self.label_52.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_52.setScaledContents(True)
        self.label_52.setObjectName("label_52")
        self.widget_52 = QtWidgets.QWidget(self.groupBox)
        self.widget_52.setGeometry(QtCore.QRect(1180, 380, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_52.sizePolicy().hasHeightForWidth())
        self.widget_52.setSizePolicy(sizePolicy)
        self.widget_52.setObjectName("widget_52")
        self.lcdNumber_24 = QtWidgets.QLCDNumber(self.widget_52)
        self.lcdNumber_24.setEnabled(False)
        self.lcdNumber_24.setGeometry(QtCore.QRect(0, 10, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_24.sizePolicy().hasHeightForWidth())
        self.lcdNumber_24.setSizePolicy(sizePolicy)
        self.lcdNumber_24.setAutoFillBackground(False)
        self.lcdNumber_24.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_24.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_24.setSmallDecimalPoint(True)
        self.lcdNumber_24.setDigitCount(6)
        self.lcdNumber_24.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_24.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_24.setProperty("value", 0.0)
        self.lcdNumber_24.setObjectName("lcdNumber_24")
        self.CH24Temp = QtWidgets.QLabel(self.widget_52)
        self.CH24Temp.setGeometry(QtCore.QRect(140, 20, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH24Temp.sizePolicy().hasHeightForWidth())
        self.CH24Temp.setSizePolicy(sizePolicy)
        self.CH24Temp.setAutoFillBackground(False)
        self.CH24Temp.setText("")
        self.CH24Temp.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.CH24Temp.setScaledContents(True)
        self.CH24Temp.setObjectName("CH24Temp")
        self.widget_53 = QtWidgets.QWidget(self.groupBox)
        self.widget_53.setGeometry(QtCore.QRect(2020, 410, 181, 61))
        self.widget_53.setObjectName("widget_53")
        self.lcdNumber_101 = QtWidgets.QLCDNumber(self.widget_53)
        self.lcdNumber_101.setEnabled(False)
        self.lcdNumber_101.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_101.setAutoFillBackground(False)
        self.lcdNumber_101.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_101.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_101.setSmallDecimalPoint(True)
        self.lcdNumber_101.setDigitCount(6)
        self.lcdNumber_101.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_101.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_101.setProperty("value", 0.0)
        self.lcdNumber_101.setObjectName("lcdNumber_101")
        self.label_54 = QtWidgets.QLabel(self.widget_53)
        self.label_54.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_54.setAutoFillBackground(False)
        self.label_54.setText("")
        self.label_54.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_54.setScaledContents(True)
        self.label_54.setObjectName("label_54")
        self.widget_54 = QtWidgets.QWidget(self.groupBox)
        self.widget_54.setGeometry(QtCore.QRect(2020, 760, 181, 61))
        self.widget_54.setObjectName("widget_54")
        self.lcdNumber_102 = QtWidgets.QLCDNumber(self.widget_54)
        self.lcdNumber_102.setEnabled(False)
        self.lcdNumber_102.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_102.setAutoFillBackground(False)
        self.lcdNumber_102.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_102.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_102.setSmallDecimalPoint(True)
        self.lcdNumber_102.setDigitCount(6)
        self.lcdNumber_102.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_102.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_102.setProperty("value", 0.0)
        self.lcdNumber_102.setObjectName("lcdNumber_102")
        self.label_55 = QtWidgets.QLabel(self.widget_54)
        self.label_55.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_55.setAutoFillBackground(False)
        self.label_55.setText("")
        self.label_55.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_55.setScaledContents(True)
        self.label_55.setObjectName("label_55")
        self.widget_55 = QtWidgets.QWidget(self.groupBox)
        self.widget_55.setGeometry(QtCore.QRect(2020, 550, 181, 61))
        self.widget_55.setObjectName("widget_55")
        self.lcdNumber_103 = QtWidgets.QLCDNumber(self.widget_55)
        self.lcdNumber_103.setEnabled(False)
        self.lcdNumber_103.setGeometry(QtCore.QRect(0, 10, 131, 51))
        self.lcdNumber_103.setAutoFillBackground(False)
        self.lcdNumber_103.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.lcdNumber_103.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_103.setSmallDecimalPoint(True)
        self.lcdNumber_103.setDigitCount(6)
        self.lcdNumber_103.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_103.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_103.setProperty("value", 0.0)
        self.lcdNumber_103.setObjectName("lcdNumber_103")
        self.label_56 = QtWidgets.QLabel(self.widget_55)
        self.label_56.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_56.setAutoFillBackground(False)
        self.label_56.setText("")
        self.label_56.setPixmap(QtGui.QPixmap(":/ico/icons/high-temperature.png"))
        self.label_56.setScaledContents(True)
        self.label_56.setObjectName("label_56")
        self.widget_56 = QtWidgets.QWidget(self.groupBox)
        self.widget_56.setGeometry(QtCore.QRect(10, 40, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_56.sizePolicy().hasHeightForWidth())
        self.widget_56.setSizePolicy(sizePolicy)
        self.widget_56.setObjectName("widget_56")
        self.CH01 = QtWidgets.QTextEdit(self.widget_56)
        self.CH01.setEnabled(False)
        self.CH01.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH01.setAcceptDrops(False)
        self.CH01.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH01.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH01.setReadOnly(True)
        self.CH01.setObjectName("CH01")
        self.CH01Check = QtWidgets.QCheckBox(self.widget_56)
        self.CH01Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH01Check.sizePolicy().hasHeightForWidth())
        self.CH01Check.setSizePolicy(sizePolicy)
        self.CH01Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH01Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH01Check.setText("")
        self.CH01Check.setIconSize(QtCore.QSize(10, 10))
        self.CH01Check.setCheckable(True)
        self.CH01Check.setChecked(False)
        self.CH01Check.setAutoRepeat(False)
        self.CH01Check.setObjectName("CH01Check")
        self.widget_57 = QtWidgets.QWidget(self.groupBox)
        self.widget_57.setGeometry(QtCore.QRect(10, 110, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_57.sizePolicy().hasHeightForWidth())
        self.widget_57.setSizePolicy(sizePolicy)
        self.widget_57.setObjectName("widget_57")
        self.CH02 = QtWidgets.QTextEdit(self.widget_57)
        self.CH02.setEnabled(False)
        self.CH02.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH02.setAcceptDrops(False)
        self.CH02.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH02.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH02.setReadOnly(True)
        self.CH02.setObjectName("CH02")
        self.CH02Check = QtWidgets.QCheckBox(self.widget_57)
        self.CH02Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH02Check.sizePolicy().hasHeightForWidth())
        self.CH02Check.setSizePolicy(sizePolicy)
        self.CH02Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH02Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH02Check.setText("")
        self.CH02Check.setIconSize(QtCore.QSize(10, 10))
        self.CH02Check.setChecked(False)
        self.CH02Check.setAutoRepeat(False)
        self.CH02Check.setObjectName("CH02Check")
        self.widget_58 = QtWidgets.QWidget(self.groupBox)
        self.widget_58.setGeometry(QtCore.QRect(10, 180, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_58.sizePolicy().hasHeightForWidth())
        self.widget_58.setSizePolicy(sizePolicy)
        self.widget_58.setObjectName("widget_58")
        self.CH03 = QtWidgets.QTextEdit(self.widget_58)
        self.CH03.setEnabled(False)
        self.CH03.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH03.setAcceptDrops(False)
        self.CH03.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH03.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH03.setReadOnly(True)
        self.CH03.setObjectName("CH03")
        self.CH03Check = QtWidgets.QCheckBox(self.widget_58)
        self.CH03Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH03Check.sizePolicy().hasHeightForWidth())
        self.CH03Check.setSizePolicy(sizePolicy)
        self.CH03Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH03Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH03Check.setText("")
        self.CH03Check.setIconSize(QtCore.QSize(10, 10))
        self.CH03Check.setChecked(False)
        self.CH03Check.setAutoRepeat(False)
        self.CH03Check.setObjectName("CH03Check")
        self.widget_59 = QtWidgets.QWidget(self.groupBox)
        self.widget_59.setGeometry(QtCore.QRect(10, 250, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_59.sizePolicy().hasHeightForWidth())
        self.widget_59.setSizePolicy(sizePolicy)
        self.widget_59.setObjectName("widget_59")
        self.CH04 = QtWidgets.QTextEdit(self.widget_59)
        self.CH04.setEnabled(False)
        self.CH04.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH04.setAcceptDrops(False)
        self.CH04.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH04.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH04.setReadOnly(True)
        self.CH04.setObjectName("CH04")
        self.CH04Check = QtWidgets.QCheckBox(self.widget_59)
        self.CH04Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH04Check.sizePolicy().hasHeightForWidth())
        self.CH04Check.setSizePolicy(sizePolicy)
        self.CH04Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH04Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH04Check.setText("")
        self.CH04Check.setIconSize(QtCore.QSize(10, 10))
        self.CH04Check.setChecked(False)
        self.CH04Check.setAutoRepeat(False)
        self.CH04Check.setObjectName("CH04Check")
        self.widget_60 = QtWidgets.QWidget(self.groupBox)
        self.widget_60.setGeometry(QtCore.QRect(10, 320, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_60.sizePolicy().hasHeightForWidth())
        self.widget_60.setSizePolicy(sizePolicy)
        self.widget_60.setObjectName("widget_60")
        self.CH05 = QtWidgets.QTextEdit(self.widget_60)
        self.CH05.setEnabled(False)
        self.CH05.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH05.setAcceptDrops(False)
        self.CH05.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH05.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH05.setReadOnly(True)
        self.CH05.setObjectName("CH05")
        self.CH05Check = QtWidgets.QCheckBox(self.widget_60)
        self.CH05Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH05Check.sizePolicy().hasHeightForWidth())
        self.CH05Check.setSizePolicy(sizePolicy)
        self.CH05Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH05Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH05Check.setText("")
        self.CH05Check.setIconSize(QtCore.QSize(10, 10))
        self.CH05Check.setChecked(False)
        self.CH05Check.setAutoRepeat(False)
        self.CH05Check.setObjectName("CH05Check")
        self.widget_61 = QtWidgets.QWidget(self.groupBox)
        self.widget_61.setGeometry(QtCore.QRect(10, 390, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_61.sizePolicy().hasHeightForWidth())
        self.widget_61.setSizePolicy(sizePolicy)
        self.widget_61.setObjectName("widget_61")
        self.CH06 = QtWidgets.QTextEdit(self.widget_61)
        self.CH06.setEnabled(False)
        self.CH06.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH06.setAcceptDrops(False)
        self.CH06.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH06.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH06.setReadOnly(True)
        self.CH06.setObjectName("CH06")
        self.CH06Check = QtWidgets.QCheckBox(self.widget_61)
        self.CH06Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH06Check.sizePolicy().hasHeightForWidth())
        self.CH06Check.setSizePolicy(sizePolicy)
        self.CH06Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH06Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH06Check.setText("")
        self.CH06Check.setIconSize(QtCore.QSize(10, 10))
        self.CH06Check.setChecked(False)
        self.CH06Check.setAutoRepeat(False)
        self.CH06Check.setObjectName("CH06Check")
        self.widget_62 = QtWidgets.QWidget(self.groupBox)
        self.widget_62.setGeometry(QtCore.QRect(350, 40, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_62.sizePolicy().hasHeightForWidth())
        self.widget_62.setSizePolicy(sizePolicy)
        self.widget_62.setObjectName("widget_62")
        self.CH07 = QtWidgets.QTextEdit(self.widget_62)
        self.CH07.setEnabled(False)
        self.CH07.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH07.setAcceptDrops(False)
        self.CH07.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH07.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH07.setReadOnly(True)
        self.CH07.setObjectName("CH07")
        self.CH07Check = QtWidgets.QCheckBox(self.widget_62)
        self.CH07Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH07Check.sizePolicy().hasHeightForWidth())
        self.CH07Check.setSizePolicy(sizePolicy)
        self.CH07Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH07Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH07Check.setText("")
        self.CH07Check.setIconSize(QtCore.QSize(10, 10))
        self.CH07Check.setChecked(False)
        self.CH07Check.setAutoRepeat(False)
        self.CH07Check.setObjectName("CH07Check")
        self.widget_63 = QtWidgets.QWidget(self.groupBox)
        self.widget_63.setGeometry(QtCore.QRect(350, 110, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_63.sizePolicy().hasHeightForWidth())
        self.widget_63.setSizePolicy(sizePolicy)
        self.widget_63.setObjectName("widget_63")
        self.CH08 = QtWidgets.QTextEdit(self.widget_63)
        self.CH08.setEnabled(False)
        self.CH08.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH08.setAcceptDrops(False)
        self.CH08.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH08.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH08.setReadOnly(True)
        self.CH08.setObjectName("CH08")
        self.CH08Check = QtWidgets.QCheckBox(self.widget_63)
        self.CH08Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH08Check.sizePolicy().hasHeightForWidth())
        self.CH08Check.setSizePolicy(sizePolicy)
        self.CH08Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH08Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH08Check.setText("")
        self.CH08Check.setIconSize(QtCore.QSize(10, 10))
        self.CH08Check.setChecked(False)
        self.CH08Check.setAutoRepeat(False)
        self.CH08Check.setObjectName("CH08Check")
        self.widget_64 = QtWidgets.QWidget(self.groupBox)
        self.widget_64.setGeometry(QtCore.QRect(350, 180, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_64.sizePolicy().hasHeightForWidth())
        self.widget_64.setSizePolicy(sizePolicy)
        self.widget_64.setObjectName("widget_64")
        self.CH09 = QtWidgets.QTextEdit(self.widget_64)
        self.CH09.setEnabled(False)
        self.CH09.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH09.setAcceptDrops(False)
        self.CH09.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH09.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH09.setReadOnly(True)
        self.CH09.setObjectName("CH09")
        self.CH09Check = QtWidgets.QCheckBox(self.widget_64)
        self.CH09Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH09Check.sizePolicy().hasHeightForWidth())
        self.CH09Check.setSizePolicy(sizePolicy)
        self.CH09Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH09Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH09Check.setText("")
        self.CH09Check.setIconSize(QtCore.QSize(10, 10))
        self.CH09Check.setChecked(False)
        self.CH09Check.setAutoRepeat(False)
        self.CH09Check.setObjectName("CH09Check")
        self.widget_65 = QtWidgets.QWidget(self.groupBox)
        self.widget_65.setGeometry(QtCore.QRect(350, 250, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_65.sizePolicy().hasHeightForWidth())
        self.widget_65.setSizePolicy(sizePolicy)
        self.widget_65.setObjectName("widget_65")
        self.CH10 = QtWidgets.QTextEdit(self.widget_65)
        self.CH10.setEnabled(False)
        self.CH10.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH10.setAcceptDrops(False)
        self.CH10.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH10.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH10.setReadOnly(True)
        self.CH10.setObjectName("CH10")
        self.CH10Check = QtWidgets.QCheckBox(self.widget_65)
        self.CH10Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH10Check.sizePolicy().hasHeightForWidth())
        self.CH10Check.setSizePolicy(sizePolicy)
        self.CH10Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH10Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH10Check.setText("")
        self.CH10Check.setIconSize(QtCore.QSize(10, 10))
        self.CH10Check.setChecked(False)
        self.CH10Check.setAutoRepeat(False)
        self.CH10Check.setObjectName("CH10Check")
        self.widget_66 = QtWidgets.QWidget(self.groupBox)
        self.widget_66.setGeometry(QtCore.QRect(350, 320, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_66.sizePolicy().hasHeightForWidth())
        self.widget_66.setSizePolicy(sizePolicy)
        self.widget_66.setObjectName("widget_66")
        self.CH11 = QtWidgets.QTextEdit(self.widget_66)
        self.CH11.setEnabled(False)
        self.CH11.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH11.setAcceptDrops(False)
        self.CH11.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH11.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH11.setReadOnly(True)
        self.CH11.setObjectName("CH11")
        self.CH11Check = QtWidgets.QCheckBox(self.widget_66)
        self.CH11Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH11Check.sizePolicy().hasHeightForWidth())
        self.CH11Check.setSizePolicy(sizePolicy)
        self.CH11Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH11Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH11Check.setText("")
        self.CH11Check.setIconSize(QtCore.QSize(10, 10))
        self.CH11Check.setChecked(False)
        self.CH11Check.setAutoRepeat(False)
        self.CH11Check.setObjectName("CH11Check")
        self.widget_67 = QtWidgets.QWidget(self.groupBox)
        self.widget_67.setGeometry(QtCore.QRect(350, 390, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_67.sizePolicy().hasHeightForWidth())
        self.widget_67.setSizePolicy(sizePolicy)
        self.widget_67.setObjectName("widget_67")
        self.CH12 = QtWidgets.QTextEdit(self.widget_67)
        self.CH12.setEnabled(False)
        self.CH12.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH12.setAcceptDrops(False)
        self.CH12.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH12.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH12.setReadOnly(True)
        self.CH12.setObjectName("CH12")
        self.CH12Check = QtWidgets.QCheckBox(self.widget_67)
        self.CH12Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH12Check.sizePolicy().hasHeightForWidth())
        self.CH12Check.setSizePolicy(sizePolicy)
        self.CH12Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH12Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH12Check.setText("")
        self.CH12Check.setIconSize(QtCore.QSize(10, 10))
        self.CH12Check.setChecked(False)
        self.CH12Check.setAutoRepeat(False)
        self.CH12Check.setObjectName("CH12Check")
        self.widget_68 = QtWidgets.QWidget(self.groupBox)
        self.widget_68.setGeometry(QtCore.QRect(690, 40, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_68.sizePolicy().hasHeightForWidth())
        self.widget_68.setSizePolicy(sizePolicy)
        self.widget_68.setObjectName("widget_68")
        self.CH13 = QtWidgets.QTextEdit(self.widget_68)
        self.CH13.setEnabled(False)
        self.CH13.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH13.setAcceptDrops(False)
        self.CH13.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH13.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH13.setReadOnly(True)
        self.CH13.setObjectName("CH13")
        self.CH13Check = QtWidgets.QCheckBox(self.widget_68)
        self.CH13Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH13Check.sizePolicy().hasHeightForWidth())
        self.CH13Check.setSizePolicy(sizePolicy)
        self.CH13Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH13Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH13Check.setText("")
        self.CH13Check.setIconSize(QtCore.QSize(10, 10))
        self.CH13Check.setChecked(False)
        self.CH13Check.setAutoRepeat(False)
        self.CH13Check.setObjectName("CH13Check")
        self.widget_69 = QtWidgets.QWidget(self.groupBox)
        self.widget_69.setGeometry(QtCore.QRect(690, 110, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_69.sizePolicy().hasHeightForWidth())
        self.widget_69.setSizePolicy(sizePolicy)
        self.widget_69.setObjectName("widget_69")
        self.CH14 = QtWidgets.QTextEdit(self.widget_69)
        self.CH14.setEnabled(False)
        self.CH14.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH14.setAcceptDrops(False)
        self.CH14.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH14.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH14.setReadOnly(True)
        self.CH14.setObjectName("CH14")
        self.CH14Check = QtWidgets.QCheckBox(self.widget_69)
        self.CH14Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH14Check.sizePolicy().hasHeightForWidth())
        self.CH14Check.setSizePolicy(sizePolicy)
        self.CH14Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH14Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH14Check.setText("")
        self.CH14Check.setIconSize(QtCore.QSize(10, 10))
        self.CH14Check.setChecked(False)
        self.CH14Check.setAutoRepeat(False)
        self.CH14Check.setObjectName("CH14Check")
        self.widget_70 = QtWidgets.QWidget(self.groupBox)
        self.widget_70.setGeometry(QtCore.QRect(690, 180, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_70.sizePolicy().hasHeightForWidth())
        self.widget_70.setSizePolicy(sizePolicy)
        self.widget_70.setObjectName("widget_70")
        self.CH15 = QtWidgets.QTextEdit(self.widget_70)
        self.CH15.setEnabled(False)
        self.CH15.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH15.setAcceptDrops(False)
        self.CH15.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH15.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH15.setReadOnly(True)
        self.CH15.setObjectName("CH15")
        self.CH15Check = QtWidgets.QCheckBox(self.widget_70)
        self.CH15Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH15Check.sizePolicy().hasHeightForWidth())
        self.CH15Check.setSizePolicy(sizePolicy)
        self.CH15Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH15Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH15Check.setText("")
        self.CH15Check.setIconSize(QtCore.QSize(10, 10))
        self.CH15Check.setChecked(False)
        self.CH15Check.setAutoRepeat(False)
        self.CH15Check.setObjectName("CH15Check")
        self.widget_71 = QtWidgets.QWidget(self.groupBox)
        self.widget_71.setGeometry(QtCore.QRect(690, 250, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_71.sizePolicy().hasHeightForWidth())
        self.widget_71.setSizePolicy(sizePolicy)
        self.widget_71.setObjectName("widget_71")
        self.CH16 = QtWidgets.QTextEdit(self.widget_71)
        self.CH16.setEnabled(False)
        self.CH16.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH16.setAcceptDrops(False)
        self.CH16.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH16.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH16.setReadOnly(True)
        self.CH16.setObjectName("CH16")
        self.CH16Check = QtWidgets.QCheckBox(self.widget_71)
        self.CH16Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH16Check.sizePolicy().hasHeightForWidth())
        self.CH16Check.setSizePolicy(sizePolicy)
        self.CH16Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH16Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH16Check.setText("")
        self.CH16Check.setIconSize(QtCore.QSize(10, 10))
        self.CH16Check.setChecked(False)
        self.CH16Check.setAutoRepeat(False)
        self.CH16Check.setObjectName("CH16Check")
        self.widget_72 = QtWidgets.QWidget(self.groupBox)
        self.widget_72.setGeometry(QtCore.QRect(690, 320, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_72.sizePolicy().hasHeightForWidth())
        self.widget_72.setSizePolicy(sizePolicy)
        self.widget_72.setObjectName("widget_72")
        self.CH17 = QtWidgets.QTextEdit(self.widget_72)
        self.CH17.setEnabled(False)
        self.CH17.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH17.setAcceptDrops(False)
        self.CH17.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH17.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH17.setReadOnly(True)
        self.CH17.setObjectName("CH17")
        self.CH17Check = QtWidgets.QCheckBox(self.widget_72)
        self.CH17Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH17Check.sizePolicy().hasHeightForWidth())
        self.CH17Check.setSizePolicy(sizePolicy)
        self.CH17Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH17Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH17Check.setText("")
        self.CH17Check.setIconSize(QtCore.QSize(10, 10))
        self.CH17Check.setChecked(False)
        self.CH17Check.setAutoRepeat(False)
        self.CH17Check.setObjectName("CH17Check")
        self.widget_73 = QtWidgets.QWidget(self.groupBox)
        self.widget_73.setGeometry(QtCore.QRect(690, 390, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_73.sizePolicy().hasHeightForWidth())
        self.widget_73.setSizePolicy(sizePolicy)
        self.widget_73.setObjectName("widget_73")
        self.CH18 = QtWidgets.QTextEdit(self.widget_73)
        self.CH18.setEnabled(False)
        self.CH18.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH18.setAcceptDrops(False)
        self.CH18.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH18.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH18.setReadOnly(True)
        self.CH18.setObjectName("CH18")
        self.CH18Check = QtWidgets.QCheckBox(self.widget_73)
        self.CH18Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH18Check.sizePolicy().hasHeightForWidth())
        self.CH18Check.setSizePolicy(sizePolicy)
        self.CH18Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH18Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH18Check.setText("")
        self.CH18Check.setIconSize(QtCore.QSize(10, 10))
        self.CH18Check.setChecked(False)
        self.CH18Check.setAutoRepeat(False)
        self.CH18Check.setObjectName("CH18Check")
        self.widget_74 = QtWidgets.QWidget(self.groupBox)
        self.widget_74.setGeometry(QtCore.QRect(1030, 40, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_74.sizePolicy().hasHeightForWidth())
        self.widget_74.setSizePolicy(sizePolicy)
        self.widget_74.setObjectName("widget_74")
        self.CH19 = QtWidgets.QTextEdit(self.widget_74)
        self.CH19.setEnabled(False)
        self.CH19.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH19.setAcceptDrops(False)
        self.CH19.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH19.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH19.setReadOnly(True)
        self.CH19.setObjectName("CH19")
        self.CH19Check = QtWidgets.QCheckBox(self.widget_74)
        self.CH19Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH19Check.sizePolicy().hasHeightForWidth())
        self.CH19Check.setSizePolicy(sizePolicy)
        self.CH19Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH19Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH19Check.setText("")
        self.CH19Check.setIconSize(QtCore.QSize(10, 10))
        self.CH19Check.setChecked(False)
        self.CH19Check.setAutoRepeat(False)
        self.CH19Check.setObjectName("CH19Check")
        self.widget_75 = QtWidgets.QWidget(self.groupBox)
        self.widget_75.setGeometry(QtCore.QRect(1030, 110, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_75.sizePolicy().hasHeightForWidth())
        self.widget_75.setSizePolicy(sizePolicy)
        self.widget_75.setObjectName("widget_75")
        self.CH20 = QtWidgets.QTextEdit(self.widget_75)
        self.CH20.setEnabled(False)
        self.CH20.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH20.setAcceptDrops(False)
        self.CH20.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH20.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH20.setReadOnly(True)
        self.CH20.setObjectName("CH20")
        self.CH20Check = QtWidgets.QCheckBox(self.widget_75)
        self.CH20Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH20Check.sizePolicy().hasHeightForWidth())
        self.CH20Check.setSizePolicy(sizePolicy)
        self.CH20Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH20Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH20Check.setText("")
        self.CH20Check.setIconSize(QtCore.QSize(10, 10))
        self.CH20Check.setChecked(False)
        self.CH20Check.setAutoRepeat(False)
        self.CH20Check.setObjectName("CH20Check")
        self.widget_76 = QtWidgets.QWidget(self.groupBox)
        self.widget_76.setGeometry(QtCore.QRect(1030, 180, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_76.sizePolicy().hasHeightForWidth())
        self.widget_76.setSizePolicy(sizePolicy)
        self.widget_76.setObjectName("widget_76")
        self.CH21 = QtWidgets.QTextEdit(self.widget_76)
        self.CH21.setEnabled(False)
        self.CH21.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH21.setAcceptDrops(False)
        self.CH21.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH21.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH21.setReadOnly(True)
        self.CH21.setObjectName("CH21")
        self.CH21Check = QtWidgets.QCheckBox(self.widget_76)
        self.CH21Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH21Check.sizePolicy().hasHeightForWidth())
        self.CH21Check.setSizePolicy(sizePolicy)
        self.CH21Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH21Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH21Check.setText("")
        self.CH21Check.setIconSize(QtCore.QSize(10, 10))
        self.CH21Check.setChecked(False)
        self.CH21Check.setAutoRepeat(False)
        self.CH21Check.setObjectName("CH21Check")
        self.widget_77 = QtWidgets.QWidget(self.groupBox)
        self.widget_77.setGeometry(QtCore.QRect(1030, 250, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_77.sizePolicy().hasHeightForWidth())
        self.widget_77.setSizePolicy(sizePolicy)
        self.widget_77.setObjectName("widget_77")
        self.CH22 = QtWidgets.QTextEdit(self.widget_77)
        self.CH22.setEnabled(False)
        self.CH22.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH22.setAcceptDrops(False)
        self.CH22.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH22.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH22.setReadOnly(True)
        self.CH22.setObjectName("CH22")
        self.CH22Check = QtWidgets.QCheckBox(self.widget_77)
        self.CH22Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH22Check.sizePolicy().hasHeightForWidth())
        self.CH22Check.setSizePolicy(sizePolicy)
        self.CH22Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH22Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH22Check.setText("")
        self.CH22Check.setIconSize(QtCore.QSize(10, 10))
        self.CH22Check.setChecked(False)
        self.CH22Check.setAutoRepeat(False)
        self.CH22Check.setObjectName("CH22Check")
        self.widget_78 = QtWidgets.QWidget(self.groupBox)
        self.widget_78.setGeometry(QtCore.QRect(1030, 320, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_78.sizePolicy().hasHeightForWidth())
        self.widget_78.setSizePolicy(sizePolicy)
        self.widget_78.setObjectName("widget_78")
        self.CH23 = QtWidgets.QTextEdit(self.widget_78)
        self.CH23.setEnabled(False)
        self.CH23.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH23.setAcceptDrops(False)
        self.CH23.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH23.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH23.setReadOnly(True)
        self.CH23.setObjectName("CH23")
        self.CH23Check = QtWidgets.QCheckBox(self.widget_78)
        self.CH23Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH23Check.sizePolicy().hasHeightForWidth())
        self.CH23Check.setSizePolicy(sizePolicy)
        self.CH23Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH23Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH23Check.setText("")
        self.CH23Check.setIconSize(QtCore.QSize(10, 10))
        self.CH23Check.setChecked(False)
        self.CH23Check.setAutoRepeat(False)
        self.CH23Check.setObjectName("CH23Check")
        self.widget_79 = QtWidgets.QWidget(self.groupBox)
        self.widget_79.setGeometry(QtCore.QRect(1030, 390, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_79.sizePolicy().hasHeightForWidth())
        self.widget_79.setSizePolicy(sizePolicy)
        self.widget_79.setObjectName("widget_79")
        self.CH24 = QtWidgets.QTextEdit(self.widget_79)
        self.CH24.setEnabled(False)
        self.CH24.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.CH24.setAcceptDrops(False)
        self.CH24.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.CH24.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.CH24.setReadOnly(True)
        self.CH24.setObjectName("CH24")
        self.CH24Check = QtWidgets.QCheckBox(self.widget_79)
        self.CH24Check.setGeometry(QtCore.QRect(10, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CH24Check.sizePolicy().hasHeightForWidth())
        self.CH24Check.setSizePolicy(sizePolicy)
        self.CH24Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CH24Check.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image:url(:/ico/icons/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image:url(:/ico/icons/switch-off.png);\n"
"}")
        self.CH24Check.setText("")
        self.CH24Check.setIconSize(QtCore.QSize(10, 10))
        self.CH24Check.setChecked(False)
        self.CH24Check.setAutoRepeat(False)
        self.CH24Check.setObjectName("CH24Check")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/icons/Datatab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.DATA, icon1, "")
        self.GRAPH = QtWidgets.QWidget()
        self.GRAPH.setObjectName("GRAPH")
        self.totalgraph = QtWidgets.QGraphicsView(self.GRAPH)
        self.totalgraph.setGeometry(QtCore.QRect(20, 20, 1389, 461))
        self.totalgraph.setObjectName("totalgraph")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico/icons/graphtab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.GRAPH, icon2, "")
        self.CSV = QtWidgets.QWidget()
        self.CSV.setObjectName("CSV")
#         self.CSV_Display_Text = QtWidgets.QLineEdit(self.CSV)
#         self.CSV_Display_Text.setGeometry(QtCore.QRect(550, 20, 311, 31))
#         self.CSV_Display_Text.setStyleSheet("background-color: #6a5acd;\n"
# "font: 10pt \"MS Shell Dlg 2\";\n"
# "color:rgb(255, 255, 255)")
#         self.CSV_Display_Text.setAlignment(QtCore.Qt.AlignCenter)
#         self.CSV_Display_Text.setReadOnly(True)
#         self.CSV_Display_Text.setObjectName("CSV_Display_Text")
        self.allcsv = QtWidgets.QFrame(self.CSV)
        self.allcsv.setGeometry(QtCore.QRect(19, 20, 1391, 461))
        self.allcsv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.allcsv.setFrameShadow(QtWidgets.QFrame.Plain)
        self.allcsv.setObjectName("allcsv")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ico/icons/csvtab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.CSV, icon3, "")
        self.ADVSETTINGS = QtWidgets.QWidget()
        self.ADVSETTINGS.setObjectName("ADVSETTINGS")
        self.pushButton = QtWidgets.QPushButton(self.ADVSETTINGS)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 201, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"text-align:right;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #28a745;\n"
"    border-width:2px;\n"
"    border-radius:5px;\n"
"    border-style:outset;\n"
"    color: rgb(0, 0, 0);\n"
"cursor: pointer;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.ADVSETTINGS)
        self.lineEdit.setGeometry(QtCore.QRect(250, 20, 431, 61))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;  /* White border with 2px width */\n"
"    border-radius: 5px;       /* Rounded corners with 5px radius */\n"
"    border-style: outset;     /* Outset border style */\n"
"    font-size: 22px;          /* Font size */\n"
"    padding: 10px;          /* Padding */\n"
"    font-family: \"MS Shell Dlg 2\"; /* Font family */\n"
"    color: white\n"
"}\n"
"")     
        self.lineEdit.setPlaceholderText("Select a File")
        palette = self.lineEdit.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(255, 255, 255, 75))
        self.lineEdit.setPalette(palette)
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.ADVSETTINGS)
        self.lineEdit_4.setGeometry(QtCore.QRect(730, 20, 660, 61))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;  /* White border with 2px width */\n"
"    border-radius: 5px;       /* Rounded corners with 5px radius */\n"
"    border-style: outset;     /* Outset border style */\n"
"    font-size: 22px;          /* Font size */\n"
"    padding: 10px;          /* Padding */\n"
"    font-family: \"MS Shell Dlg 2\"; /* Font family */\n"
"    color: white\n"
"}\n"
"")     
        self.lineEdit_4.setPlaceholderText("Enter Company Name")
        palette = self.lineEdit_4.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(255, 255, 255, 75))
        self.lineEdit_4.setPalette(palette)
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.label = QtWidgets.QLabel(self.ADVSETTINGS)
        self.label.setGeometry(QtCore.QRect(40, 30, 51, 41))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("QLabel {\n"
"    background-color: rgba(0, 0, 0, 0);  /* Fully transparent background */\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ico/icons/filogo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.selection = QtWidgets.QWidget(self.ADVSETTINGS)
        self.selection.setGeometry(QtCore.QRect(30, 100, 651, 361))
        self.selection.setStyleSheet("#selection {\n"
"    border: 1px solid rgb(255, 255, 255);  /* Dodger Blue border */\n"
"    border-radius: 5px;         /* Rounded corners */\n"
"    padding: 5px;               /* Padding inside the border */\n"
" /* Light background color */\n"
"}")
        self.selection.setObjectName("selection")
        self.TelemetryData_2 = QtWidgets.QLineEdit(self.selection)
        self.TelemetryData_2.setEnabled(False)
        self.TelemetryData_2.setGeometry(QtCore.QRect(170, 10, 311, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TelemetryData_2.sizePolicy().hasHeightForWidth())
        self.TelemetryData_2.setSizePolicy(sizePolicy)
        self.TelemetryData_2.setStyleSheet("border-style:outset;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-radius: 10px;\n"
"border-color: rgb(0, 160, 227);\n"
"color: rgb(0, 0, 0);")
        self.TelemetryData_2.setAlignment(QtCore.Qt.AlignCenter)
        self.TelemetryData_2.setReadOnly(True)
        self.TelemetryData_2.setObjectName("TelemetryData_2")
        self.BaudRate_2 = QtWidgets.QLineEdit(self.selection)
        self.BaudRate_2.setEnabled(False)
        self.BaudRate_2.setGeometry(QtCore.QRect(160, 70, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudRate_2.sizePolicy().hasHeightForWidth())
        self.BaudRate_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BaudRate_2.setFont(font)
        self.BaudRate_2.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: #ffffff;\n"
"font-weight: bold;")
        self.BaudRate_2.setFrame(False)
        self.BaudRate_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BaudRate_2.setReadOnly(True)
        self.BaudRate_2.setObjectName("BaudRate_2")
        self.BaudRate_3 = QtWidgets.QLineEdit(self.selection)
        self.BaudRate_3.setEnabled(False)
        self.BaudRate_3.setGeometry(QtCore.QRect(10, 120, 111, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudRate_3.sizePolicy().hasHeightForWidth())
        self.BaudRate_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.BaudRate_3.setFont(font)
        self.BaudRate_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-width:5px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.BaudRate_3.setAlignment(QtCore.Qt.AlignCenter)
        self.BaudRate_3.setReadOnly(True)
        self.BaudRate_3.setObjectName("BaudRate_3")
        self.BaudRate_4 = QtWidgets.QLineEdit(self.selection)
        self.BaudRate_4.setEnabled(False)
        self.BaudRate_4.setGeometry(QtCore.QRect(25, 200, 81, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudRate_4.sizePolicy().hasHeightForWidth())
        self.BaudRate_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.BaudRate_4.setFont(font)
        self.BaudRate_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-width:5px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.BaudRate_4.setAlignment(QtCore.Qt.AlignCenter)
        self.BaudRate_4.setReadOnly(True)
        self.BaudRate_4.setObjectName("BaudRate_4")
        self.BaudRate_5 = QtWidgets.QLineEdit(self.selection)
        self.BaudRate_5.setEnabled(False)
        self.BaudRate_5.setGeometry(QtCore.QRect(410, 70, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudRate_5.sizePolicy().hasHeightForWidth())
        self.BaudRate_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BaudRate_5.setFont(font)
        self.BaudRate_5.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: #ffffff;\n"
"font-weight: bold;")
        self.BaudRate_5.setFrame(False)
        self.BaudRate_5.setAlignment(QtCore.Qt.AlignCenter)
        self.BaudRate_5.setReadOnly(True)
        self.BaudRate_5.setObjectName("BaudRate_5")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.selection)
        self.dateEdit_2.setGeometry(QtCore.QRect(120, 120, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dateEdit_2.setStyleSheet("QDateEdit{\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    border: solid rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px; /* Width of the dropdown button */\n"
"    border-left: solid #00A0E3; /* Border for the dropdown button */\n"
"    /* background-color: rgb(255, 255, 255); */\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* QCalendarWidget styles */\n"
"QCalendarWidget {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* QCalendarWidget navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #00A0E3; /* Background color of the navigation bar */\n"
"}\n"
"\n"
"/* QCalendarWidget header row */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar QToolButton {\n"
"    color: white; /* Text color of the navigation bar buttons */\n"
"    background-color: #00A0E3; /* Background color of the navigation bar buttons */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth, \n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth {\n"
"    border: none;\n"
"    qproperty-icon: none;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::menu-indicator {\n"
"    width: 0px;\n"
"}\n"
"\n"
"/* QCalendarWidget header row - month and year */\n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton {\n"
"    color: white; /* Text color for month and year */\n"
"    background-color: black; /* Background color for month and year */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"/* Ensure the text color is white when these buttons are focused, active, or selected */\n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton:pressed, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton:pressed, \n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton:focus, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton:focus, \n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton:checked, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton:checked {\n"
"    color: white; /* Text color for month and year when focused, pressed, or checked */\n"
"}\n"
"\n"
"/* QMenu (dropdown list) styling for the month list */\n"
"QMenu {\n"
"    background-color: #00A0E3; /* Background color of the dropdown menu */\n"
"    color: white; /* Text color of the dropdown menu items */\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: black; /* Background color of each item */\n"
"    color: white; /* Text color of each item */\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #00A0E3; /* Text color of the selected item */\n"
"}\n"
"\n"
"/* QCalendarWidget selected date */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    color: blue; /* Text color */\n"
"    selection-background-color: #00A0E3; /* Background color for selected date */\n"
"    selection-color: black; /* Text color for selected date */\n"
"    border: none;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    outline: 0;\n"
"}\n"
"")
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setDisplayFormat("dd-MM-yy")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.selection)
        self.dateEdit_3.setGeometry(QtCore.QRect(120, 200, 191, 51))
        self.dateEdit_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateEdit_3.setDisplayFormat("dd-MM-yy")
        self.dateEdit_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dateEdit_3.setStyleSheet("QDateEdit{\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    border: solid rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px; /* Width of the dropdown button */\n"
"    border-left: solid #00A0E3; /* Border for the dropdown button */\n"
"    /* background-color: rgb(255, 255, 255); */\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* QCalendarWidget styles */\n"
"QCalendarWidget {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* QCalendarWidget navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #00A0E3; /* Background color of the navigation bar */\n"
"}\n"
"\n"
"/* QCalendarWidget header row */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar QToolButton {\n"
"    color: white; /* Text color of the navigation bar buttons */\n"
"    background-color: #00A0E3; /* Background color of the navigation bar buttons */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth, \n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth {\n"
"    border: none;\n"
"    qproperty-icon: none;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::menu-indicator {\n"
"    width: 0px;\n"
"}\n"
"\n"
"/* QCalendarWidget header row - month and year */\n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton {\n"
"    color: white; /* Text color for month and year */\n"
"    background-color: black; /* Background color for month and year */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"/* Ensure the text color is white when these buttons are focused, active, or selected */\n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton:pressed, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton:pressed, \n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton:focus, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton:focus, \n"
"QCalendarWidget QToolButton#qt_calendar_monthbutton:checked, \n"
"QCalendarWidget QToolButton#qt_calendar_yearbutton:checked {\n"
"    color: white; /* Text color for month and year when focused, pressed, or checked */\n"
"}\n"
"\n"
"/* QMenu (dropdown list) styling for the month list */\n"
"QMenu {\n"
"    background-color: #00A0E3; /* Background color of the dropdown menu */\n"
"    color: white; /* Text color of the dropdown menu items */\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: black; /* Background color of each item */\n"
"    color: white; /* Text color of each item */\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #00A0E3; /* Text color of the selected item */\n"
"}\n"
"\n"
"/* QCalendarWidget selected date */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    color: blue; /* Text color */\n"
"    selection-background-color: #00A0E3; /* Background color for selected date */\n"
"    selection-color: black; /* Text color for selected date */\n"
"    border: none;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    outline: 0;\n"
"}\n"
"")
        self.dateEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_3.setReadOnly(False)
        self.dateEdit_3.setTime(QtCore.QTime(2, 0, 0))
        self.dateEdit_3.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.selection)
        self.timeEdit_2.setGeometry(QtCore.QRect(370, 120, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_2.sizePolicy().hasHeightForWidth())
        self.timeEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.timeEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.timeEdit_2.setAutoFillBackground(False)
        self.timeEdit_2.setStyleSheet("QTimeEdit {\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    border: solid rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Style the up and down buttons */\n"
"QTimeEdit::up-button, QTimeEdit::down-button {\n"
"    width: 20px;\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"/* Style the up arrow */\n"
"QTimeEdit::up-arrow {\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-bottom: 6px solid white; /* Arrow color */\n"
"}\n"
"\n"
"/* Style the down arrow */\n"
"QTimeEdit::down-arrow {\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid white; /* Arrow color */\n"
"}\n"
"\n"
"  ")
        self.timeEdit_2.setWrapping(False)
        self.timeEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.timeEdit_2.setAccelerated(False)
        self.timeEdit_2.setProperty("showGroupSeparator", False)
        self.timeEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit_2.setCalendarPopup(False)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.timeEdit_4 = QtWidgets.QTimeEdit(self.selection)
        self.timeEdit_4.setGeometry(QtCore.QRect(370, 200, 181, 51))
        self.timeEdit_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.timeEdit_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.timeEdit_4.setStyleSheet("QTimeEdit {\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    border: solid rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Style the up and down buttons */\n"
"QTimeEdit::up-button, QTimeEdit::down-button {\n"
"    width: 20px;\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"/* Style the up arrow */\n"
"QTimeEdit::up-arrow {\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-bottom: 6px solid white; /* Arrow color */\n"
"}\n"
"\n"
"/* Style the down arrow */\n"
"QTimeEdit::down-arrow {\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid white; /* Arrow color */\n"
"}\n"
"")
        self.timeEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.timeEdit_4.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit_4.setCalendarPopup(True)
        self.timeEdit_4.setObjectName("timeEdit_4")
        self.Start_2 = QtWidgets.QPushButton(self.selection)
        self.Start_2.setGeometry(QtCore.QRect(100, 290, 101, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_2.sizePolicy().hasHeightForWidth())
        self.Start_2.setSizePolicy(sizePolicy)
        self.Start_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start_2.setStyleSheet("QPushButton{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"text-align:right;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-width:2px;\n"
"border-radius:5px;\n"
"border-style:outset;\n"
"border-color:rgb(85, 170, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.Start_2.setObjectName("Start_2")
        self.Start_3 = QtWidgets.QPushButton(self.selection)
        self.Start_3.setGeometry(QtCore.QRect(270, 290, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_3.sizePolicy().hasHeightForWidth())
        self.Start_3.setSizePolicy(sizePolicy)
        self.Start_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start_3.setStyleSheet("QPushButton{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"text-align:right;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(40, 167, 69);\n"
"    border-width:2px;\n"
"border-radius:5px;\n"
"border-style:outset;\n"
"border-color: #4caf50;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.Start_3.setObjectName("Start_3")
        self.Start_4 = QtWidgets.QPushButton(self.selection)
        self.Start_4.setGeometry(QtCore.QRect(460, 290, 121, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_4.sizePolicy().hasHeightForWidth())
        self.Start_4.setSizePolicy(sizePolicy)
        self.Start_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start_4.setStyleSheet("QPushButton{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"text-align:right;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #20C997;\n"
"    border-color: #74E2C0;\n"
"    border-width:2px;\n"
"    border-radius:5px;\n"
"    border-style:outset;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.Start_4.setObjectName("Start_4")
        self.label_2 = QtWidgets.QLabel(self.selection)
        self.label_2.setGeometry(QtCore.QRect(110, 300, 31, 31))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("QLabel {\n"
"    background-color: rgba(0, 0, 0, 0);  /* Fully transparent background */\n"
"}")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/ico/icons/set.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.selection)
        self.label_3.setGeometry(QtCore.QRect(290, 300, 31, 31))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet("QLabel {\n"
"    background-color: rgba(0, 0, 0, 0);  /* Fully transparent background */\n"
"}")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/ico/icons/check.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.selection)
        self.label_4.setGeometry(QtCore.QRect(480, 300, 31, 31))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("QLabel {\n"
"    background-color: rgba(0, 0, 0, 0);  /* Fully transparent background */\n"
"}")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/ico/icons/print.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.ADVSETTINGS)
        self.textEdit.setGeometry(QtCore.QRect(730, 150, 661, 131))
        self.textEdit.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"    border: 1px solid black;  /* White border with 2px width */\n"
"    border-radius: 5px;       /* Rounded corners with 5px radius */\n"
"    border-style: outset; ")
        self.textEdit.setPlaceholderText("Enter Text")
        palette = self.textEdit.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(0, 0, 0, 75))
        self.textEdit.setPalette(palette)
        self.textEdit.setObjectName("textEdit")
        self.Header = QtWidgets.QLineEdit(self.ADVSETTINGS)
        self.Header.setEnabled(False)
        self.Header.setGeometry(QtCore.QRect(730, 100, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header.sizePolicy().hasHeightForWidth())
        self.Header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Header.setFont(font)
        self.Header.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Header.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-width:5px;\n"
"border-radius: 10px;\n"
"color: white;\n"
"text-align: left;")
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setReadOnly(True)
        self.Header.setObjectName("Header")
#         self.Header_2 = QtWidgets.QLineEdit(self.ADVSETTINGS)
#         self.Header_2.setEnabled(False)
#         self.Header_2.setGeometry(QtCore.QRect(730, 250, 231, 41))
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.Header_2.sizePolicy().hasHeightForWidth())
#         self.Header_2.setSizePolicy(sizePolicy)
#         font = QtGui.QFont()
#         font.setFamily("MS Shell Dlg 2")
#         font.setPointSize(12)
#         font.setBold(False)
#         font.setItalic(False)
#         font.setWeight(9)
#         self.Header_2.setFont(font)
#         self.Header_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#         self.Header_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
# "border-width:5px;\n"
# "border-radius: 10px;\n"
# "color: white;\n"
# "text-align: left;")
#         self.Header_2.setAlignment(QtCore.Qt.AlignCenter)
#         self.Header_2.setReadOnly(True)
#         self.Header_2.setObjectName("Header_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.ADVSETTINGS)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 304, 201, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"text-align:right;\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #28a745;\n"
"    border-width:2px;\n"
"    border-radius:5px;\n"
"    border-style:outset;\n"
"    color: rgb(0, 0, 0);\n"
"cursor: pointer;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.ADVSETTINGS)
        self.label_5.setGeometry(QtCore.QRect(740, 314, 51, 41))
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setStyleSheet("QLabel {\n"
"    background-color: rgba(0, 0, 0, 0);  /* Fully transparent background */\n"
"}")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/ico/icons/letterhead.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.ADVSETTINGS)
        self.lineEdit_2.setGeometry(QtCore.QRect(950, 300, 440, 68))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;  /* White border with 2px width */\n"
"    border-radius: 5px;       /* Rounded corners with 5px radius */\n"
"    border-style: outset;     /* Outset border style */\n"
"    font-size: 22px;          /* Font size */\n"
"    padding: 10px;          /* Padding */\n"
"    font-family: \"MS Shell Dlg 2\"; /* Font family */\n"
"    color: white\n"
"}\n"
"")     
        self.lineEdit_2.setPlaceholderText("Upload Letterhead File")
        palette = self.lineEdit_2.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(255, 255, 255, 75))
        self.lineEdit_2.setPalette(palette)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        # LHFILE Display
        self.lineEdit_3 = QtWidgets.QLineEdit(self.ADVSETTINGS)
        self.lineEdit_3.setGeometry(QtCore.QRect(730, 390, 661, 68))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;  /* White border with 2px width */\n"
"    border-radius: 5px;       /* Rounded corners with 5px radius */\n"
"    border-style: outset;     /* Outset border style */\n"
"    font-size: 22px;          /* Font size */\n"
"    padding: 10px;          /* Padding */\n"
"    font-family: \"MS Shell Dlg 2\"; /* Font family */\n"
"    color: white\n"
"}\n"
"")
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ico/icons/settingtab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.ADVSETTINGS, icon4, "")
        self.Telemetry = QtWidgets.QWidget(self.centralwidget)
        self.Telemetry.setGeometry(QtCore.QRect(20, 680, 391, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Telemetry.sizePolicy().hasHeightForWidth())
        self.Telemetry.setSizePolicy(sizePolicy)
        self.Telemetry.setStyleSheet("#Telemetry {\n"
"    border: 1px solid rgb(255, 255, 255);  /* Dodger Blue border */\n"
"    border-radius: 5px;         /* Rounded corners */\n"
"    padding: 5px;               /* Padding inside the border */\n"
" /* Light background color */\n"
"}")
        self.Telemetry.setObjectName("Telemetry")
        self.TelemetryData = QtWidgets.QLineEdit(self.Telemetry)
        self.TelemetryData.setEnabled(False)
        self.TelemetryData.setGeometry(QtCore.QRect(50, 20, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TelemetryData.sizePolicy().hasHeightForWidth())
        self.TelemetryData.setSizePolicy(sizePolicy)
        self.TelemetryData.setStyleSheet("border-style:outset;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-radius: 10px;\n"
"border-color: rgb(0, 160, 227);\n"
"color: rgb(0, 0, 0);")
        self.TelemetryData.setAlignment(QtCore.Qt.AlignCenter)
        self.TelemetryData.setObjectName("TelemetryData")
        self.Start = QtWidgets.QPushButton(self.Telemetry)
        self.Start.setGeometry(QtCore.QRect(50, 80, 131, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start.sizePolicy().hasHeightForWidth())
        self.Start.setSizePolicy(sizePolicy)
        self.Start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-width:2px;\n"
"border-radius:5px;\n"
"border-style:outset;\n"
"    border-color: rgb(85, 170, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.Start.setObjectName("Start")
        self.Stop = QtWidgets.QPushButton(self.Telemetry)
        self.Stop.setGeometry(QtCore.QRect(205, 80, 131, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Stop.sizePolicy().hasHeightForWidth())
        self.Stop.setSizePolicy(sizePolicy)
        self.Stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Stop.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(228, 29, 82);\n"
"    border-width:2px;\n"
"border-radius:5px;\n"
"border-style:outset;\n"
"border-color:rgb(228, 29, 82);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.Stop.setObjectName("Stop")
        self.Serial = QtWidgets.QWidget(self.centralwidget)
        self.Serial.setGeometry(QtCore.QRect(20, 220, 391, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Serial.sizePolicy().hasHeightForWidth())
        self.Serial.setSizePolicy(sizePolicy)
        self.Serial.setStyleSheet("#Serial {\n"
"    border: 1px solid rgb(255, 255, 255);  /* Dodger Blue border */\n"
"    border-radius: 5px;         /* Rounded corners */\n"
"    padding: 5px;               /* Padding inside the border */\n"
" /* Light background color */\n"
"}")
        self.Serial.setObjectName("Serial")
        self.Settings = QtWidgets.QLineEdit(self.Serial)
        self.Settings.setEnabled(False)
        self.Settings.setGeometry(QtCore.QRect(50, 20, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        self.Settings.setStyleSheet("border-style:outset;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-radius: 10px;\n"
"border-color: rgb(0, 160, 227);\n"
"color: rgb(0, 0, 0);")
        self.Settings.setAlignment(QtCore.Qt.AlignCenter)
        self.Settings.setObjectName("Settings")
        self.SerialPort = QtWidgets.QLineEdit(self.Serial)
        self.SerialPort.setEnabled(False)
        self.SerialPort.setGeometry(QtCore.QRect(40, 80, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SerialPort.sizePolicy().hasHeightForWidth())
        self.SerialPort.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SerialPort.setFont(font)
        self.SerialPort.setMouseTracking(False)
        self.SerialPort.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-width:5px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.SerialPort.setCursorPosition(13)
        self.SerialPort.setAlignment(QtCore.Qt.AlignCenter)
        self.SerialPort.setObjectName("SerialPort")
        self.COMport = QtWidgets.QComboBox(self.Serial)
        self.COMport.setGeometry(QtCore.QRect(30, 120, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.COMport.sizePolicy().hasHeightForWidth())
        self.COMport.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.COMport.setFont(font)
        self.COMport.setAutoFillBackground(False)
        self.COMport.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:  solid rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;                /* Width of the dropdown button */\n"
"     border-left: solid #00A0E3; \n"
"}\n"
"QComboBox::down-arrow {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid rgb(255, 255, 255);\n"
"}\n"
"#comboBox QAbstractItemView {\n"
"    border: 2px solid #00A0E3;  /* Border for the dropdown list */\n"
"    selection-background-color: #ADD8E6; /* Background color for selected\n"
" items */\n"
"    color: rgb(170, 85, 255);\n"
"}")
        self.COMport.setEditable(False)
        self.COMport.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.COMport.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.COMport.setObjectName("COMport")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.COMport.addItem("")
        self.BaudRate = QtWidgets.QLineEdit(self.Serial)
        self.BaudRate.setEnabled(False)
        self.BaudRate.setGeometry(QtCore.QRect(230, 80, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudRate.sizePolicy().hasHeightForWidth())
        self.BaudRate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.BaudRate.setFont(font)
        self.BaudRate.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-width:5px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.BaudRate.setAlignment(QtCore.Qt.AlignCenter)
        self.BaudRate.setReadOnly(True)
        self.BaudRate.setObjectName("BaudRate")
        #Hello
        
        self.Parity = QtWidgets.QLineEdit(self.Serial)
        self.Parity.setEnabled(False)
        self.Parity.setGeometry(QtCore.QRect(210, 180, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Parity.sizePolicy().hasHeightForWidth())
        self.Parity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Parity.setFont(font)
        self.Parity.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-width:5px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.Parity.setAlignment(QtCore.Qt.AlignCenter)
        self.Parity.setReadOnly(True)
        self.Parity.setObjectName("Parity")
        #Hello
        
        self.StopBit = QtWidgets.QLineEdit(self.Serial)
        self.StopBit.setEnabled(False)
        self.StopBit.setGeometry(QtCore.QRect(225, 280, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopBit.sizePolicy().hasHeightForWidth())
        self.StopBit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.StopBit.setFont(font)
        self.StopBit.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-width:5px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.StopBit.setAlignment(QtCore.Qt.AlignCenter)
        self.StopBit.setReadOnly(True)
        self.StopBit.setObjectName("StopBit")
        
        #Hello
        self.SlaveID = QtWidgets.QLineEdit(self.Serial)
        self.SlaveID.setEnabled(False)
        self.SlaveID.setGeometry(QtCore.QRect(30, 180, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SlaveID.sizePolicy().hasHeightForWidth())
        self.SlaveID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SlaveID.setFont(font)
        self.SlaveID.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-width:5px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.SlaveID.setAlignment(QtCore.Qt.AlignCenter)
        self.SlaveID.setReadOnly(True)
        self.SlaveID.setObjectName("SlaveID")
        #Hello
        
        self.StartBit = QtWidgets.QLineEdit(self.Serial)
        self.StartBit.setEnabled(False)
        self.StartBit.setGeometry(QtCore.QRect(35, 280, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartBit.sizePolicy().hasHeightForWidth())
        self.StartBit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.StartBit.setFont(font)
        self.StartBit.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-width:5px;\n"
"border-radius: 10px;\n"
"color: white;")
        self.StartBit.setAlignment(QtCore.Qt.AlignCenter)
        self.StartBit.setReadOnly(True)
        self.StartBit.setObjectName("StartBit")
        
        #Hello
        
        self.Baud = QtWidgets.QComboBox(self.Serial)
        self.Baud.setGeometry(QtCore.QRect(220, 120, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Baud.sizePolicy().hasHeightForWidth())
        self.Baud.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Baud.setFont(font)
        self.Baud.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:  solid rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;                /* Width of the dropdown button */\n"
"    border-left: solid #00A0E3;  \n"
"/* Border for the dropdown button */\n"
"/*    background-color: rgb(255, 255, 255);*/\n"
"\n"
"}\n"
"QComboBox::down-arrow {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid rgb(255, 255, 255);\n"
"}")
        self.Baud.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.Baud.setFrame(True)
        self.Baud.setObjectName("Baud")
        self.Baud.addItem("")
        self.Baud.addItem("")
        self.Baud.addItem("")
        self.Baud.addItem("")
        #Hello
        
        self.Slave = QtWidgets.QComboBox(self.Serial)
        self.Slave.setGeometry(QtCore.QRect(30, 220, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slave.sizePolicy().hasHeightForWidth())
        self.Slave.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Slave.setFont(font)
        self.Slave.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:  solid rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;                /* Width of the dropdown button */\n"
"    border-left: solid #00A0E3;  \n"
"/* Border for the dropdown button */\n"
"/*    background-color: rgb(255, 255, 255);*/\n"
"\n"
"}\n"
"QComboBox::down-arrow {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid rgb(255, 255, 255);\n"
"}")
        self.Slave.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.Slave.setFrame(True)
        self.Slave.setObjectName("Slave")
        self.Slave.addItem("")
        self.Slave.addItem("")
        self.Slave.addItem("")
        self.Slave.addItem("")
        self.Slave.addItem("")
        self.Slave.addItem("")
        self.Slave.addItem("")
        self.Slave.addItem("")
        #Hello
        
        self.StartBitOpt = QtWidgets.QComboBox(self.Serial)
        self.StartBitOpt.setGeometry(QtCore.QRect(30, 320, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartBitOpt.sizePolicy().hasHeightForWidth())
        self.StartBitOpt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.StartBitOpt.setFont(font)
        self.StartBitOpt.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:  solid rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;                /* Width of the dropdown button */\n"
"    border-left: solid #00A0E3;  \n"
"/* Border for the dropdown button */\n"
"/*    background-color: rgb(255, 255, 255);*/\n"
"\n"
"}\n"
"QComboBox::down-arrow {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid rgb(255, 255, 255);\n"
"}")
        self.StartBitOpt.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.StartBitOpt.setFrame(True)
        self.StartBitOpt.setObjectName("StartBitOpt")
        self.StartBitOpt.addItem("")
        self.StartBitOpt.addItem("")
        
        #Hello
        
        self.ParityType = QtWidgets.QComboBox(self.Serial)
        self.ParityType.setGeometry(QtCore.QRect(220, 220, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ParityType.sizePolicy().hasHeightForWidth())
        self.ParityType.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ParityType.setFont(font)
        self.ParityType.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:  solid rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;                /* Width of the dropdown button */\n"
"    border-left: solid #00A0E3;  \n"
"/* Border for the dropdown button */\n"
"/*    background-color: rgb(255, 255, 255);*/\n"
"\n"
"}\n"
"QComboBox::down-arrow {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid rgb(255, 255, 255);\n"
"}")
        self.ParityType.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.ParityType.setFrame(True)
        self.ParityType.setObjectName("ParityType")
        self.ParityType.addItem("")
        self.ParityType.addItem("")
        self.ParityType.addItem("")
        #Hello
        
        self.StopBitOpt = QtWidgets.QComboBox(self.Serial)
        self.StopBitOpt.setGeometry(QtCore.QRect(220, 320, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopBitOpt.sizePolicy().hasHeightForWidth())
        self.StopBitOpt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.StopBitOpt.setFont(font)
        self.StopBitOpt.setStyleSheet("QComboBox{\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:  solid rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;                /* Width of the dropdown button */\n"
"    border-left: solid #00A0E3;  \n"
"/* Border for the dropdown button */\n"
"/*    background-color: rgb(255, 255, 255);*/\n"
"\n"
"}\n"
"QComboBox::down-arrow {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 6px solid;\n"
"    border-right: 6px solid;\n"
"    border-top: 6px solid rgb(255, 255, 255);\n"
"}")
        self.StopBitOpt.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.StopBitOpt.setFrame(True)
        self.StopBitOpt.setObjectName("StopBitOpt")
        self.StopBitOpt.addItem("")
        self.StopBitOpt.addItem("")
        self.StopBitOpt.addItem("")
        
        #Hello
        self.Save = QtWidgets.QPushButton(self.Serial)
        self.Save.setGeometry(QtCore.QRect(50, 390, 131, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Save.sizePolicy().hasHeightForWidth())
        self.Save.setSizePolicy(sizePolicy)
        self.Save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Save.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(40, 167, 69);\n"
"    border-width:2px;\n"
"border-radius:5px;\n"
"border-style:outset;\n"
"    border-color: #4caf50;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.Save.setObjectName("Save")
        self.IDSetting = QtWidgets.QPushButton(self.Serial)
        self.IDSetting.setGeometry(QtCore.QRect(210, 390, 131, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDSetting.sizePolicy().hasHeightForWidth())
        self.IDSetting.setSizePolicy(sizePolicy)
        self.IDSetting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IDSetting.setStyleSheet("QPushButton{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-width:2px;\n"
"border-radius:5px;\n"
"border-style:outset;\n"
"border-color:rgb(85, 170, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.IDSetting.setObjectName("IDSetting")
        
        #Hello
        self.ScannerSoftware = QtWidgets.QLineEdit(self.centralwidget)
        self.ScannerSoftware.setGeometry(QtCore.QRect(40, 145, 351, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScannerSoftware.sizePolicy().hasHeightForWidth())
        self.ScannerSoftware.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ScannerSoftware.setFont(font)
        self.ScannerSoftware.setStyleSheet("border-style:outset;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:5px;\n"
"border-radius: 15px;\n"
"border-color: rgb(0, 160, 227);\n"
"color: rgb(0, 0, 0);")
        self.ScannerSoftware.setCursorPosition(16)
        self.ScannerSoftware.setAlignment(QtCore.Qt.AlignCenter)
        self.ScannerSoftware.setReadOnly(True)
        self.ScannerSoftware.setObjectName("ScannerSoftware")
        self.TD = QtWidgets.QWidget(self.centralwidget)
        self.TD.setGeometry(QtCore.QRect(20, 830, 391, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TD.sizePolicy().hasHeightForWidth())
        self.TD.setSizePolicy(sizePolicy)
        self.TD.setStyleSheet("#TD {\n"
"    border: 1px solid rgb(255, 255, 255);  /* Dodger Blue border */\n"
"    border-radius: 5px;         /* Rounded corners */\n"
"    padding: 5px;               /* Padding inside the border */\n"
" /* Light background color */\n"
"}")
        self.TD.setObjectName("TD")
        self.DateTime = QtWidgets.QLineEdit(self.TD)
        self.DateTime.setEnabled(False)
        self.DateTime.setGeometry(QtCore.QRect(50, 20, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DateTime.sizePolicy().hasHeightForWidth())
        self.DateTime.setSizePolicy(sizePolicy)
        self.DateTime.setStyleSheet("border-style:outset;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-radius: 10px;\n"
"border-color: rgb(0, 160, 227);\n"
"color: rgb(0, 0, 0);")
        self.DateTime.setAlignment(QtCore.Qt.AlignCenter)
        self.DateTime.setObjectName("DateTime")
        self.dateEdit = QtWidgets.QDateEdit(self.TD)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setGeometry(QtCore.QRect(50, 80, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setStyleSheet("border:  solid rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setKeyboardTracking(True)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.TD)
        self.timeEdit.setEnabled(False)
        self.timeEdit.setGeometry(QtCore.QRect(207, 80, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        self.timeEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:  solid rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-radius: 10px;")
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setObjectName("timeEdit")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setEnabled(True)
        # self.logo.setGeometry(QtCore.QRect(20, 10, 391, 121))
        # Outer white box stays exactly same
        self.logo.setGeometry(QtCore.QRect(20, 10, 391, 121))

        # Image inside
        self.logo.setContentsMargins(12,12,12,12)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setScaledContents(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setStyleSheet("background-color:white; border:2px solid white; border-radius:8px;")       
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/ico/icons/Sigma_Logo_Temp.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setWordWrap(True)
        self.logo.setObjectName("logo")
        self.multigraph = QtWidgets.QGraphicsView(self.centralwidget)
        self.multigraph.setGeometry(QtCore.QRect(1180, 10, 711, 411))
        self.multigraph.setObjectName("multigraph")
        self.csv10 = QtWidgets.QFrame(self.centralwidget)
        self.csv10.setGeometry(QtCore.QRect(460, 10, 691, 411))
        self.csv10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.csv10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.csv10.setObjectName("csv10")
        self.Serial.raise_()
        self.tabWidget.raise_()
        self.Telemetry.raise_()
        self.ScannerSoftware.raise_()
        self.TD.raise_()
        self.logo.raise_()
        self.multigraph.raise_()
        self.csv10.raise_()
        SigmaControls.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SigmaControls)
        self.statusbar.setObjectName("statusbar")
        SigmaControls.setStatusBar(self.statusbar)

        self.retranslateUi(SigmaControls)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(SigmaControls)

    def retranslateUi(self, SigmaControls):
        _translate = QtCore.QCoreApplication.translate
        SigmaControls.setWindowTitle(_translate("SigmaControls", "Sigma Controls | IntelliScan"))
        self.groupBox.setTitle(_translate("SigmaControls", "Telemetry Data"))
        self.CH01.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH01</span></p></body></html>"))
        self.CH02.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH02</span></p></body></html>"))
        self.CH03.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH03</span></p></body></html>"))
        self.CH04.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH04</span></p></body></html>"))
        self.CH05.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH05</span></p></body></html>"))
        self.CH06.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH06</span></p></body></html>"))
        self.CH07.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH07</span></p></body></html>"))
        self.CH08.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH08</span></p></body></html>"))
        self.CH09.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH09</span></p></body></html>"))
        self.CH10.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH10</span></p></body></html>"))
        self.CH11.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH11</span></p></body></html>"))
        self.CH12.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH12</span></p></body></html>"))
        self.CH13.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH13</span></p></body></html>"))
        self.CH14.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH14</span></p></body></html>"))
        self.CH15.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH15</span></p></body></html>"))
        self.CH16.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH16</span></p></body></html>"))
        self.CH17.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH17</span></p></body></html>"))
        self.CH18.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH18</span></p></body></html>"))
        self.CH19.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH19</span></p></body></html>"))
        self.CH20.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH20</span></p></body></html>"))
        self.CH21.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH21</span></p></body></html>"))
        self.CH22.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH22</span></p></body></html>"))
        self.CH23.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH23</span></p></body></html>"))
        self.CH24.setHtml(_translate("SigmaControls", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:14pt;\">CH24</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DATA), _translate("SigmaControls", "DATA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GRAPH), _translate("SigmaControls", "GRAPH"))
        # self.CSV_Display_Text.setText(_translate("SigmaControls", "Temp_Today.csv"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CSV), _translate("SigmaControls", "CSV"))
        self.pushButton.setWhatsThis(_translate("SigmaControls", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Open File<br/></span></p></body></html>"))
        self.pushButton.setText(_translate("SigmaControls", "Open File"))
        self.TelemetryData_2.setText(_translate("SigmaControls", "Date & Time Selection"))
        self.BaudRate_2.setText(_translate("SigmaControls", "Date"))
        self.BaudRate_3.setText(_translate("SigmaControls", "Start :"))
        self.BaudRate_4.setText(_translate("SigmaControls", "End :"))
        self.BaudRate_5.setText(_translate("SigmaControls", "Time"))
        self.timeEdit_2.setDisplayFormat(_translate("SigmaControls", "HH:mm:ss"))
        self.timeEdit_4.setDisplayFormat(_translate("SigmaControls", "HH:mm:ss"))
        self.Start_2.setText(_translate("SigmaControls", "Set"))
        self.Start_3.setText(_translate("SigmaControls", "Submit"))
        self.Start_4.setText(_translate("SigmaControls", "Print"))
        self.Header.setText(_translate("SigmaControls", "Header :"))
        # self.Header_2.setText(_translate("SigmaControls", "Upload Letter Head :"))
        self.pushButton_2.setWhatsThis(_translate("SigmaControls", "<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">Open File<br/></span></p></body></html>"))
        self.pushButton_2.setText(_translate("SigmaControls", "Open File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ADVSETTINGS), _translate("SigmaControls", "ADV. SETTINGS"))
        self.TelemetryData.setText(_translate("SigmaControls", "Telemetry Data"))
        self.Start.setText(_translate("SigmaControls", "Start"))
        self.Stop.setText(_translate("SigmaControls", "Stop"))
        
        self.Save.setText(_translate("SigmaControls", "Save"))
        self.IDSetting.setText(_translate("SigmaControls", "ID Settings"))
        
        self.Settings.setText(_translate("SigmaControls", "Settings"))
        self.SerialPort.setText(_translate("SigmaControls", "Serial Port :"))
        self.COMport.setItemText(0, _translate("SigmaControls", "  COM1"))
        self.COMport.setItemText(1, _translate("SigmaControls", "  COM2"))
        self.COMport.setItemText(2, _translate("SigmaControls", "  COM3"))
        self.COMport.setItemText(3, _translate("SigmaControls", "  COM4"))
        self.COMport.setItemText(4, _translate("SigmaControls", "  COM5"))
        self.COMport.setItemText(5, _translate("SigmaControls", "  COM6"))
        self.COMport.setItemText(6, _translate("SigmaControls", "  COM7"))
        self.COMport.setItemText(7, _translate("SigmaControls", "  COM8"))
        self.COMport.setItemText(8, _translate("SigmaControls", "  COM9"))
        self.COMport.setItemText(9, _translate("SigmaControls", "  COM10"))
        self.COMport.setItemText(10, _translate("SigmaControls", "  COM11"))
        self.COMport.setItemText(11, _translate("SigmaControls", "  COM12"))
        self.COMport.setItemText(12, _translate("SigmaControls", "  COM13"))
        self.COMport.setItemText(13, _translate("SigmaControls", "  COM14"))
        self.COMport.setItemText(14, _translate("SigmaControls", "  COM15"))
        self.COMport.setItemText(15, _translate("SigmaControls", "  COM16"))
        self.COMport.setItemText(16, _translate("SigmaControls", "  COM17"))
        self.COMport.setItemText(17, _translate("SigmaControls", "  COM18"))
        self.COMport.setItemText(18, _translate("SigmaControls", "  COM19"))
        self.COMport.setItemText(19, _translate("SigmaControls", "  COM20"))
        
        
        self.BaudRate.setText(_translate("SigmaControls", "Baud Rate :"))
        self.Parity.setText(_translate("SigmaControls", "Parity :"))
        self.StopBit.setText(_translate("SigmaControls", "Stop Bits :"))
        self.SlaveID.setText(_translate("SigmaControls", "Slave ID :")) 
        self.StartBit.setText(_translate("SigmaControls", "Data Bits :"))  
        
        self.Baud.setItemText(0, _translate("SigmaControls", "  9600"))
        self.Baud.setItemText(1, _translate("SigmaControls", "  19200"))
        self.Baud.setItemText(2, _translate("SigmaControls", "  115200"))
        self.Baud.setItemText(3, _translate("SigmaControls", "  230400"))
        
        self.StopBitOpt.setItemText(0, _translate("SigmaControls", "  1"))
        self.StopBitOpt.setItemText(1, _translate("SigmaControls", "  2"))
        self.ParityType.setItemText(0, _translate("SigmaControls", "  N"))
        self.ParityType.setItemText(1, _translate("SigmaControls", "  E"))
        self.ParityType.setItemText(2, _translate("SigmaControls", "  O"))
        
        self.Slave.setItemText(0, _translate("SigmaControls", "  1"))
        self.Slave.setItemText(1, _translate("SigmaControls", "  2"))
        self.Slave.setItemText(2, _translate("SigmaControls", "  3"))
        self.Slave.setItemText(3, _translate("SigmaControls", "  4"))
        self.Slave.setItemText(4, _translate("SigmaControls", "  5"))
        self.Slave.setItemText(5, _translate("SigmaControls", "  6"))
        self.Slave.setItemText(6, _translate("SigmaControls", "  7"))
        self.Slave.setItemText(7, _translate("SigmaControls", "  8"))
        
        self.StartBitOpt.setItemText(0, _translate("SigmaControls", "  7"))
        self.StartBitOpt.setItemText(1, _translate("SigmaControls", "  8"))
        
        self.ScannerSoftware.setText(_translate("SigmaControls", "Scanner Software"))
        self.DateTime.setText(_translate("SigmaControls", "Date & Time"))
        self.dateEdit.setDisplayFormat(_translate("SigmaControls", "dd-MM-yyyy"))
        self.timeEdit.setDisplayFormat(_translate("SigmaControls", "HH:mm:ss"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SigmaControls = QtWidgets.QMainWindow()
    ui = Ui_SigmaControls_1()
    ui.setupUi(SigmaControls)
    SigmaControls.show()
    sys.exit(app.exec_())