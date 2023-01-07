import random
from LineDataContainer import LineDataContainer
from WordAssociator import WordAssociator

def writeText(topic):

	lineData = LineDataContainer('MCMdb.txt')

	text = ""
	withTopic = (not topic == "")
	for i in range(0,8):
		if withTopic:
			text += addTopicLine(topic)
			withTopic = False
		else:
			text += addline(lineData)

	print(text)
	return text

def addline(lineData):
	text = ""
	randint_for_line_type = random.randint(0, 24)
	if randint_for_line_type > 22:
		text+= getRandomElement(lineData.substantive_mehrzahl) + " haben ne " + getRandomElement(lineData.substantive_weiblich)
	elif randint_for_line_type > 21:
		substantive = getRandomElementsExclusive(lineData.substantive_maennlich,2)
		text+= "Jeder "+ substantive[0] +" will mich dissen \nJeder "+substantive[1]+" kann sich verpissen \n"+getRandomElement(lineData.substantive_mehrzahl)+" haben schlechtes Gewissen"
	elif randint_for_line_type > 15:
		text+= getRandomElement(lineData.line_standalones)
	elif randint_for_line_type > 1:
		text+= getRandomElement(lineData.line_beginnings) + getRandomElement(lineData.line_endings)
	elif randint_for_line_type > 0:
		text+= "Was soll ich tun? \nSoll ich "+getRandomElement(lineData.line_verbs)+" oder ruhn?"
	else:
		verb = getRandomElementsExclusive(lineData.line_verbs,3)
		text+= verb[0] +", " +verb[1] +", "+verb[2] +" und zählen die Scheine" 
		text = text.capitalize()
	return text +" \n"

def addTopicLine(word):
	text = ""
	wa = WordAssociator(word)
	text += "Ich bin eine "+getRandomElement(wa.nouns) +" und ich mag "+ getRandomElement(wa.verbs)
	return text + "\n"

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

if __name__ == '__main__':
	writeText("Nutte")