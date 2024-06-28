import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
	props = {
		"href": "https://www.google.com",
		"target": "_blank"
	}
	node = HTMLNode("a", "This is a hyperlink", None, props)
	print(node.props_to_html())

if __name__ == "__main__":
	unittest.main()