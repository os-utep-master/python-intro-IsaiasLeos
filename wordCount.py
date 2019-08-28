import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists


#Checks the amount of argument variables given when executing this program.
if len(sys.argv) is not 3:
    print("Usage: wordCount.py <input> <output>")
    exit()

#Assigns the following variables to the input and output files given when executing this program.
inputName = sys.argv[1]
outputName = sys.argv[2]
words = {}

#Checks if the following output file exists
if not os.path.exists(outputName):
    print("Output %s file doesn't exist! Terminating..." % outputName)
    exit()

with open(inputName,'r') as words:
    for line in words:
        print(line)