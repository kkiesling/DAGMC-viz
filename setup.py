#!/usr/bin/env python

VERSION = '1.0'

from io import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))


def main():

    packages = ['scripts', 'tests', 'images']
    pack_dir = {'scripts': 'scripts', 'tests': 'tests', 'images': 'img'}
    package_data = {'': ['*', '*/*', '*/**/**/*']}
    setup_kwargs = {
        "name": "dagmc-viz",
        "version": VERSION,
        "description": 'DAGMC Visualization Tools',
        "long_description": open(path.join(here,'README.md')).read(),
        "long_description_content_type": 'text/markdown',
        "author": 'Svalinn Development Team',
        "url": 'https://github.com/svalinn/DAGMC-viz',
        "classifiers": ['Programming Language :: Python :: 2.7'],
        "install_requires": ['numpy', 'pytest', 'xmldiff'],
        "packages": packages,
        "package_dir": pack_dir,
        "package_data": package_data
        }
    rtn = setup(**setup_kwargs)

    return rtn


if __name__ == "__main__":
    main()