
def deposit(amt):
	balance = 0
        balance += amt
	print balance


def withdraw(amt):
	global balance
	balance -= amt
	print balance

deposit(100)

