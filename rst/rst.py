#Copyright (C) 2012, Kushal Das <kushaldas@gmail.com>

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

import codecs
import StringIO


def create_section(text, depth):
    marks = u'=-+#'
    if depth == 1:
        return marks[depth -1] * len(text) + u'\n' + text + u'\n' + marks[depth -1] * len(text) + u'\n\n'
    else:
        return u'\n' + text + u'\n' + marks[depth -1] * len(text) + u'\n\n'


def print_table(out, header):
    for i, hdr in enumerate(header):
        if i == 0:
            out.write(u'    * -  %s\n' % hdr)
        else:
            out.write(u'      -  %s\n' % hdr)


class Document(object):
    """
    Returns a ``Document`` object.
    """
    def __init__(self, title):
        self.title = unicode(title)
        self.children = []

    def add_child(self, node):
        """
        Adds a ``Node`` object to the Document.
        Returns ``True`` in case of success. 
        """
        self.children.append(node)
        return True

    def save(self, path):
        """
        Saves the document in the given path.

        :arg path: Path to save the document.
        """
        fobj = codecs.open(path, 'w', 'utf-8')
        fobj.write(self.get_rst())
        fobj.close()

    def get_rst(self):
        """
        Returns the rst representation of the document in unicode format.
        """
        out = StringIO.StringIO()
        text = create_section(self.title, 1)
        out.write(text)
        #Now goto each children
        for child in self.children:
            if isinstance(child, Paragraph):
                #We have a paragraph here
                out.write(child.text + u'\n\n')
            elif isinstance(child, Section):
                text = create_section(child.text, child.depth)
                out.write(text)
            elif isinstance(child, Bulletlist):
                for ch in child.children:
                    out.write(u' ' * 4 + '* ' + ch + u'\n')
                out.write(u'\n')
            elif isinstance(child, Orderedlist):
                for i, ch in enumerate(child.children):
                    out.write(u' ' * 4 + u'%s. ' % str(i + 1) + ch + u'\n')
                out.write(u'\n')
            elif isinstance(child, Table):
                out.write(u'.. list-table:: %s\n' % child.text)
                if child.width:
                    out.write(u'    %s' % child.width)
                if child.header:
                    out.write(u'    :header-rows: 1\n\n')
                    print_table(out, child.header)
                for ch in child.children:
                    print_table(out, ch)

        return out.getvalue()


class Node(object):
    """
    Returns a ``Node`` object.
    """
    def __init__(self):
        self.depth = 1
        self.children = []
        self.text = None

    def add_child(self, node):
        """
        Adds a ``Node`` object to the current.
        Returns ``True`` in case of success.
        """
        self.children.append(node)
        return True


class Paragraph(Node):
    """
    Represents a paragraph
    """
    def __init__(self, text=''):
        Node.__init__(self)
        self.text = unicode(text)


class Section(Node):
    """
    Represents a ``Section`` object.
    If you add it under some other node, it will become subsection.
    """
    def __init__(self, title, depth):
        Node.__init__(self)
        self.depth = depth
        self.text = unicode(title)


class Bulletlist(Node):
    """
    Represents a Bullet List.
    """
    def __init__(self):
        Node.__init__(self)

    def add_item(self, text):
        self.children.append(unicode(text))


class Orderedlist(Node):
    """
    Represents a Ordered List.
    """
    def __init__(self):
        Node.__init__(self)

    def add_item(self, text):
        self.children.append(unicode(text))


class Table(Node):
    """
    Represents a Table, (will be wriiten in csv-table style)
    """
    def __init__(self, title='', header=None, width=None):
        Node.__init__(self)
        self.text = unicode(title)
        self.header = header
        self.width = width

    def add_item(self, row):
        self.children.append([unicode(txt) for txt in row])

if __name__ == '__main__':
    doc = Document('Title of the report')
    para = Paragraph('Just another paragraph. We need few more of these.')
    doc.add_child(para)
    sec = Section('Another', 2)
    doc.add_child(sec)
    para = Paragraph('Can we do this? Yes we can.')
    doc.add_child(para)

    blt = Orderedlist()
    blt.add_child('Red Hat')
    blt.add_child('Fedora')
    blt.add_child('Debian')

    doc.add_child(blt)

    sec2 = Section('Why Python is awesome?', 2)
    doc.add_child(sec)

    tbl = Table('My friends', ['Name', 'Major Project'])
    tbl.add_child(('Ramki', 'Python'))
    tbl.add_child(('Pradeepto', 'Kde'))
    tbl.add_child(('Nicubunu', 'Fedora'))
    doc.add_child(tbl)

    print doc.get_rst()
