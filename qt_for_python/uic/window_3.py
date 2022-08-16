# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_3.ui'
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
        Form.resize(1100, 160)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 1077, 52))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_RES = QLineEdit(self.layoutWidget)
        self.lineEdit_RES.setObjectName(u"lineEdit_RES")

        self.gridLayout.addWidget(self.lineEdit_RES, 1, 7, 1, 1)

        self.lineEdit_A = QLineEdit(self.layoutWidget)
        self.lineEdit_A.setObjectName(u"lineEdit_A")
        self.lineEdit_A.setEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_A, 1, 0, 1, 1)

        self.label_C = QLabel(self.layoutWidget)
        self.label_C.setObjectName(u"label_C")
        self.label_C.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_C, 0, 3, 1, 1)

        self.lineEdit_B = QLineEdit(self.layoutWidget)
        self.lineEdit_B.setObjectName(u"lineEdit_B")

        self.gridLayout.addWidget(self.lineEdit_B, 1, 1, 1, 2)

        self.label_XS = QLabel(self.layoutWidget)
        self.label_XS.setObjectName(u"label_XS")
        self.label_XS.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_XS, 0, 4, 1, 1)

        self.label_RES = QLabel(self.layoutWidget)
        self.label_RES.setObjectName(u"label_RES")
        self.label_RES.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_RES, 0, 7, 1, 1)

        self.lineEdit_C = QLineEdit(self.layoutWidget)
        self.lineEdit_C.setObjectName(u"lineEdit_C")

        self.gridLayout.addWidget(self.lineEdit_C, 1, 3, 1, 1)

        self.lineEdit_D = QLineEdit(self.layoutWidget)
        self.lineEdit_D.setObjectName(u"lineEdit_D")

        self.gridLayout.addWidget(self.lineEdit_D, 1, 5, 1, 1)

        self.label_B = QLabel(self.layoutWidget)
        self.label_B.setObjectName(u"label_B")
        self.label_B.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_B, 0, 1, 1, 2)

        self.label_XS_var = QLabel(self.layoutWidget)
        self.label_XS_var.setObjectName(u"label_XS_var")
        self.label_XS_var.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_XS_var, 1, 4, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 6, 1, 1)

        self.label_A = QLabel(self.layoutWidget)
        self.label_A.setObjectName(u"label_A")
        self.label_A.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_A, 0, 0, 1, 1)

        self.label_D = QLabel(self.layoutWidget)
        self.label_D.setObjectName(u"label_D")
        self.label_D.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_D, 0, 5, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u89d2\u94a2", None))
        self.label_C.setText(QCoreApplication.translate("Form", u"C(mm)", None))
        self.label_XS.setText(QCoreApplication.translate("Form", u"\u7cfb\u6570(kg/m)", None))
        self.label_RES.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c(\u5143/m)", None))
        self.label_B.setText(QCoreApplication.translate("Form", u"B(mm)", None))
        self.label_XS_var.setText(QCoreApplication.translate("Form", u"xs", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6362\u7b97", None))
        self.label_A.setText(QCoreApplication.translate("Form", u"A(mm)", None))
        self.label_D.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c(\u5143/kg)", None))
    # retranslateUi

