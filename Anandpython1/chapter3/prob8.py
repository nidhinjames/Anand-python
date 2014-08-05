import re
import os
import urllib
x = urllib.urlopen("http://python.org/").readlines()
for item in x:
	if "http://" in item:
		print item[item.index("http://"):]
