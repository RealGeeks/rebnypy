#!/usr/bin/env python

from setuptools import setup

setup(name='rebnypy',
      version='0.1.2',
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
      install_requires=['requests'],
      tests_require=['pytest','mock'],
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'License :: OSI Approved :: MIT License',
      ],
)
