from ClocktailGenerator import ClocktailGenerator
from History import History
from ClocktailsCLOpts import CLOpts
import shelve

class InitFromArgs:
	def __init__(self, clopts):
		self.__args = clopts 
		self.shelfName = "clocktails.objs"
		self.shelfGen = "ctgen"
		self.shelfHist = "cthist"
		self.shelfVer = "ctver"

	def loadFile(self, name):
		strings = []
		with open(name) as f:
			for line in f:
				if line is not None and line != "":
					strings.append(line.replace("\n", ""))
		return strings

	def initFromScratch(self):
		#load files
		a = self.__args
		spiritStrings = self.loadFile(a[a.spiritNameOpt])
		mixerStrings = self.loadFile(a[a.mixerNameOpt])
		nameStrings = (self.loadFile(a[a.nameFilesOpt][0]), self.loadFile(a[a.nameFilesOpt][1]))
		spiritsRep = int(a[a.spiritsRepOpt])
		mixersRep = int(a[a.mixersRepOpt])
		clockGen = ClocktailGenerator(spiritStrings, spiritsRep, mixerStrings, mixersRep, nameStrings)

		# if history already exists don't destroy it
		history = History()
		s = shelve.open(self.shelfName)
		if self.shelfHist in s:
			history = s[self.shelfHist]
		s.close()

		return clockGen, history

	def initFromState(self):
		s = shelve.open(self.shelfName)
		ctgen = None
		cthist = None
		if self.shelfGen in s:
			ctgen = s[self.shelfGen]
		if self.shelfHist in s:
			cthist = s[self.shelfHist]
		s.close()
		return (ctgen, cthist)

	def saveState(self, clocktailsGen, history):
		s = shelve.open(self.shelfName)
		s[self.shelfGen] = clocktailsGen
		s[self.shelfHist] = history
		s[self.shelfVer] = "0.0.1"
		s.close()

	def initClockTails(self):
		clockTails = None
		a = self.__args
		if a[a.initOpt] == True:
			# initialise from scratch
			clockTails = self.initFromScratch()
		else:
			#initialise from stored state
			clockTails = self.initFromState()	
		return clockTails

