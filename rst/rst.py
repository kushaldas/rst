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

from __future__ import print_function

import codecs
from abc import abstractmethod

try:
    import StringIO
except:
    import io
from six import u



class Document(object):
    """
    Returns a ``Document`` object.

    .. doctest::

        >>> import rst
        >>> doc = rst.Document('Title of the report')
        >>> print(doc.get_rst())
        ===================
        Title of the report
        ===================
        <BLANKLINE>
        <BLANKLINE>

    """
    def __init__(self, title):
        self.title = title
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
        try:
            out = StringIO.StringIO()
        except:
            out = io.StringIO()
        text = Section(self.title,1)
        text.write_rst(out)
        #Now goto each children
        for child in self.children:
            child.write_rst(out)
        return out.getvalue()


class Node(object):
    """
    Returns a ``Node`` object.

    Inherit this if you want to add something new to the API.
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

    @abstractmethod
    def write_rst(self, output) -> None:
        """Return a utf8 representation of a node.
         inherited node must provide a concrete implementation.
         This must use output.write() for each line of its definition"""


class Paragraph(Node,):
    """
    Represents a paragraph

    :arg text: Text to be present in the paragraph.

    . doctest::

        >>> import rst
        >>> doc = rst.Document('Title of the report')
        >>> para = rst.Paragraph('This is a paragraph. A long one.')
        >>> doc.add_child(para)
        True
        >>> print(doc.get_rst())
        ===================
        Title of the report
        ===================
        <BLANKLINE>
        This is a paragraph. A long one.
        <BLANKLINE>
        <BLANKLINE>
    """
    def __init__(self, text=''):
        Node.__init__(self)
        self.text = text

    def write_rst(self,output):
        output.write( self.text + u('\n\n'))


class Section(Node):
    """
    Represents a ``Section`` object.

    :arg depth: Depth of the section, default is 1
    :arg text: Title of the section
    """
    def __init__(self, title, depth=1):
        Node.__init__(self)
        self.depth = depth
        self.text = title

    def _create_section(self):
        marks = u('=-+#')
        index = self.depth - 1
        text_length = len(self.text)
        if self.depth == 1:
            return u(
                "{}\n{}\n{}\n\n".format(marks[index] * text_length,
                                        self.text,
                                        marks[index] * text_length))
        else:
            # return u'\n' + text + u'\n' +  + u'\n\n'
            return u("\n{}\n{}\n\n".format(self.text, marks[index] * text_length))

    def write_rst(self, output):
        result = self._create_section()
        output.write(result)

class Bulletlist(Node):
    """
    Represents a Bullet List.

    .. doctest::

        >>> import rst
        >>> doc = rst.Document('Title of the report')
        >>> blt = rst.Bulletlist()
        >>> blt.add_item('Fedora')
        >>> blt.add_item('Debian')
        >>> doc.add_child(blt)
        True
        >>> print(doc.get_rst())
        ===================
        Title of the report
        ===================
        <BLANKLINE>
            * Fedora
            * Debian
        <BLANKLINE>
        <BLANKLINE>

    """
    def __init__(self):
        Node.__init__(self)

    def add_item(self, text):
        """
        Adds a new text block in the Bulletlist.

        :arg text: text to be added in the list.
        """
        self.children.append(text)

    def write_rst(self,output):
        for ch in self.children:
            output.write(u("{}* {}\n".format(' ' * 4, ch)))
        output.write(u('\n'))


class Orderedlist(Node):
    """
    Represents a Ordered List.

    .. doctest::

        >>> import rst
        >>> doc = rst.Document('Title of the report')
        >>> blt = rst.Orderedlist()
        >>> blt.add_item('Fedora')
        >>> blt.add_item('Debian')
        >>> doc.add_child(blt)
        True
        >>> print(doc.get_rst())
        ===================
        Title of the report
        ===================
        <BLANKLINE>
            1. Fedora
            2. Debian
        <BLANKLINE>
        <BLANKLINE>

    """
    def __init__(self):
        Node.__init__(self)

    def add_item(self, text):
        """
        Adds a new text block in the Bulletlist.

        :arg text: text to be added in the list, remember it is ordered list.
        """
        self.children.append(text)

    def write_rst(self, output) -> None:
        for i, ch in enumerate(self.children):
            output.write(u("{}{}. {}\n".format(' ' * 4, str(i + 1), ch)))
        output.write(u('\n'))


class Table(Node):
    """
    Represents a Table, (will be wriiten in csv-table style)

    .. doctest::

        >>> import rst
        >>> doc = rst.Document('Title of the report')
        >>> tbl = rst.Table('My friends', ['Name', 'Major Project'])
        >>> tbl.add_item(('Ramki', 'Python'))
        >>> tbl.add_item(('Pradeepto', 'Kde'))
        >>> tbl.add_item(('Nicubunu', 'Fedora'))
        >>> doc.add_child(tbl)
        True
        >>> print(doc.get_rst())
        ===================
        Title of the report
        ===================
        <BLANKLINE>
        .. list-table:: My friends
            :header-rows: 1
        <BLANKLINE>
            * -  Name
              -  Major Project
            * -  Ramki
              -  Python
            * -  Pradeepto
              -  Kde
            * -  Nicubunu
              -  Fedora
        <BLANKLINE>

    """
    def __init__(self, title='', header=None, width=None):
        Node.__init__(self)
        self.text = title
        self.header = header
        self.width = width

    def add_item(self, row):
        """
        Adds a new row to the table.

        :arg row: list of items in the table.
        """
        self.children.append([txt for txt in row])

    @staticmethod
    def _print_table(out, header):
        for i, hdr in enumerate(header):
            if i == 0:
                out.write(u('    * -  %s\n') % hdr)
            else:
                out.write(u('      -  %s\n') % hdr)
    def write_rst(self, output) -> None:
        output.write(u('.. list-table:: %s\n') % self.text)
        if self.width:
            output.write(u('    %s') % self.width)
        if self.header:
            output.write(u('    :header-rows: 1\n\n'))
            self._print_table(output, self.header)
        for ch in self.children:
            self._print_table(output,ch)
        output.write(u('\n'))


class CodeBlock(Node):
    r"""
    Represents a Code Block.

    .. doctest::

        >>> import rst
        >>> doc = rst.Document('Title of the report')
        >>> code = rst.CodeBlock("import sys\nsys.stdout.write('Working')", lang="python", linenos=True)
        >>> doc.add_child(code)
        True
        >>> print(doc.get_rst())
        ===================
        Title of the report
        ===================
        <BLANKLINE>
        .. code-block:: python
            :linenos:
        <BLANKLINE>
            import sys
            sys.stdout.write('Working')
        <BLANKLINE>

    """
    def __init__(self, code, lang='', linenos=False):
        Node.__init__(self)
        self.code = code
        self.lang = lang
        self.linenos = linenos

    def write_rst(self, output) -> None:
        output.write(u('.. code-block:: %s\n') % self.lang)
        if self.linenos:
            output.write(u('    :linenos:\n\n'))
        indented = "\n".join(
                "    {}".format(l) for l in self.code.split("\n"))
        output.write(u("{}\n".format(indented)))


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

    code = CodeBlock("import sys\nsys.stdout.write('Working')", lang="python", linenos=True)
    doc.add_child(code)

    print(doc.get_rst())
