import sys

from anonymizeSkype import anonymizeSkype
from anonymizePhone import anonymizePhone
from anonymizeEmail import anonymizeEmail

if (len(sys.argv) < 3):
	 print("Pass input and output file names to script as command line arguments!")
	 sys.exit(1)

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

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

	text = anonymizeSkype(text)
	text = anonymizePhone(text)
	text = anonymizeEmail(text)

	with open(outputFileName, "w") as outputFile:
		outputFile.write(text)
