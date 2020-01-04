from setuptools import setup
import os

version = '0.2.0'


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='medium2md',
    version=version,
    description="Python API for Medium",
    long_description=read('README.md'),
    keywords='apis, Medium',
    author='Cléber Zavadniak',
    author_email='contato@cleber.solutions',
    url='https://github.com/cleberzavadniak/medium2md',
    license='MIT',
    packages=['medium2md'],
    entry_points='''
        [console_scripts]
        medium2md=medium2md.cli:run
    ''',
    package_dir={'medium2md': 'medium2md'},
    zip_safe=False,
    install_requires=['bs4', 'newspaper3k'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ),
)
