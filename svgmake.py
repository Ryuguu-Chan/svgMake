# for parsing the command line arguments
import sys

# for usijg
import os.path

# for computing all thr magic
import include.CONST

# for computing things
import include.COM

# sys.argv[1] -> the source code's filename
# sys.argv[2] -> 
if len(sys.argv) == 2:
	
	# checking wether the file (argv[1]) exists or not
	if os.path.isfile(sys.argv[1]):
		print("computing the file's content...")
		
		# getting the file content in the memory
		fileContent  = open(sys.argv[1], 'r').read()
		
		# removing all the unecessary characters
		# this is done in order to save up memory
		fileContent = fileContent.replace('\n', '') # the newline char
		fileContent = fileContent.replace('\t', '') # the tabulation char
		
		# TODO: Planning/Designing our programming language
	else:
		print(sys.argv[1] + " not found")
else:
	print("here's the syntax\n\npython svgmake.py [*.svcode source code filename] [*.svg output filename]")