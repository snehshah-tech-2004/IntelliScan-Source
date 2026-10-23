import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def _resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Ui_SigmaControls_2(object):
    def setupUi(self, SigmaControls):
        SigmaControls.setObjectName("SigmaControls")
        SigmaControls.resize(641, 446)
        icon = QtGui.QIcon(_resource_path("SIGMA_ICON.svg"))
        SigmaControls.setWindowIcon(icon)
        SigmaControls.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "border: 1px solid black;\n"
            "border-radius: 12px;"
        )
        SigmaControls.setIconSize(QtCore.QSize(100, 100))
        self.centralwidget = QtWidgets.QWidget(SigmaControls)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 641, 446))
        self.widget.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "border: 1px solid black;\n"
            "border-radius: 12px;"
        )
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 391, 51))
        self.lineEdit.setStyleSheet(
            "border-style:outset;\n"
            'font: 14pt "MS Shell Dlg 2";\n'
            "background-color: rgb(255, 255, 255);\n"
            "border-width:5px;\n"
            "border-radius: 15px;\n"
            "border-color: rgb(0, 160, 227);\n"
            "color: rgb(0, 0, 0);"
        )
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 130, 121, 61))
        self.lineEdit_2.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 220, 121, 61))
        self.lineEdit_3.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "padding-right: -50px; \n"
            "color: white;"
        )
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 140, 361, 51))
        self.lineEdit_4.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 220, 361, 51))
        self.lineEdit_5.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.Start_2 = QtWidgets.QPushButton(self.widget)
        self.Start_2.setGeometry(QtCore.QRect(240, 320, 141, 51))
        self.Start_2.setCheckable(True)
        self.Start_2.setChecked(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_2.sizePolicy().hasHeightForWidth())
        self.Start_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Start_2.setFont(font)
        self.Start_2.setStyleSheet(
            "QPushButton{\n"
            "    border-color: rgb(85, 255, 125);\n"
            'font: 12pt "MS Shell Dlg 2";\n'
            "    color: rgb(255, 255, 255);\n"
            "border: 1px solid white;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(40, 167, 69);\n"
            "    border-width:2px;\n"
            "border-radius:5px;\n"
            "border-style:outset;\n"
            "    border-color: #4caf50;\n"
            "    color: rgb(0, 0, 0);\n"
            "}\n"
            ""
        )
        self.Start_2.setObjectName("Start_2")
        SigmaControls.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SigmaControls)
        self.statusbar.setObjectName("statusbar")
        SigmaControls.setStatusBar(self.statusbar)

        self.retranslateUi(SigmaControls)
        QtCore.QMetaObject.connectSlotsByName(SigmaControls)

    def retranslateUi(self, SigmaControls):
        _translate = QtCore.QCoreApplication.translate
        SigmaControls.setWindowTitle(
            _translate("SigmaControls", "Sigma Controls | Login")
        )
        self.lineEdit.setText(_translate("SigmaControls", "Login Credentials"))
        self.lineEdit_2.setText(_translate("SigmaControls", "User ID :"))
        self.lineEdit_3.setText(_translate("SigmaControls", "Password :"))
        self.Start_2.setText(_translate("SigmaControls", "Submit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SigmaControls = QtWidgets.QMainWindow()
    SigmaControls.setMaximumSize(641, 446)

    ui = Ui_SigmaControls_2()
    ui.setupUi(SigmaControls)
    SigmaControls.show()

    sys.exit(app.exec_())