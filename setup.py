#!/usr/bin/python3

"""Setup script for handwrit."""

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def get_version(fname='handwrit/_version.py'):
    """Fetch version from file."""
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return (line.split('=')[-1].strip().strip('"'))


setup(
    name="handwrit",

    version=get_version(),

    description="Simple playlist library",
    long_description=long_description,

    # The project URL.
    url='https://github.com/tablet-mode/handwrit',

    # Author details
    author='Thomas Kager',
    author_email='tablet-mode@monochromatic.cc',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: GPLv3 License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='',

    packages=find_packages(exclude=["docs", "tests*"]),

    install_requires=[
    ],

    package_data={},

    data_files=[],
    entry_points={
    },
)
