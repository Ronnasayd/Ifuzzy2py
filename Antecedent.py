class Antecedent:
	def __init__(self):
		""" Creates an antecedent object """
		self.Mf = []
		self.qtdMf = 0
			
	def addMf(self,Mf):
		""" Adds membership functions to an antecedent object, 
		and updates the amount of membership functions added to this object """
		self.Mf.append(Mf) 
		self.qtdMf = self.qtdMf + 1 

