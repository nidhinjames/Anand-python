import urllib, json

data = json.loads(urllib.urlopen("http://ip.google.com/").read())
print data["ip"]
