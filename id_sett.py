import os
import json
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


def _resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ruff: noqa: E402,F403,F405,F541,E722,F841,E701

CONFIG_FILE = "config.json"


class Ui_SigmaControls_4(object):
    def setupUi(self, SigmaControls):
        self.SigmaControls = SigmaControls
        SigmaControls.setObjectName("SigmaControls")
        SigmaControls.resize(1400, 800)
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
        self.widget.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        self.widget.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "border: 1px solid black;\n"
            "border-radius: 12px;"
        )
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(505, 20, 391, 51))
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
        self.log_time = QtWidgets.QLineEdit(self.widget)
        self.log_time.setEnabled(False)
        self.log_time.setGeometry(QtCore.QRect(500, 705, 201, 61))
        self.log_time.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.log_time.setObjectName("log_time")

        self.log_time_value = QtWidgets.QLineEdit(self.widget)
        self.log_time_value.setGeometry(QtCore.QRect(720, 710, 180, 51))
        self.log_time_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.log_time_value.setText("")
        self.log_time_value.setObjectName("log_time_value")

        # CH1 Settings
        self.div_factor_id1 = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id1.setEnabled(False)
        self.div_factor_id1.setGeometry(QtCore.QRect(10, 180, 201, 31))
        self.div_factor_id1.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "padding-right: -50px; \n"
            "color: white;"
        )
        self.div_factor_id1.setObjectName("div_factor_id1")

        self.div_factor_id1_value = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id1_value.setGeometry(QtCore.QRect(170, 180, 141, 41))
        self.div_factor_id1_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.div_factor_id1_value.setText("")
        self.div_factor_id1_value.setObjectName("div_factor_id1_value")

        self.yaxis_text_id1 = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id1.setEnabled(False)
        self.yaxis_text_id1.setGeometry(QtCore.QRect(10, 250, 201, 31))
        self.yaxis_text_id1.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id1.setObjectName("yaxis_text_id1")

        self.yaxis_text_id1_value = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id1_value.setGeometry(QtCore.QRect(170, 247, 141, 41))
        self.yaxis_text_id1_value.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id1_value.setText("")
        self.yaxis_text_id1_value.setObjectName("yaxis_text_id1_value")

        self.address_id1 = QtWidgets.QLineEdit(self.widget)
        self.address_id1.setEnabled(False)
        self.address_id1.setGeometry(QtCore.QRect(10, 320, 201, 31))
        self.address_id1.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id1.setObjectName("address_id1")

        self.address_id1_value = QtWidgets.QLineEdit(self.widget)
        self.address_id1_value.setGeometry(QtCore.QRect(170, 317, 141, 41))
        self.address_id1_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id1_value.setText("")
        self.address_id1_value.setObjectName("address_id1_value")

        # CH2 Settings
        #         self.id2_label = QtWidgets.QLineEdit(self.widget)
        #         self.id2_label.setEnabled(False)
        #         self.id2_label.setGeometry(QtCore.QRect(455, 120, 201, 31))
        #         self.id2_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        # "border-width:5px;\n"
        # "border-radius: 10px;\n"
        # "padding-right: -50px; \n"
        # "color: white;")
        #         self.id2_label.setObjectName("id2_label")

        self.div_factor_id2 = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id2.setEnabled(False)
        self.div_factor_id2.setGeometry(QtCore.QRect(370, 180, 201, 31))
        self.div_factor_id2.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "padding-right: -50px; \n"
            "color: white;"
        )
        self.div_factor_id2.setObjectName("div_factor_id2")

        self.div_factor_id2_value = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id2_value.setGeometry(QtCore.QRect(530, 180, 141, 41))
        self.div_factor_id2_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.div_factor_id2_value.setText("")
        self.div_factor_id2_value.setObjectName("div_factor_id2_value")

        self.yaxis_text_id2 = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id2.setEnabled(False)
        self.yaxis_text_id2.setGeometry(QtCore.QRect(370, 250, 201, 31))
        self.yaxis_text_id2.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id2.setObjectName("yaxis_text_id2")

        self.yaxis_text_id2_value = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id2_value.setGeometry(QtCore.QRect(530, 247, 141, 41))
        self.yaxis_text_id2_value.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id2_value.setText("")
        self.yaxis_text_id2_value.setObjectName("yaxis_text_id2_value")

        self.address_id2 = QtWidgets.QLineEdit(self.widget)
        self.address_id2.setEnabled(False)
        self.address_id2.setGeometry(QtCore.QRect(370, 320, 201, 31))
        self.address_id2.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id2.setObjectName("address_id2")

        self.address_id2_value = QtWidgets.QLineEdit(self.widget)
        self.address_id2_value.setGeometry(QtCore.QRect(530, 317, 141, 41))
        self.address_id2_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id2_value.setText("")
        self.address_id2_value.setObjectName("address_id2_value")

        # CH3 Settings
        #         self.id3_label = QtWidgets.QLineEdit(self.widget)
        #         self.id3_label.setEnabled(False)
        #         self.id3_label.setGeometry(QtCore.QRect(810, 120, 201, 31))
        #         self.id3_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        # "border-width:5px;\n"
        # "border-radius: 10px;\n"
        # "padding-right: -50px; \n"
        # "color: white;")
        #         self.id3_label.setObjectName("id3_label")

        self.div_factor_id3 = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id3.setEnabled(False)
        self.div_factor_id3.setGeometry(QtCore.QRect(725, 180, 201, 31))
        self.div_factor_id3.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "padding-right: -50px; \n"
            "color: white;"
        )
        self.div_factor_id3.setObjectName("div_factor_id3")

        self.div_factor_id3_value = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id3_value.setGeometry(QtCore.QRect(885, 180, 141, 41))
        self.div_factor_id3_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.div_factor_id3_value.setText("")
        self.div_factor_id3_value.setObjectName("div_factor_id3_value")

        self.yaxis_text_id3 = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id3.setEnabled(False)
        self.yaxis_text_id3.setGeometry(QtCore.QRect(725, 250, 201, 31))
        self.yaxis_text_id3.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id3.setObjectName("yaxis_text_id3")

        self.yaxis_text_id3_value = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id3_value.setGeometry(QtCore.QRect(885, 247, 141, 41))
        self.yaxis_text_id3_value.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id3_value.setText("")
        self.yaxis_text_id3_value.setObjectName("yaxis_text_id3_value")

        self.address_id3 = QtWidgets.QLineEdit(self.widget)
        self.address_id3.setEnabled(False)
        self.address_id3.setGeometry(QtCore.QRect(725, 320, 201, 31))
        self.address_id3.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id3.setObjectName("address_id3")

        self.address_id3_value = QtWidgets.QLineEdit(self.widget)
        self.address_id3_value.setGeometry(QtCore.QRect(885, 317, 141, 41))
        self.address_id3_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id3_value.setText("")
        self.address_id3_value.setObjectName("address_id3_value")

        # CH4 Settings
        #         self.id4_label = QtWidgets.QLineEdit(self.widget)
        #         self.id4_label.setEnabled(False)
        #         self.id4_label.setGeometry(QtCore.QRect(1165, 120, 201, 31))
        #         self.id4_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        # "border-width:5px;\n"
        # "border-radius: 10px;\n"
        # "padding-right: -50px; \n"
        # "color: white;")
        #         self.id4_label.setObjectName("id4_label")

        self.div_factor_id4 = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id4.setEnabled(False)
        self.div_factor_id4.setGeometry(QtCore.QRect(1080, 180, 201, 31))
        self.div_factor_id4.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "padding-right: -50px; \n"
            "color: white;"
        )
        self.div_factor_id4.setObjectName("div_factor_id4")

        self.div_factor_id4_value = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id4_value.setGeometry(QtCore.QRect(1240, 180, 141, 41))
        self.div_factor_id4_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.div_factor_id4_value.setText("")
        self.div_factor_id4_value.setObjectName("div_factor_id4_value")

        self.yaxis_text_id4 = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id4.setEnabled(False)
        self.yaxis_text_id4.setGeometry(QtCore.QRect(1080, 250, 201, 31))
        self.yaxis_text_id4.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id4.setObjectName("yaxis_text_id4")

        self.yaxis_text_id4_value = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id4_value.setGeometry(QtCore.QRect(1240, 247, 141, 41))
        self.yaxis_text_id4_value.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id4_value.setText("")
        self.yaxis_text_id4_value.setObjectName("yaxis_text_id4_value")

        self.address_id4 = QtWidgets.QLineEdit(self.widget)
        self.address_id4.setEnabled(False)
        self.address_id4.setGeometry(QtCore.QRect(1080, 320, 201, 31))
        self.address_id4.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id4.setObjectName("address_id4")

        self.address_id4_value = QtWidgets.QLineEdit(self.widget)
        self.address_id4_value.setGeometry(QtCore.QRect(1240, 317, 141, 41))
        self.address_id4_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id4_value.setText("")
        self.address_id4_value.setObjectName("address_id4_value")

        # Second Half
        # CH5 Settings
        #         self.id5_label = QtWidgets.QLineEdit(self.widget)
        #         self.id5_label.setEnabled(False)
        #         self.id5_label.setGeometry(QtCore.QRect(100, 420, 201, 31))
        #         self.id5_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        # "border-width:5px;\n"
        # "border-radius: 10px;\n"
        # "padding-right: -50px; \n"
        # "color: white;")
        #         self.id5_label.setObjectName("id5_label")

        self.div_factor_id5 = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id5.setEnabled(False)
        self.div_factor_id5.setGeometry(QtCore.QRect(10, 490, 201, 31))
        self.div_factor_id5.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "padding-right: -50px; \n"
            "color: white;"
        )
        self.div_factor_id5.setObjectName("div_factor_id5")

        self.div_factor_id5_value = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id5_value.setGeometry(QtCore.QRect(170, 490, 141, 41))
        self.div_factor_id5_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.div_factor_id5_value.setText("")
        self.div_factor_id5_value.setObjectName("div_factor_id5_value")

        self.yaxis_text_id5 = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id5.setEnabled(False)
        self.yaxis_text_id5.setGeometry(QtCore.QRect(10, 560, 201, 31))
        self.yaxis_text_id5.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id5.setObjectName("yaxis_text_id5")

        self.yaxis_text_id5_value = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id5_value.setGeometry(QtCore.QRect(170, 557, 141, 41))
        self.yaxis_text_id5_value.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id5_value.setText("")
        self.yaxis_text_id5_value.setObjectName("yaxis_text_id5_value")

        self.address_id5 = QtWidgets.QLineEdit(self.widget)
        self.address_id5.setEnabled(False)
        self.address_id5.setGeometry(QtCore.QRect(10, 630, 201, 31))
        self.address_id5.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id5.setObjectName("address_id5")

        self.address_id5_value = QtWidgets.QLineEdit(self.widget)
        self.address_id5_value.setGeometry(QtCore.QRect(170, 627, 141, 41))
        self.address_id5_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id5_value.setText("")
        self.address_id5_value.setObjectName("address_id5_value")

        # CH6 Settings
        #         self.id6_label = QtWidgets.QLineEdit(self.widget)
        #         self.id6_label.setEnabled(False)
        #         self.id6_label.setGeometry(QtCore.QRect(455, 420, 201, 31))
        #         self.id6_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        # "border-width:5px;\n"
        # "border-radius: 10px;\n"
        # "padding-right: -50px; \n"
        # "color: white;")
        #         self.id6_label.setObjectName("id6_label")

        self.div_factor_id6 = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id6.setEnabled(False)
        self.div_factor_id6.setGeometry(QtCore.QRect(370, 490, 201, 31))
        self.div_factor_id6.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "padding-right: -50px; \n"
            "color: white;"
        )
        self.div_factor_id6.setObjectName("div_factor_id6")

        self.div_factor_id6_value = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id6_value.setGeometry(QtCore.QRect(530, 490, 141, 41))
        self.div_factor_id6_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.div_factor_id6_value.setText("")
        self.div_factor_id6_value.setObjectName("div_factor_id6_value")

        self.yaxis_text_id6 = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id6.setEnabled(False)
        self.yaxis_text_id6.setGeometry(QtCore.QRect(370, 560, 201, 31))
        self.yaxis_text_id6.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id6.setObjectName("yaxis_text_id6")

        self.yaxis_text_id6_value = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id6_value.setGeometry(QtCore.QRect(530, 557, 141, 41))
        self.yaxis_text_id6_value.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id6_value.setText("")
        self.yaxis_text_id6_value.setObjectName("yaxis_text_id6_value")

        self.address_id6 = QtWidgets.QLineEdit(self.widget)
        self.address_id6.setEnabled(False)
        self.address_id6.setGeometry(QtCore.QRect(370, 630, 201, 31))
        self.address_id6.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id6.setObjectName("address_id6")

        self.address_id6_value = QtWidgets.QLineEdit(self.widget)
        self.address_id6_value.setGeometry(QtCore.QRect(530, 627, 141, 41))
        self.address_id6_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id6_value.setText("")
        self.address_id6_value.setObjectName("address_id6_value")

        # CH7 Settings
        #         self.id7_label = QtWidgets.QLineEdit(self.widget)
        #         self.id7_label.setEnabled(False)
        #         self.id7_label.setGeometry(QtCore.QRect(810, 420, 201, 31))
        #         self.id7_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        # "border-width:5px;\n"
        # "border-radius: 10px;\n"
        # "padding-right: -50px; \n"
        # "color: white;")
        #         self.id7_label.setObjectName("id7_label")

        self.div_factor_id7 = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id7.setEnabled(False)
        self.div_factor_id7.setGeometry(QtCore.QRect(725, 490, 201, 31))
        self.div_factor_id7.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "padding-right: -50px; \n"
            "color: white;"
        )
        self.div_factor_id7.setObjectName("div_factor_id7")

        self.div_factor_id7_value = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id7_value.setGeometry(QtCore.QRect(885, 490, 141, 41))
        self.div_factor_id7_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.div_factor_id7_value.setText("")
        self.div_factor_id7_value.setObjectName("div_factor_id7_value")

        self.yaxis_text_id7 = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id7.setEnabled(False)
        self.yaxis_text_id7.setGeometry(QtCore.QRect(725, 560, 201, 31))
        self.yaxis_text_id7.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id7.setObjectName("yaxis_text_id7")

        self.yaxis_text_id7_value = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id7_value.setGeometry(QtCore.QRect(885, 557, 141, 41))
        self.yaxis_text_id7_value.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id7_value.setText("")
        self.yaxis_text_id7_value.setObjectName("yaxis_text_id7_value")

        self.address_id7 = QtWidgets.QLineEdit(self.widget)
        self.address_id7.setEnabled(False)
        self.address_id7.setGeometry(QtCore.QRect(725, 630, 201, 31))
        self.address_id7.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id7.setObjectName("address_id7")

        self.address_id7_value = QtWidgets.QLineEdit(self.widget)
        self.address_id7_value.setGeometry(QtCore.QRect(885, 627, 141, 41))
        self.address_id7_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id7_value.setText("")
        self.address_id7_value.setObjectName("address_id7_value")

        # CH8 Settings
        #         self.id8_label = QtWidgets.QLineEdit(self.widget)
        #         self.id8_label.setEnabled(False)
        #         self.id8_label.setGeometry(QtCore.QRect(1165, 420, 201, 31))
        #         self.id8_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        # "border-width:5px;\n"
        # "border-radius: 10px;\n"
        # "padding-right: -50px; \n"
        # "color: white;")
        #         self.id8_label.setObjectName("id8_label")

        self.div_factor_id8 = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id8.setEnabled(False)
        self.div_factor_id8.setGeometry(QtCore.QRect(1080, 490, 201, 31))
        self.div_factor_id8.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "padding-right: -50px; \n"
            "color: white;"
        )
        self.div_factor_id8.setObjectName("div_factor_id8")

        self.div_factor_id8_value = QtWidgets.QLineEdit(self.widget)
        self.div_factor_id8_value.setGeometry(QtCore.QRect(1240, 490, 141, 41))
        self.div_factor_id8_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.div_factor_id8_value.setText("")
        self.div_factor_id8_value.setObjectName("div_factor_id8_value")

        self.yaxis_text_id8 = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id8.setEnabled(False)
        self.yaxis_text_id8.setGeometry(QtCore.QRect(1080, 560, 201, 31))
        self.yaxis_text_id8.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id8.setObjectName("yaxis_text_id8")

        self.yaxis_text_id8_value = QtWidgets.QLineEdit(self.widget)
        self.yaxis_text_id8_value.setGeometry(QtCore.QRect(1240, 557, 141, 41))
        self.yaxis_text_id8_value.setStyleSheet(
            'font: 8pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.yaxis_text_id8_value.setText("")
        self.yaxis_text_id8_value.setObjectName("yaxis_text_id8_value")

        self.address_id8 = QtWidgets.QLineEdit(self.widget)
        self.address_id8.setEnabled(False)
        self.address_id8.setGeometry(QtCore.QRect(1080, 630, 201, 31))
        self.address_id8.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border-width:5px;\n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id8.setObjectName("address_id8")

        self.address_id8_value = QtWidgets.QLineEdit(self.widget)
        self.address_id8_value.setGeometry(QtCore.QRect(1240, 627, 141, 41))
        self.address_id8_value.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n'
            "border:1px solid white; \n"
            "border-radius: 10px;\n"
            "color: white;"
        )
        self.address_id8_value.setText("")
        self.address_id8_value.setObjectName("address_id8_value")

        # Vertical Lines
        # Vertical divider line — adjust x, y, height as needed
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(
            QtCore.QRect(345, 110, 1, 270)
        )  # x=700 (center), y=20, width=1, height=500
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setStyleSheet(
            "background-color: white; border: none; border-radius: 0px;"
        )
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(
            QtCore.QRect(700, 110, 1, 270)
        )  # x=700 (center), y=20, width=1, height=500
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setStyleSheet(
            "background-color: white; border: none; border-radius: 0px;"
        )
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(
            QtCore.QRect(1055, 110, 1, 270)
        )  # x=700 (center), y=20, width=1, height=500
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setStyleSheet(
            "background-color: white; border: none; border-radius: 0px;"
        )
        self.line_3.setObjectName("line_3")

        self.line8 = QtWidgets.QFrame(self.widget)
        self.line8.setGeometry(
            QtCore.QRect(345, 420, 1, 270)
        )  # x=700 (center), y=20, width=1, height=500
        self.line8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line8.setStyleSheet(
            "background-color: white; border: none; border-radius: 0px;"
        )
        self.line8.setObjectName("line8")

        self.line_9 = QtWidgets.QFrame(self.widget)
        self.line_9.setGeometry(
            QtCore.QRect(700, 420, 1, 270)
        )  # x=700 (center), y=20, width=1, height=500
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setStyleSheet(
            "background-color: white; border: none; border-radius: 0px;"
        )
        self.line_9.setObjectName("line_9")

        self.line_10 = QtWidgets.QFrame(self.widget)
        self.line_10.setGeometry(
            QtCore.QRect(1055, 420, 1, 270)
        )  # x=700 (center), y=20, width=1, height=500
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setStyleSheet(
            "background-color: white; border: none; border-radius: 0px;"
        )
        self.line_10.setObjectName("line_10")

        # Horizontal Lines
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setGeometry(
            QtCore.QRect(20, 400, 300, 1)
        )  # x=700 (center), y=20, width=1, height=500
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setStyleSheet(
            "background-color: white; border: none; border-radius: 0px;"
        )
        self.line_4.setObjectName("line_4")

        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setGeometry(
            QtCore.QRect(370, 400, 305, 1)
        )  # x=700 (center), y=20, width=1, height=500
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setStyleSheet(
            "background-color: white; border: none; border-radius: 0px;"
        )
        self.line_5.setObjectName("line_5")

        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setGeometry(
            QtCore.QRect(725, 400, 305, 1)
        )  # x=700 (center), y=20, width=1, height=500
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setStyleSheet(
            "background-color: white; border: none; border-radius: 0px;"
        )
        self.line_6.setObjectName("line_6")

        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setGeometry(
            QtCore.QRect(1080, 400, 300, 1)
        )  # x=700 (center), y=20, width=1, height=500
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setStyleSheet(
            "background-color: white; border: none; border-radius: 0px;"
        )
        self.line_7.setObjectName("line_7")

        # Switches ON/OFF
        # ============================================================
        # SLAVE ID WIDGETS (1-8)
        # ============================================================

        # --- Slave 1 ---
        self.widget_1 = QtWidgets.QWidget(self.widget)
        self.widget_1.setGeometry(QtCore.QRect(80, 110, 191, 51))  # UPDATE COORDS
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.widget_1.setSizePolicy(sizePolicy)
        self.widget_1.setObjectName("widget_1")
        self.widget_1.setStyleSheet(
            "QWidget#widget_1 {\nbackground-color: #6a5acd;\nborder: 1px solid white;\nborder-radius: 0px;\n}"
        )

        self.ID1_Check = QtWidgets.QCheckBox(self.widget_1)
        self.ID1_Check.setGeometry(QtCore.QRect(5, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.ID1_Check.setSizePolicy(sizePolicy)
        self.ID1_Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID1_Check.setStyleSheet(
            "QCheckBox {\nbackground-color: transparent;\nborder: none;\n}\n"
            "QCheckBox::indicator {\nbackground-color: transparent;\nwidth: 42px;\nheight: 32px;\nborder: none;\n}\n"
            "QCheckBox::indicator:checked {\nimage: url(:/ico/icons/switch-on.png);\n}\n"
            "QCheckBox::indicator:unchecked {\nimage: url(:/ico/icons/switch-off.png);\n}"
        )
        self.ID1_Check.setText("")
        self.ID1_Check.setIconSize(QtCore.QSize(10, 10))
        self.ID1_Check.setChecked(False)
        self.ID1_Check.setAutoRepeat(False)
        self.ID1_Check.setObjectName("ID1_Check")
        self.ID1_Check.stateChanged.connect(
            lambda state, n=1: self._toggle_slave_fields(n, state)
        )

        self.id1_label = QtWidgets.QLineEdit(self.widget_1)
        self.id1_label.setEnabled(False)
        self.id1_label.setGeometry(QtCore.QRect(50, 10, 131, 31))
        self.id1_label.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\nbackground-color: transparent;\nborder: none;\ncolor: white;'
        )
        self.id1_label.setObjectName("id1_label")

        # --- Slave 2 ---
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(425, 110, 191, 51))  # UPDATE COORDS
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet(
            "QWidget#widget_2 {\nbackground-color: #6a5acd;\nborder: 1px solid white;\nborder-radius: 0px;\n}"
        )

        self.ID2_Check = QtWidgets.QCheckBox(self.widget_2)
        self.ID2_Check.setGeometry(QtCore.QRect(5, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.ID2_Check.setSizePolicy(sizePolicy)
        self.ID2_Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID2_Check.setStyleSheet(
            "QCheckBox {\nbackground-color: transparent;\nborder: none;\n}\n"
            "QCheckBox::indicator {\nbackground-color: transparent;\nwidth: 42px;\nheight: 32px;\nborder: none;\n}\n"
            "QCheckBox::indicator:checked {\nimage: url(:/ico/icons/switch-on.png);\n}\n"
            "QCheckBox::indicator:unchecked {\nimage: url(:/ico/icons/switch-off.png);\n}"
        )
        self.ID2_Check.setText("")
        self.ID2_Check.setIconSize(QtCore.QSize(10, 10))
        self.ID2_Check.setChecked(False)
        self.ID2_Check.setAutoRepeat(False)
        self.ID2_Check.setObjectName("ID2_Check")
        self.ID2_Check.stateChanged.connect(
            lambda state, n=2: self._toggle_slave_fields(n, state)
        )

        self.id2_label = QtWidgets.QLineEdit(self.widget_2)
        self.id2_label.setEnabled(False)
        self.id2_label.setGeometry(QtCore.QRect(50, 10, 131, 31))
        self.id2_label.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\nbackground-color: transparent;\nborder: none;\ncolor: white;'
        )
        self.id2_label.setObjectName("id2_label")

        # --- Slave 3 ---
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(785, 110, 191, 51))  # UPDATE COORDS
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setStyleSheet(
            "QWidget#widget_3 {\nbackground-color: #6a5acd;\nborder: 1px solid white;\nborder-radius: 0px;\n}"
        )

        self.ID3_Check = QtWidgets.QCheckBox(self.widget_3)
        self.ID3_Check.setGeometry(QtCore.QRect(5, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.ID3_Check.setSizePolicy(sizePolicy)
        self.ID3_Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID3_Check.setStyleSheet(
            "QCheckBox {\nbackground-color: transparent;\nborder: none;\n}\n"
            "QCheckBox::indicator {\nbackground-color: transparent;\nwidth: 42px;\nheight: 32px;\nborder: none;\n}\n"
            "QCheckBox::indicator:checked {\nimage: url(:/ico/icons/switch-on.png);\n}\n"
            "QCheckBox::indicator:unchecked {\nimage: url(:/ico/icons/switch-off.png);\n}"
        )
        self.ID3_Check.setText("")
        self.ID3_Check.setIconSize(QtCore.QSize(10, 10))
        self.ID3_Check.setChecked(False)
        self.ID3_Check.setAutoRepeat(False)
        self.ID3_Check.setObjectName("ID3_Check")
        self.ID3_Check.stateChanged.connect(
            lambda state, n=3: self._toggle_slave_fields(n, state)
        )

        self.id3_label = QtWidgets.QLineEdit(self.widget_3)
        self.id3_label.setEnabled(False)
        self.id3_label.setGeometry(QtCore.QRect(50, 10, 131, 31))
        self.id3_label.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\nbackground-color: transparent;\nborder: none;\ncolor: white;'
        )
        self.id3_label.setObjectName("id3_label")

        # --- Slave 4 ---
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(1135, 110, 191, 51))  # UPDATE COORDS
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setStyleSheet(
            "QWidget#widget_4 {\nbackground-color: #6a5acd;\nborder: 1px solid white;\nborder-radius: 0px;\n}"
        )

        self.ID4_Check = QtWidgets.QCheckBox(self.widget_4)
        self.ID4_Check.setGeometry(QtCore.QRect(5, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.ID4_Check.setSizePolicy(sizePolicy)
        self.ID4_Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID4_Check.setStyleSheet(
            "QCheckBox {\nbackground-color: transparent;\nborder: none;\n}\n"
            "QCheckBox::indicator {\nbackground-color: transparent;\nwidth: 42px;\nheight: 32px;\nborder: none;\n}\n"
            "QCheckBox::indicator:checked {\nimage: url(:/ico/icons/switch-on.png);\n}\n"
            "QCheckBox::indicator:unchecked {\nimage: url(:/ico/icons/switch-off.png);\n}"
        )
        self.ID4_Check.setText("")
        self.ID4_Check.setIconSize(QtCore.QSize(10, 10))
        self.ID4_Check.setChecked(False)
        self.ID4_Check.setAutoRepeat(False)
        self.ID4_Check.setObjectName("ID4_Check")
        self.ID4_Check.stateChanged.connect(
            lambda state, n=4: self._toggle_slave_fields(n, state)
        )

        self.id4_label = QtWidgets.QLineEdit(self.widget_4)
        self.id4_label.setEnabled(False)
        self.id4_label.setGeometry(QtCore.QRect(50, 10, 131, 31))
        self.id4_label.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\nbackground-color: transparent;\nborder: none;\ncolor: white;'
        )
        self.id4_label.setObjectName("id4_label")

        # --- Slave 5 ---
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(80, 420, 191, 51))  # UPDATE COORDS
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.widget_5.setStyleSheet(
            "QWidget#widget_5 {\nbackground-color: #6a5acd;\nborder: 1px solid white;\nborder-radius: 0px;\n}"
        )

        self.ID5_Check = QtWidgets.QCheckBox(self.widget_5)
        self.ID5_Check.setGeometry(QtCore.QRect(5, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.ID5_Check.setSizePolicy(sizePolicy)
        self.ID5_Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID5_Check.setStyleSheet(
            "QCheckBox {\nbackground-color: transparent;\nborder: none;\n}\n"
            "QCheckBox::indicator {\nbackground-color: transparent;\nwidth: 42px;\nheight: 32px;\nborder: none;\n}\n"
            "QCheckBox::indicator:checked {\nimage: url(:/ico/icons/switch-on.png);\n}\n"
            "QCheckBox::indicator:unchecked {\nimage: url(:/ico/icons/switch-off.png);\n}"
        )
        self.ID5_Check.setText("")
        self.ID5_Check.setIconSize(QtCore.QSize(10, 10))
        self.ID5_Check.setChecked(False)
        self.ID5_Check.setAutoRepeat(False)
        self.ID5_Check.setObjectName("ID5_Check")
        self.ID5_Check.stateChanged.connect(
            lambda state, n=5: self._toggle_slave_fields(n, state)
        )

        self.id5_label = QtWidgets.QLineEdit(self.widget_5)
        self.id5_label.setEnabled(False)
        self.id5_label.setGeometry(QtCore.QRect(50, 10, 131, 31))
        self.id5_label.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\nbackground-color: transparent;\nborder: none;\ncolor: white;'
        )
        self.id5_label.setObjectName("id5_label")

        # --- Slave 6 ---
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setGeometry(QtCore.QRect(425, 420, 191, 51))  # UPDATE COORDS
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.widget_6.setStyleSheet(
            "QWidget#widget_6 {\nbackground-color: #6a5acd;\nborder: 1px solid white;\nborder-radius: 0px;\n}"
        )

        self.ID6_Check = QtWidgets.QCheckBox(self.widget_6)
        self.ID6_Check.setGeometry(QtCore.QRect(5, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.ID6_Check.setSizePolicy(sizePolicy)
        self.ID6_Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID6_Check.setStyleSheet(
            "QCheckBox {\nbackground-color: transparent;\nborder: none;\n}\n"
            "QCheckBox::indicator {\nbackground-color: transparent;\nwidth: 42px;\nheight: 32px;\nborder: none;\n}\n"
            "QCheckBox::indicator:checked {\nimage: url(:/ico/icons/switch-on.png);\n}\n"
            "QCheckBox::indicator:unchecked {\nimage: url(:/ico/icons/switch-off.png);\n}"
        )
        self.ID6_Check.setText("")
        self.ID6_Check.setIconSize(QtCore.QSize(10, 10))
        self.ID6_Check.setChecked(False)
        self.ID6_Check.setAutoRepeat(False)
        self.ID6_Check.setObjectName("ID6_Check")
        self.ID6_Check.stateChanged.connect(
            lambda state, n=6: self._toggle_slave_fields(n, state)
        )

        self.id6_label = QtWidgets.QLineEdit(self.widget_6)
        self.id6_label.setEnabled(False)
        self.id6_label.setGeometry(QtCore.QRect(50, 10, 131, 31))
        self.id6_label.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\nbackground-color: transparent;\nborder: none;\ncolor: white;'
        )
        self.id6_label.setObjectName("id6_label")

        # --- Slave 7 ---
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setGeometry(QtCore.QRect(785, 420, 191, 51))  # UPDATE COORDS
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.widget_7.setStyleSheet(
            "QWidget#widget_7 {\nbackground-color: #6a5acd;\nborder: 1px solid white;\nborder-radius: 0px;\n}"
        )

        self.ID7_Check = QtWidgets.QCheckBox(self.widget_7)
        self.ID7_Check.setGeometry(QtCore.QRect(5, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.ID7_Check.setSizePolicy(sizePolicy)
        self.ID7_Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID7_Check.setStyleSheet(
            "QCheckBox {\nbackground-color: transparent;\nborder: none;\n}\n"
            "QCheckBox::indicator {\nbackground-color: transparent;\nwidth: 42px;\nheight: 32px;\nborder: none;\n}\n"
            "QCheckBox::indicator:checked {\nimage: url(:/ico/icons/switch-on.png);\n}\n"
            "QCheckBox::indicator:unchecked {\nimage: url(:/ico/icons/switch-off.png);\n}"
        )
        self.ID7_Check.setText("")
        self.ID7_Check.setIconSize(QtCore.QSize(10, 10))
        self.ID7_Check.setChecked(False)
        self.ID7_Check.setAutoRepeat(False)
        self.ID7_Check.setObjectName("ID7_Check")
        self.ID7_Check.stateChanged.connect(
            lambda state, n=7: self._toggle_slave_fields(n, state)
        )

        self.id7_label = QtWidgets.QLineEdit(self.widget_7)
        self.id7_label.setEnabled(False)
        self.id7_label.setGeometry(QtCore.QRect(50, 10, 131, 31))
        self.id7_label.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\nbackground-color: transparent;\nborder: none;\ncolor: white;'
        )
        self.id7_label.setObjectName("id7_label")

        # --- Slave 8 ---
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setGeometry(QtCore.QRect(1135, 420, 191, 51))  # UPDATE COORDS
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.widget_8.setStyleSheet(
            "QWidget#widget_8 {\nbackground-color: #6a5acd;\nborder: 1px solid white;\nborder-radius: 0px;\n}"
        )

        self.ID8_Check = QtWidgets.QCheckBox(self.widget_8)
        self.ID8_Check.setGeometry(QtCore.QRect(5, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.ID8_Check.setSizePolicy(sizePolicy)
        self.ID8_Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ID8_Check.setStyleSheet(
            "QCheckBox {\nbackground-color: transparent;\nborder: none;\n}\n"
            "QCheckBox::indicator {\nbackground-color: transparent;\nwidth: 42px;\nheight: 32px;\nborder: none;\n}\n"
            "QCheckBox::indicator:checked {\nimage: url(:/ico/icons/switch-on.png);\n}\n"
            "QCheckBox::indicator:unchecked {\nimage: url(:/ico/icons/switch-off.png);\n}"
        )
        self.ID8_Check.setText("")
        self.ID8_Check.setIconSize(QtCore.QSize(10, 10))
        self.ID8_Check.setChecked(False)
        self.ID8_Check.setAutoRepeat(False)
        self.ID8_Check.setObjectName("ID8_Check")
        self.ID8_Check.stateChanged.connect(
            lambda state, n=8: self._toggle_slave_fields(n, state)
        )

        self.id8_label = QtWidgets.QLineEdit(self.widget_8)
        self.id8_label.setEnabled(False)
        self.id8_label.setGeometry(QtCore.QRect(50, 10, 131, 31))
        self.id8_label.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\nbackground-color: transparent;\nborder: none;\ncolor: white;'
        )
        self.id8_label.setObjectName("id8_label")

        # Save Button
        self.SaveButton = QtWidgets.QPushButton(self.widget)
        self.SaveButton.setGeometry(QtCore.QRect(1160, 710, 141, 51))
        self.SaveButton.setCheckable(True)
        self.SaveButton.setChecked(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SaveButton.setFont(font)
        self.SaveButton.setStyleSheet(
            "QPushButton{\n"
            'font: 12pt "MS Shell Dlg 2";\n'
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
            ""
        )
        self.SaveButton.setObjectName("SaveButton")
        SigmaControls.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SigmaControls)
        self.statusbar.setObjectName("statusbar")
        SigmaControls.setStatusBar(self.statusbar)

        self.retranslateUi(SigmaControls)
        QtCore.QMetaObject.connectSlotsByName(SigmaControls)
        self.load_config()
        self.SaveButton.clicked.connect(self.save_config)

    # Change here also

    def retranslateUi(self, SigmaControls):
        _translate = QtCore.QCoreApplication.translate
        SigmaControls.setWindowTitle(
            _translate("SigmaControls", "Sigma Controls | Slave ID Settings")
        )
        self.lineEdit.setText(_translate("SigmaControls", "Slave ID Settings"))
        self.log_time.setText(_translate("SigmaControls", "Log Time (Sec) :"))
        self.id1_label.setText(_translate("SigmaControls", "Slave ID-1"))
        self.div_factor_id1.setText(_translate("SigmaControls", "Div. Factor :"))
        self.yaxis_text_id1.setText(_translate("SigmaControls", "Y-Axis Text :"))
        self.address_id1.setText(_translate("SigmaControls", "Address :"))
        self.id2_label.setText(_translate("SigmaControls", "Slave ID-2"))
        self.div_factor_id2.setText(_translate("SigmaControls", "Div. Factor :"))
        self.yaxis_text_id2.setText(_translate("SigmaControls", "Y-Axis Text :"))
        self.address_id2.setText(_translate("SigmaControls", "Address :"))
        self.id3_label.setText(_translate("SigmaControls", "Slave ID-3"))
        self.div_factor_id3.setText(_translate("SigmaControls", "Div. Factor :"))
        self.yaxis_text_id3.setText(_translate("SigmaControls", "Y-Axis Text :"))
        self.address_id3.setText(_translate("SigmaControls", "Address :"))
        self.id4_label.setText(_translate("SigmaControls", "Slave ID-4"))
        self.div_factor_id4.setText(_translate("SigmaControls", "Div. Factor :"))
        self.yaxis_text_id4.setText(_translate("SigmaControls", "Y-Axis Text :"))
        self.address_id4.setText(_translate("SigmaControls", "Address :"))
        self.id5_label.setText(_translate("SigmaControls", "Slave ID-5"))
        self.div_factor_id5.setText(_translate("SigmaControls", "Div. Factor :"))
        self.yaxis_text_id5.setText(_translate("SigmaControls", "Y-Axis Text :"))
        self.address_id5.setText(_translate("SigmaControls", "Address :"))
        self.id6_label.setText(_translate("SigmaControls", "Slave ID-6"))
        self.div_factor_id6.setText(_translate("SigmaControls", "Div. Factor :"))
        self.yaxis_text_id6.setText(_translate("SigmaControls", "Y-Axis Text :"))
        self.address_id6.setText(_translate("SigmaControls", "Address :"))
        self.id7_label.setText(_translate("SigmaControls", "Slave ID-7"))
        self.div_factor_id7.setText(_translate("SigmaControls", "Div. Factor :"))
        self.yaxis_text_id7.setText(_translate("SigmaControls", "Y-Axis Text :"))
        self.address_id7.setText(_translate("SigmaControls", "Address :"))
        self.id8_label.setText(_translate("SigmaControls", "Slave ID-8"))
        self.div_factor_id8.setText(_translate("SigmaControls", "Div. Factor :"))
        self.yaxis_text_id8.setText(_translate("SigmaControls", "Y-Axis Text :"))
        self.address_id8.setText(_translate("SigmaControls", "Address :"))
        self.SaveButton.setText(_translate("SigmaControls", "Save"))

        # self.log_time_value.setPlaceholderText("e.g. 2.0")
        # for i in range(1, 9):
        #         df_el = getattr(self, f'div_factor_id{i}_value', None)
        #         ya_el = getattr(self, f'yaxis_text_id{i}_value', None)
        #         ad_el = getattr(self, f'address_id{i}_value', None)
        #         if df_el: df_el.setPlaceholderText("e.g. 10")
        #         if ya_el: ya_el.setPlaceholderText("e.g. Temperature (°C)")
        #         if ad_el: ad_el.setPlaceholderText("e.g. 0")

    def show_message(self, title, text, color):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)

        # Add logo icon
        icon = QtGui.QIcon(_resource_path("SIGMA_ICON.svg"))
        msg.setWindowIcon(icon)

        msg.setStyleSheet(f"""
                QMessageBox {{ background-color: #000000; }}
                QLabel {{ color: {color}; font-size: 18px; }}
                QPushButton {{
                background-color: #e0dede; color: #000000;
                min-width: 80px; min-height: 28px;
                border-radius: 4px; font-size: 16px;
                }}
        """)
        msg.exec_()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)

            self.log_time_value.setText(str(config.get("log_time", "")))

            for i in range(1, 9):
                df_el = getattr(self, f"div_factor_id{i}_value", None)
                ya_el = getattr(self, f"yaxis_text_id{i}_value", None)
                ad_el = getattr(self, f"address_id{i}_value", None)
                chk_el = getattr(self, f"ID{i}_Check", None)

                if df_el:
                    df_el.setText(str(config.get(f"div_factor_{i}", "")))
                if ya_el:
                    ya_el.setText(str(config.get(f"y_axis_text_{i}", "")))
                if ad_el:
                    ad_el.setText(str(config.get(f"address_{i}", "")))
                if chk_el:
                    checked = bool(config.get(f"slave_enabled_{i}", False))
                    chk_el.setChecked(checked)
                    self._toggle_slave_fields(i, 2 if checked else 0)

            print("Config Loaded:", config)

    def _toggle_slave_fields(self, i, state):
        enabled = state == 2  # Qt.Checked == 2

        field_fonts = {
            f"div_factor_id{i}_value": "12pt",
            f"yaxis_text_id{i}_value": "8pt",
            f"address_id{i}_value": "12pt",
        }

        for widget_name, font_size in field_fonts.items():
            el = getattr(self, widget_name, None)
            if el:
                el.setEnabled(enabled)
                el.setStyleSheet(
                    f'font: {font_size} "MS Shell Dlg 2";\nborder:1px solid white;\n'
                    "border-radius: 10px;\ncolor: white;"
                    if enabled
                    else f'font: {font_size} "MS Shell Dlg 2";\nborder:1px solid grey;\n'
                    "border-radius: 10px;\ncolor: grey;"
                )

    def save_config(self):

        # Validate — enabled slaves must have Div Factor and Address filled
        for i in range(1, 9):
            chk_el = getattr(self, f"ID{i}_Check", None)
            df_el = getattr(self, f"div_factor_id{i}_value", None)
            ad_el = getattr(self, f"address_id{i}_value", None)

            if chk_el and chk_el.isChecked():
                if df_el and not df_el.text().strip():
                    self.show_message(
                        "Error",
                        f"Slave ID-{i} is ON but Div. Factor is empty!",
                        "#ff4c4c",
                    )
                    return

                if ad_el and not ad_el.text().strip():
                    self.show_message(
                        "Error", f"Slave ID-{i} is ON but Address is empty!", "#ff4c4c"
                    )
                    return

        log_time = self.log_time_value.text().strip()

        if not log_time:
            self.show_message("Error", "Log Time cannot be empty!", "#ff4c4c")
            return

        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
        else:
            config = {}

        config["log_time"] = log_time

        for i in range(1, 9):
            df_el = getattr(self, f"div_factor_id{i}_value", None)
            ya_el = getattr(self, f"yaxis_text_id{i}_value", None)
            ad_el = getattr(self, f"address_id{i}_value", None)
            chk_el = getattr(self, f"ID{i}_Check", None)

            config[f"div_factor_{i}"] = df_el.text().strip() if df_el else ""

            config[f"y_axis_text_{i}"] = ya_el.text().strip() if ya_el else ""

            config[f"address_{i}"] = ad_el.text().strip() if ad_el else ""

            config[f"slave_enabled_{i}"] = chk_el.isChecked() if chk_el else False

        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)

        print("SAVED CONFIG =", config)
        print("Value Stored")

        self.show_message("Saved", "Settings Saved Successfully!", "#02c702")

        self.SigmaControls.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SigmaControls = QtWidgets.QMainWindow()
    SigmaControls.setMinimumSize(1400, 800)

    ui = Ui_SigmaControls_4()
    ui.setupUi(SigmaControls)
    SigmaControls.show()

    sys.exit(app.exec_())