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

from math import exp


class Mfunction:

    def __init__(
        self,
        flag=3,
        mean=None,
        dp=None,
        x1=None,
        x2=None,
        x3=None,
        x4=None,
        y1=None,
        y2=None,
        y3=None,
        y4=None,
        ):
        """ Creates a Membership function object (flag: Trapezoid = 1 ; Triangle = 2 ; Gaussian = 3)"""

        self.flag = flag
        self.stack = []
        if self.flag == 3:
            self.mean = mean
            self.dp = dp
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

    def setPertinence(self, X):
        """ Set internal pertinence for calculations """
        #val = 0.0
        if self.flag == 1 or self.flag == 2:

            if X > self.x1 and X <= self.x2:
                val = self.y1 + (self.y2 - self.y1) / (self.x2
                        - self.x1) * (X - self.x1)
            elif X > self.x2 and X <= self.x3:
                val = self.y2 + (self.y3 - self.y2) / (self.x3
                        - self.x2) * (X - self.x2)
            elif X > self.x3 and X <= self.x4:
                val = self.y3 + (self.y4 - self.y3) / (self.x4
                        - self.x3) * (X - self.x3)
            elif X <= self.x1:
                val = self.y1
            elif X >= self.x4:
                val = self.y4

        if self.flag == 3:
            val = exp(-1 * ((X - self.mean) * (X - self.mean)
                            / (2 * self.dp * self.dp)))
        if abs(1-val)<0.000001:
            val = 1.0
        if abs(val) < 0.000001:
            val = 0.0
        self.pert = val

    def addPert(self):
        """ Adds the resultant pertinence of a inference module to the output membeship function """
        #print(len(self.stack))
        if len(self.stack) == 0:
            #print('caiu aki',)
            self.stack = [0]
        m = 1
        for i in range(len(self.stack)):
            if self.stack[i] < m:
                m = self.stack[i]
        self.pert = m

    def getPertinence(self, X):
        """ Returns the pertinence for an input data """
        auxVal = 1.0
        if self.flag == 1 or self.flag == 2:

            if X > self.x1 and X <= self.x2:
                auxVal = self.y1 + (self.y2 - self.y1) / (self.x2
                        - self.x1) * (X - self.x1)
            elif X > self.x2 and X <= self.x3:
                auxVal = self.y2 + (self.y3 - self.y2) / (self.x3
                        - self.x2) * (X - self.x2)
            elif X > self.x3 and X <= self.x4:
                auxVal = self.y3 + (self.y4 - self.y3) / (self.x4
                        - self.x3) * (X - self.x3)
            elif X <= self.x1:
                auxVal = self.y1
            elif X > self.x4:
                auxVal = self.y4

        if self.flag == 3:
            auxVal = exp(-1 * ((X - self.mean) * (X - self.mean) / (2
                         * self.dp * self.dp)))
        #print(auxVal,"-",self.pert)
        if abs(1-auxVal)<0.000001:
            auxVal = 1.0
        if abs(auxVal) < 0.000001:
            auxVal = 0.0

        if auxVal < self.pert:
            return auxVal
        else:
            return self.pert



			
