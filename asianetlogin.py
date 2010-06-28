#========================================================================#
# File Name    : asianetlogin.py
# Date         : Jun 7, 2010
# Author       : Anoop Panavalappil
# Description  : Asianet Login GUI Class Implementation
#========================================================================#

"""
Copyright 2010 Anoop Panavalappil <gnuanu@gmail.com@>
http://www.librecode.org

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Library General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

If you find any bugs or have any suggestions email: gnuanu@gmail.com
URL: http://www.librecode.org
"""

from ui_asianetlogin import Ui_AsianetLogin      # The generated UI class
from asianetloginmain import AsianetLoginMain    # The main class

from PyQt4 import QtCore, QtGui

import os.path
import sys

class AsianetLogin(QtGui.QDialog, Ui_AsianetLogin):
	def __init__(self, parent = None):
		super(AsianetLogin, self).__init__(parent)
		self.setupUi(self)
		self.running = False
		
		
		if os.path.exists("asianetconf"):
			file = open("asianetconf", 'r')
			text = file.readline()
			data = text.split("=")
			self.edUsername.setText(data[0])
			self.edPassword.setText(data[1])
			file.close()
		
		self.login = AsianetLoginMain(self)
		self.connect(self.login, QtCore.SIGNAL("diplayMessage(QString)"), self.displayLog)
		
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
			
		# Check whether the thread is running or not
		if not self.running:			
			self.login.initialize(self.edUsername.text(), self.edPassword.text())
			self.login.start()
			self.running = True
		else:
			if self.login.isFinished():
				self.running = False
				self.onConnect()
	
	def displayLog(self, log):
		display_log = self.teLog.toPlainText()
		display_log += log + "\n"
		self.teLog.setText(display_log)
		scrollbar = self.teLog.verticalScrollBar()
		scrollbar.setValue(scrollbar.maximum())

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	
	dlg = AsianetLogin()
	dlg.show()
	
	sys.exit(app.exec_())
