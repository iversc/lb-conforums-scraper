try:
	import urllib.request as urllib2
except ImportError:
	import urllib2

from bs4 import BeautifulSoup
import os

f = open("index.html", "r")
contents = f.read()
f.close()

soup = BeautifulSoup(contents, "lxml")

#Scope in to the main table for the board list
#Resulting list is the contents of all the <font> tags under this element
#that have a size of 2.
#Further filtering is done once we have that list.
res = soup.find("div", id="mainboard").td.find_all("table", recursive=False)[2].table.find_all("font",size=2)

f = open("boardurls.txt", "w+")

#Keeps track of whether or not we've come across one of the boards called "Staff Discussion"
STAFFFLAG = False

for tag in res:
	#The only tags that have <font size='2'> tags will either be individual numbers, or board names with links.
	#This filters down to just the ones with links.  It scrapes the links, and grabs the contents of the 
	#contained <B> tag.
	if tag.a is not None:
		full_board_name = tag.b.contents[1]
		print(full_board_name)

		board_url = tag.a.get("href")
		board_name = board_url.split("=")[1]
		f.write(tag.a.get("href") + "|" + full_board_name + "\n")
		try:
			os.mkdir(board_name)
		except OSError:	
			pass
