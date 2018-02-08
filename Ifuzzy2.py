#!/usr/bin/python
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


class Ifuzzy2:

    def __init__(
        self,
        inputs=[],
        outputs=[],
        rules=[],
        N=1000,
        ):
        """ Creates a fuzzy object """

        self.inputs = inputs
        self.outputs = outputs
        self.rules = rules
        self.N = N
        self.yal = []
        self.yar = []

    def fuzzyfication(self, X):
        """ Makes the fuzzyfication step for the vector input"""

        lx = len(X)
        if lx == self.inputs.qtdInput:
            for i in range(lx):
                for j in range(self.inputs.input[i].qtdMf):
                    self.inputs.input[i].Mf[j].setPertinence(X[i])

    def inference(self):
        """ Makes the inference step """

        for i in range(self.rules.qtdRule):
            maxLower = 0
            maxUpper = 0
            #auxL = []
            #auxU = []
            for j in range(self.rules.rule[i].antecedent.qtdMf):
                #auxL.append(self.rules.rule[i].antecedent.Mf[j].lower.pert)
                #auxU.append(self.rules.rule[i].antecedent.Mf[j].upper.pert)
                if self.rules.rule[i].antecedent.Mf[j].lower.pert > maxLower:
                    maxLower = self.rules.rule[i].antecedent.Mf[j].lower.pert
                if self.rules.rule[i].antecedent.Mf[j].upper.pert > maxUpper:
                    maxUpper = self.rules.rule[i].antecedent.Mf[j].upper.pert
            #print(i,auxL)
            #print(i,auxU)
            for k in range(self.rules.rule[i].consequent.qtdMf):
                self.rules.rule[i].consequent.Mf[k].lower.stack.append(maxLower)
                self.rules.rule[i].consequent.Mf[k].upper.stack.append(maxUpper)
        #print('[+]-------------------------------------------------------------------[+]')
            #print([i,maxUpper,maxLower])
            #print(self.rules.rule[i].consequent.Mf[0].lower.stack)
        for i in range(self.outputs.qtdOutput):
            for j in range(self.outputs.output[i].qtdMf):
                #print(i,j,self.outputs.output[i].Mf[j].lower.stack)
                self.outputs.output[i].Mf[j].addPert()
                self.outputs.output[i].Mf[j].resetstack()
                #print(i,j,self.outputs.output[i].Mf[j].lower.stack)

    def typeReduction(self):
        """ Makes the type reduction step with the Karnik and Mendel algorithm """
        self.yal = []
        self.yar = []
        for i in range(self.outputs.qtdOutput):
            points = []
            lower = []
            upper = []
            interation = (self.outputs.output[i].end
                          - self.outputs.output[i].init) / self.N

            # print('interation',interation)

            num = 0
            den = 5e-324
            point = self.outputs.output[i].init
            for j in range(self.N + 1):
                points.append(point)
                auxlower = []
                auxupper = []
                for k in range(self.outputs.output[i].qtdMf):
                    auxlower.append(self.outputs.output[i].Mf[k].lower.getPertinence(point))
                    auxupper.append(self.outputs.output[i].Mf[k].upper.getPertinence(point))
                    #print(i,k,self.outputs.output[0].Mf[k].lower.getPertinence(point),self.outputs.output[1].Mf[k].lower.getPertinence(point))

                l = max(auxlower)
                lower.append(l)
                u = max(auxupper)
                upper.append(u)

                # print('ponto',point,'max_lower',l,'max_upper',u)

                den = den + (l + u) / 2
                num = num + (l + u) / 2 * point

                point = point + interation
            ykGeneral = num / den

            # print(yk)

            for k in range(1, self.N + 1):
                if points[k] >= ykGeneral:
                    delimiterGeneral = k - 1
                    break

            yk = ykGeneral
            delimiter = delimiterGeneral

            #print(yk,':',delimiter)

            while True:
                num = 0
                den = 5e-324

                # print('yl:',points[delimiter],yk,points[delimiter+1],delimiter)

                for k in range(delimiter + 1):
                    num = num + points[k] * upper[k]
                    den = den + upper[k]

                for k in range(delimiter + 1, self.N + 1):
                    num = num + points[k] * lower[k]
                    den = den + lower[k]

                yl = num / den

                #print(yl,yk,delimiter)

                if abs(yl - yk) < 0.001:
                    #print(yl)
                    self.yal.append(yl)
                    #print(i,self.yal)
                    break
                else:
                    yk = yl
                    for k in range(1, self.N + 1):
                        if points[k] >= yk:
                            delimiter = k - 1
                            break

            yk = ykGeneral
            delimiter = delimiterGeneral

            #print(yk,delimiter)

            while True:
                num = 0
                den = 5e-324
                for k in range(delimiter + 1):
                    print(k,':',delimiter+1)
                    num = num + points[k] * lower[k]
                    den = den + lower[k]

                for k in range(delimiter + 1, self.N + 1):
                    print(k,':',self.N + 1)
                    num = num + points[k] * upper[k]
                    den = den + upper[k]

                yr = num / den

                # print(yr,yk,delimiter)

                if abs(yr - yk)<0.001:
                    self.yar.append(yr)
                    break
                else:
                    yk = yr
                    for k in range(1, self.N + 1):
                        if points[k] >= yk:
                            delimiter = k - 1
                            break

    def getReducedFuzzy(self, ind):
        """ Returns the reduced fuzzy values for the karnik mendel algorithm """

        return [self.yal[ind - 1], self.yar[ind - 1]]

    def defuzzyfication(self, ind):
        """ Makes the defuzzyfication step """

        return (self.yal[ind - 1] + self.yar[ind - 1]) / 2

    def fuzzyfy(self, X):
        """ Makes the fuzzyfication and inference steps """

        self.fuzzyfication(X)
        self.inference()

    def defuzzyfy(self, ind):
        """ Makes the type reduction and defuzzyfication steps """

        self.typeReduction()
        return self.defuzzyfication(ind)



			
