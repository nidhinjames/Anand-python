import urllib
response = urllib.urlopen("http://python.org/")
print response.headers
####print response.header['Content-Type']
