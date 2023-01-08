import sys

from Textwriter import Textwriter

if __name__ == '__main__':

	writer = None
	
	if len(sys.argv) == 2:
		
		topic = sys.argv[1]
		writer = Textwriter(topic)

	elif len(sys.argv) > 2:

		topic = sys.argv[1]
		lineCount = sys.argv[2]

		writer = Textwriter(topic,lineCount) 
		
	else:

		writer = Textwriter()

	writer.writeText()