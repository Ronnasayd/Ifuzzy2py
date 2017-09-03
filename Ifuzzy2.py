class Ifuzzy2:
	def __init__(self,inputs=[],outputs=[],rules=[],N=1000):
		self.inputs = inputs
		self.outputs = outputs
		self.rules = rules
		self.N = N
		
	def fuzzyfication(self,X):
		lx = len(X)
		if lx == self.inputs.qtdInput:
			for i in range(lx):
				for j in range(self.inputs.input[i].qtdMf):
					self.inputs.input[i].Mf[j].setPertinence(X[i])

	def inference(self):
		for i in range(self.rules.qtdRule):
			maxLower = 0
			maxUpper = 0
			for j in range(self.rules.rule[i].antescedent.qtdMf):
				if self.rules.rule[i].antescedent.Mf[j].lower.pert > maxLower:
					maxLower = self.rules.rule[i].antescedent.Mf[j].lower.pert
				if self.rules.rule[i].antescedent.Mf[j].upper.pert > maxUpper:
					maxUpper = self.rules.rule[i].antescedent.Mf[j].upper.pert

			print([i,maxUpper,maxLower])



