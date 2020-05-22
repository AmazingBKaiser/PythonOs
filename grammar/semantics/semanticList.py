class SemanticList:
	semnatics = {}

	def __init__(self, s):
		self.semnatics = s

	def call(self, a, b, p):
		return self.semnatics[a].call(b, p)