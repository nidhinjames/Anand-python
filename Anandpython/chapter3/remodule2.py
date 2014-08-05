import re
pattern = 'this'
text = 'Does this text match the pattern'
match = re.search(pattern, text)
s = match.start()
e = mach.end()

print 'found "%s" in "%s" from %d to %d ("%s")' %  
(match.re.pattern ,match.string , s, e, text[s:e])
