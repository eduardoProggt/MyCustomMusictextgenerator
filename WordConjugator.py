import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import sys
from pattern.de import pluralize

class WordConjugator():

	def getPlural(self,word):
		return pluralize(word)

	def addArticle(self,word):
		url = "https://de.wiktionary.org/wiki/"+word
		response = requests.get(url)
		response.encoding ='utf-8'
		html_doc = response.text
		soup = BeautifulSoup(html_doc,'lxml')
		input_tag = soup.find_all(attrs={"class" : "mw-headline"})

		if not  input_tag or not input_tag[1].em.contents:
			return "der " + word
		if input_tag[1].em.contents[0] == "f":
			return "die " + word
		if input_tag[1].em.contents[0] == "m":
			return "der " + word
		if input_tag[1].em.contents[0] == "n":
			return "das " + word



	def determine_gender(self,noun):
		# Funzt noch nicht :(
	    parsed_noun = parse(noun)
	    for token in parsed_noun:
	        if token[1] == "NN":  # NN steht für Substantiv (neuter)
	            return "n"
	        elif token[1] == "NNS":  # NNS steht für Substantiv (maskulin)
	            return "m"
	        elif token[1] == "NNP":  # NNP steht für Substantiv (feminin)
	            return "f"
	    return "unbekannt"

#		<span class="mw-headline" id="Substantiv,_f"><a href="/wiki/Hilfe:Wortart#Substantiv" title="Hilfe:Wortart">Substantiv</a>, <em title="Genus: Femininum (grammatikal. Geschlecht: weiblich)">f</em></span>

wc = WordConjugator()

wc.addArticle("Nutte")
wc.addArticle("Teppich")
wc.addArticle("Fenster")
wc.addArticle("Nutella")
wc.addArticle("Ketchup")
wc.addArticle("Rapper")
wc.addArticle("Knast")
wc.addArticle("Straße")

