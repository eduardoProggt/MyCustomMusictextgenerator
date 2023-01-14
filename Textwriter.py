import random
from LineDataContainer import LineDataContainer
from WordAssociator import WordAssociator
import WordConjugator as wc

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
		self.topic = str(topic).capitalize()
		self.lineCount = int(lineCount)
		self.text = ""
		self.lineData = LineDataContainer('MCMdb.json')

	def writeText(self):

		withTopic = (not self.topic == "")
		if withTopic:
			wa = WordAssociator(self.topic)

		while self.lineCount > 0:
			if withTopic and random.randint(0, 4) == 4:
				self.addTopicLine(wa)
			else:
				self.addRandomLine()

		return self.text

	def addRandomLine(self):
		
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

		randomMap[randint_for_line_type](self.lineData)


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
		
		verb = getRandomElementsExclusive(lineData.line_verbs,3)
		text = verb[0].capitalize() +", " +verb[1] +", "+verb[2] +" und zählen die Scheine" 
		self.addLine(text)

	def addTopicLine(self,wa):
		
		randomMap = {
			9: self.addLineInderEckeSitzt,#
			8: self.addLineSoGenial,#
			7: self.addLineAgalObXYoderZ,#
			6: self.addLineJederMachtEinenAuf,#	
			5: self.addLineObXYOderNicht,#
			4: self.addLineWasIstDennLosMoos,#		
			3: self.addLineEgalObSieLachen,#		
			2: self.addLineLassEsSeinSoGemein,#	
			1 : self.addLineEsBrauchtKeine,#		
			0 : self.addLineAlleRapperSagen,#
		}

		#Die Untersten Keys haben Zeilen die auch ohne Assoziationen gehen
		randint_for_line_type = random.randint(0, 9) if len(wa.nouns) > 0 else random.randint(0,4)

		randomMap[randint_for_line_type](wa)

	def addLineInderEckeSitzt(self,wa):
		self.addLine("In der Ecke Sitzt "+wc.addArticle(getRandomElement(wa.nouns))+", "+wc.getPlural(getRandomElement(wa.nouns)) +" sollten sich schämen.")
	def addLineSoGenial(self, wa):
		self.addLine(wc.getPlural(getRandomElement(wa.getNouns()))+" "+getRandomElement(wa.verbs) +" so genial "+ getRandomElement(self.lineData.line_endings))
	def addLineAgalObXYoderZ(self,wa):
		topicNouns = getRandomElementsExclusive(wa.nouns,3)
		self.addLine("Egal, ob "+wc.getPlural(topicNouns[0])+", "+topicNouns[1]+" oder "+topicNouns[2])
	def addLineJederMachtEinenAuf(self,wa):
		self.addLine("Jeder macht einen auf "+getRandomElement(wa.verbs))
	def addLineObXYOderNicht(self,wa):
		self.addLine("Ob "+wc.getPlural(getRandomElement(wa.getNouns()))+" "+getRandomElement(wa.verbs)+" oder nicht")

	def addLineWasIstDennLosMoos(self,wa):
		self.addLine("Was ist denn los? seid ihr "+wc.getPlural(getRandomElement(wa.getNouns()))+" oder Moos?")
	def addLineEgalObSieLachen(self,wa):
		self.addLine("Es ist mir egal, ob die " + wc.getPlural(getRandomElement(wa.getNouns())) + " über mich lachen")
	def addLineLassEsSeinSoGemein(self,wa):
		self.addLine(getRandomElement(self.lineData.line_beginnings)+" lass es aber sein") 
		self.addLine("Guck die ganzen "+wc.getPlural(getRandomElement(wa.getNouns()))+" sind so gemein") 
	def addLineEsBrauchtKeine(self, wa):
		if self.lineCount < 2:
			return
		self.addLine("Es braucht keine "+wc.getPlural(getRandomElement(wa.getNouns()))+" auf der Welt")
		self.addLine("Dass es "+wc.getPlural(getRandomElement(wa.getNouns()))+" auch gefällt") 
	def addLineAlleRapperSagen(self,wa):
		self.addLine("Alle Rapper sagen "+wa.word+", bin so gemein")
	# Weitere Ideen:
		# alle sind die <Mehrzahl> mehr aber nein
		# Alle <Mehrzahl> <verb> auf der Straße

	def addLine(self,text):
		if self.lineCount <=0:
			return
		self.text += text +" \n"
		self.lineCount -=1

