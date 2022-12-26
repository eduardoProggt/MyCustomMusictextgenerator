import json

class LineDataContainer():

	def __init__(self,path_to_json):

		json_file = open(path_to_json)
		data = json.load(json_file)

		self.line_beginnings = data["Line_Beginnings"]
		self.line_endings = data["Line_Endings"]
		self.line_standalones = data["Line_Standalone"]
		self.line_verbs = data['Verben']
		self.substantive_maennlich = data['Substantiv_maennlich']
		self.substantive_mehrzahl = data["Substantiv_mehrzahl"]
