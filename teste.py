from IMfuzzy2 import IMfuzzy2
from Mfunction import Mfunction
from Antescedent import Antescedent
from Consequent import Consequent
from Rule import Rule
from Rules import Rules

TRAP = 1
TRIA = 2
GAUS = 3

rules = Rules()



lower = Mfunction(TRIA,None,None,0,0,1.5,1,1.5,1,3,0)
upper = Mfunction(TRIA,None,None,0.5,0,1.5,1,1.5,1,2.5,0)
Baixa = IMfuzzy2(lower,upper)


lower = Mfunction(TRIA,None,None,2,0,3.5,1,3.5,1,5,0)
upper = Mfunction(TRIA,None,None,2.5,0,3.5,1,3.5,1,4.5,0)
Alta =  IMfuzzy2(lower,upper)

ant = Antescedent()
ant.addMf(Baixa,1)
cont = Consequent()
cont.addMf(Alta,1)
rule = Rule(ant,cont)
rules.addRule(rule)

ant = Antescedent()
ant.addMf(Alta,1)
cont = Consequent()
cont.addMf(Baixa,1)
rule = Rule(ant,cont)
rules.addRule(rule)
