class Input:
	def __init__(self,init = None,end = None):
		self.qtdMf = 0
		self.Mf = []
		self.init = init
		self.end = end
	def addMf(self,Mf):
		self.Mf.append(Mf)
		self.qtdMf = self.qtdMf + 1