import zipfile
z = zipfile.ZipFile("a.zip","r")
for name in z.zipnamelist():
	print name
