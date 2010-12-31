from Combinator import Combinator
from WordSet import WordSet
from Clocktail import Clocktail

class ClocktailGenerator:
	def __init__(self, spirits, repSpirits, mixers, repMixers, names):
		self.__namesCombinations = Combinator([WordSet(names[0],1), WordSet(names[1], 1)])
		self.__drinksCombinations = Combinator([WordSet(spirits, repSpirits), WordSet(mixers, repMixers)])

	def removeAlreadyGenerated(self, history):
		doneNames = history.getGeneratedNames()
		self.__namesCombinations.remove(doneNames)
		doneDrinks = history.getGeneratedIngredients()
		self.__drinksCombinations.remove(doneDrinks)
	
	def getNextClocktail(self):
		nameGen = self.__namesCombinations.iterateRandomly()	
		ctGen = self.__drinksCombinations.iterateRandomly()
		finished = False
		while not finished:
			try:
				nextName = nameGen.next()
				nextCt = ctGen.next()
			except:
				finished = True 
			if not finished:
				yield Clocktail(nextName, nextCt)

	def numDrinksLeft(self):
		return self.__drinksCombinations.numLeft()

	def numNamesLeft(self):
		return self.__namesCombinations.numLeft()
