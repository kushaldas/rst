import rst
import unittest


class RstTest(unittest.TestCase):

    def test_title(self):
        "test the title of the document"
        doc = rst.Document("Sample document")
        text = doc.get_rst()
        actual_text = """===============
Sample document
===============

"""
        self.assertEqual(text, actual_text)


    def test_paragraph(self):
        "test the paragraph in the document"
        doc = rst.Document("")
        para = rst.Paragraph('This is a paragraph.')
        doc.add_child(para)
        text = doc.get_rst()
        actual_text = u'\n\n\n\nThis is a paragraph.\n\n'
        self.assertEqual(text, actual_text)


    def test_sections(self):
        "test the sections in the document"
        doc = rst.Document("Title")
        sec = rst.Section('Section One', 2)
        doc.add_child(sec)
        sec2 = rst.Section('Section Two', 3)
        doc.add_child(sec2)
        text = doc.get_rst()
        actual_text = u'=====\nTitle\n=====\n\n\nSection One\n-----------\n\n\nSection Two\n+++++++++++\n\n'
        self.assertEqual(text, actual_text)

    def test_orderedlist(self):
        "test the OrderedList in the document"
        doc = rst.Document("T")
        blt = rst.Orderedlist()
        blt.add_item('Fedora')
        blt.add_item('Debian')
        doc.add_child(blt)
        text = doc.get_rst()
        actual_text = u'=\nT\n=\n\n    1. Fedora\n    2. Debian\n\n'
        self.assertEqual(text, actual_text)


if __name__ == '__main__':
    unittest.main()