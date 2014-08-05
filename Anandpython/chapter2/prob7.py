def minmax(x):
    print ":::LIST:::"
    print x
    i = 0
    n = len(x) 
    big = x[0]
    small = x[0]
    while i < n:
	if big < x[i]:
            big = x[i]
        if small > x[i]:
            small = x[i]
	i += 1
    print "Biggest element"
    print big
    print "smallest element"
    print small





minmax([1, 2, 3, 4, 5])
