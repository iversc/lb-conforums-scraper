import forumLogin 

print("Performing Login...")
forumLogin.doLogin()

contents = forumLogin.resp.read()

print("Creating board index.html...")
f = open("index.html", "w+")
f.write(contents.decode("ISO-8859-1"))
f.close()

print("Downloaded data.")
