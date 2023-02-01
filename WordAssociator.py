import requests, re
import xml.etree.ElementTree as ET
#Besser:
from bs4 import BeautifulSoup

between = False

class WordAssociator():

	def __init__(self,word):
		self.nouns = []
		self.adjectives = []
		self.verbs = []
		self.adverbs = []
		self.word = word

		url = "https://wordassociations.net/de/assoziationen-mit-dem-wort/"+word
		response = requests.get(url)
		response.encoding ='utf-8'

		text = response.text.replace("&raquo;","'").replace("&laquo;","'").replace("&copy;","(C)")

		root = ET.fromstring(text)
		body = root[1]
		main = body[0]
		container = main[1]
		content = container[4]
		if len(content) == 0:
			self.getWikiInfo()
		else:
			content_left = content[0]
			words_column = content_left[0]
			if words_column.attrib["class"] == "wordscolumn":
				substantive= words_column[0]
				adjectives = [[],[]]
				verbs = [[],[]]
				if len(words_column) >= 3:
					adjectives = words_column[1]
					verbs      = words_column[2]
				#adverbs    = words_column[3]  TODO: Fehler fangen, wenn es gewisse Worttypen (Wie hier Adverben) nicht gibt

				for child in substantive[1]:
					self.nouns.append(child[0].text)
				for child in adjectives[1]:
					self.adjectives.append(child[0].text.lower())
				for child in verbs[1]:
					self.verbs.append(child[0].text.lower())
				#for child in adverbs[1]:
					#self.adverbs.append(child[0].text)
		print("\""+self.word+"\" wurde eingegeben.")
		print("Substantive:")
		print(self.nouns)

	def getWikiInfo(self):
		words = self.word.split(" ")
		capiWords = []
		for w in words:
			capiWords.append(w.capitalize())
		word = "_".join(capiWords)
		url = "https://de.wikipedia.org/wiki/"+word
		response = requests.get(url)
		response.encoding ='utf-8'
		html_doc = response.text
		soup = BeautifulSoup(html_doc,'lxml')
		if len(soup.find_all(attrs={"class":"noarticletext"})) > 0:
			return
		contentP = soup.find_all(attrs={"id" : "bodyContent"})[0]
		paragraphs = contentP.find_all("p")

		contentLI = soup.find_all(attrs={"class" : "mw-parser-output"})[0]
		entries = []
		for lists in contentLI.find_all("ul"):
			entries += lists.find_all("li")
			for i in entries:
				print(i.text)

		paragraphsAndEntries = paragraphs+entries
		hrefs = []
		for p in paragraphsAndEntries:

			links = p.find_all("a")
			hrefs = hrefs + links
		for ref in hrefs:
			try:
				noun = ref["title"]
			except Exception as e:
				continue
			noun = re.sub("[\(\[].*?[\)\]]", "", noun)
			self.nouns.append(noun.rstrip())
			if(len(self.nouns)>=100):
				break
		return self.nouns

	def tryIfOverviewPage(self, soup):
		mainPage = soup.find_all(attrs={"class":"mw-parser-output"})
		if len(mainPage) > 0:
			for listEntry in mainPage[0].find_all("li"):
				links = p.find_all("a")
				hrefs = hrefs + links
			for ref in hrefs:
				try:
					noun = ref["title"]
				except Exception as e:
					continue
				noun = re.sub("[\(\[].*?[\)\]]", "", noun)
				self.nouns.append(noun.rstrip())
				if(len(self.nouns)>=100):
					break
			return self.nouns	
	def getNouns(self):
		wordList = []
		wordList.append(self.word)
		print( len(self.nouns))
		print(wordList)
		return self.nouns if len(self.nouns) > 0 else wordList

if __name__ == '__main__':
	import sys
	wa = WordAssociator(sys.argv[1])
	print(wa.getWikiInfo())