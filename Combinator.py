from WordSet import WordSet
from random import randint

class Combinator:
	""" takes a list of type [WordSet] """
	def __init__(self, wordsets):
		self.__allCombis = self.generateAllCombinations(wordsets)

	def generateAllCombinations(self, wordsets):
		return self.generateCombisInner(0, wordsets, [])	

	def generateCombisRepeats(self, wordset, index, currentArray, numRepeats):
		newCombisRep = []
		if (numRepeats == 1):
			for i in range(index, len(wordset)):
				nextVal = currentArray[:]
				nextVal.append(wordset[i])
				newCombisRep.append(nextVal)
		else:
			for i in range(index, len(wordset)):
				newArray = currentArray[:]
				newArray.append(wordset[i])
				newCombisRep.extend(self.generateCombisRepeats(wordset, i+1, newArray, numRepeats-1))
		return newCombisRep

	def generateCombisInner(self, index, wordsets, currentArray):
		newCombis = []
		if (index == (len(wordsets) - 1)):
			for w in self.generateCombisRepeats(wordsets[index], 0, [], wordsets[index].repeats()):
				nextVal = currentArray[:]
				nextVal.extend(w)
				newCombis.append(nextVal)
		else:
			for w in self.generateCombisRepeats(wordsets[index], 0, [], wordsets[index].repeats()):
				newArray = currentArray[:]
				newArray.extend(w)
				newCombis.extend(self.generateCombisInner(index+1, wordsets, newArray))
		return newCombis

	def iterateInOrder(self):
		for l in self.__allCombis:
			yield l

	def iterateRandomly(self):
		# generate a new copy of the list of combinations and remove things randomly from it.
		while len(self.__allCombis) > 0:
			index = randint(0, len(self.__allCombis)-1)
			val = self.__allCombis[index]
			del self.__allCombis[index]
			yield val

	def remove(self, items):
		combihash = {}
		for c in enumerate(self.__allCombis):
			combihash[" ".join(sorted(map(lambda x: x.lower(), c[1])))] = c[0]
		toremove = []
		for i in items:
			if i in combihash:
				toremove.append(combihash[i])
		self.__allCombis = [i for j,i in enumerate(self.__allCombis) if j not in toremove]

	def numLeft(self):
		return len(self.__allCombis)

if __name__=="__main__":
	ws1 = WordSet(["test1","test2","test3","test4"],1)
	ws2 = WordSet(["ant","bear","cub"],1)
	ws3 = WordSet(["d","e","f"],1)
	combi = Combinator([ws1,ws2])	

#	print "InnerCombisTest"
#	innerset = combi.generateCombisRepeats(ws1, 0, [], 3)
#	print innerset

#	print "AllCombisTest"
#	print list(combi.iterateInOrder())

#	print "RandomCombisTest"
#	print list(combi.iterateRandomly())
