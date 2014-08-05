import re
a = '<FNT name="Century schoolbook" size="22">Title</FNT>'
b = re.sub('<[^>]*>','', a)
print b
