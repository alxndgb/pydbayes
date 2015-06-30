#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    setup(
          name = 'pydbayes',
          version='0.0.2',
          description = '''''',
          long_description='''<class 'pybuilder.core.description'>''',
          author = "",
          author_email = "",
          license = '',
          url = '',
          scripts = ['scripts/driver.py', 'scripts/neapolitantest.py'],
          packages=['pydbayes'],
          py_modules=[],
          classifiers = ['Development Status :: 3 - Alpha', 'Programming Language :: Python'],
          entry_points={
          'console_scripts':
              []
          },
             #  data files
             # package data
          
          
          zip_safe=True
    )
