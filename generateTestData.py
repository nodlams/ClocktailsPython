def generateFile(fname, prefix, numToGen):
	f = open(fname,"w")
	for i in range(0, numToGen):
		f.write(prefix + str(i) + "\n")
	f.close()

if __name__=="__main__":
	generateFile("spiritstest.txt", "spirit", 100)
	generateFile("mixerstest.txt", "mixer", 100)
	generateFile("nametest1.txt", "n1-", 100)
	generateFile("nametest2.txt", "n2-", 100)
