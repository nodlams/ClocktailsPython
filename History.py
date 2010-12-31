""" Stores and manages list of clocktails which have already been generated, with associated scores """
from Messages import logMessage
from datetime import datetime

class History:
	def __init__(self):
		self.__generatedClocktails = []
		self.__nameToClocktail = {}
		self.__ingredientsToClocktail = {} 

	def addClocktail(self, clocktail):
		now = datetime.now()
		clocktail.datetime(now)
		self.__generatedClocktails.append(clocktail)
		self.__nameToClocktail[clocktail.nameHashString()] = clocktail
		self.__ingredientsToClocktail[clocktail.ingredientsHashString()] = clocktail
	
	def getGeneratedNames(self):
		return self.__nameToClocktail.keys()

	def getGeneratedIngredients(self):
		return self.__ingredientsToClocktail.keys()

	def previouslyGeneratedClocktails(self):
		return self.__generatedClocktails
