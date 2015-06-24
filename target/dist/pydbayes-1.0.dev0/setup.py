#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    setup(
          name = 'pydbayes',
          version = '0.0.1',
          description = '''''',
          long_description = '''''',
          author = "",
          author_email = "",
          license = '',
          url = '',
          scripts = ['scripts/driver.py', 'scripts/neapolitantest.py'],
          packages = [],
          py_modules = ['scoring', 'timer', 'utilities'],
          classifiers = ['Development Status :: 3 - Alpha', 'Programming Language :: Python'],
          entry_points={
          'console_scripts':
              []
          },
             #  data files
             # package data
          
          
          zip_safe=True
    )
