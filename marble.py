#************************************************
# marble.py
#
# Interpreter for the marble language.
# Aubrey Alston 2015
#************************************************

import lib.marble_parser as parser
import os.path
import sys

def main(file_location):
	# Open and read the file
	if not os.path.isfile(file_location):
		print_error("Specified file ("+file_location+") does not exist.")
		
	file = open(file_location)

	# Parse the file contents
	parsed = parser.parse(file.read())

	file.close

	print parsed

def print_error(message):
	''' Prints error and exits with non-zero exit code. '''
	print "Error: " + message
	sys.exit(1)

if len(sys.argv) < 2:
	print_error("No file specified.  Usage: marble [file]")

# Interpret the file
main(sys.argv[1])

