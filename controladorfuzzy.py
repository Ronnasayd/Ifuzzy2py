
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from IMfuzzy2 import IMfuzzy2
from Mfunction import Mfunction
from Antecedent import Antecedent
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

# FRONTAL
u1 = Mfunction(TRAP,None,None,0,0,0.153,0.3016, 1,1,1,0)
l1 = Mfunction(TRAP,None,None,0,0,0.153,0.2516, 1,1,1,0)
mpF = IMfuzzy2(l1, u1)

u2 = Mfunction(TRIA,None,None,0.1784,0.3122,0.3122,0.4344, 0,1,1,0)
l2 = Mfunction(TRIA,None,None,0.2284,0.3122,0.3122,0.3844, 0,1,1,0)
pF = IMfuzzy2(l2, u2)

u3 = Mfunction(TRIA,None,None,0.256,0.3989,0.3989,0.524, 0,1,1,0)
l3 = Mfunction(TRIA,None,None,0.306,0.3989,0.3989,0.474, 0,1,1,0)
mF = IMfuzzy2(l3, u3)

u4 = Mfunction(TRAP,None,None,0.384,0.512,0.8,0.8, 0,1,1,1)
l4 = Mfunction(TRAP,None,None,0.434,0.512,0.8,0.8, 0,1,1,1)
dF = IMfuzzy2(l4, u4)

# ESQUERDO
u5 = Mfunction(TRAP,None,None,0,0,0.128,0.256, 1,1,1,0)
l5 = Mfunction(TRAP,None,None,0,0,0.128,0.206, 1,1,1,0)
mpE = IMfuzzy2(l5, u5)

u6 = Mfunction(TRIA,None,None,0.128,0.256,0.256,0.384, 0,1,1,0)
l6 = Mfunction(TRIA,None,None,0.178,0.256,0.256,0.334, 0,1,1,0)
pE = IMfuzzy2(l6, u6)

u7 = Mfunction(TRIA,None,None,0.256,0.384,0.384,0.512, 0,1,1,0)
l7 = Mfunction(TRIA,None,None,0.306,0.384,0.384,0.462, 0,1,1,0)
mE = IMfuzzy2(l7, u7)

u8 = Mfunction(TRAP,None,None,0.384,0.512,0.8,0.8, 0,1,1,1)
l8 = Mfunction(TRAP,None,None,0.434,0.512,0.8,0.8, 0,1,1,1)
dE = IMfuzzy2(l8, u8)

# DIREITO
u9 = Mfunction(TRAP,None,None,0,0,0.128,0.256, 1,1,1,0)
l9 = Mfunction(TRAP,None,None,0,0,0.128,0.206, 1,1,1,0)
mpD = IMfuzzy2(l9, u9)

u10 = Mfunction(TRIA,None,None,0.128,0.256,0.256,0.384, 0,1,1,0)
l10 = Mfunction(TRIA,None,None,0.178,0.256,0.256,0.334, 0,1,1,0)
pD = IMfuzzy2(l10, u10)

u11 = Mfunction(TRIA,None,None,0.256,0.384,0.384,0.512, 0,1,1,0)
l11 = Mfunction(TRIA,None,None,0.306,0.384,0.384,0.462, 0,1,1,0)
mD = IMfuzzy2(l11, u11)

u12 = Mfunction(TRAP,None,None,0.384,0.512,0.8,0.8, 0,1,1,1)
l12 = Mfunction(TRAP,None,None,0.434,0.512,0.8,0.8, 0,1,1,1)
dD = IMfuzzy2(l12, u12)

# SAIDA RODA DIREITA
u13 = Mfunction(TRAP,None,None,0,0,1,2, 1,1,1,0)
l13 = Mfunction(TRAP,None,None,0,0,1,1.5,1,1,1,0)
muitoBaixaD = IMfuzzy2(l13, u13)

u14 = Mfunction(TRIA,None,None,1,2,2,3, 0,1,1,0)
l14 = Mfunction(TRIA,None,None,1.5,2,2,2.5, 0,1,1,0)
baixaD = IMfuzzy2(l14, u14)

u15 = Mfunction(TRIA,None,None,2,3,3,4, 0,1,1,0)
l15 = Mfunction(TRIA,None,None,2.5,3,3,3.5, 0,1,1,0)
mediaD = IMfuzzy2(l15, u15)

u16 = Mfunction(TRAP,None,None,3,4,5,5, 0,1,1,1)
l16 = Mfunction(TRAP,None,None,3.5,4,5,5, 0,1,1,1)
altaD = IMfuzzy2(l16, u16)

# SAIDA RODA ESQUERDA
u17 = Mfunction(TRAP,None,None,0,0,1,2, 1,1,1,0)
l17 = Mfunction(TRAP,None,None,0,0,1,1.5, 1,1,1,0)
muitoBaixaE = IMfuzzy2(l17, u17)

u18 = Mfunction(TRIA,None,None,1,2,2,3, 0,1,1,0)
l18 = Mfunction(TRIA,None,None,1.5,2,2,2.5, 0,1,1,0)
baixaE = IMfuzzy2(l18, u18)

u19 = Mfunction(TRIA,None,None,2,3,3,4, 0,1,1,0)
l19 = Mfunction(TRIA,None,None,2.5,3,3,3.5, 0,1,1,0)
mediaE = IMfuzzy2(l19, u19)

u20 = Mfunction(TRAP,None,None,3,4,5,5, 0,1,1,1)
l20 = Mfunction(TRAP,None,None,3.5,4,5,5, 0,1,1,1)
altaE = IMfuzzy2(l20, u20)

# ENTRADAS E SAIDAS

distanciaFrontal = Input(0, 0.8)
distanciaFrontal.addMf(mpF)
distanciaFrontal.addMf(pF)
distanciaFrontal.addMf(mF)
distanciaFrontal.addMf(dF)

distanciaEsquerda = Input(0, 0.8)
distanciaEsquerda.addMf(mpE)
distanciaEsquerda.addMf(pE)
distanciaEsquerda.addMf(mE)
distanciaEsquerda.addMf(dE)

distanciaDireita = Input(0, 0.8)
distanciaDireita.addMf(mpD)
distanciaDireita.addMf(pD)
distanciaDireita.addMf(mD)
distanciaDireita.addMf(dD)


velocidadeRodaEsquerda = Output(0, 5)
velocidadeRodaEsquerda.addMf(muitoBaixaE)
velocidadeRodaEsquerda.addMf(baixaE)
velocidadeRodaEsquerda.addMf(mediaE)
velocidadeRodaEsquerda.addMf(altaE)

velocidadeRodaDireita = Output(0, 5)
velocidadeRodaDireita.addMf(muitoBaixaD)
velocidadeRodaDireita.addMf(baixaD)
velocidadeRodaDireita.addMf(mediaD)
velocidadeRodaDireita.addMf(altaD)

inputs = Inputs()
inputs.addInput(distanciaFrontal)
inputs.addInput(distanciaEsquerda)
inputs.addInput(distanciaDireita)

outputs = Outputs()
outputs.addOutput(velocidadeRodaEsquerda)
outputs.addOutput(velocidadeRodaDireita)

# R1
ant1 = Antecedent()
ant1.addMf(mpF)
ant1.addMf(mpE)
ant1.addMf(mpD)
cont1 = Consequent()
cont1.addMf(muitoBaixaE)
cont1.addMf(altaD)
rule1 = Rule(ant1, cont1)
rules.addRule(rule1)
# R2
ant2 = Antecedent()
ant2.addMf(mpF)
ant2.addMf(mpE)
ant2.addMf(pD)
cont2 = Consequent()
cont2.addMf(muitoBaixaE)
cont2.addMf(altaD)
rule2 = Rule(ant2, cont2)
rules.addRule(rule2)
# R3
ant3 = Antecedent()
ant3.addMf(mpF)
ant3.addMf(mpE)
ant3.addMf(mD)
cont3 = Consequent()
cont3.addMf(muitoBaixaE)
cont3.addMf(altaD)
rule3 = Rule(ant3, cont3)
rules.addRule(rule3)
# R4
ant4 = Antecedent()
ant4.addMf(mpF)
ant4.addMf(mpE)
ant4.addMf(dD)
cont4 = Consequent()
cont4.addMf(muitoBaixaE)
cont = cont4.addMf(altaD)
rule4 = Rule(ant4, cont4)
rules.addRule(rule4)
# R5
ant5 = Antecedent()
ant5.addMf(mpF)
ant5.addMf(pE)
ant5.addMf(mpD)
cont5 = Consequent()
cont5.addMf(muitoBaixaE)
cont5.addMf(altaD)
rule5 = Rule(ant5, cont5)
rules.addRule(rule5)
# R6
ant6 = Antecedent()
ant6.addMf(mpF)
ant6.addMf(pE)
ant6.addMf(pD)
cont6 = Consequent()
cont6.addMf(muitoBaixaE)
cont6.addMf(altaD)
rule6 = Rule(ant6, cont6)
rules.addRule(rule6)
# R7
ant7 = Antecedent()
ant7.addMf(mpF)
ant7.addMf(pE)
ant7.addMf(mD)
cont7 = Consequent()
cont7.addMf(muitoBaixaE)
cont7.addMf(altaD)
rule7 = Rule(ant7, cont7)
rules.addRule(rule7)


# R8

ant8 = Antecedent()

ant8.addMf(mpF)

ant8.addMf(pE)

ant8.addMf(dD)

cont8 = Consequent()

cont8.addMf(muitoBaixaE)

cont8.addMf(altaD)

rule8 = Rule(ant8, cont8)

rules.addRule(rule8)

# R9

ant9 = Antecedent()

ant9.addMf(mpF)

ant9.addMf(mE)

ant9.addMf(mpD)

cont9 = Consequent()

cont9.addMf(muitoBaixaE)

cont9.addMf(altaD)

rule9 = Rule(ant9, cont9)

rules.addRule(rule9)

# R10

ant10 = Antecedent()

ant10.addMf(mpF)

ant10.addMf(mE)

ant10.addMf(pD)

cont10 = Consequent()

cont10.addMf(muitoBaixaE)

cont10.addMf(altaD)

rule10 = Rule(ant10, cont10)

rules.addRule(rule10)

# R11

ant11 = Antecedent()

ant11.addMf(mpF)

ant11.addMf(mE)

ant11.addMf(mD)

cont11 = Consequent()

cont11.addMf(muitoBaixaE)

cont11.addMf(altaD)

rule11 = Rule(ant11, cont11)

rules.addRule(rule11)

# R12

ant12 = Antecedent()

ant12.addMf(mpF)

ant12.addMf(mE)

ant12.addMf(dD)

cont12 = Consequent()

cont12.addMf(muitoBaixaE)

cont12.addMf(altaD)

rule12 = Rule(ant12, cont12)

rules.addRule(rule12)

# R13

ant13 = Antecedent()

ant13.addMf(mpF)

ant13.addMf(dE)

ant13.addMf(mpD)

cont13 = Consequent()

cont13.addMf(muitoBaixaE)

cont13.addMf(altaD)

rule13 = Rule(ant13, cont13)

rules.addRule(rule13)

# R14

ant14 = Antecedent()

ant14.addMf(mpF)

ant14.addMf(dE)

ant14.addMf(pD)

cont14 = Consequent()

cont14.addMf(muitoBaixaE)

cont14.addMf(altaD)

rule14 = Rule(ant14, cont14)

rules.addRule(rule14)

# R15

ant15 = Antecedent()

ant15.addMf(mpF)

ant15.addMf(dE)

ant15.addMf(mD)

cont15 = Consequent()

cont15.addMf(muitoBaixaE)

cont15.addMf(altaD)

rule15 = Rule(ant15, cont15)

rules.addRule(rule15)

# R16

ant16 = Antecedent()

ant16.addMf(mpF)

ant16.addMf(dE)

ant16.addMf(dD)

cont16 = Consequent()

cont16.addMf(muitoBaixaE)

cont16.addMf(altaD)

rule16 = Rule(ant16, cont16)

rules.addRule(rule16)

# R17

ant17 = Antecedent()

ant17.addMf(pF)

ant17.addMf(mpE)

ant17.addMf(mpD)

cont17 = Consequent()

cont17.addMf(muitoBaixaE)

cont17.addMf(altaD)

rule17 = Rule(ant17, cont17)

rules.addRule(rule17)

# R18

ant18 = Antecedent()

ant18.addMf(pF)

ant18.addMf(mpE)

ant18.addMf(pD)

cont18 = Consequent()

cont18.addMf(muitoBaixaE)

cont18.addMf(altaD)

rule18 = Rule(ant18, cont18)

rules.addRule(rule18)

# R19

ant19 = Antecedent()

ant19.addMf(pF)

ant19.addMf(mpE)

ant19.addMf(mD)

cont19 = Consequent()

cont19.addMf(mediaE)

cont19.addMf(altaD)

rule19 = Rule(ant19, cont19)

rules.addRule(rule19)

# R20

ant20 = Antecedent()

ant20.addMf(pF)

ant20.addMf(mpE)

ant20.addMf(dD)

cont20 = Consequent()

cont20.addMf(mediaE)

cont20.addMf(mediaD)

rule20 = Rule(ant20, cont20)

rules.addRule(rule20)

# R21

ant21 = Antecedent()

ant21.addMf(pF)

ant21.addMf(pE)

ant21.addMf(mpD)

cont21 = Consequent()

cont21.addMf(muitoBaixaE)

cont21.addMf(altaD)

rule21 = Rule(ant21, cont21)

rules.addRule(rule21)

# R22

ant22 = Antecedent()

ant22.addMf(pF)

ant22.addMf(pE)

ant22.addMf(pD)

cont22 = Consequent()

cont22.addMf(muitoBaixaE)

cont22.addMf(altaD)

rule22 = Rule(ant22, cont22)

rules.addRule(rule22)

# R23

ant23 = Antecedent()

ant23.addMf(pF)

ant23.addMf(pE)

ant23.addMf(mD)

cont23 = Consequent()

cont23.addMf(mediaE)

cont23.addMf(altaD)

rule23 = Rule(ant23, cont23)

rules.addRule(rule23)

# R24

ant24 = Antecedent()

ant24.addMf(pF)

ant24.addMf(pE)

ant24.addMf(dD)

cont24 = Consequent()

cont24.addMf(mediaE)

cont24.addMf(mediaD)

rule24 = Rule(ant24, cont24)

rules.addRule(rule24)

# R25

ant25 = Antecedent()

ant25.addMf(pF)

ant25.addMf(mE)

ant25.addMf(mpD)

cont25 = Consequent()

cont25.addMf(muitoBaixaE)

cont25.addMf(altaD)

rule25 = Rule(ant25, cont25)

rules.addRule(rule25)

# R26

ant26 = Antecedent()

ant26.addMf(pF)

ant26.addMf(mE)

ant26.addMf(pD)

cont26 = Consequent()

cont26.addMf(muitoBaixaE)

cont26.addMf(altaD)

rule26 = Rule(ant26, cont26)

rules.addRule(rule26)

# R27

ant27 = Antecedent()

ant27.addMf(pF)

ant27.addMf(mE)

ant27.addMf(mD)

cont27 = Consequent()

cont27.addMf(mediaE)

cont27.addMf(altaD)

rule27 = Rule(ant27, cont27)

rules.addRule(rule27)

# R28

ant28 = Antecedent()

ant28.addMf(pF)

ant28.addMf(mE)

ant28.addMf(dD)

cont28 = Consequent()

cont28.addMf(mediaE)

cont28.addMf(mediaD)

rule28 = Rule(ant28, cont28)

rules.addRule(rule28)

# R29

ant29 = Antecedent()

ant29.addMf(pF)

ant29.addMf(dE)

ant29.addMf(mpD)

cont29 = Consequent()

cont29.addMf(muitoBaixaE)

cont29.addMf(altaD)

rule29 = Rule(ant29, cont29)

rules.addRule(rule29)

# R30

ant30 = Antecedent()

ant30.addMf(pF)

ant30.addMf(dE)

ant30.addMf(pD)

cont30 = Consequent()

cont30.addMf(muitoBaixaE)

cont30.addMf(altaD)

rule30 = Rule(ant30, cont30)

rules.addRule(rule30)

# R31

ant31 = Antecedent()

ant31.addMf(pF)

ant31.addMf(dE)

ant31.addMf(mD)

cont31 = Consequent()

cont31.addMf(mediaE)

cont31.addMf(altaD)

rule31 = Rule(ant31, cont31)

rules.addRule(rule31)

# R32

ant32 = Antecedent()

ant32.addMf(pF)

ant32.addMf(dE)

ant32.addMf(dD)

cont32 = Consequent()

cont32.addMf(mediaE)

cont32.addMf(mediaD)

rule32 = Rule(ant32, cont32)

rules.addRule(rule32)

# R33

ant33 = Antecedent()

ant33.addMf(mF)

ant33.addMf(mpE)

ant33.addMf(mpD)

cont33 = Consequent()

cont33.addMf(baixaE)

cont33.addMf(mediaD)

rule33 = Rule(ant33, cont33)

rules.addRule(rule33)

# R34

ant34 = Antecedent()

ant34.addMf(mF)

ant34.addMf(mpE)

ant34.addMf(pD)

cont34 = Consequent()

cont34.addMf(mediaE)

cont34.addMf(mediaD)

rule34 = Rule(ant34, cont34)

rules.addRule(rule34)

# R35

ant35 = Antecedent()

ant35.addMf(mF)

ant35.addMf(mpE)

ant35.addMf(mD)

cont35 = Consequent()

cont35.addMf(mediaE)

cont35.addMf(baixaD)

rule35 = Rule(ant35, cont35)

rules.addRule(rule35)

# R36

ant36 = Antecedent()

ant36.addMf(mF)

ant36.addMf(mpE)

ant36.addMf(dD)

cont36 = Consequent()

cont36.addMf(altaE)

cont36.addMf(baixaD)

rule36 = Rule(ant36, cont36)

rules.addRule(rule36)

# R37

ant37 = Antecedent()

ant37.addMf(mF)

ant37.addMf(pE)

ant37.addMf(mpD)

cont37 = Consequent()

cont37.addMf(baixaE)

cont37.addMf(mediaD)

rule37 = Rule(ant37, cont37)

rules.addRule(rule37)

# R38

ant38 = Antecedent()

ant38.addMf(mF)

ant38.addMf(pE)

ant38.addMf(pD)

cont38 = Consequent()

cont38.addMf(mediaE)

cont38.addMf(mediaD)

rule38 = Rule(ant38, cont38)

rules.addRule(rule38)

# R39

ant39 = Antecedent()

ant39.addMf(mF)

ant39.addMf(pE)

ant39.addMf(mD)

cont39 = Consequent()

cont39.addMf(mediaE)

cont39.addMf(baixaD)

rule39 = Rule(ant39, cont39)

rules.addRule(rule39)

# R40

ant40 = Antecedent()

ant40.addMf(mF)

ant40.addMf(pE)

ant40.addMf(dD)

cont40 = Consequent()

cont40.addMf(altaE)

cont40.addMf(baixaD)

rule40 = Rule(ant40, cont40)

rules.addRule(rule40)

# R41

ant41 = Antecedent()

ant41.addMf(mF)

ant41.addMf(mE)

ant41.addMf(mpD)

cont41 = Consequent()

cont41.addMf(baixaE)

cont41.addMf(mediaD)

rule41 = Rule(ant41, cont41)

rules.addRule(rule41)

# R42

ant42 = Antecedent()

ant42.addMf(mF)

ant42.addMf(mE)

ant42.addMf(pD)

cont42 = Consequent()

cont42.addMf(mediaE)

cont42.addMf(mediaD)

rule42 = Rule(ant42, cont42)

rules.addRule(rule42)

# R43

ant43 = Antecedent()

ant43.addMf(mF)

ant43.addMf(mE)

ant43.addMf(mD)

cont43 = Consequent()

cont43.addMf(mediaE)

cont43.addMf(baixaD)

rule43 = Rule(ant43, cont43)

rules.addRule(rule43)

# R44

ant44 = Antecedent()

ant44.addMf(mF)

ant44.addMf(mE)

ant44.addMf(dD)

cont44 = Consequent()

cont44.addMf(altaE)

cont44.addMf(baixaD)

rule44 = Rule(ant44, cont44)

rules.addRule(rule44)

# R45

ant45 = Antecedent()

ant45.addMf(mF)

ant45.addMf(dE)

ant45.addMf(mpD)

cont45 = Consequent()

cont45.addMf(baixaE)

cont45.addMf(mediaD)

rule45 = Rule(ant45, cont45)

rules.addRule(rule45)

# R46

ant46 = Antecedent()

ant46.addMf(mF)

ant46.addMf(dE)

ant46.addMf(pD)

cont46 = Consequent()

cont46.addMf(mediaE)

cont46.addMf(mediaD)

rule46 = Rule(ant46, cont46)

rules.addRule(rule46)

# R47

ant47 = Antecedent()

ant47.addMf(mF)

ant47.addMf(dE)

ant47.addMf(mD)

cont47 = Consequent()

cont47.addMf(mediaE)

cont47.addMf(baixaD)

rule47 = Rule(ant47, cont47)

rules.addRule(rule47)

# R48

ant48 = Antecedent()

ant48.addMf(mF)

ant48.addMf(dE)

ant48.addMf(dD)

cont48 = Consequent()

cont48.addMf(altaE)

cont48.addMf(baixaD)

rule48 = Rule(ant48, cont48)

rules.addRule(rule48)

# R49

ant49 = Antecedent()

ant49.addMf(dF)

ant49.addMf(mpE)

ant49.addMf(mpD)

cont49 = Consequent()

cont49.addMf(baixaE)

cont49.addMf(baixaD)

rule49 = Rule(ant49, cont49)

rules.addRule(rule49)

# R50

ant50 = Antecedent()

ant50.addMf(dF)

ant50.addMf(mpE)

ant50.addMf(pD)

cont50 = Consequent()

cont50.addMf(mediaE)

cont50.addMf(mediaD)

rule50 = Rule(ant50, cont50)

rules.addRule(rule50)

# R51

ant51 = Antecedent()

ant51.addMf(dF)

ant51.addMf(mpE)

ant51.addMf(mD)

cont51 = Consequent()

cont51.addMf(mediaE)

cont51.addMf(baixaD)

rule51 = Rule(ant51, cont51)

rules.addRule(rule51)

# R52

ant52 = Antecedent()

ant52.addMf(dF)

ant52.addMf(mpE)

ant52.addMf(dD)

cont52 = Consequent()

cont52.addMf(altaE)

cont52.addMf(baixaD)

rule52 = Rule(ant52, cont52)

rules.addRule(rule52)

# R53

ant53 = Antecedent()

ant53.addMf(dF)

ant53.addMf(pE)

ant53.addMf(mpD)

cont53 = Consequent()

cont53.addMf(baixaE)

cont53.addMf(baixaD)

rule53 = Rule(ant53, cont53)

rules.addRule(rule53)

# R54

ant54 = Antecedent()

ant54.addMf(dF)

ant54.addMf(pE)

ant54.addMf(pD)

cont54 = Consequent()

cont54.addMf(mediaE)

cont54.addMf(mediaD)

rule54 = Rule(ant54, cont54)

rules.addRule(rule54)

# R55

ant55 = Antecedent()

ant55.addMf(dF)

ant55.addMf(pE)

ant55.addMf(mD)

cont55 = Consequent()

cont55.addMf(mediaE)

cont55.addMf(baixaD)

rule55 = Rule(ant55, cont55)

rules.addRule(rule55)

# R56

ant56 = Antecedent()

ant56.addMf(dF)

ant56.addMf(pE)

ant56.addMf(dD)

cont56 = Consequent()

cont56.addMf(altaE)

cont56.addMf(baixaD)

rule56 = Rule(ant56, cont56)

rules.addRule(rule56)

# R57

ant57 = Antecedent()

ant57.addMf(dF)

ant57.addMf(mE)

ant57.addMf(mpD)

cont57 = Consequent()

cont57.addMf(baixaE)

cont57.addMf(baixaD)

rule57 = Rule(ant57, cont57)

rules.addRule(rule57)

# R58

ant58 = Antecedent()

ant58.addMf(dF)

ant58.addMf(mE)

ant58.addMf(pD)

cont58 = Consequent()

cont58.addMf(mediaE)

cont58.addMf(mediaD)

rule58 = Rule(ant58, cont58)

rules.addRule(rule58)

# R59

ant59 = Antecedent()

ant59.addMf(dF)

ant59.addMf(mE)

ant59.addMf(mD)

cont59 = Consequent()

cont59.addMf(mediaE)

cont59.addMf(baixaD)

rule59 = Rule(ant59, cont59)

rules.addRule(rule59)

# R60

ant60 = Antecedent()

ant60.addMf(dF)

ant60.addMf(mE)

ant60.addMf(dD)

cont60 = Consequent()

cont60.addMf(altaE)

cont60.addMf(baixaD)

rule60 = Rule(ant60, cont60)

rules.addRule(rule60)

# R61

ant61 = Antecedent()

ant61.addMf(dF)

ant61.addMf(dE)

ant61.addMf(mpD)

cont61 = Consequent()

cont61.addMf(baixaE)

cont61.addMf(baixaD)

rule61 = Rule(ant61, cont61)

rules.addRule(rule61)

# R62

ant62 = Antecedent()

ant62.addMf(dF)

ant62.addMf(dE)

ant62.addMf(pD)

cont62 = Consequent()

cont62.addMf(mediaE)

cont62.addMf(mediaD)

rule62 = Rule(ant62, cont62)

rules.addRule(rule62)

# R63

ant63 = Antecedent()

ant63.addMf(dF)

ant63.addMf(dE)

ant63.addMf(mD)

cont63 = Consequent()

cont63.addMf(mediaE)

cont63.addMf(baixaD)

rule63 = Rule(ant63, cont63)

rules.addRule(rule63)

# R64

ant64 = Antecedent()

ant64.addMf(dF)

ant64.addMf(dE)

ant64.addMf(dD)

cont64 = Consequent()

cont64.addMf(altaE)

cont64.addMf(baixaD)

rule64 = Rule(ant64, cont64)

rules.addRule(rule64)





fuzzy = Ifuzzy2(inputs, outputs, rules, 200)



# mpE.setPertinence(0.203)
# pE.setPertinence(0.203)
# mE.setPertinence(0.203)
# dE.setPertinence(0.203)

# fuzzy.fuzzyfy([0,0.203,0])

# print(mpE.lower.pert,pE.lower.pert,mE.lower.pert,dE.lower.pert)
# print(mpE.upper.pert,pE.upper.pert,mE.upper.pert,dE.upper.pert)


# fuzzy.fuzzyfy([0.083,0.783,0.083])

# ye = fuzzy.defuzzyfy(1)
# yd = fuzzy.defuzzyfy(2)
# print(ye,':',yd)


for DF in range(0,9,1):

    for DE in range(0,9,1):

        for DD in range(0,9,1):

            fuzzy.fuzzyfy([DF/10,DE/10,DD/10])

            ye = fuzzy.defuzzyfy(1)
            #[yl, yr] = fuzzy.getReducedFuzzy(1)
            #print(yl,'--',yr)
            yd = fuzzy.defuzzyfy(2)

            print(DF/10,':',DE/10,':',DD/10,':',ye,':',yd)
