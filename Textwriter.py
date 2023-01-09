import random
from LineDataContainer import LineDataContainer
from WordAssociator import WordAssociator
from chatbot.ChatBot import ChatBot
from WordConjugator import WordConjugator

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
		self.lineData = LineDataContainer('MCMdb.json')

	def writeText(self):

		withTopic = (not self.topic == "")
		while self.lineCount > 0:
			if withTopic and random.randint(0, 15) == 15:
				self.addTopicLine()
			else:
				self.addRandomLine()
		print(self.text)
		return self.text

	def addRandomLine(self):
		text = ""
		lineData = self.lineData

		randint_for_line_type = random.randint(0, 29)
		if randint_for_line_type > 27:
			self.addLine("Wenn du denkst, was du hast")
			self.addLine(getRandomElement(lineData.line_endings)[1:].capitalize() + " kleiner Spast")
			if random.randint(0, 10) == 10:
				self.addLine("Du wohnst in den Knast")
		elif randint_for_line_type > 26:
			self.addLine("Alle "+getRandomElement(lineData.substantive_mehrzahl)+ " haben sich doch nur vor Lachen bepisst")
		elif randint_for_line_type > 24 and self.lineCount >= 2:
			self.addLine("Jeder will nur das Eine")
			self.addLine(getRandomElement(lineData.substantive_maennlich) + " und die Scheine")
		elif randint_for_line_type > 23:
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
			text+= verb[0].capitalize() +", " +verb[1] +", "+verb[2] +" und zählen die Scheine" 
			self.addLine(text)

	def addTopicLine(self):
		text = ""
		wa = WordAssociator(self.topic)
		wc = WordConjugator()
		#cb = ChatBot()
		#text = cb.generate_response("Schreibe eine Zeile mit den Worten '"+getRandomElement(wa.nouns)+"', '"+getRandomElement(wa.verbs)+"' und '"+getRandomElement(wa.adjectives)+"'")
		
		self.addLine("In der Ecke Sitzt "+wc.addArticle(getRandomElement(wa.substantive))+", "+wc.getPlural(getRandomElement(wa.substantive)) +" sollten sich schämen.")
		#self.addLine(text.replace('"',''))

	def addLine(self,text):
		if self.lineCount <=0:
			return
		self.text += text +" \n"
		self.lineCount -=1

