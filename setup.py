#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup

setup(name='CI Hello World',
      version='1.0',
      description='CI Hello World',
      author='Gleb Lobov',
      author_email='lobzison@gmail.com',
      url='',
      packages=['ci-hello-world', 'tests'],
      license='MIT',
      test_suite='tests'
      )
