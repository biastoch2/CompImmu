class AminoAcids:
	def getHeader(self):
		return "A1 A2 A3 A4 A5 A6 A7 A8 A9".split(' ')

	def getFeatures(self, data_vector):
		return list(data_vector['aa'])