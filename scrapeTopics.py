import forumLogin
from bs4 import BeautifulSoup

f = open("boardindexes.txt", "r")
boards = f.readlines()
f.close()

print("Logging in to forum...")
forumLogin.doLogin()

print("Scanning topics...")

for board in boards:
	board = board.split("/")[0]

	print("    Checking progress for board '" + board + "'...")
	progress_file = board + "/" + board + "-progress.txt"

	progress = ""

	try:
		f = open(progress_file, "r")
		progress = f.read()
		f.close()
	except FileNotFoundError:
		pass

	if progress == "COMPLETE":
		print("        Scraping board '" + board + "' has already been completed.")
		continue

	topic_url_base = forumLogin.board_url + "index.cgi?board=" + board + "&action=display&num="

	numProgress = 0
	if progress != "":
		numProgress = int(progress)

	print("        Scraping topics for board '" + board + "'...")

	if numProgress > 0:
		print("    " + str(numProgress) + " topic(s) have already been scraped.")

	topic_list = board + "/" + board + "-topic-list.txt"
	f = open(topic_list, "r")
	topics = f.readlines()
	f.close()

	numTopics = len(topics)

	print("        " + str(numTopics) + " topics found.")

	for x in range(numProgress, numTopics):
		print("        Scraping topic " + str(x + 1) + " of " + str(numTopics) + "...")
		
		topic_id = topics[x].split("|")[0]
		topic_url = topic_url_base + topic_id

		topic_file_base = board + "/topic-" + topic_id + "-p"
		topic_file = topic_file_base + "000.html"

		print("            Downloading topic...")
		resp = forumLogin.urllib2.urlopen(topic_url)
		data = resp.read().decode("ISO-8859-1")

		f = open(topic_file, "w+")
		f.write(data)
		f.close()

		print("            Checking for additional pages...")
		soup = BeautifulSoup(data, "lxml")

		fonts = soup.find("b",string="Pages:").parent.find_all("font")

		if len(fonts) != 0:
			numPages = int(fonts[-1].string)
			print("            Found " + str(numPages) + " pages.")

			for page in range(1, numPages):
				topic_file = topic_file_base + ("000" + str(page))[-3:] + ".html"
				start = page * 15

				page_url = topic_url + "&start=" + str(start)

				print("            Downloading page " + str(page + 1) + " of " + str(numPages) + "...")
				resp = forumLogin.urllib2.urlopen(page_url)
				data = resp.read().decode("ISO-8859-1")

				f = open(topic_file, "w+")
				f.write(data)
				f.close()		
		else:
			print("            No additional pages.")

		f = open(progress_file, "w+")
		f.write(str(x))
		f.close()


	f = open(progress_file, "w+")
	f.write("COMPLETE")
	f.close()
	

