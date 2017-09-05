from math import exp
class Mfunction:

	def __init__(self,flag=3,media=None,dp=None,x1=None,y1=None,x2=None,y2=None,x3=None,y3=None,x4=None,y4=None):
		""" Creates a Membership function object (flag: Trapezoid = 1 ; Triangle = 2 ; Gaussian = 3)"""
		self.flag = flag
		self.stack = []
		if self.flag == 3:
			self.media = media 
			self.dp  = dp 
			self.pert = None 
		else:
			self.x1 = x1 
			self.x2 = x2 
			self.x3 = x3 
			self.x4 = x4 
			self.y1 = y1 
			self.y2 = y2 
			self.y3 = y3 
			self.y4 = y4 
			self.pert = None 

	def setPertinence(self,X):
		""" Set internal pertinence for calculations """
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
			self.pert = exp(-1*(((X - self.media)*(X - self.media))/(2*self.dp*self.dp)))


	def addPert(self):
		""" Adds the resultant pertinence of a inference module to the output membeship function """
		m = 1
		for i in range(len(self.stack)):
			if self.stack[i] < m:
				m = self.stack[i]
		self.pert = m

	def getPertinence(self,X):
		""" Returns the pertinence for an input data """
		if self.flag == 1 or self.flag == 2:

			if X > self.x1 and X <= self.x2:
				auxVal = self.y1 + (self.y2 - self.y1)/(self.x2 - self.x1)*(X - self.x1)
			elif X > self.x2 and X <= self.x3:
				auxVal = self.y2 + (self.y3 - self.y2)/(self.x3 - self.x2)*(X - self.x2)
			elif X > self.x3 and X <= self.x4:
				auxVal = self.y3 + (self.y4 - self.y3)/(self.x4 - self.x3)*(X - self.x3)
			elif X <= self.x1:
				auxVal = self.y1
			elif X > self.x4:
				auxVal = self.y4

		if self.flag == 3:
			auxVal = exp(-1*(((X - self.media)*(X - self.media))/(2*self.dp*self.dp)))

		if auxVal < self.pert:
			return auxVal
		else:
			return self.pert









