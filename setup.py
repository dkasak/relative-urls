#!/usr/bin/env python3
from setuptools import setup

setup(name = 'relativeurls',
      version = '1.0',
      author = 'Denis Kasak',
      author_email = 'dkasak[at]termina.org.uk',
      url = 'https://github.com/dkasak/relative-urls',
      description = ('A tool to extract endpoints (relative URLs) from stdin or files.'),
      license = 'ISC',
      packages = ['relativeurls'],
      entry_points = {
            'console_scripts': ['relative-urls=relativeurls.relativeurls:main']
      }
)
