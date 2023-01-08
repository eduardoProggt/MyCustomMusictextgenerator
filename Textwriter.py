import random
from LineDataContainer import LineDataContainer
from WordAssociator import WordAssociator

from copy import deepcopy

def getRandomElement(line):
	return line[random.randint(0, len(line) - 1)]

def getRandomElementsExclusive(line,noOfLines):
	lines = []
	lineIn = deepcopy(line)
	for i in range(0,noOfLines):
		newLine = getRandomElement(lineIn)
		lines.append(newLine)
		lineIn.remove(newLine)
	return lines

class Textwriter:

	def __init__(self, topic = "", lineCount = 8):
		self.topic = str(topic)
		self.lineCount = int(lineCount)
		self.text = ""
		self.lineData = LineDataContainer('MCMdb.txt')

	def writeText(self):

		withTopic = (not self.topic == "")
		while self.lineCount > 0:
			if withTopic:
				self.addTopicLine()
				withTopic = False
			else:
				self.addRandomLine()
		print(self.text)
		return self.text

	def addRandomLine(self):
		text = ""
		lineData = self.lineData

		randint_for_line_type = random.randint(0, 24)
		if randint_for_line_type > 22:
			self.addLine(getRandomElement(lineData.substantive_mehrzahl) + " haben ne " + getRandomElement(lineData.substantive_weiblich))
		elif randint_for_line_type > 21 and self.lineCount >=2:
			substantive = getRandomElementsExclusive(lineData.substantive_maennlich,2)
			self.addLine("Jeder "+ substantive[0] +" will mich dissen")
			self.addLine("Jeder "+substantive[1]+" kann sich verpissen")
			if random.randint(0, 1) == 0:
				self.addLine(getRandomElement(lineData.substantive_mehrzahl)+" haben schlechtes Gewissen")
		elif randint_for_line_type > 15:
			self.addLine(getRandomElement(lineData.line_standalones))
		elif randint_for_line_type > 1:
			self.addLine(getRandomElement(lineData.line_beginnings) + getRandomElement(lineData.line_endings))
		elif randint_for_line_type > 0 and self.lineCount >= 2:
			self.addLine("Was soll ich tun?")
			self.addLine("Soll ich "+getRandomElement(lineData.line_verbs)+" oder ruhn?")
		else:
			verb = getRandomElementsExclusive(lineData.line_verbs,3)
			text+= verb[0] +", " +verb[1] +", "+verb[2] +" und zählen die Scheine" 
			text = text.capitalize()
			self.addLine(text)

	def addTopicLine(self):
		text = ""
		wa = WordAssociator(self.topic)
		text += "Ich bin eine "+getRandomElement(wa.nouns) +" und ich mag "+ getRandomElement(wa.verbs)
		self.addLine(text)

	def addLine(self,text):
		if self.lineCount <=0:
			return
		self.text += text +" \n"
		self.lineCount -=1

