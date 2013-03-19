#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import find_packages, setup

setup(name='rst',
      version=0.1,
      description='Module to generate reStructuredText',
      long_description='Module to generate reStructuredText',
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

