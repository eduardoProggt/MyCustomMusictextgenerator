import random
from LineDataContainer import LineDataContainer
from WordAssociator import WordAssociator
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
		
		lineData = self.lineData

		randomMap = {
			29: self.addLineHastSpastKnast,
			27: self.addLineVorLachenBepisst,
			26: self.addLineJederWillDasEine,		
			24: self.addLineXhabenNeY,		
			23: self.addLineDissenVerpissenGewissen,		
			21: self.addLineStandalone,		
			15: self.addLineCombined,		
			1 : self.addLineSollichXOderRuhn,		
			0 : self.addLineZaehleDieScheine,
		}
		randint_for_line_type = random.randint(0, 29)

		while not randint_for_line_type in randomMap:
			randint_for_line_type +=1

		randomMap[randint_for_line_type](lineData)


	def addLineHastSpastKnast(self,lineData):
		self.addLine("Wenn du denkst, was du hast")
		self.addLine(getRandomElement(lineData.line_endings)[1:].capitalize() + " kleiner Spast")
		if random.randint(0, 10) == 10:
			self.addLine("Du wohnst in den Knast")

	def addLineVorLachenBepisst(self,lineData):
		self.addLine("Alle "+getRandomElement(lineData.substantive_mehrzahl)+ " haben sich doch nur vor Lachen bepisst")

	def addLineJederWillDasEine(self,lineData):
		if self.lineCount < 2:
			return
		self.addLine("Jeder will nur das Eine")
		self.addLine(getRandomElement(lineData.substantive_maennlich) + " und die Scheine")

	def addLineXhabenNeY(self,lineData):
			self.addLine(getRandomElement(lineData.substantive_mehrzahl) + " haben ne " + getRandomElement(lineData.substantive_weiblich))

	def addLineDissenVerpissenGewissen(self,lineData):
		if self.lineCount < 2:
			return
		substantive = getRandomElementsExclusive(lineData.substantive_maennlich,2)
		self.addLine("Jeder "+ substantive[0] +" will mich dissen")
		self.addLine("Jeder "+substantive[1]+" kann sich verpissen")
		if random.randint(0, 1) == 0:
			self.addLine(getRandomElement(lineData.substantive_mehrzahl)+" haben schlechtes Gewissen")

	def addLineStandalone(self,lineData):
		self.addLine(getRandomElement(lineData.line_standalones))

	def addLineCombined(self,lineData):
		self.addLine(getRandomElement(lineData.line_beginnings) + getRandomElement(lineData.line_endings))
			
	def addLineSollichXOderRuhn(self,lineData):
		if self.lineCount < 2:
			return
		self.addLine("Was soll ich tun?")
		self.addLine("Soll ich "+getRandomElement(lineData.line_verbs)+" oder ruhn?")

	def addLineZaehleDieScheine(self,lineData):
		text = ""
		verb = getRandomElementsExclusive(lineData.line_verbs,3)
		text+= verb[0].capitalize() +", " +verb[1] +", "+verb[2] +" und zählen die Scheine" 
		self.addLine(text)

	def addTopicLine(self):
		text = ""
		wa = WordAssociator(self.topic)
		wc = WordConjugator()
		#cb = ChatBot()
		#text = cb.generate_response("Schreibe eine Zeile mit den Worten '"+getRandomElement(wa.nouns)+"', '"+getRandomElement(wa.verbs)+"' und '"+getRandomElement(wa.adjectives)+"'")
		
		if len(wa.substantive) == 0: # Wenn keine Assoziationen gefunden wurden.
			self.addLine("Alle Rapper sagen "+self.topic+" bin so gemein")
			return
		self.addLine("In der Ecke Sitzt "+wc.addArticle(getRandomElement(wa.substantive))+", "+wc.getPlural(getRandomElement(wa.substantive)) +" sollten sich schämen.")
		# es braucht keine x auf der Welt \n dass es y auch gefällt 
	def addLine(self,text):
		if self.lineCount <=0:
			return
		self.text += text +" \n"
		self.lineCount -=1

