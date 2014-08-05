def make_slug(a):
	import re
	b = re.sub(" ", "-", a)
	print b



make_slug("hello world")
make_slug("hello  world")
make_slug("hello- world--")
