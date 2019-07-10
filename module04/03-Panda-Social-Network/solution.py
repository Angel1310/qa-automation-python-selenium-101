class Panda():

	def __init__(self, name, email, gender):
		self.name = name
		self.email = email
		if gender == 'male':
			self.gender = True
		else:
			self.gender = False

	def name(self):
		return self.name

	def email(self):
		return self.email

	def gender(self):
		if self.gender:
			return 'male'
		else:
			return 'female'



class PandaSocialNetwork():

	pass