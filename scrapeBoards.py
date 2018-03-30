import lbLogin 

print("Logging in to LB conforums site...")

lbLogin.doLogin()

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
	index_file_name = folder_name + "/" + index_board_name + "-index-000.html"

	f = open(index_file_name, "w+")
	bif.write(index_file_name + "\n")

	resp = lbLogin.urllib2.urlopen(board_url)
	contents = resp.read()

	f.write(contents.decode("ISO-8859-1"))
	f.close()	

bif.close()
print("Downloaded data.")
