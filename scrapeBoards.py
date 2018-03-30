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

print("Logging in to LB conforums site...")
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
resp = urllib2.urlopen(req)

print("Grabbing list of scraped boards...")
f = open("boardurls.txt", "r")
boards = f.readlines()
f.close()

print(str(len(boards)) + " boards found.")
print("")

board_url_base = "http://libertybasic.conforums.com/"
bif = open("boardindexes.txt", "w+")

for board in boards:
	(board_url_suffix,folder_name) = board.strip().split("|")
	board_url = board_url_base + board_url_suffix

	print("    Downloading index for board '" + folder_name + "'...")
	(dummy,index_board_name) = board_url_suffix.split("=")
	index_file_name = folder_name + "/" + index_board_name + "-index.html"

	f = open(index_file_name, "w+")
	bif.write(index_file_name + "\n")

	resp = urllib2.urlopen(board_url)
	contents = resp.read()

	f.write(contents.decode("utf-8"))
	f.close()	

bif.close()
print("Downloaded data.")
