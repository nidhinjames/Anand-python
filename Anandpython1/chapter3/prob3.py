import os
import time
f='/home/nidhin/my_prgms/Anandpython/chapter3'
a=os.listdir(f)
print "filename  size  time"
for i in a:
	x=os.path.getsize(i)
	y=os.path.getatime(i)
	print i  ,x  ,y
