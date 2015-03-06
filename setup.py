#!/usr/bin/env python

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(name='rebnypy',
      version='0.0.1',
      description="A Python library for interacting with the REBNY listing service",
      author='Kevin McCarthy',
      author_email='me@kevinmccarthy.org',
      url='https://github.com/RealGeeks/rebnypy',
      packages = [
        'rebnypy',
      ],
      package_dir={
        'rebnypy': 'rebnypy',
      },
      license='MIT',
      tests_require=['pytest','mock'],
      cmdclass={'test': PyTest},
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'License :: OSI Approved :: MIT License',
      ],
)
