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



upperBI = Mfunction(TRIA,None,None,0,0,1.5,1,1.5,1,3,0)
lowerBI = Mfunction(TRIA,None,None,0.5,0,1.5,1,1.5,1,2.5,0)
BaixaI = IMfuzzy2(lowerBI,upperBI)


upperAI = Mfunction(TRIA,None,None,2,0,3.5,1,3.5,1,5,0)
lowerAI = Mfunction(TRIA,None,None,2.5,0,3.5,1,3.5,1,4.5,0)
AltaI =  IMfuzzy2(lowerAI,upperAI)

upperBO = Mfunction(TRIA,None,None,0,0,1.5,1,1.5,1,3,0)
lowerBO = Mfunction(TRIA,None,None,0.5,0,1.5,1,1.5,1,2.5,0)
BaixaO = IMfuzzy2(lowerBO,upperBO)


upperAO = Mfunction(TRIA,None,None,2,0,3.5,1,3.5,1,5,0)
lowerAO = Mfunction(TRIA,None,None,2.5,0,3.5,1,3.5,1,4.5,0)
AltaO =  IMfuzzy2(lowerAO,upperAO)

I = Input()
I.addMf(BaixaI)
I.addMf(AltaI)

O = Output()
O.addMf(BaixaO)
O.addMf(AltaO)

inputs = Inputs()
inputs.addInput(I)

outputs = Outputs()
outputs = addOutput(O)



ant = Antescedent()
ant.addMf(BaixaI,1)
cont = Consequent()
cont.addMf(AltaO,1)
rule = Rule(ant,cont)
rules.addRule(rule)

ant = Antescedent()
ant.addMf(AltaI,1)
cont = Consequent()
cont.addMf(BaixaO,1)
rule = Rule(ant,cont)
rules.addRule(rule)


fuzzy = Ifuzzy2(inputs,outputs,rules,1000)
fuzzy.fuzzyfication([2.6])
fuzzy.inference()