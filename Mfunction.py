class Mfunction:
	from math import exp,sqrt,pi

	def __init__(self,flag,media,dp):
		self.flag = flag # flag que representa o tipo de função
		self.media = media # media da função gaussiana
		self.dp  = dp # desvio padrao da função gaussiana
		self.pert = None #pertinencia de ativação para um determinado valor de entrada

	def __init__(self,flag,x1,y1,x2,y2,x3,y3,x4,y4):
		self.flag = flag # flag que representa o tipo de função
		self.x1 = x1 # abissiça ponto 1
		self.x2 = x2 # abissiça ponto 2
		self.x3 = x3 # abissiça ponto 3
		self.x4 = x4 # abissiça ponto 4
		self.y1 = y1 # ordenada ponto 1
		self.y2 = y2 # ordenada ponto 2
		self.y3 = y3 # ordenada ponto 3
		self.y4 = y4 # ordenada ponto 4a
		self.pert = None #pertinencia de ativação para um determinado valor de entrada

	def setPertinence(self,X):
		if self.flag == 1 or self.flag == 2:

			if X > self.x1 and X <= self.x2:
				self.pert = self.y1 + (self.y2 - self.y1)/(self.x2 - self.x1)*(X - self.x1)
			elif X > self.x2 and X <= self.x3:
				self.pert = self.y2 + (self.y3 - self.y2)/(self.x3 - self.x2)*(X - self.x2)
			elif X > self.x3 and X <= self.x4:
				self.pert = self.y3 + (self.y4 - self.y3)/(self.x4 - self.x3)*(X - self.x3)
			elif X <= self.x1:
				self.pert = self.y1
			elif X > self.x4:
				self.pert = self.y4

		if self.flag == 3:

			self.pert = exp(-1*(((X - self.media)*(X - self.media))/(2*self.dp*self.dp)))*(1/(self.dp*sqrt(2*pi)))








