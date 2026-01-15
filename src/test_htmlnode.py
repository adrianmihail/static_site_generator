import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a","test link",None,{"href":"https://www.google.com","target":"_blank",})
        node2 = HTMLNode("p","test paragraph")
        node3 = HTMLNode("l","test link",None,{"type":"bold", "address":"myass.com", "holo":"bolo",})

        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
        self.assertEqual(node2.props_to_html(),'')
        self.assertEqual(node3.props_to_html(),' type="bold" address="myass.com" holo="bolo"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a","link to the universe",{"test":"response",})
        node3 = LeafNode("testo"," ")

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), '<a test="response">link to the universe</a>')
        self.assertEqual(node3.to_html(),'<testo> </testo>')

if __name__ == "__main__":
    unittest.main()