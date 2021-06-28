class Donator:

	def __init__(self,Number, Name, Amount, Date, Mode, Email):
		self.Number = Number
		self.Name = Name
		self.Amount = Amount
		self.Date = Date
		self.Mode = Mode
		self.Email = Email

	def __str__(self):
		return f'Number: {self.Number} Name: {self.Name} Amount: {self.Amount} Date: {self.Date} Mode: {self.Mode} Email: {self.Email}'
