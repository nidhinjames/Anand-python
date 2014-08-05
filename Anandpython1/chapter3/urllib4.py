import re
import os
import urllib
a = "http://python.org"
b = os.path.basename(a)
r = urllib.urlopen(a)
print r.headers
c = r.read()
d = re.sub('<[^>]*>','',c)
print d




