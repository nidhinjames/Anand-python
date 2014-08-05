def group(x,y):
	print "::LIST::"
	print x
	i = 0
	b = []
	while (x[i:i+y] <> []):
		b.append(x[i:i+y])
		i += y
		
	print b 










group([1, 2, 3 , 4, 5, 6, 7, 8],3)
