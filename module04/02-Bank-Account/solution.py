class BankAccount:

	def __init__(self, name, initial_balance, currency):
		if initial_balance < 0 or currency == "":
			raise ValueError()

		self.name = name
		self._balance = initial_balance
		self.currency = currency
		self._history = []
		self._history.append("Account was created")

	def deposit(self, amount):

		if amount < 0:
			raise ValueError("Amount is smaller than zero.")

		self._balance += amount
		self._history.append("Deposited {}{}".format(amount, self.currency))

	def balance(self):
		self._history.append("Balance check -> {}{}".format(self._balance, self.currency))
		return self._balance

	def history(self):
		return self._history

	def withdraw(self, amount):
		if amount < self._balance:
			self._history.append("{}{} was withdrawn".format(amount, self.currency))
			self._balance -= amount
			return True

		return False

	def transfer_to(self, account, amount):
		if amount < 0:
			raise ValueError()

		if(self.currency == account.currency):
			if amount > self._balance:
				self._history.append("Transfer to {} for {}{} failed" .format(account.name, self._balance, self.currency))
				self._history.append("Transfer from {} for {}{} failed" .format(self.name, self._balance, self.currency))
				raise ValueError()
			else:
				self._balance -= amount
				account._balance += amount
				self._history.append("Transfer to {} for {}{}" .format(account.name, self._balance, self.currency))
				self._history.append("Transfer from {} for {}{}" .format(self.name, self._balance, self.currency))

				return True
		else:			
			self._history.append("Transfer to {} for {}{} failed" .format(account.name, self._balance, self.currency))
			self._history.append("Transfer from {} for {}{} failed" .format(self.name, self._balance, self.currency))

		raise TypeError()


	def __str__(self):
		return "Bank account for {} with balance of {}{}".format(self.name, self._balance, self.currency)

	def __int__(self):
		self._history.append("__int__ check -> {}{}".format(self._balance, self.currency))
		return self._balance
