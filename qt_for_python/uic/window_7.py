# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_7.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(547, 95)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_D = QLabel(Form)
        self.label_D.setObjectName(u"label_D")
        self.label_D.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_D, 0, 2, 1, 1)

        self.label_RES = QLabel(Form)
        self.label_RES.setObjectName(u"label_RES")
        self.label_RES.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_RES, 0, 4, 1, 1)

        self.label_XS = QLabel(Form)
        self.label_XS.setObjectName(u"label_XS")
        self.label_XS.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_XS, 0, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.label_XS_var = QLabel(Form)
        self.label_XS_var.setObjectName(u"label_XS_var")
        self.label_XS_var.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_XS_var, 1, 1, 1, 1)

        self.lineEdit_D = QLineEdit(Form)
        self.lineEdit_D.setObjectName(u"lineEdit_D")

        self.gridLayout.addWidget(self.lineEdit_D, 1, 2, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)

        self.lineEdit_RES = QLineEdit(Form)
        self.lineEdit_RES.setObjectName(u"lineEdit_RES")

        self.gridLayout.addWidget(self.lineEdit_RES, 1, 4, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u9540\u950c\u94a2\u7ba1", None))
        self.label_D.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c(\u5143/kg)", None))
        self.label_RES.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c(\u5143/m)", None))
        self.label_XS.setText(QCoreApplication.translate("Form", u"\u7cfb\u6570(kg/m)", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u578b\u53f7(mm)", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"15", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"20", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"25", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"32", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"40", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"50", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"65", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Form", u"80", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Form", u"100", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Form", u"125", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Form", u"150", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Form", u"200", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("Form", u"250", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("Form", u"300", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("Form", u"500", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("Form", u"600", None))

        self.label_XS_var.setText(QCoreApplication.translate("Form", u"xs", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6362\u7b97", None))
    # retranslateUi

