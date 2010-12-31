class Clocktail:
	def __init__(self, name, ingredients):
		self.__name = name
		self.__ingredients = ingredients
		self.__rating = -1.0
		self.__comment = None
		self.__dateGened = None

	def __str__(self):
		cstr = ""
		if self.__dateGened != None:
			cstr = cstr + self.__dateGened.ctime() + " - "
		cstr = cstr + self.nameString() + " contains " + self.ingredientsString()
		if self.__rating >= 0.0:
			if self.__rating==0.0:
				cstr = cstr + " Rating: Skipped"
			else:
				cstr = cstr + " Rating: " + str(self.__rating)
		if self.__comment != None and self.__comment != "":
			cstr = cstr + "\nComment: " + self.__comment
		return cstr

	def nameComponents(self):
		return self.__name

	def ingredients(self):
		return self.__ingredients

	def nameString(self):
		return " ".join(self.__name)
	def ingredientsString(self):
		return ", ".join(self.__ingredients[0:len(self.__ingredients)-1]) + " and " + self.__ingredients[-1]

	def nameHashString(self):
		return " ".join(sorted(map(lambda x: x.lower(), self.__name)))

	def ingredientsHashString(self):
		return " ".join(sorted(map(lambda x: x.lower(), self.__ingredients)))

	def rating(self):
		return self.__rating

	def rating(self, newrating):
		self.__rating = newrating

	def comment(self):
		return self.__comment

	def comment(self, comment):
		self.__comment = comment

	def datetime(self):
		return self.__dateGened

	def datetime(self, date):
		self.__dateGened = date

