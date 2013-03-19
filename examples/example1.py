#!/usr/bin/env python
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

def main():
    doc = rst.Document('Title of the report')
    para = rst.Paragraph('Just another paragraph. We need few more of these.')
    doc.add_child(para)
    sec = rst.Section('Another', 2)
    doc.add_child(sec)
    para = rst.Paragraph('Can we do this? Yes we can.')
    doc.add_child(para)

    blt = rst.Orderedlist()
    blt.add_item('Red Hat')
    blt.add_item('Fedora')
    blt.add_item('Debian')

    doc.add_child(blt)

    blt = rst.Bulletlist()
    blt.add_item('Python')
    blt.add_item('C')
    blt.add_item('C++')
    blt.add_item('Lisp')

    doc.add_child(blt)



    sec2 = rst.Section('Why Python is awesome?', 2)
    sec.add_child(sec2)

    tbl = rst.Table('My friends', ['Name', 'Major Project'])
    tbl.add_item(('Ramki', 'Python'))
    tbl.add_item(('Pradeepto', 'Kde'))
    tbl.add_item(('Nicubunu', 'Fedora'))
    doc.add_child(tbl)

    print doc.get_rst()

if __name__ == '__main__':
    main()
