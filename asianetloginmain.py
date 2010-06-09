'''
Created on Jun 7, 2010

@author: Anoop Panavalappil
'''

from PyQt4 import QtCore
import httplib, urllib
import time
import os.path


class Log(QtCore.QThread):
	def __init__(self):
		super(Log, self).__init__()
		logfile = "asianet_log"
		self.log = open(logfile, 'a')
		
	def writeLog(self, message):
		self.logmsg = time.ctime() + " - " + message + '\n'
		self.log.write(self.logmsg)
		
	def run(self):
		self.emit(QtCore.SIGNAL("displayMessage(QString)"), self.logmsg)
		
	def __del__(self):
		self.log.close()
		
class AsianetLoginMain:
	def __init__(self, username, password, parent = None):
		self.username = username
		self.password = password
		self.parent = parent
		
		self.accept = "Login"
		self.url_file = "asianet_url"
		
		self.log = Log()
		
	def connectAsianet(self):
		self.log.writeLog("Starting Asianet auto login...")
		self.log.start()
		self.log.wait()
			
		check_url = "www.google.com"
		check_res = "/intl/en/privacy.html"
		
		conn = httplib.HTTPConnection(check_url)
		
		try:
			self.log.writeLog("Checking current connection status")
			self.log.start()
			self.log.wait()
			
			self.log.writeLog("Connecting to " + check_url)
			self.log.start()
			self.log.wait()
			
			conn.request("GET", check_res)
			
			res = conn.getresponse()
			conn.close()
			
			self.log.writeLog("Response = {0}".format(httplib.responses[res.status]))
			self.log.start()
			self.log.wait()
			
			if res.status == 200 or res.status == 202:
				self.log.writeLog("An active connection is already present")
				self.log.start()
				self.log.wait()
				
			if res.status == 302:
				self.log.writeLog("Couldn't connect to google")
				self.log.start()
				self.log.wait()
				
				login_url = res.getheader('location').split("?")[0]
				self.loginToInternet(login_url)
		except:
			self.log.writeLog("Network error. Check your connection")
			self.log.start()
			self.log.wait()
			
	def loginToInternet(self, login_url):
		self.log.writeLog("Logging in to Asianet..")
		self.log.start()
		self.log.wait()
		
		self.saveLoginUrl(login_url)
		params = urllib.urlencode({'auth_user': self.username, 'auth_pass': self.password, 'accept': self.accept})
		response = urllib.urlopen(login_url, params).info()
		self.log.writeLog("Response = {0}".format(response))
		self.log.start()
		self.log.wait()
		
		if response.status == 200 or response.status == 202 or response.status == "":
			self.log.writeLog("Login Successful")
			self.log.start()
			self.log.wait()
		else:
			self.log.writeLog("Login Failed. Try again later..")
			self.log.start()
			self.log.wait()
			
	def getLoginUrl(self):
		url = ""
		if os.path.exists(self.url_file):
			urlfile = open(self.url_file, 'r')
			url = urlfile.readline()
			urlfile.close()
		return url
	
	def saveLoginUrl(self, url):
		urlfile = open(self.url_file, 'w')
		urlfile.write(url)
		urlfile.close()
	
if __name__ == "__main__":
	username = "your username"
	password = "your password"
	login = AsianetLoginMain(username, password)
	login.connectAsianet()