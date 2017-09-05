class Consequent:
	def __init__(self):
		""" Creates an consequent object """
		self.Mf = []
		self.qtdMf = 0
	
	def addMf(self,Mf):
		""" Adds membership functions to a consequent object, 
		and updates the amount of membership functions added to this object """
		self.Mf.append(Mf) 
		self.qtdMf = self.qtdMf + 1 
