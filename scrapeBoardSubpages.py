from bs4 import BeautifulSoup
import forumLogin

f = open("boardindexes.txt", "r")
indexes = f.readlines()
f.close()

print("Logging in to LB forums...")
forumLogin.doLogin()

board_base_url = forumLogin.board_url + "index.cgi?board="

for index in indexes:
	index = index.strip()

	f = open(index, "r")
	contents = f.read()
	f.close()

	(board_name,file_name) = index.split("/")
	board_url = board_base_url + board_name
	
	soup = BeautifulSoup(contents, "lxml")

	pages = int(soup.find_all("b",string="Pages:")[0].parent.find_all("font")[-1].string)

	print("Board '" + board_name + "':")
	print("    "+ str(pages) + " pages detected.")
	print()
	print("    Collecting subpages...")
	print("        Preparing to scrape subpages of " + board_url + "...")

	for x in range(1, pages):
		print("        Downloading page "+ str(x + 1) + " of " + str(pages) + "...")

		start = x * 20
		page_url = board_url + "&start=" + str(start)
		index_file_name = folder + "/" + board_name + "-index-" + ("000" + str(x))[-3:] + ".html"

		f = open(index_file_name, "w+")
		
		resp = forumLogin.urllib2.urlopen(page_url)

		f.write(resp.read().decode("ISO-8859-1"))
		f.close()
		
