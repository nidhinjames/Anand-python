def dup(x):
	
	print ":::list:::"
	print x
	b = []
	c = []
	for i in x:
		if(x.count(i) > 1):
		 	b.append(i)
	for i in b:
		if i not in c:
			c.append(i)
                                  

	print "-:::DUPLICATE ELEMENTS:::-"
	print c





dup([1,2,3,4,5,1,2,3,11])	
