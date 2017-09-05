class Rule:
	def __init__(self,ant = None,cons = None):
		""" Creates a rule object with this antecedent and consequent objects """
		self.antecedent = ant
		self.consequent = cons