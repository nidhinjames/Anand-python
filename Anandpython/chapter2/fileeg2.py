def word_count(x):
	print "::FILE NAME::"
	print x
	count=len(open(x).read().split())
	print ":::word count:::"
	print count






word_count("nidhin.txt")
