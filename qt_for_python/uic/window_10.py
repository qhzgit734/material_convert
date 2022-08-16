# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_10.ui'
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
        Form.resize(1083, 370)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 110, 522, 177))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.lineEdit_D = QLineEdit(self.groupBox_2)
        self.lineEdit_D.setObjectName(u"lineEdit_D")

        self.horizontalLayout.addWidget(self.lineEdit_D)


        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.comboBox_1 = QComboBox(self.groupBox_2)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")

        self.gridLayout_4.addWidget(self.comboBox_1, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton = QRadioButton(self.groupBox_3)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_3)
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_3)
        self.buttonGroup.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout.addWidget(self.radioButton_4)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(550, 110, 521, 221))
        self.textBrowser = QTextBrowser(self.groupBox_5)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 20, 501, 191))
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 90, 1061, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 1041, 52))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_A = QLabel(self.layoutWidget)
        self.label_A.setObjectName(u"label_A")
        self.label_A.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_A, 0, 0, 1, 1)

        self.label_B = QLabel(self.layoutWidget)
        self.label_B.setObjectName(u"label_B")
        self.label_B.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_B, 0, 1, 1, 1)

        self.label_C = QLabel(self.layoutWidget)
        self.label_C.setObjectName(u"label_C")
        self.label_C.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_C, 0, 2, 1, 1)

        self.label_JZ = QLabel(self.layoutWidget)
        self.label_JZ.setObjectName(u"label_JZ")
        self.label_JZ.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_JZ, 0, 3, 1, 1)

        self.label_XS = QLabel(self.layoutWidget)
        self.label_XS.setObjectName(u"label_XS")
        self.label_XS.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_XS, 0, 4, 1, 1)

        self.label_RES = QLabel(self.layoutWidget)
        self.label_RES.setObjectName(u"label_RES")
        self.label_RES.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_RES, 0, 6, 1, 1)

        self.lineEdit_A = QLineEdit(self.layoutWidget)
        self.lineEdit_A.setObjectName(u"lineEdit_A")

        self.gridLayout.addWidget(self.lineEdit_A, 1, 0, 1, 1)

        self.lineEdit_B = QLineEdit(self.layoutWidget)
        self.lineEdit_B.setObjectName(u"lineEdit_B")

        self.gridLayout.addWidget(self.lineEdit_B, 1, 1, 1, 1)

        self.lineEdit_C = QLineEdit(self.layoutWidget)
        self.lineEdit_C.setObjectName(u"lineEdit_C")
        self.lineEdit_C.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_C, 1, 2, 1, 1)

        self.label_JZ_var = QLabel(self.layoutWidget)
        self.label_JZ_var.setObjectName(u"label_JZ_var")
        self.label_JZ_var.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_JZ_var, 1, 3, 1, 1)

        self.label_XS_var = QLabel(self.layoutWidget)
        self.label_XS_var.setObjectName(u"label_XS_var")
        self.label_XS_var.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_XS_var, 1, 4, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 5, 1, 1)

        self.lineEdit_RES = QLineEdit(self.layoutWidget)
        self.lineEdit_RES.setObjectName(u"lineEdit_RES")

        self.gridLayout.addWidget(self.lineEdit_RES, 1, 6, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u98ce\u7ba1\u9644\u4ef6", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5c5e\u6027", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u7c7b\u578b(\u5143/kg):", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"\u9540\u950c\u94a2\u677f", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"\u94dd\u5408\u91d1\u677f", None))

        self.lineEdit_D.setText(QCoreApplication.translate("Form", u"5.57", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("Form", u"\u98ce\u7ba1\u9632\u706b\u9600", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("Form", u"\u98ce\u7ba1\u6392\u70df\u9600", None))
        self.comboBox_1.setItemText(2, QCoreApplication.translate("Form", u"\u98ce\u7ba1\u6b62\u56de\u9600", None))
        self.comboBox_1.setItemText(3, QCoreApplication.translate("Form", u"\u98ce\u7ba1\u8c03\u8282\u9600-\u5bf9\u5f00\u591a\u53f6", None))
        self.comboBox_1.setItemText(4, QCoreApplication.translate("Form", u"\u98ce\u7ba1\u63d2\u677f\uff08\u5bc6\u95ed\uff09\u9600", None))
        self.comboBox_1.setItemText(5, QCoreApplication.translate("Form", u"\u98ce\u53e3-\u5355\u5c42", None))
        self.comboBox_1.setItemText(6, QCoreApplication.translate("Form", u"\u98ce\u53e3-\u53cc\u5c42", None))
        self.comboBox_1.setItemText(7, QCoreApplication.translate("Form", u"\u98ce\u53e3-\u9632\u706b", None))
        self.comboBox_1.setItemText(8, QCoreApplication.translate("Form", u"\u98ce\u53e3-\u6392\u70df", None))
        self.comboBox_1.setItemText(9, QCoreApplication.translate("Form", u"\u98ce\u53e3-\u9632\u96e8", None))
        self.comboBox_1.setItemText(10, QCoreApplication.translate("Form", u"\u9759\u538b\u7bb1", None))
        self.comboBox_1.setItemText(11, QCoreApplication.translate("Form", u"\u9759\u538b\u7bb1-\u6d88\u58f0", None))
        self.comboBox_1.setItemText(12, QCoreApplication.translate("Form", u"\u6d88\u58f0\u5668ZP100", None))
        self.comboBox_1.setItemText(13, QCoreApplication.translate("Form", u"\u6d88\u58f0\u5f2f\u5934", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u6267\u884c\u673a\u6784:", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u65e0", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u7535\u52a8", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u6e29\u63a7", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"\u9065\u63a7", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u5176\u4ed6:", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u5706\u5f62", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u4e0d\u9508\u94a2", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u8bf4\u660e\uff1a", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1\u3001\u6750\u8d28304\u4e0d\u9508\u94a2\u98ce\u9600\u3001\u6d88\u58f0\u5668\u3001\u98ce\u53e3\u6309\u4ee5\u4e0a\u4ef7\u683c\u4e584\u500d\uff1b</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2\u3001\u98ce\u9600\u91c7\u7528\u70ed\u8f67\u6216\u51b7\u8f67\u94a2\u677f\u5236\u65f6\u4ef7\u683c\u53c2\u7167\u76f8\u540c\u578b\u53f7\u4e0b\u6d6e10%\uff1b      </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3\u3001\u5f27"
                        "\u5f62\u98ce\u53e3\u4ef7\u683c\u6309\u7ebf\u6761\u5f62\u98ce\u53e3\u6bcf\u7c73\u5355\u4ef7\u00d71.75\uff1b</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4\u3001\u98ce\u53e3\u8868\u9762\u767d\u8272\u9759\u7535\u55b7\u5851\u4ef7\u683c\u4e0a\u6d6e15%\uff1b\u7279\u6b8a\u989c\u8272\u4ef7\u683c\u4e0a\u6d6e30%\uff1b\u98ce\u53e3\u8868\u9762\u91c7\u7528\u672c\u8272\u805a\u6c28\u916f\u6cb9\u6f063\u9053\u4ef7\u683c\u53e6\u5916\u518d\u4e0a\u6d6e40%\uff1b  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5\u3001\u55b7\u53e3\u3001\u98ce\u53e3\u52a0\u667a\u80fd\u63a7\u5236\u88c5\u7f6e,\u7535\u52a8\u8c03\u8282\u95f4\u589e\u52a0400\u5143/\u5957,\u6e29\u611f\u8c03\u8282\u589e\u52a0700\u5143/\u5957,\u9065\u63a7\u8c03\u8282\u589e\u52a01000\u5143/\u5957\uff1b</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px;\">6\u3001\u98ce\u53e3\u5e26\u8c03\u8282\u9600\u7684\u4ef7\u683c\u8ba1\u7b97\u516c\u5f0f\u662f\u6839\u636e\u9009\u5b9a\u578b\u53f7\u7684\u98ce\u53e3\u4ef7\u683c\u548c\u7528\u4e8e\u98ce\u53e3\u7684\u5bf9\u5f00\u591a\u53f6\u8c03\u8282\u9600\u7684\u4ef7\u683c\u76f8\u52a0\u5f97\u51fa\uff1b</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7\u3001\u5706\u5f62\u6563\u6d41\u5668(\u5e26\u9600)\u3001\u65cb\u6d41\u98ce\u53e3\u548c\u7403\u5f62\u55b7\u53e3\u7684\u4ef7\u683c\u8ba1\u7b97\u4ee5\u76f4\u5f84\u4e3a\u8ba1\u7b97\u4f9d\u636e\u3002</p></body></html>", None))
        self.label_A.setText(QCoreApplication.translate("Form", u"A(mm)", None))
        self.label_B.setText(QCoreApplication.translate("Form", u"B(mm)", None))
        self.label_C.setText(QCoreApplication.translate("Form", u"C(mm)", None))
        self.label_JZ.setText(QCoreApplication.translate("Form", u"\u57fa\u51c6\u4ef7(\u5143/\u4e2a)", None))
        self.label_XS.setText(QCoreApplication.translate("Form", u"\u7cfb\u6570", None))
        self.label_RES.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c(\u5143/\u4e2a)", None))
        self.label_JZ_var.setText(QCoreApplication.translate("Form", u"jz", None))
        self.label_XS_var.setText(QCoreApplication.translate("Form", u"xs", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6362\u7b97", None))
    # retranslateUi

