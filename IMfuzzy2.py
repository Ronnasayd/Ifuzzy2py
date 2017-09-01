class IMfuzzy2:
	def __init__(self,lower,upper):
		self.lower = lower
		self.upper = upper
	def setPertinence(self,X):
		self.lower.setPertinence(X)
		self.upper.setPertinence(X)