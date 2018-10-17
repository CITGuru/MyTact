from setuptools import setup , find_packages
setup (
	name = 'MyTact',
	description = 'A Simple Contacts App CLI',
	version = '1.0.0',
	packages = find_packages(), # list of all packages
    	install_requires = ['click', "pyinquirer"],
    	python_requires='>=2.7', # any python greater than 2.7
	entry_points='''
        [console_scripts]
        mytact=mytact.__main__:main
    ''',
	)

# pip install wheel 
# 	