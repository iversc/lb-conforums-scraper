import lbLogin 

print("Performing Login...")
lbLogin.doLogin()

contents = lbLogin.resp.read()

print("Creating board index.html...")
f = open("index.html", "w+")
f.write(contents.decode("ISO-8859-1"))
f.close()

print("Downloaded data.")
