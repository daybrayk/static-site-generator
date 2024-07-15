from htmlnode import HTMLNode

class LeafNode(HTMLNode):
	
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value == None:
			raise ValueError(f"Leaf node ({repr(self)}) has no value")

		if self.tag == None:
			return self.value
		props_html = self.props_to_html()
		
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
