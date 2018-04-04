#! /usr/bin/env python

from setuptools import find_packages, setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Open_eQuarterPy',
    version='0.0.1',
    author='Uwe Krien',
    author_email='uwe.krien@rl-institut.de',
    description='Stand alone python script of the Open_eQuarter qgis plugin.',
    namespace_package=['Open_eQuarterPy'],
    long_description=read('README.rst'),
    packages=find_packages(),
    package_dir={'Open_eQuarterPy': 'Open_eQuarterPy'},
    install_requires=['pandas >= 0.18', 'numpy']
    )
