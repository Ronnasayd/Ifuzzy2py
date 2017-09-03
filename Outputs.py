class Outputs:
	def __init__(self):
		self.output = []
		self.qtdOutput = 0
	def addOutput(self,output):
		self.output.append(output)
		self.qtdOutput = self.qtdOutput + 1