# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(909, 282)
        MainWindow.setStyleSheet(u"")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QTabWidget::pane{background-color: rgb();}")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabBar::tab::selected{background-color:#c8dcff;}\n"
"#tab_1{background-color:#c8dcff;}\n"
"#tab_2{background-color:#c8dcff;}\n"
"#tab_3{background-color:#c8dcff;}\n"
"#tab_4{background-color:#c8dcff;}\n"
"#tab_5{background-color:#c8dcff;}")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tab_1.setStyleSheet(u"")
        self.formLayout = QFormLayout(self.tab_1)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_1 = QPushButton(self.tab_1)
        self.pushButton_1.setObjectName(u"pushButton_1")
        palette = QPalette()
        self.pushButton_1.setPalette(palette)

        self.horizontalLayout_3.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.tab_1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_1, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), u"\u677f\u6750")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"")
        self.formLayout_2 = QFormLayout(self.tab_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.tab_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout.addWidget(self.pushButton_6)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout)

        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), u"\u578b\u94a2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"")
        self.formLayout_3 = QFormLayout(self.tab_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_7 = QPushButton(self.tab_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.tab_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_4.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.tab_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_4.addWidget(self.pushButton_9)


        self.formLayout_3.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), u"\u7ba1\u6750")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setStyleSheet(u"")
        self.pushButton_12 = QPushButton(self.tab_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setGeometry(QRect(210, 10, 93, 28))
        self.pushButton_10 = QPushButton(self.tab_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(10, 10, 93, 28))
        self.pushButton_11 = QPushButton(self.tab_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(110, 10, 93, 28))
        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 909, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.actionhelp)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"material_convert", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"version", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u9540\u950c\u94a2\u677f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u9540\u950c\u8584\u94a2\u677f", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u94a2", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u69fd\u94a2", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u9540\u950c\u5706\u94a2", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u9540\u950c\u6241\u94a2", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u9540\u950c\u94a2\u7ba1", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u710a\u63a5\u94a2\u7ba1", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u9508\u94a2\u7ba1", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u6297\u9707\u652f\u67b6", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u98ce\u7ba1\u9644\u4ef6", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u6865\u67b6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u91d1\u5c5e\u6750\u6599", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

