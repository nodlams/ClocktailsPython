class WordSet:
	""" initialise the wordset with a list of strings """
	def __init__(self, words, timesRepeated):
		self.__wordList = words
		self.__repeat = timesRepeated

	def next(self):
		for i in range(0, len(self.__wordList)):
			yield self.__wordList[i]
	def __iter__(self):
		return self.next()
	""" The number of times that this wordset should be repeated to generated all the combinations """
	def repeats(self):
		return self.__repeat

	def __len__(self):
		return len(self.__wordList)

	def __getitem__(self, index):
		return self.__wordList[index]

if __name__=="__main__":
	testlist = WordSet(["a","b","c","d","e", "f", "g"],3)
	for t in testlist:
		print t
	for t in testlist:
		print t
	print "Number of times to repeat is: " + str(testlist.repeat())
