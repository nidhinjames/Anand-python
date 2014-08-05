def reverse(x):
    print "::LIST::"
    print x
    m = len(x)
    print "length of list" 
    print m
    print ":::REVERSED LIST:::"
    n = m - 1
    i = 0
    j = 0
    a = [] 
    while i <= n:
          print x[n]
	  a.append(x[n])
	  n -= 1 
 

    print a
	  
    


reverse([1, 2, 3, 4, 5])	
