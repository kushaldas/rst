#Copyright (C) 2012-2013, Kushal Das <kushaldas@gmail.com>

#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#of the Software, and to permit persons to whom the Software is furnished to do
#so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import rst
import unittest
from six import u


class RstTest(unittest.TestCase):

    def test_title(self):
        "test the title of the document"
        doc = rst.Document(u("Sample document"))
        text = doc.get_rst()
        actual_text = u("""===============
Sample document
===============

""")
        self.assertEqual(text, actual_text)

    def test_paragraph(self):
        "test the paragraph in the document"
        doc = rst.Document(u(""))
        para = rst.Paragraph(u('This is a paragraph.'))
        doc.add_child(para)
        text = doc.get_rst()
        actual_text = u('\n\n\n\nThis is a paragraph.\n\n')
        self.assertEqual(text, actual_text)

    def test_sections(self):
        "test the sections in the document"
        doc = rst.Document(u("Title"))
        sec = rst.Section('Section One', 2)
        doc.add_child(sec)
        sec2 = rst.Section('Section Two', 3)
        doc.add_child(sec2)
        text = doc.get_rst()
        actual_text = u('=====\nTitle\n=====\n\n\nSection One\n-----------\n\n\nSection Two\n+++++++++++\n\n')
        self.assertEqual(text, actual_text)

    def test_orderedlist(self):
        "test the OrderedList in the document"
        doc = rst.Document(u("T"))
        blt = rst.Orderedlist()
        blt.add_item('Fedora')
        blt.add_item('Debian')
        doc.add_child(blt)
        text = doc.get_rst()
        actual_text = u('=\nT\n=\n\n    1. Fedora\n    2. Debian\n\n')
        self.assertEqual(text, actual_text)


if __name__ == '__main__':
    unittest.main()