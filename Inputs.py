class Inputs:
	def __init__(self):
		""" Creates an Inputs object """
		self.input= []
		self.qtdInput = 0
	def addInput(self,input):
		""" Add Memership functions to an Inputs object, 
		and updates the amount of membership functions added to this object """
		self.input.append(input)
		self.qtdInput = self.qtdInput + 1