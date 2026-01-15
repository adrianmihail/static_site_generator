import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertTrue(node.text_type == TextType.BOLD)
        self.assertFalse(node.text_type == TextType.IMAGE)


if __name__ == "__main__":
    unittest.main()