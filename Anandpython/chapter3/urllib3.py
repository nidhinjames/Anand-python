import os
import urllib
a='http://docs.python.org/tutorial/interpreter.html/'
b=os.path.basename(a)
print "base name"
print b
if a[-1]=='/':
	c = a + 'index.html'
	print c
