import forumLogin 

print("Logging in to conforums site...")

forumLogin.doLogin()

print("Grabbing list of scraped boards...")
f = open("boardurls.txt", "r")
boards = f.readlines()
f.close()

print(str(len(boards)) + " boards found.")
print("")

board_url_base = forumLogin.board_url 
bif = open("boardindexes.txt", "w+")

for board in boards:
	board_url_suffix = board.strip().split("|")[0]
	board_name = board_url_suffix.split("=")[1]
	board_url = board_url_base + board_url_suffix

	print("    Downloading index for board '" + board_name + "'...")
	index_file_name = board_name + "/" + board_name + "-index-000.html"

	f = open(index_file_name, "w+")
	bif.write(index_file_name + "\n")

	resp = forumLogin.urllib2.urlopen(board_url)
	contents = resp.read()

	f.write(contents.decode("ISO-8859-1"))
	f.close()	

bif.close()
print("Downloaded data.")
