# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asianetlogin.ui'
#
# Created: Mon Jun  7 19:25:45 2010
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
        self.widget = QtGui.QWidget(AsianetLogin)
        self.widget.setGeometry(QtCore.QRect(10, 10, 501, 191))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbUsername = QtGui.QLabel(self.widget)
        self.lbUsername.setObjectName("lbUsername")
        self.horizontalLayout.addWidget(self.lbUsername)
        self.edUsername = QtGui.QLineEdit(self.widget)
        self.edUsername.setObjectName("edUsername")
        self.horizontalLayout.addWidget(self.edUsername)
        self.lbPassword = QtGui.QLabel(self.widget)
        self.lbPassword.setObjectName("lbPassword")
        self.horizontalLayout.addWidget(self.lbPassword)
        self.edPassword = QtGui.QLineEdit(self.widget)
        self.edPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.edPassword.setObjectName("edPassword")
        self.horizontalLayout.addWidget(self.edPassword)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chkRemember = QtGui.QCheckBox(self.widget)
        self.chkRemember.setObjectName("chkRemember")
        self.horizontalLayout_2.addWidget(self.chkRemember)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bnClose = QtGui.QPushButton(self.widget)
        self.bnClose.setObjectName("bnClose")
        self.horizontalLayout_2.addWidget(self.bnClose)
        self.bnConnect = QtGui.QPushButton(self.widget)
        self.bnConnect.setObjectName("bnConnect")
        self.horizontalLayout_2.addWidget(self.bnConnect)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.teLog = QtGui.QTextEdit(self.widget)
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

