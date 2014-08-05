class BankAccount:
	def __init__(self):
		self.balance = 0

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance
	def deposit(self, amount):
		self.balance += amount
		return self.balance
a = BankAccount()
b = BankAccount()
o = a.deposit(100)
p = b.deposit(100)
q = a.withdraw(10)
print o
print p
print q
