from IMfuzzy2 import IMfuzzy2
from Mfunction import Mfunction
from Antescendet import Antescendet

TRAP = 1
TRIA = 2
GAUS = 3

lower = Mfunction(TRAP,None,None,0,0,2.5,1,5,1,5,1)
upper = Mfunction(TRAP,None,None,0,0,2.5,1,5,1,5,1)

Alta = IMfuzzy2(lower,upper)

Antescendet = Antescendet()
Antescendet.addMf(Alta)