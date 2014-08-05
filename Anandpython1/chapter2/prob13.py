def lensort(x):
	print "-:::LIST:::-"
	print x
	for i in sorted(x, key=len):
		print i




lensort(["python", "c", "java", "perl", "c++"])
