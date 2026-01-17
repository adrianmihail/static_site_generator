import unittest

from textnode import TextNode, TextType
from convert_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_split(self):
        node1 = TextNode("Test Node in `code block` ghezau",TextType.TEXT)
        node2 = TextNode("Test Node in **bold block** ghezau",TextType.TEXT)
        node3 = TextNode("Test Node in _italic block_ ghezau", TextType.TEXT)
        node4 = TextNode("boldo puternico", TextType.BOLD)
        node5 = TextNode("grande intaliano",TextType.ITALIC)
        node6 = TextNode("bip bip bip",TextType.CODE)

        self.assertEqual(split_nodes_delimiter([node1],"`",TextType.CODE),[
            TextNode("Test Node in ",TextType.TEXT),
            TextNode("code block",TextType.CODE),
            TextNode(" ghezau",TextType.TEXT)
            ]
        )

        self.assertEqual(split_nodes_delimiter([node2],"**",TextType.BOLD),[
            TextNode("Test Node in ",TextType.TEXT),
            TextNode("bold block",TextType.BOLD),
            TextNode(" ghezau",TextType.TEXT)
            ]
        )

        self.assertEqual(split_nodes_delimiter([node3],"_",TextType.ITALIC),[
            TextNode("Test Node in ",TextType.TEXT),
            TextNode("italic block",TextType.ITALIC),
            TextNode(" ghezau",TextType.TEXT)
            ]
        )

        self.assertEqual(split_nodes_delimiter([node4],"**",TextType.BOLD),[
            TextNode("boldo puternico",TextType.BOLD),
            ]
        )

        self.assertEqual(split_nodes_delimiter([node5],"_",TextType.ITALIC),[
            TextNode("grande intaliano",TextType.ITALIC),
            ]
        )

        self.assertEqual(split_nodes_delimiter([node6],"`",TextType.CODE),[
            TextNode("bip bip bip",TextType.CODE),
            ]
        )

    def test_extract_link(self):
        text1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg"
        text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev"

        #self.assertEqual(extract_markdown_images(text1), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        #self.assertEqual(extract_markdown_links(text2), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

if __name__ == "__main__":
    unittest.main()