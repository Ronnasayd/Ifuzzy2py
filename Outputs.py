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
class Outputs:
	def __init__(self):
		""" Creates an Outputs object """
		self.output = []
		self.qtdOutput = 0
	def addOutput(self,output):
		""" Add Memership functions to an Outputs object, 
		and updates the amount of membership functions added to this object """
		self.output.append(output)
		self.qtdOutput = self.qtdOutput + 1