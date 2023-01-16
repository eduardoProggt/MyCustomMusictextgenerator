import json

class LineDataContainer():

	def __init__(self,path_to_json):

		json_file = open(path_to_json, encoding='utf-8')
		data = json.load(json_file)

		self.line_beginnings = data["Line_Beginnings"]
		self.line_endings = data["Line_Endings"]
		self.line_endings_rhymes = data["Line_Endings_Rhymes"]
		self.line_standalones = data["Line_Standalone"]
		self.line_standalones_rhymes = data["Line_Standalone_Rhymes"]
		self.line_verbs = data['Verben']
		self.substantive_maennlich = data['Substantiv_maennlich']
		self.substantive_weiblich = data['Substantiv_weiblich']
		self.substantive_mehrzahl = data["Substantiv_mehrzahl"]
