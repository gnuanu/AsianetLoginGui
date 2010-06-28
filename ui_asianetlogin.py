# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asianetlogin.ui'
#
# Created: Tue Jun 29 00:09:39 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AsianetLogin(object):
    def setupUi(self, AsianetLogin):
        AsianetLogin.setObjectName("AsianetLogin")
        AsianetLogin.resize(521, 211)
        AsianetLogin.setMinimumSize(QtCore.QSize(521, 211))
        AsianetLogin.setMaximumSize(QtCore.QSize(521, 211))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/logo16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AsianetLogin.setWindowIcon(icon)
        self.layoutWidget = QtGui.QWidget(AsianetLogin)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbUsername = QtGui.QLabel(self.layoutWidget)
        self.lbUsername.setObjectName("lbUsername")
        self.horizontalLayout.addWidget(self.lbUsername)
        self.edUsername = QtGui.QLineEdit(self.layoutWidget)
        self.edUsername.setObjectName("edUsername")
        self.horizontalLayout.addWidget(self.edUsername)
        self.lbPassword = QtGui.QLabel(self.layoutWidget)
        self.lbPassword.setObjectName("lbPassword")
        self.horizontalLayout.addWidget(self.lbPassword)
        self.edPassword = QtGui.QLineEdit(self.layoutWidget)
        self.edPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.edPassword.setObjectName("edPassword")
        self.horizontalLayout.addWidget(self.edPassword)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chkRemember = QtGui.QCheckBox(self.layoutWidget)
        self.chkRemember.setObjectName("chkRemember")
        self.horizontalLayout_2.addWidget(self.chkRemember)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bnClose = QtGui.QPushButton(self.layoutWidget)
        self.bnClose.setObjectName("bnClose")
        self.horizontalLayout_2.addWidget(self.bnClose)
        self.bnConnect = QtGui.QPushButton(self.layoutWidget)
        self.bnConnect.setObjectName("bnConnect")
        self.horizontalLayout_2.addWidget(self.bnConnect)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.teLog = QtGui.QTextEdit(self.layoutWidget)
        self.teLog.setReadOnly(True)
        self.teLog.setObjectName("teLog")
        self.verticalLayout.addWidget(self.teLog)

        self.retranslateUi(AsianetLogin)
        QtCore.QMetaObject.connectSlotsByName(AsianetLogin)

    def retranslateUi(self, AsianetLogin):
        AsianetLogin.setWindowTitle(QtGui.QApplication.translate("AsianetLogin", "Asianet Login", None, QtGui.QApplication.UnicodeUTF8))
        self.lbUsername.setText(QtGui.QApplication.translate("AsianetLogin", "User Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lbPassword.setText(QtGui.QApplication.translate("AsianetLogin", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.chkRemember.setText(QtGui.QApplication.translate("AsianetLogin", "Remember", None, QtGui.QApplication.UnicodeUTF8))
        self.bnClose.setText(QtGui.QApplication.translate("AsianetLogin", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.bnConnect.setText(QtGui.QApplication.translate("AsianetLogin", "Connect", None, QtGui.QApplication.UnicodeUTF8))

import asianetlogin_rc
