def linecount(x):
	print "::FILE_NAME::"
	print x
	count=len(open(x).readlines())
	print ":::line_count:::"
	print count




linecount("nidhin.txt")
