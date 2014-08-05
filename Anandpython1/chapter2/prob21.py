def wrap():
	temp = []
	x = raw_input("Enter the file name::")
	n = int(raw_input("Enter the wrap size::"))
	print "::File name::"
	print x
	print "::Wrap size::"
	print n
	f = open(x,'r')
	temp = f.readlines()	
	print temp
	
	for i in temp:
		l = 0
		for k in temp:
			print i[l:l+n]
			l = l + n


wrap()
	
