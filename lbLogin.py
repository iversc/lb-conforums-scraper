try:
	from http.cookiejar import CookieJar
except ImportError:
	from cookielib import CookieJar

try:
	import urllib.parse as urllib
except ImportError:
	import urllib

try:
	import urllib.request as urllib2
except ImportError:
	import urllib2

import credentials

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Testing')]
urllib2.install_opener(opener)
auth_url = "http://libertybasic.conforums.com/index.cgi?action=login2"

#Credential payload must be of this exact form:
#
#payload = {
#    "form_passed": "1",
#	 "username": "LB_USERNAME",
#	 "password": "LB_PASSWORD"
#}
#
#See demo_credentials.py

payload = credentials.payload
data = urllib.urlencode(payload).encode("utf-8")
req = urllib2.Request(auth_url, data)
resp = None 

def doLogin():
	global resp
	resp = urllib2.urlopen(req)
