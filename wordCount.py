import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

# Save argument to variables
inputName = sys.argv[1]
outputName = sys.argv[2]
wordDictionary = {}

# Checks if the following output.txt file exists
if not os.path.exists(outputName):
    print("File output.txt %s doesn't exist! Terminating..." % outputName)
    exit() #Exit program

with open(inputName, 'r') as input:  # Read the file
    for line in input:  # Assign each line from 'input' into the variable 'line'

        # Remove punctuation and make sentence lowercase
        line = re.sub('[^A-Za-z]+', ' ', line).lower()

        # Split the 'line' variable by blank spaces
        line = line.split(' ')

        # Iterate through each line and check if the word is in the dictionary
        for word in line:
            # Increase word count in dictionary
            if word in wordDictionary:
                wordDictionary[word] += 1
            else:
                # Add word to dictionary
                wordDictionary[word] = 1

wordDictionary.pop('') # Pop unexpected word empty space in dictionary
output = open(outputName,'a+') # Open file to write to in 'appending mode'
for key in sorted(wordDictionary): # Iterate through a sorted dictionary
    output.write(key + ' ' + str(wordDictionary[key]) + "\n") # Write to file in a correct format
output.close() # Close opened file