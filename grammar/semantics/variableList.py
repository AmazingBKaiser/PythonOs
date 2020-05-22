class VariableList:
	variables = {}

	def __init__(self, v):
		self.variables = v

	def call(self, a, p):
		return variables[a]

	def add(self, a, v):
		variables[a] = v