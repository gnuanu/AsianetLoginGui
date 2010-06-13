#========================================================================#
# File Name		: asianetloginmain.py
# Date			: Jun 7, 2010
# Author		: Anoop Panavalappil
# Description	: Asianet Login Main Class Implementation (command line)
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

from PyQt4 import QtCore

import httplib, urllib
import time

class AsianetLoginMain(QtCore.QThread):
	def __init__(self, parent = None):
		super(AsianetLoginMain, self).__init__()
		self.parent = parent
		
		self.accept = "Login"
		self.url_file = "asianet_url"
		self.log = open("asianet_log", 'a')
		
	def initialize(self , username, password):
		self.username = username
		self.password = password
		
	def run(self):
		self.writeLog("Starting Asianet auto login...")
		
		check_url = "www.google.com"
		check_res = "/intl/en/privacy.html"
		
		conn = httplib.HTTPConnection(check_url)
		
		try:
			self.writeLog("Checking current connection status")
			
			self.writeLog("Connecting to " + check_url)
			conn.request("GET", check_res)
			
			res = conn.getresponse()
			conn.close()
			
			self.writeLog("Response = {0}".format(httplib.responses[res.status]))
			
			if res.status == 200 or res.status == 202:
				self.writeLog("An active connection is already present")
				
			if res.status == 302:
				self.writeLog("Couldn't connect to " + check_url)
				login_url = res.getheader('location').split("?")[0]
				self.loginToInternet(login_url)
		except:
			self.writeLog("Network error. Check your connection")
	
	def loginToInternet(self, login_url):
		self.writeLog("Logging in to Asianet..")
		params = urllib.urlencode({'auth_user': self.username, 'auth_pass': self.password, 'accept': self.accept})
		response = urllib.urlopen(login_url, params).info()
		self.writeLog("Response = {0}".format(response.status))
		if response.status == 200 or response.status == 202 or response.status == "":
			self.writeLog("Login Successful")
		else:
			self.writeLog("Login Failed. Try again later..")
	
	def writeLog(self, message):
		print message
		self.message = message
		log = time.ctime() + " - " + message + '\n'
		self.log.write(log)
		self.emit(QtCore.SIGNAL("diplayMessage(QString)"), self.message)

if __name__ == "__main__":
	username = "your username"
	password = "your password"
	
	login = AsianetLoginMain()
	login.initialize(username, password)
	
	login.start()
	login.wait()
