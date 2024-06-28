class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		html = ""
		for item in self.props.items():
			html += f"{item[0]}=\"{item[1]}\" "

			html.rstrip()
		return html

	def __repr__(self):
		return f"HTMLNode:\ntag={self.tag}\nvalue={self.value}\nChildren:\n{self.children}\nProps:\n{self.props}"