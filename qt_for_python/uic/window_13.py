# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_13.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(469, 486)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.commandLinkButton = QCommandLinkButton(Dialog)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.gridLayout.addWidget(self.commandLinkButton, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"help", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">maerial_convert</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">V2.0</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin"
                        "-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">---------------</span><span style=\" font-size:12pt; font-weight:600;\">help</span><span style=\" font-weight:600;\">---------------</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u8bf4\u660e\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u672c\u7a0b\u5e8f\u4ef7\u683c\u4e3a\u9664\u7a0e\u4ef7\uff01</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u4e00\u3001\u98ce\u7ba1\u9644\u4ef6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1\u3001\u98ce\u7ba1\u9644\u4ef6\u8ba1\u7b97\u65b9\u6cd5\u4e3b\u8981\u53c2\u8003\u6d59"
                        "\u6c5f\u4fe1\u606f\u4ef72022.05</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2\u3001\u98ce\u7ba1\u9644\u4ef6\u6a21\u5757\u4e2d\u5706\u5f62\u5c3a\u5bf8\uff0c\u5728A\u3001B\u4e2d\u540c\u65f6\u8f93\u5165\u76f4\u5f84</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3\u3001\u70ed\u9540\u950c\u677f6200\u5143/t,\u5176\u4ef7\u683c\u5f71\u54cd\u7cfb\u6570\u4e3a:\u6bcf\u6da8(\u8dcc)300\u5143/t\u65f6,\u4ef7\u683c\u4e0a\u4e0b\u6d6e\u52a83%</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4\u3001\u94dd\u5408\u91d1\u98ce\u53e3\u578b\u6750\u6309\u4e0a\u6d77\u671f\u8d27\u94dd\u952d22000\u5143/t\uff1b\u5176\u4ef7\u683c\u5f71\u54cd\u7cfb\u6570\u4e3a:\u6bcf\u6da8(\u8dcc)1500\u5143/t\u65f6,\u4ef7\u683c\u4e0a\u4e0b\u6d6e\u52a85%</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u4e8c\u3001\u710a\u63a5\u94a2\u7ba1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5957\u7ba1=\u7535\u7f06\u4fdd\u62a4\u7ba1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u4e09\u3001\u9540\u950c\u94a2\u7ba1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1\u3001\u6307\u6c34\u7ba1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2\u3001\u70ed\u9540\u950c=\u70ed\u6d78\u950c=\u70ed\u6d78\u950c\u52a0\u539a\uff0cKBG/JDG\u4e3a\u8584\u58c1\u9540\u950c\u94a2\u7ba1\uff1c\u6c34</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom"
                        ":0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Dialog", u"Github", None))
    # retranslateUi

