.. _install:

Installation
============

This part of the documentation covers the installation of rst.
The first step to using any software package is getting it properly installed.


Distribute & Pip
----------------

Installing rst is simple with `pip <https://pip.pypa.io/en/stable/getting-started/>`_::

    $ python3 -m pip install rst



Get the Code
------------

rst is actively developed on GitHub, where the code is
`always available <https://github.com/kushaldas/rst>`_.

You can either clone the public repository::

    git clone git://github.com/kushaldas/rst.git

Download the `tarball <https://github.com/kushaldas/rst/tarball/master>`_::

    $ curl -OL https://github.com/kushaldas/rst/tarball/master

Or, download the `zip file <https://github.com/kushaldas/rst/zipball/master>`_::

    $ curl -OL https://github.com/kushaldas/rst/zipball/master


Once you have a copy of the source, you can embed it in your Python package,
or install it into your site-packages easily.

Local build and install
-------------------------

To build and install the package locally, run the following commands::

    $ python3 -m venv .venv
    $ .venv/bin/activate
    $ python3 -m pip install flit
    $ python3 -m pip install -e .
