class Card:

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return self.value

	def getVal(self):
		return self.value

	def CardSuit(self):
		return self.value[-1]

	# Technically does not return correctly for 10, but 10 doesn't trigger anything worthwhile for this program so that
	# issue is ignored
	def CardValue(self):
		return self.value[0]
