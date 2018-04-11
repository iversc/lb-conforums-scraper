import forumLogin 
import os
from bs4 import BeautifulSoup

print("Logging in to conforums site...")

forumLogin.doLogin()

print("Creating member indexes folder...")
try:
	os.mkdir("member-indexes")
except OSError:
	pass

members_url = "http://libertybasic.conforums.com/index.cgi?action=mlall"

print("Scraping members index page...")
resp = forumLogin.urllib2.urlopen(members_url)
contents = resp.read()

f = open("member-indexes/member-index-000.html", "w+")
f.write(contents.decode("ISO-8859-1"))
f.close()

print("Checking number of member pages...")
soup = BeautifulSoup(contents, "lxml")
pages = int( soup.find_all("option")[-1].string)
print(str(pages) + " member pages found.")

for x in range(1, pages):
	print("Scraping page " + str(x+1) + " of " + str(pages) + "...")
	members_subpage_url = members_url + "&start=" + str(x * 20)
	file_name = "member-indexes/member-index-" + ("000" + str(x))[-3:] + ".html"

	f = open(file_name, "w+")
	resp = forumLogin.urllib2.urlopen(members_subpage_url)
	f.write(resp.read().decode("ISO-8859-1"))
	f.close()


