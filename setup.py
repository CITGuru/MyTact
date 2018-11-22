from setuptools import setup, find_packages
from io import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]
setup (
	name = 'MyTact',
	description = 'A Simple Contacts App for managing contacts right from the command line',
	version = '1.0.0',
	packages = find_packages(), # list of all packages
    install_requires = install_requires,
    python_requires='>=2.7', # any python greater than 2.7
	entry_points='''
        [console_scripts]
        mytact=mytact.__main__:main
    ''',
	author="Oyetoke Toby",
	keyword="pyinquirer, click, snap, cli, cla, contacts, mytact",
	long_description=long_description,
    license='MIT',
    url='https://github.com/CITGuru/MyTact/',
	download_url='https://github.com/CITGuru/MyTact/archive/1.0.0.tar.gz',
    dependency_links=dependency_links,
    author_email='oyetoketoby80@gmail.com',


	)

# pip install wheel 
# 	