import re

patterns = [ 'this', 'that']
text = 'Does this text match the pattern?'

for pattern in patterns:
	print 'looking for "%s" in "%s" ->' % (pattern, text)
if re.search(pattern, text):
	print 'found match'
else:
	print 'no match'
