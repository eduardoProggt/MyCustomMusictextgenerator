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
	randint_for_line_type = random.randint(0, 20)
	if randint_for_line_type > 15:
		text+= getRandomElement(line_standalones)
	elif randint_for_line_type > 1:
		text+= getRandomElement(line_line_beginnings) + getRandomElement(line_endings)
	elif randint_for_line_type > 0:
		text+= "Was soll ich tun \nSoll ich "+getRandomElement(line_verbs)+" oder ruhn?"
	else:
		text+= getRandomElement(line_verbs) +", " +getRandomElement(line_verbs) +", "+getRandomElement(line_verbs) +" und zählen die Scheine" 
	return text +" \n"

def getRandomElement(line):
	return line[random.randint(0, len(line) - 1)]


for i in range(1,8):
	text += addline()

print(text)