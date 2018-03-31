# lb-conforums-scraper
HTML page scraper to store the LB conforums download data

How to use these scripts:

1. Install Python 2.7 or Python 3.  This should work on Windows, as well.
2. Install the BeautifulSoup python module.  From an admin command line, run the command:

    `pip install bs4`
3. Set up the `credentials.py` file.
    1. Copy `demo-credentials.py` to `credentials.py`
    2. Edit `credentials.py` and fill in the username and password to use to sign in to the forum.
4. Edit the forum URL to point to your forum.
    1. In the `forumLogin.py` file, find the line that says `board_url = "http://libertybasic.conforums.com"`
    2. Replace `"libertybasic"` with the name of your own ConForums board.
5. Run the `scrapeIndex.py` script.  This should log in to the target forum and download the index page to `index.html`.
6. Run the `parseIndex.py` script.  This will generate a list of boards on the forum, and create subfolders for each board.
7. Run the `scrapeBoards.py` script.  This will login in to the target forum, and download each board's first page.  The HTML files will be saved in each board's folder, as `board-index-000.html`.
8. Run the `scrapeBoardSubpages.py` script.  This will log in to the target forum, and parse the already downloaded first pages of each board to find how many additional pages each board has.  It will then download all of those pages, to each board's folder.
9. Run the `parseBoards.py` script.  This will go through all of the downloaded board index pages, and generate lists of topic IDs in each forum.  The ID list will be saved in each folder, with the name `board-topic-list.txt`.

A script is coming soon to use the generated topic ID lists to scrape every topic.
