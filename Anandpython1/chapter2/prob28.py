def enumerate(b):
	print
	print "::LIST::"
	print 
	print b
	a = []
	print 
	for i in range(len(b)):
		a.append(i)
	print "::::enumerate::::"
	print
	print "[(INDEX,VALUE)]"
	print
	d = [(a[x],b[y]) for x in range(len(a)) for y in range(len(b)) if x == y]	
	print d


















enumerate(["a","b","c","d","e"])
