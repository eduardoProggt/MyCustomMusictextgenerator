import random
from LineDataContainer import LineDataContainer
from WordAssociator import WordAssociator
import WordConjugator as wc

import sqlite3

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
		self.lastRhyme = "ei"
		self.lastLineId = 0
		try:
			dbConnection = sqlite3.connect("database.db")
		except Exception as e:
			print("Keine database.db vorhanden. Script createDB ausgeführt?")
		self.dbCursor = dbConnection.cursor()

	def writeText(self):

		withTopic = (not self.topic == "")
		if withTopic:
			wa = WordAssociator(self.topic)

		while self.lineCount > 0:
			if withTopic and random.randint(0, 2) == 2:
				self.addTopicLine(wa)
			else:
				self.addRandomLine()

		return self.text

	def addRandomLine(self):
		
		randomMap = {
			36: self.addLineWasWillstDuVonMirABCTrinkeMeinBier,
			35: self.addLinePeopleSindDerBesteRapper,
			33: self.addLineHastSpastKnast,
			31: self.addLineVorLachenBepisst,
			30: self.addLineJederWillDasEine,		
			28: self.addLineXhabenNeY,		
			27: self.addLineDissenVerpissenGewissen,		
			25: self.addLineStandalone,		
			18: self.addLineCombined,		
			1 : self.addLineSollichXOderRuhn,		
			0 : self.addLineZaehleDieScheine,
		}
		randint_for_line_type = random.randint(0, len(randomMap))

		while not randint_for_line_type in randomMap:
			randint_for_line_type +=1

		randomMap[randint_for_line_type](self.lineData)
	def addLineWasWillstDuVonMirABCTrinkeMeinBier(self,lineData):
		if self.lineCount < 3:
			return
		self.addLine("Was willst du von mir")
		if random.randint(0,2) == 2:
			self.addLineStandalone(self.lineData)
		else:
			self.addLineCombined(self.lineData)
		self.addLine("Trinke mein Bier")

	def addLinePeopleSindDerBesteRapper(self,lineData):
		person1,person2 = getRandomElementsExclusive(lineData.people,2)
		self.addLine(person1 + " ist der beste Rapper andere sind Messerstecher")
		if random.randint(0,2) == 2:
			self.addLine(person2 + " ist besser")

	def addLineHastSpastKnast(self,lineData):
		self.addLine("Wenn du denkst, was du hast")
		self.addLine(getRandomElement(lineData.line_endings)[1:].capitalize() + " kleiner Spast")
		if random.randint(0, 10) == 10:
			self.addLine("Du wohnst in den Knast")

	def addLineVorLachenBepisst(self,lineData):
		self.addLine("Alle "+getRandomElement(lineData.substantive_mehrzahl)+ " haben sich doch nur vor Lachen bepisst")
		self.lastRhyme = "isst"

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

	def getRhymingLine(self, table):
		# Zufall entscheidet, ob es sich reimen soll, wenn ja, wird in der DB nach reimen gesucht.
		# Wenn er keine findet, wird nochmal ohne Reime gesucht.
		request = ("SELECT * from " + table)
		if random.randint(0,2) == 2:
			request+= " WHERE rhyme == \""+self.lastRhyme+"\""
		results = self.dbCursor.execute(request).fetchall()
		if len(results) == 1: #Wiederkehren ein und derselben Zeile verhindern
			if self.lastLineId == int(results[0][0]):# id des einzigen elements
				results = []#Schmeiß raus.
		if len(results) > 0:
			result = getRandomElement(results)
		else: 
			result = getRandomElement(self.dbCursor.execute("SELECT * from " + table).fetchall())
		self.lastLineId = int(result[0])
		self.lastRhyme = result[2]
		return result[1]

	def addLineStandalone(self,lineData):
		line = self.getRhymingLine("line_standalone")
		self.addLine(line)

	def addLineCombined(self,lineData):
		ending = self.getRhymingLine("line_ending")
		self.addLine(getRandomElement(lineData.line_beginnings) + ending)
			
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
			15: self.addLineAlleXYAufDerStraße,
			14: self.addLineSitzeHierZieheMirEinenRein,
			13: self.addLineFrueherWarnAufDemRasen,
			12: self.addLineInderEckeSitzt,#
			11: self.addLineSoGenial,#
			10: self.addLineAgalObXYoderZ,#
			9: self.addLineJederMachtEinenAuf,#	
			8: self.addLineObXYOderNicht,#
			#
			7: self.addLineZeigIchDirDenXYsolltenWeitergehn,
			6: self.addLineEsIstImmerGenauDasGleicheWieX,
			5: self.addLineSindNichtMehrAlsDerHass,
			4: self.addLineWasIstDennLosMoos,#		
			3: self.addLineEgalObSieLachen,#		
			2: self.addLineLassEsSeinSoGemein,#	
			1 : self.addLineEsBrauchtKeine,#		
			0 : self.addLineAlleRapperSagen,#
		}

		#Die Untersten Keys haben Zeilen die auch ohne Assoziationen gehen
		randint_for_line_type = random.randint(0, 15) if len(wa.verbs) > 0 else random.randint(0,7)
		randomMap[randint_for_line_type](wa)

	def addLineAlleXYAufDerStraße(self,wa):
		self.addLine("Alle "+wc.getPlural(getRandomElement(wa.getNouns()))+" "+getRandomElement(wa.verbs)+" auf der Straße")
	def addLineSitzeHierZieheMirEinenRein(self,wa):
		self.addLine("Sitze hier, zieh mir einen "+getRandomElement(wa.getNouns())+" rein aber nein")
	def addLineFrueherWarnAufDemRasen(self,wa):
		verb1, verb2 = getRandomElementsExclusive(wa.verbs,2)
		self.addLine("Früher warn es immer "+verb1+", "+ verb2+", blasen, auf dem Rasen")
	def addLineInderEckeSitzt(self,wa):
		self.addLine("In der Ecke Sitzt "+wc.addArticle(getRandomElement(wa.nouns))+", "+wc.getPlural(getRandomElement(wa.nouns)) +" sollten sich schämen.")
	def addLineSoGenial(self, wa):
		self.addLine(wc.getPlural(getRandomElement(wa.getNouns()))+" "+getRandomElement(wa.verbs) +" so genial"+ getRandomElement(self.lineData.line_endings))
	def addLineAgalObXYoderZ(self,wa):
		topicNouns = getRandomElementsExclusive(wa.nouns,3)
		self.addLine("Egal, ob "+wc.getPlural(topicNouns[0])+", "+topicNouns[1]+" oder "+topicNouns[2])
	def addLineJederMachtEinenAuf(self,wa):
		self.addLine("Jeder macht einen auf "+getRandomElement(wa.verbs))
	def addLineObXYOderNicht(self,wa):
		self.addLine("Ob "+wc.getPlural(getRandomElement(wa.getNouns()))+" "+getRandomElement(wa.verbs)+" oder nicht")

	def addLineZeigIchDirDenXYsolltenWeitergehn(self,wa):
		nounA,nounB = getRandomElementsExclusive(wa.getNouns(),2)
		self.addLine("Zeig ich dir den "+nounA+", "+nounB+" sollten doch nun weitergehn")
	def addLineEsIstImmerGenauDasGleicheWieX(self,wa):
		self.addLine("Es ist immer genau das gleiche wie "+getRandomElement(wa.getNouns()))
	def addLineSindNichtMehrAlsDerHass(self,wa):
		self.addLine(wc.getPlural(getRandomElement(wa.getNouns())) +" sind nicht mehr als der Hass und Neid")
	def addLineWasIstDennLosMoos(self,wa):
		self.addLine("Was ist denn los? Seid ihr "+wc.getPlural(getRandomElement(wa.getNouns()))+" oder Moos?")
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
		self.addLine("Alle Rapper sagen "+getRandomElement(wa.getNouns())+", bin so gemein")

	def addLine(self,text):
		if self.lineCount <=0:
			return
		self.text += text +" \n"
		self.lineCount -=1
		self.lastRhyme

