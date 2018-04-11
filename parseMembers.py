try:
	import urllib.request as urllib2
except ImportError:
	import urllib2

from bs4 import BeautifulSoup
import os


print("Parsing member data...")

folder = "member-indexes"
files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))
	and ".html" in f]

total_files = str(len(files))
print(total_files + " files to scan.")
file_count = 0

member_list_file = open("boardmembers.txt","w+")

for file_name in sorted(files):
	file_count += 1
	print("    Parsing file " + str(file_count) + " of " + total_files + "...")
	
	full_file_name = "member-indexes/" + file_name
	f = open(full_file_name, "r")
	contents = f.read()
	f.close()

	soup = BeautifulSoup(contents, "lxml")
	trs = soup.find(string="Name").parent.parent.parent.parent.parent.find_all("tr",recursive=False)

	#Strip off the first two and the last table rows, to only retrieve user data
	trs = trs[2:-1]

	for tr in trs:
		tds = tr.find_all("td")
		name_td = tds[0]
		posts_td = tds[4]

		display_name = name_td.string
		user_name = name_td.a.get("href").split("=")[-1]

		print("        Found user " + display_name + "(" + user_name + ")...")
		posts = posts_td.string
		if (posts is None) or (int(posts)== 0):
			print("            User has zero posts.  Skipping user...")
			continue

		member_list_file.write(user_name + "," + display_name + "\n")

print("All files parsed.  Complete.")
member_list_file.close()
