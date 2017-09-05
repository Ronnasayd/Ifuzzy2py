class Rules:
	def __init__(self):
		""" Creates a rules object """
		self.rule = []
		self.qtdRule = 0
	def addRule(self,rule):
		""" Add Rule object to a Rules object, 
		and updates the amount of rules added to this object """
		self.rule.append(rule)
		self.qtdRule = self.qtdRule + 1