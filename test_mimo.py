#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Copyright 2017 Ronnasayd Machado <ronnasayd@hotmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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

upperBI1 = Mfunction(
    TRIA,
    None,
    None,
    0,
    1,
    0,
    1,
    2,
    1,
    4,
    0,
    )
lowerBI1 = Mfunction(
    TRIA,
    None,
    None,
    0,
    1,
    0,
    1,
    0,
    1,
    2,
    0,
    )
BaixaI1 = IMfuzzy2(lowerBI1, upperBI1)

upperAI1 = Mfunction(
    TRIA,
    None,
    None,
    1,
    0,
    3,
    1,
    5,
    1,
    5,
    1,
    )
lowerAI1 = Mfunction(
    TRIA,
    None,
    None,
    3,
    0,
    5,
    1,
    5,
    1,
    5,
    1,
    )
AltaI1 = IMfuzzy2(lowerAI1, upperAI1)

upperBO1 = Mfunction(
    TRIA,
    None,
    None,
    0,
    1,
    0,
    1,
    2,
    1,
    4,
    0,
    )
lowerBO1 = Mfunction(
    TRIA,
    None,
    None,
    0,
    1,
    0,
    1,
    0,
    1,
    2,
    0,
    )
BaixaO1 = IMfuzzy2(lowerBO1, upperBO1)

upperAO1 = Mfunction(
    TRIA,
    None,
    None,
    1,
    0,
    3,
    1,
    5,
    1,
    5,
    1,
    )
lowerAO1 = Mfunction(
    TRIA,
    None,
    None,
    3,
    0,
    5,
    1,
    5,
    1,
    5,
    1,
    )
AltaO1 = IMfuzzy2(lowerAO1, upperAO1)

I1 = Input(0, 5)
I1.addMf(BaixaI1)
I1.addMf(AltaI1)

O1 = Output(0, 5)
O1.addMf(BaixaO1)
O1.addMf(AltaO1)
#####################################################################################################################
upperBI2 = Mfunction(
    TRIA,
    None,
    None,
    0,
    1,
    0,
    1,
    2,
    1,
    4,
    0,
    )
lowerBI2 = Mfunction(
    TRIA,
    None,
    None,
    0,
    1,
    0,
    1,
    0,
    1,
    2,
    0,
    )
BaixaI2 = IMfuzzy2(lowerBI2, upperBI2)

upperAI2 = Mfunction(
    TRIA,
    None,
    None,
    1,
    0,
    3,
    1,
    5,
    1,
    5,
    1,
    )
lowerAI2 = Mfunction(
    TRIA,
    None,
    None,
    3,
    0,
    5,
    1,
    5,
    1,
    5,
    1,
    )
AltaI2 = IMfuzzy2(lowerAI2, upperAI2)

upperBO2 = Mfunction(
    TRIA,
    None,
    None,
    0,
    1,
    0,
    1,
    2,
    1,
    4,
    0,
    )
lowerBO2 = Mfunction(
    TRIA,
    None,
    None,
    0,
    1,
    0,
    1,
    0,
    1,
    2,
    0,
    )
BaixaO2 = IMfuzzy2(lowerBO2, upperBO2)

upperAO2 = Mfunction(
    TRIA,
    None,
    None,
    1,
    0,
    3,
    1,
    5,
    1,
    5,
    1,
    )
lowerAO2 = Mfunction(
    TRIA,
    None,
    None,
    3,
    0,
    5,
    1,
    5,
    1,
    5,
    1,
    )
AltaO2 = IMfuzzy2(lowerAO2, upperAO2)

I2 = Input(0, 5)
I2.addMf(BaixaI2)
I2.addMf(AltaI2)

O2 = Output(0, 5)
O2.addMf(BaixaO2)
O2.addMf(AltaO2)

##################################################################################
inputs = Inputs()
inputs.addInput(I1)
inputs.addInput(I2)

outputs = Outputs()
outputs.addOutput(O1)
outputs.addOutput(O2)

ant1 = Antecedent()
ant1.addMf(BaixaI1)
cont1 = Consequent()
cont1.addMf(AltaO1)
rule1 = Rule(ant1, cont1)
rules.addRule(rule1)

ant2 = Antecedent()
ant2.addMf(AltaI1)
cont2 = Consequent()
cont2.addMf(BaixaO1)
rule2 = Rule(ant2, cont2)
rules.addRule(rule2)

ant3 = Antecedent()
ant3.addMf(BaixaI2)
cont3 = Consequent()
cont3.addMf(AltaO2)
rule3 = Rule(ant3, cont3)
rules.addRule(rule3)

ant4 = Antecedent()
ant4.addMf(AltaI2)
cont4 = Consequent()
cont4.addMf(BaixaO2)
rule4 = Rule(ant4, cont4)
rules.addRule(rule4)

fuzzy = Ifuzzy2(inputs, outputs, rules,100)
for x in range(0, 6):
    for z in range(0, 6):
        fuzzy.fuzzyfy([x,z])
        y1 = fuzzy.defuzzyfy(1)
        #[yl1, yr1] = fuzzy.getReducedFuzzy(1)
        #print (yl1,":",yr1,":",y1)
        y2 = fuzzy.defuzzyfy(2)
        #[yl2, yr2] = fuzzy.getReducedFuzzy(2)
        #print (yl2,":",yr2,":",y2)

        print(x,z,y1,y2)


            
