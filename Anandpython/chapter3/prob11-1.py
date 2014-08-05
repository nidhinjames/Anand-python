import zipfile
import glob
import os
name = ["nidhin.txt"]
file = zipfile.ZipFile("new.zip","w")
for n in name:
	file.write(n,os.path.basename(n),zipfile.ZIP_DEFLATED)
file.close()

