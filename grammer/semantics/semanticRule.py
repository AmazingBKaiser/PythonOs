class SemanticRule:
	symbol = ""
	func = ""
	operands = 0

	def __init__(self, symbol, func, operands):
		self.symbol = symbol
		self.func = func
		self.operands = operands

	def __str__(self):
		s = self.symbol + " = " + self.func + "(" + str(self.operands) + ")"
		return s
