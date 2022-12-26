import random
from LineDataContainer import LineDataContainer

lineData = LineDataContainer("mock")
line_verbs = lineData.line_verbs
line_standalones = lineData.line_standalones
line_line_beginnings = lineData.line_beginnings
line_endings = lineData.line_endings

text = ""

def addline():
	text = ""
	randint_for_line_type = random.randint(0, 22)
	if randint_for_line_type > 20:
		substantive = getRandomElementsExclusive(lineData.substantive_maennlich,2)
		text+= "Jeder "+ substantive[0] +" will mich dissen \nJeder "+substantive[1]+" kann sich verpissen \n"+getRandomElement(lineData.substantive_mehrzahl)+" haben schlechtes Gewissen"
	elif randint_for_line_type > 15:
		text+= getRandomElement(line_standalones)
	elif randint_for_line_type > 1:
		text+= getRandomElement(line_line_beginnings) + getRandomElement(line_endings)
	elif randint_for_line_type > 0:
		text+= "Was soll ich tun? \nSoll ich "+getRandomElement(line_verbs)+" oder ruhn?"
	else:
		verb = getRandomElementsExclusive(line_verbs,3)
		text+= verb[0] +", " +verb[1] +", "+verb[2] +" und zählen die Scheine" 
	return text +" \n"
	
	#Mehrzahl haben ne Weiblich
	#'blamage, visage'

def getRandomElement(line):
	return line[random.randint(0, len(line) - 1)]

def getRandomElementsExclusive(line,noOfLines):
	lines = []
	lineIn = line
	for i in range(0,noOfLines):
		newLine = getRandomElement(lineIn)
		lines.append(newLine)
		lineIn.remove(newLine)
	return lines

for i in range(0,8):
	text += addline()

print(text)