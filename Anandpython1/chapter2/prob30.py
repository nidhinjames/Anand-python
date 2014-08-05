def csv(a):
	print "FILE NAME IS:::"
	print a
	b = []
	f = open(a, 'r')
	for i in f.readlines():
		b.append(i)
	print [i.split() for i in b]
	






csv("a.csv")
