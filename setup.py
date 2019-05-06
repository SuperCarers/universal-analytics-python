# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup
    from distutils.core.command.install import install

import metadata as m

here = os.path.abspath(os.path.dirname(__file__))

VERSION=m.version
print("Preparing version {0}\n".format(VERSION or "NOTFOUND"), file=sys.stderr)


try:
    long_description = open('DESCRIPTION.rst', 'rt').read()
except Exception:
    long_description = ("Universal Analytics in Python; an implementation of "
                        "Google's Universal Analytics Measurement Protocol")

setup(
    name="universal-analytics-python",
    description="Universal Analytics Python Module",
    long_description=long_description,
    version=VERSION,
    author='Sam Briesemeister',
    author_email='opensource@analyticspros.com',
    url='https://github.com/analytics-pros/universal-analytics-python',
    download_url="https://github.com/analytics-pros/universal-analytics-python/tarball/" + VERSION,
    license='BSD',
    packages=["UniversalAnalytics"],
    install_requires=['six'],
    zip_safe=True,
)
