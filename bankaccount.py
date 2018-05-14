"""
TITLE: bankaccount.py
AUTHOR: Renato Lima
Python class that can be used to create and manipulate a personal bank account.
The bank account class you'll create should have methods for each of the following:
Accepting deposits
Allowing withdrawals
Showing the balance
Showing the details of the account
"""

class BankAccount(object):
	balance = 0
	def __init__(self, name):
	 	self.name = name
	def __repr__(self):
	 	return "%s's account. Balance: $%.2f" % (self.name, self.balance)
	def show_balance(self):
	 	print "Balance: $%.2f" % (self.balance)
	def deposit(self, amount):
	 	if amount <= 0:
	 		print "Error"
	 		return
	 	else:
	 		print "Amount: $%.2f" % (amount)
	 		self.balance += amount
	 		self.show_balance()
	def withdraw(self, amount):
	 	if amount <= 0:
	 		print "Error"
	 		return
	 	else:
	 		print "Amount: $%.2f" % (amount)
	 		self.balance -= amount
        	self.show_balance()

my_account = BankAccount("Antonio")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
