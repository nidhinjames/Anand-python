import zipfile
file = zipfile.ZipFile("nidhin.zip","r")
for name in file.namelist():
	print name
for info in file.infolist():
	print info.filename,info.date_time,info.file_size 
