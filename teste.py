from IMfuzzy2 import IMfuzzy2
from Mfunction import Mfunction

TRAP = 1
TRIA = 2
GAUS = 3

lower = Mfunction(TRAP,None,None,0,0,2.5,1,5,1,5,1)
upper = Mfunction(TRAP,None,None,0,0,2.5,1,5,1,5,1)

Alta = IMfuzzy2(lower,upper)
Alta.setPertinence(2)
print(Alta.lower.pert)
print(Alta.upper.pert)