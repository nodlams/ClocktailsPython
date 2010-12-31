from optparse import OptionParser
from CTException import CTException

class CLOpts:
	def __init__(self, args):
		self.__origargs = args
		self.__args = None
		self.__options = None
		self.initOpt = "initCT"
		self.genOpt = "genCT"
		self.spiritNameOpt = "spiritsFname"
		self.spiritsRepOpt = "spiritsRep"
		self.mixerNameOpt = "mixersFname"
		self.mixersRepOpt = "mixersRep"
		self.nameFilesOpt = "nameFnames"
		self.listPrevOpt = "listPrev"
		self.parseCLOpts()
		self.checkOpts()
	
	def parseCLOpts(self):
		parser = OptionParser()
		parser.add_option("-i", "--init", action="store_true", dest=self.initOpt, help="if present, clocktails initialises clocktail combinations from specified files")
		parser.add_option("-g", "--generate", action="store_true", dest=self.genOpt, help="if present, generate clocktail and request rating")
		parser.add_option("-l", "--list", action="store_true", dest=self.listPrevOpt, help="List all previously generated clocktails")
		parser.add_option("-s", "--spirits", dest=self.spiritNameOpt, help="The text file containing spirits")
		parser.add_option("-r", "--repeatspirits", dest=self.spiritsRepOpt, help="How many spirits to put in each clocktail")
		parser.add_option("-m", "--mixers", dest=self.mixerNameOpt, help="The text file containing mixers")
		parser.add_option("-q", "--repeatmixers", dest=self.mixersRepOpt, help="How many mixers to put in each clocktail")
		parser.add_option("-n", "--name", dest=self.nameFilesOpt, nargs=2, help="The 2 text files containing the name strings") 
		(options, args) = parser.parse_args(self.__origargs)
		self.__options = vars(options)
		self.__args = args

	def checkOpts(self):
		if self[self.initOpt] == True:
			sn = self[self.spiritNameOpt]
			mn = self[self.mixerNameOpt]
			nf = self[self.nameFilesOpt]
			ns = self[self.spiritsRepOpt]
			nm = self[self.mixersRepOpt]
			if sn == None or mn == None or nf == None or ns == None or nm == None:
				raise CTException("-s -r -m -q -n must all be specified for initialisation")

	def __getitem__(self, key):
		return self.__options[key]
