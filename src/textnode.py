class TextNode():
	def __init__(self, text, text_type, url = None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		text_eq = self.text == other.text
		type_eq = self.text_type == other.text_type
		url_eq = self.url == other.url
		return text_eq and type_eq and url_eq

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"