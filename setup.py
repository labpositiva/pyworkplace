# -*- coding: utf-8 -*-
# This is purely the result of trial and error.
import codecs
import sys

from setuptools import find_packages
from setuptools import setup
from setuptools.command.test import test as TestCommand

import pyworkplace


class PyTest(TestCommand):
    # `$ python setup.py test' simply installs minimal requirements
    # and runs the tests with no fancy stuff like parallel execution.
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--doctest-modules', '--verbose',
            './pyworkplace', './tests',
        ]
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))


tests_require = [
    'mock',
    'PyHamcrest',
    'pytest',
]

install_requires = [
    'requests>=2.11.0',
    'verify>=1.1.1'
    'yamlreader>=3.0.4',
]


extras_require = {
    # http://wheel.readthedocs.io/en/latest/#defining-conditional-dependencies
    ' or python_version == "3.0"'
    ' or python_version == "3.1" ': ['argparse>=1.2.1'],
}


def long_description():
    with codecs.open('README.rst', encoding='utf8') as f:
        return f.read()


setup(
    name='pyworkplace',
    version=pyworkplace.__version__,
    description=pyworkplace.__doc__.strip(),
    long_description=long_description(),
    url='http://pyworkplace.org/',
    download_url='https://github.com/labpositiva/pyworkplace',
    author=pyworkplace.__author__,
    author_email=pyworkplace.__email__,
    license=pyworkplace.__licence__,
    packages=find_packages(exclude=['tests*']),
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
)
