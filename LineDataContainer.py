import json

class LineDataContainer():

	def __init__(self,path_to_json):

		json_file = open(path_to_json)
		data = json.load(json_file)

		self.line_beginnings= ["Alle Leute sagen zu mir",
		"Es ist nicht so leicht",
		"Kann es aber sein",
		"Es ist mir egal",
		"Auch wenn du denkst",
		"Ohne nice",
		"Gebe niemals auf"]

		self.line_endings = [" bin so genial.", " bist so abgezeckt", " du wohnst in den Knast", " geh widder Heim", " es ist der pure Neid", " lass es aber sein"]

		self.line_standalones = [
		"Zeig\' ich dir den Mittelfinger",
		"Bleib ich wie ich bin",
		"Mach es ausm Kopf",
		"Bin der King mit dem dicken Ding"
		]

		self.line_verbs = data['Verben']

		self.substantive_maennlich =[
		"Mann",
		"Porno",
		"Knast",
		"Schwanz",
		"MCM",
		"Nazi",
		"Spast",
		"Dreck",
		"Gangbang",
		"Fame",
		]
		self.substantive_mehrzahl = [
		"Fotzen",
		"Leute",
		"Hater",
		"Drackskinder",
		"Rapper",
		"Wichser",
		"Nutten"
		]