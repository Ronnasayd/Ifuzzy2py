class Input:
	def __init__(self,init = None,end = None):
		""" Creates an Input object with this respective range (initial value and final value) """
		self.qtdMf = 0
		self.Mf = []
		self.init = init
		self.end = end
	def addMf(self,Mf):
		""" Adds Memership functions to an Input object, 
		and updates the amount of membership functions added to this object """
		self.Mf.append(Mf)
		self.qtdMf = self.qtdMf + 1