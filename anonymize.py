import sys
import re

from anonymizeSkype import anonymizeSkype
from anonymizePhone import anonymizePhone
from anonymizeEmail import anonymizeEmail

if (len(sys.argv) < 4):
	print("Pass command, input and output file names to script as command line arguments!")
	print("For example: python3 ep i.txt o.txt")
	sys.exit(1)

anonymizeCommand = sys.argv[1]

if(re.search("[^eps]", anonymizeCommand) != None):
	print("Unknown commands, use one of e, p, s or their combination.")
	sys.exit(1)

inputFileName = sys.argv[2]
outputFileName = sys.argv[3]

try:
	with open(inputFileName, "r") as inpuFile:
		pass
except FileNotFoundError:
	print("File not exist: ", inputFileName)
	sys.exit(1)
except OSError:
	print("Some error while opening file: ", inputFileName)
	sys.exit(1)

try:
	with open(outputFileName, "w") as outputFile:
		pass
except OSError:
	print("Some error while opening file: ", outputFileName)
	sys.exit(1)

with open(inputFileName, "r") as inpuFile:
	text = inpuFile.read()

	if(re.search("[e]", anonymizeCommand) != None):
		text = anonymizeEmail(text)
	if(re.search("[s]", anonymizeCommand) != None):
			text = anonymizeSkype(text)
	if(re.search("[p]", anonymizeCommand) != None):
		text = anonymizePhone(text)

	with open(outputFileName, "w") as outputFile:
		outputFile.write(text)
