class Ifuzzy2:
	def __init__(self,inputs=None,outputs=None,rules=None,N=1000):
		self.inputs = inputs
		self.outputs = outputs
		self.rules = rules
		self.N = N
	def fuzzyfication(X):
		lx = length(X)
		li = length(self.inputs)
