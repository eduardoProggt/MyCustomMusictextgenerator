import json

class LineDataContainer():

	def __init__(self,path_to_json):

		json_file = open(path_to_json)
		data = json.load(json_file)

		self.line_beginnings= ["Alle Leute sagen zu mir:",
		"Es ist nicht so leicht",
		"Kann es aber sein",
		"Es ist mir egal",
		"Auch wenn du denkst",
		"Ohne nice",
		"Gebe niemals auf",
		"Mach es ausm Kopf",
		"Weiß ich ganz genau"]

		self.line_endings = [" bin so genial.", " bist so abgezeckt", " du wohnst in den Knast", " geh widder Heim", " es ist der pure Neid", " lass es aber sein", " ihr werdet schon sehn"]

		self.line_standalones = [
		"Zeig\' ich dir den Mittelfinger",
		"Bleib ich wie ich bin",
		"Bin der King mit dem dicken Ding",
		"Es ist wie ein Stich in Herz"
		]

		self.line_verbs = data['Verben']
		self.substantive_maennlich = data['Substantiv_maennlich']
		self.substantive_mehrzahl = data["Substantiv_mehrzahl"]
