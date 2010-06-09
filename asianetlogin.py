'''
Created on Jun 7, 2010

@author: Anoop Panavalappil
'''
from ui_asianetlogin import Ui_AsianetLogin
from asianetloginmain import AsianetLoginMain
from PyQt4 import QtCore, QtGui

import os.path
import sys

class AsianetLogin(QtGui.QDialog, Ui_AsianetLogin):
	def __init__(self, parent = None):
		super(AsianetLogin, self).__init__(parent)
		self.setupUi(self)
		
		if os.path.exists("asianetconf"):
			file = open("asianetconf", 'r')
			text = file.readline()
			data = text.split("=") 
			self.edUsername.setText(data[0])
			self.edPassword.setText(data[1])
			file.close()
		
		self.connect(self.bnClose, QtCore.SIGNAL("clicked()"), self.close)
		self.connect(self.bnConnect, QtCore.SIGNAL("clicked()"), self.onConnect)

	def onConnect(self):
		if self.edUsername.text() == "" or self.edPassword.text() == "":
			QtGui.QMessageBox.warning(self, "Error - AsianetLogin", "Username and Password are mandatory fields")
			return
		
		if self.chkRemember.isChecked():
			file = open("asianetconf", 'w')
			file.write(self.edUsername.text() + "=" + self.edPassword.text())
			file.close()
		
		self.login = AsianetLoginMain(self.edUsername.text(), self.edPassword.text(), self)
		self.connect(self.login.log, QtCore.SIGNAL("displayMessage(QString)"), self.displayLog)	
		self.login.connectAsianet()
			
	def displayLog(self, log):
		display_log = self.teLog.toPlainText()
		display_log += log
		self.teLog.setText(display_log)
		scrollbar = self.teLog.verticalScrollBar()
		scrollbar.setValue(scrollbar.maximum())
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	
	dlg = AsianetLogin()
	dlg.show()
	
	sys.exit(app.exec_())