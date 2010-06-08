'''
Created on Jun 7, 2010

@author: anoop.panavalappil
'''

import httplib, urllib
import time
import os.path


class Log:
	def __init__(self, parent):
		self.parent = parent
		logfile = "asianet_log"
		self.log = open(logfile, 'a')
		
	def writeLog(self, message):
		log = time.ctime() + " - " + message + '\n'
		if self.parent != None:
			self.parent.displayLog(message)
			
		self.log.write(log)
		
	def __del__(self):
		self.log.close()
		
class AsianetLoginMain:
	def __init__(self, username, password, parent = None):
		self.username = username
		self.password = password
		self.parent = parent
		
		self.accept = "Login"
		self.url_file = "asianet_url"
		
		self.log = Log(self.parent)
		
	def connectAsianet(self):
		self.log.writeLog("Starting Asianet auto login...")
			
		check_url = "www.google.com"
		check_res = "/intl/en/privacy.html"
		
		conn = httplib.HTTPConnection(check_url)
		
		try:
			self.log.writeLog("Checking current connection status")
			self.log.writeLog("Connecting to " + check_url)
			conn.request("GET", check_res)
			
			res = conn.getresponse()
			conn.close()
			
			self.log.writeLog("Response = {0}".format(httplib.responses[res.status]))
			
			if res.status == 200 or res.status == 202:
				self.log.writeLog("An active connection is already present")
			if res.status == 302:
				self.log.writeLog("Couldn't connect to google")
				login_url = res.getheader('location').split("?")[0]
				self.loginToInternet(login_url)
		except:
			self.log.writeLog("Network error. Check your connection")
			
	def loginToInternet(self, login_url):
		self.log.writeLog("Logging in to Asianet..")
		self.saveLoginUrl(login_url)
		params = urllib.urlencode({'auth_user': self.username, 'auth_pass': self.password, 'accept': self.accept})
		response = urllib.urlopen(login_url, params).info()
		self.log.writeLog("Response = {0}".format(response))
		if response.status == 200 or response.status == 202 or response.status == "":
			self.log.writeLog("Login Successful")
		else:
			self.log.writeLog("Login Failed. Try again later..")
			
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