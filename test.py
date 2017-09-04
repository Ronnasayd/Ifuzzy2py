from IMfuzzy2 import IMfuzzy2
from Mfunction import Mfunction
from Antescedent import Antescedent
from Consequent import Consequent
from Rule import Rule
from Rules import Rules
from Input import Input
from Output import Output
from Inputs import Inputs
from Outputs import Outputs
from Ifuzzy2 import Ifuzzy2

TRAP = 1
TRIA = 2
GAUS = 3

rules = Rules()



upperBI = Mfunction(TRIA,None,None,0,1,0,1,2,1,4,0)
lowerBI = Mfunction(TRIA,None,None,0,1,0,1,0,1,2,0)
BaixaI = IMfuzzy2(lowerBI,upperBI)


upperAI = Mfunction(TRIA,None,None,1,0,3,1,5,1,5,1)
lowerAI = Mfunction(TRIA,None,None,3,0,5,1,5,1,5,1)
AltaI =  IMfuzzy2(lowerAI,upperAI)

upperBO = Mfunction(TRIA,None,None,0,1,0,1,2,1,4,0)
lowerBO = Mfunction(TRIA,None,None,0,1,0,1,0,1,2,0)
BaixaO = IMfuzzy2(lowerBO,upperBO)


upperAO = Mfunction(TRIA,None,None,1,0,3,1,5,1,5,1)
lowerAO = Mfunction(TRIA,None,None,3,0,5,1,5,1,5,1)
AltaO =  IMfuzzy2(lowerAO,upperAO)

I = Input(0,5)
I.addMf(BaixaI)
I.addMf(AltaI)

O = Output(0,5)
O.addMf(BaixaO)
O.addMf(AltaO)

inputs = Inputs()
inputs.addInput(I)

outputs = Outputs()
outputs.addOutput(O)



ant = Antescedent()
ant.addMf(BaixaI)
cont = Consequent()
cont.addMf(AltaO)
rule = Rule(ant,cont)
rules.addRule(rule)

ant = Antescedent()
ant.addMf(AltaI)
cont = Consequent()
cont.addMf(BaixaO)
rule = Rule(ant,cont)
rules.addRule(rule)


fuzzy = Ifuzzy2(inputs,outputs,rules,1000)
for x in range(0,6):
	fuzzy.fuzzyfy([x])
	y = fuzzy.defuzzyfy(1)
	print(fuzzy.yl,fuzzy.yr,y)


print('fim')
