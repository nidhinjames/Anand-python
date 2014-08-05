import re
str = "nidhin@gmail.com, najeeb@gmail.com,qeqeeqe"
emails = re.findall(r'[\w\.-]+@[\w\.-]+',str)
for email in emails:
	print email

