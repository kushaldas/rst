#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


from setuptools import find_packages, setup

setup(name='rst',
      version=0.1,
      description='Module to create reStructuredText documents through code.',
      long_description='rst is a python module to create reStructuredText documents through code.',
      author='Kushal Das',
      author_email='kushaldas@gmail.com',
      maintainer='Kushal Das',
      maintainer_email='kushaldas@gmail.com',
      license='MIT',
      url='http://rst.rtfd.org',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Topic :: System :: Distributed Computing',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2'
          ],
      packages=find_packages(),
      data_files=[],
      install_requires=[
          'six'
      ],
      test_suite='tests',
      tests_require=[
          'mock'
      ]
)

