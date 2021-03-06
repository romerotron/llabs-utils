#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'feedparser', 
    'requests', 
    'beautifulsoup4'
]

setup_requirements = [
    # TODO(romerotron): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'feedparser', 
    'requests', 
    'beautifulsoup4',
    'pytest'
]

setup(
    name='llabs-utils',
    version='0.1.0',
    description="Python utilities for craigslist, google docs",
    long_description=readme + '\n\n' + history,
    author="Allen Romero",
    author_email='romeroax@gmail.com',
    url='https://github.com/romerotron/llabs-utils',
    packages=find_packages(include=['llabs-utils']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='llabs-utils craigslist google docs',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
