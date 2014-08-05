def reverse_content(x):
	print ":::REVERSE A FILE:::"
	print ""
	print "CONTENT OF  " + x
	print ""
	for i in (open(x).readlines()):
		print i
	
	
	print "::::::content in reversed order:::::::"
	print ""
	for i in reversed(open(x).readlines()):
		print i



reverse_content("she.txt")
