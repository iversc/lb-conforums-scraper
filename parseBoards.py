try:
	import urllib.request as urllib2
except ImportError:
	import urllib2

from bs4 import BeautifulSoup
import os


f = open("boardindexes.txt", "r")
indexes = f.readlines()
f.close()

print("Scanning indexes...")

for index in indexes:
	folder = index.strip().split("/")[0]
	print("    Parsing indexes for board '" + folder + "'...")

	files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) 
		and folder in f and ".html" in f]
	print("        Indexes for " + str(len(files)) + " pages found.")

	topic_list_file = folder + "/" + folder + "-topic-list.txt"
	topic_list = open(topic_list_file, "w+")

	for file_name in sorted(files):
		print("        Parsing index '" + file_name + "'...")
		file_path = folder + "/" + file_name

		f = open(file_path, "r")
		contents = f.read()
		f.close()

		soup = BeautifulSoup(contents, "lxml")
		subjects = soup.find_all("b", string="Subject")

		for subject in subjects:
			table = subject.parent.parent.parent.parent
			fonts = table.find_all("font",size="2")

			for font in fonts:
				#Get last a-tag returned, in case there are multiple.
				#The "unread message" indicator will otherwise mess with this.
				list_a = font.find_all("a", recursive=False)
				if len(list_a) == 0:
					continue

				a = list_a[-1]

				if a is not None:
					topic_link = a.get("href")
					topic_id = topic_link.split("num=")[1]

					#Grab the topic title from between the two comments
					topic_title = a.b.contents[1]
					print("            " + topic_title + " - " + topic_id)
					topic_list.write(topic_id + "|" + topic_title + "\n")

	topic_list.close()

