def download(a):
	import os
	import urllib
	##response = urllib.urlopen(a)
	##print response.headers
	b = os.path.basename(a)
	r=urllib.urlopen(a)
	print b,r.headers




download("http://python.org/")
