#!/usr/bin/python3
import os
import re
from setuptools import setup, find_packages

def get_version():
    init = open(os.path.join(os.path.dirname(__file__), 'currency2text',
                             '__init__.py')).read()
    return re.search(r"""__version__ = '([0-9.\sA-Za-z]*)'""", init).group(1)

setup(
    name="currency2text",
    url="http://www.alistek.com/",
    author="Alistek Ltd",
    author_email="info@alistek.com",
    maintainer=u"Alistek Ltd",
    maintainer_email="info@alistek.com",
    description="The library converts currency to text in various languages",
    long_description="""
currency2text
=========

This is modular multilingual multi-currency amount to text converter written in
Python. Module can be used to convert numbers to the text representation in
various languages for various currencies. It's aim is to provide correct textual
representation.
    """,
    license="GPL License",
    version=get_version(),
    packages=find_packages(),
    python_requires='>=3',
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
    ],
    test_suite="nose.collector",
    )
