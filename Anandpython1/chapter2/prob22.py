def extsort():
	x = ["b.py", "c.py","n.c", "d.txt"]
	print "::LIST:::"
	print x
	ext = []
	f = []
	s = []
	
	for i in x:
		ext.append(i.split('.'))
	ext.sort(key=lambda x: x[1])			
		
	print "-:::extension sorted list:::-"

	for i in ext:
		s.append(".".join([i[0],i[1]]))



	print s


	

		
	



extsort()	
