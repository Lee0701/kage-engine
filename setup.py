from setuptools import setup, find_packages

setup(
    name='kage-engine',
    version='0.0.1',
    packages=find_packages(include=['kage', 'kage.*']),
    install_requires=[
        'svgwrite==1.4.3',
        'numpy==1.26.4',
    ],
)