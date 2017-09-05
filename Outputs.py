class Outputs:
	def __init__(self):
		""" Creates an Outputs object """
		self.output = []
		self.qtdOutput = 0
	def addOutput(self,output):
		""" Add Memership functions to an Outputs object, 
		and updates the amount of membership functions added to this object """
		self.output.append(output)
		self.qtdOutput = self.qtdOutput + 1