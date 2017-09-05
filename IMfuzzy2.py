class IMfuzzy2:
	def __init__(self,lower,upper):
		""" Creates a interval fuzzy type 2 membership function 
		with the lower and upper membership functions"""
		self.lower = lower
		self.upper = upper
	def setPertinence(self,X):
		""" Set the internal pertinence used in calculations of upper and lower 
		membership functions of a interval fuzzy type 2 membership function """
		self.lower.setPertinence(X)
		self.upper.setPertinence(X)
	def addPert(self):
		""" Adds pertinence of actived input membership functions in 
		inference module to the output membership functions """
		self.lower.addPert()
		self.upper.addPert()
	def resetstack(self):
		""" Resets the stack of actived membership functions in inference module """
		self.lower.stack = []
		self.upper.stack = []