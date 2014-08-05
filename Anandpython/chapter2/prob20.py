def grep():
	count = 0
	x = raw_input("file name:")
	y = raw_input("enter pattern:")
	print 
	print "file_name: "+ x
	print
	print "pattern: "+ y 
	print 
	f = open(x, "r")
	s = f.readlines()
	print 

	
	print ":::MATCHED LINES:::"
	print 

	for i in s:
		if y in i:
			print i
			count += 1
                                
	print "count of lines:::"
	print count



grep()
