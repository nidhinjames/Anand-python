import zipfile
file = zipfile.ZipFile("a/a.zip","r")
for name in file.nalelist():
	print name
