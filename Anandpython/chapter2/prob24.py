def zip():
	a = [1, 2, 3, 4]
	b = ["a", "b", "c"]
	d = []
	d = [(a[x],b[y]) for x in range(len(a)) for y in range (len(b)) if x == y]
	print d





zip() 
