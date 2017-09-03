class Antescedent:
	def __init__(self):
		self.Mf = []
		self.nI = []
		self.qtdMf = 0
		self.qtdInput = 0
		
	def addMf(self,Mf,numberInput):
		self.Mf.append(Mf)
		self.qtdMf = self.qtdMf + 1
		self.nI.append(numberInput)
		self.qtdInput = self.qtdInput + 1
