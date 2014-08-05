balance = 0
def deposit(amount):
	global balance
	balance += amount
	return balance
def withdraw(amount):
	global balance
	balance -= amount
	return balance


e = deposit(100)
f = withdraw(100)
print f
