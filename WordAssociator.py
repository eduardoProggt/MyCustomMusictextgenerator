import requests
import xml.etree.ElementTree as ET

between = False

class WordAssociator():

	def __init__(self,word):
		self.nouns = []
		self.adjectives = []
		self.verbs = []
		self.adverbs = []

		url = "https://wordassociations.net/de/assoziationen-mit-dem-wort/"+word
		response = requests.get(url)
		response.encoding ='utf-8'

		text = response.text.replace("&raquo;","'").replace("&laquo;",",").replace("&copy;","(C)")

		root = ET.fromstring(text)
		body = root[1]
		main = body[0]
		container = main[1]
		content = container[4]
		content_left = content[0]
		words_column = content_left[0]
		if words_column.attrib["class"] == "wordscolumn":

			nouns      = words_column[0]
			adjectives = words_column[1]
			verbs      = words_column[2]
			adverbs    = words_column[3]

			for child in nouns[1]:
				self.nouns.append(child[0].text)
			for child in adjectives[1]:
				self.adjectives.append(child[0].text)
			for child in verbs[1]:
				self.verbs.append(child[0].text)
			for child in adverbs[1]:
				self.adverbs.append(child[0].text)

		else:
			pass # TODO Nach Synonymen von word suchen und nochmal probieren 