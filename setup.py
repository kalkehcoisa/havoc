#!/usr/bin/env python

""" mixer -- Generate tests data.

mixer -- Description

"""
import re
import sys
from os import path as op

from setuptools import setup


def _read(fname):
    try:
        return open(op.join(op.dirname(__file__), fname)).read()
    except IOError:
        return ''

#_meta = _read('mixer/__init__.py')
#_license = re.search(r'^__license__\s*=\s*"(.*)"', _meta, re.M).group(1)
#_project = re.search(r'^__project__\s*=\s*"(.*)"', _meta, re.M).group(1)
#_version = re.search(r'^__version__\s*=\s*"(.*)"', _meta, re.M).group(1)

install_requires = [
    l for l in _read('requirements.txt').split('\n')
    if l and not l.startswith('#')]

tests_require = [
    l for l in _read('requirements-tests.txt').split('\n')
    if l and not l.startswith('#')]

# FIXME: Fix fake-factory installation
# if sys.version_info < (2, 7, 0):
#    install_requires.append('importlib')


setup(
    name=_project,
    version=_version,
    license=_license,
    description=_read('DESCRIPTION'),
    long_description=_read('README.rst'),
    platforms=('Any'),
    keywords = "sqlalchemy testing mock stub data".split(), # noqa

    author='Jayme Tosi Neto',
    author_email='kalkehcoisa@gmail.com',
    url='http://github.com/kalkehcoisa/parrot',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Natural Language :: Portuguese',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],

    packages=['elizabeth'],
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='tests',
)

# lint_ignore=F0401
