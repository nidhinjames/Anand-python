def triplet(n):
	ans = [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x + y == z ]
 	print ans




triplet(5)
