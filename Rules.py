class Rules:
	def __init__(self):
		self.rule = []
		self.qtdRule = 0
	def addRule(self,rule):
		self.rule.append(rule)
		self.qtdRule = self.qtdRule + 1