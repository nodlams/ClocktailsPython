""" Main module for clocktails 29/12/10 """
import sys
import traceback
from InitFromArgs import InitFromArgs
from optparse import OptionParser
from Messages import logMessage
from History import History
from ClocktailsCLOpts import CLOpts
from CTException import CTException

def handleNewGenerator(clocktailsGen, history):
	logMessage("initialising clocktails generator")
	clocktailsGen.removeAlreadyGenerated(history)

def handleGenerateCT(clocktailsGen, history):
	c = clocktailsGen.getNextClocktail().next()
	print c
	done = False
	ratInt = -1

	while not done:
		try:
			ratStr = raw_input("Enter rating 1-10 (Enter to skip): ") 
			done = False
			if ratStr == "":
				done = True
				ratInt = 0
			else:
				ratInt = int(ratStr)
				if ratInt >= 1 or ratInt <= 10:
					done = True
		except:
			pass

	comStr = raw_input("Enter comment (enter to skip): ")
	c.rating(float(ratInt))
	c.comment(comStr)
	history.addClocktail(c)
	print "There are " + str(clocktailsGen.numDrinksLeft()) + " unique drinks and " + str(clocktailsGen.numNamesLeft()) + " unique names remaining"

def handleListPrevious(history):
	previous = history.previouslyGeneratedClocktails()
	for p in previous:
		print str(p)
	
def doSomething(clocktailsGen, history, clopts):
	if clopts[clopts.initOpt] == True:
		#cut down new clocktails gen based on history
		handleNewGenerator(clocktailsGen, history)
	elif clopts[clopts.genOpt] == True:
		handleGenerateCT(clocktailsGen, history)
	elif clopts[clopts.listPrevOpt] == True:
		handleListPrevious(history)

def main(args):
	# Set everything up
	try:
		clopts = CLOpts(args)
		initialiser = InitFromArgs(clopts)
		(clocktailsGen, history) = initialiser.initClockTails()

		if clocktailsGen == None or history == None:
			raise CTException("initialise the generator with spirits, mixers, names etc first")

		doSomething(clocktailsGen, history, clopts)

		#store resulting generator and history to disk
		initialiser.saveState(clocktailsGen, history)		
	except StopIteration as e:
		print "Error: ran out of unique recipes or names"
		print "There are " + str(clocktailsGen.numDrinksLeft()) + " unique drinks and " + str(clocktailsGen.numNamesLeft()) + " unique names remaining"
	except CTException as e:
		print "Error: " + str(e)
		print "See help for more info (-h)"
	except Exception as e:
		print "Unexpected error: " + str(e)
		traceback.print_exc(file=sys.stdout)
		

if __name__=="__main__":
	main(sys.argv[1:])
