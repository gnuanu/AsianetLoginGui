'''
Created on Jun 7, 2010

@author: anoop.panavalappil
'''

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
