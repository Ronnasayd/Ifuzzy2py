class Input:
	def __init__(self):
		self.qtdMf = 0
		self.Mf = []
	def addMf(self,Mf):
		self.Mf.append(Mf)
		self.qtdMf = self.qtdMf + 1