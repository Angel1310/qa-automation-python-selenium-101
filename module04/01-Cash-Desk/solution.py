
class Bill:
    def __init__(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Amount is not a number.")
        if amount <= 0:
            raise ValueError("Amount is smaller than zero.")
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return "A {}$ bill".format(self.__class__)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return self.amount


class BatchBill:
    def __init__(self, bills):
        self.bills = bills
        self.index = len(bills)

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, item):
        return self.bills[item]

    def total(self):
        total = 0
        for bill in self.bills:
            total += int(bill)

        return total

class CashDesk:

	def __init__(self):
		self.bills = []

	def take_money(self, bills):
		try:
			for bill in bills:
				self.bills.append(bill)
		except:
			self.bills.append(bills)

	def total(self):
		result = 0
		for bill in self.bills:
			result += int(bill)
		return result
	
	def inspect(self):
		result = """We have a total of {}$ in the desk
We have the following count of bills, sorted in ascending order:""".format(self.total())
		bills_dict = {}
		for bill in self.bills:
			if not int(bill) in bills_dict:
				bills_dict[int(bill)] = 1
			else:
				bills_dict[int(bill)] += 1

		

		for key in sorted(bills_dict.keys()):
			result += '\n' + str(key) + "$ bills - " + str(bills_dict[key]) 
			
		return result

