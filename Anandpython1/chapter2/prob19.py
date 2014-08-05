def tail_head():
	x = raw_input("enter the file name::")
	print x
	b = []
	f = open(x , "r")
	s = f.readlines()
	for i in rane(10, s):
		b.append(i)
	
	print b
   
	
		




tail_head()
