import sys

from anonymizeSkype import anonymizeSkype
from anonymizePhone import anonymizePhone
from anonymizeEmail import anonymizeEmail

if (len(sys.argv) < 3):
	raise Error("Pass input and output file names to script as command line arguments!")

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

try:
	with open(inputFileName, "r") as inpuFile:
		pass
except FileNotFoundError:
	print("File not exist: ", inputFileName)
except OSError:
	print("Some error while opening file: ", inputFileName)

try:
	with open(outputFileName, "w") as outputFile:
		pass
except OSError:
	print("Some error while opening file: ", outputFileName)

with open(inputFileName, "r") as inpuFile:
	text = inpuFile.read()

	text = anonymizeSkype(text)
	text = anonymizePhone(text)
	text = anonymizeEmail(text)

	with open(outputFileName, "w") as outputFile:
		outputFile.write(text)
