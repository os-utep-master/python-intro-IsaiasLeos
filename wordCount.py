import os
import re
import sys

#Checks the amount of argument variables given when executing this program.
if len(sys.argv) is not 3:
    print("Usage: wordCount.py <input> <output>")
    exit()

#Assigns the following variables to the input and output files given when executing this program.
inputName = sys.argv[1]
outputName = sys.argv[2]
words = {}