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


class Rules:

    def __init__(self):
        """ Creates a rules object """

        self.rule = []
        self.qtdRule = 0

    def addRule(self, rule):
        """ Add Rule object to a Rules object, 
........and updates the amount of rules added to this object """

        self.rule.append(rule)
        self.qtdRule = self.qtdRule + 1



			