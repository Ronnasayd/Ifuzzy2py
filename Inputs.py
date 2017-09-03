class Inputs:
	def __init__(self):
		self.input= []
		self.qtdInput = 0
	def addInput(self,input):
		self.input.append(input)
		self.qtdInput = self.qtdInput + 1