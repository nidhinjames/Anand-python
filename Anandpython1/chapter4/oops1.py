def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    print account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    print account['balance']



a = make_account()
b = make_account()
deposit(a, 100)
deposit(b, 50)
withdraw(b, 10)
withdraw(a, 10)
