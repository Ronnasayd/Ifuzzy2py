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


class IMfuzzy2:

    def __init__(self, lower, upper):
        """ Creates a interval fuzzy type 2 membership function 
........with the lower and upper membership functions"""

        self.lower = lower
        self.upper = upper

    def setPertinence(self, X):
        """ Set the internal pertinence used in calculations of upper and lower 
........membership functions of a interval fuzzy type 2 membership function """

        self.lower.setPertinence(X)
        self.upper.setPertinence(X)

    def addPert(self):
        """ Adds pertinence of actived input membership functions in 
........inference module to the output membership functions """

        self.lower.addPert()
        self.upper.addPert()

    def resetstack(self):
        """ Resets the stack of actived membership functions in inference module """

        self.lower.stack = []
        self.upper.stack = []



			