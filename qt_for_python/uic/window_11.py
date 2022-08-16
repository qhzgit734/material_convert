# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_11.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(782, 115)
        self.horizontalLayout = QHBoxLayout(widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 3, 1, 1)

        self.lineEdit_A = QLineEdit(widget)
        self.lineEdit_A.setObjectName(u"lineEdit_A")

        self.gridLayout.addWidget(self.lineEdit_A, 1, 1, 1, 1)

        self.label_B = QLabel(widget)
        self.label_B.setObjectName(u"label_B")
        self.label_B.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_B, 0, 2, 1, 1)

        self.label_D = QLabel(widget)
        self.label_D.setObjectName(u"label_D")
        self.label_D.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_D, 0, 4, 1, 1)

        self.label_4 = QLabel(widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.lineEdit_B = QLineEdit(widget)
        self.lineEdit_B.setObjectName(u"lineEdit_B")

        self.gridLayout.addWidget(self.lineEdit_B, 1, 2, 1, 1)

        self.label_A = QLabel(widget)
        self.label_A.setObjectName(u"label_A")
        self.label_A.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_A, 0, 1, 1, 1)

        self.lineEdit_D = QLineEdit(widget)
        self.lineEdit_D.setObjectName(u"lineEdit_D")

        self.gridLayout.addWidget(self.lineEdit_D, 1, 4, 1, 1)

        self.lineEdit_RES = QLineEdit(widget)
        self.lineEdit_RES.setObjectName(u"lineEdit_RES")

        self.gridLayout.addWidget(self.lineEdit_RES, 3, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.lineEdit_C = QLineEdit(widget)
        self.lineEdit_C.setObjectName(u"lineEdit_C")

        self.gridLayout.addWidget(self.lineEdit_C, 3, 1, 1, 1)

        self.lineEdit_E = QLineEdit(widget)
        self.lineEdit_E.setObjectName(u"lineEdit_E")

        self.gridLayout.addWidget(self.lineEdit_E, 3, 2, 1, 1)

        self.line = QFrame(widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 5)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\u6362\u7b97", None))
        self.lineEdit_A.setText(QCoreApplication.translate("widget", u"300", None))
        self.label_B.setText(QCoreApplication.translate("widget", u"B(mm)", None))
        self.label_D.setText(QCoreApplication.translate("widget", u"\u4ef7\u683c(\u5143/m)", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"\u53c2\u8003\u6865\u67b6\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("widget", u"\u6362\u7b97\u6865\u67b6\uff1a", None))
        self.lineEdit_B.setText(QCoreApplication.translate("widget", u"100", None))
        self.label_A.setText(QCoreApplication.translate("widget", u"A(mm)", None))
        self.lineEdit_D.setText(QCoreApplication.translate("widget", u"117.5", None))
    # retranslateUi

