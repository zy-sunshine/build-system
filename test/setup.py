#!/usr/bin/env python
import sys
sys.path.append(sys.path.pop(0))
print sys.path
from distutils.core import setup
setup(
    name='Distutils',
    version='1.0',
    description='Python Distribution Utilities',
    author='Greg Ward',
    author_email='gward@python.net',
    url='http://www.python.org/sigs/distutils-sig/',
    packages=['distutils', 'distutils.command'],
)
