#! /usr/bin/env python

from setuptools import setup

setup(name='Open_eQuarterPy',
      version='0.0.1',
      author='Uwe Krien',
      author_email='uwe.krien@rl-institut.de',
      description='A local heat and power system',
      package_dir={'Open_eQuarterPy': 'Open_eQuarterPy'},
      install_requires=['pandas >= 0.18', 'numpy']
      )
