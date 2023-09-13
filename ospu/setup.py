#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Jeferson Dario Quiguantar",
    author_email='jeffersonquiguantar@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Predecir como las moleculas pequeñas cambian la expresion genetica en diferentes tipos de celulas",
    entry_points={
        'console_scripts': [
            'ospu=ospu.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ospu',
    name='ospu',
    packages=find_packages(include=['ospu', 'ospu.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jefersonqui/ospu',
    version='0.1.0',
    zip_safe=False,
)
