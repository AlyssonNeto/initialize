# Creating Custom Functions to to Add it To Hook
# Python Specific

import os
from initialize.utils import write_to_file, get_github_link
from initialize._templates import PYTHON_INSTALLATION, Contributing

def readme_py(working_path, file, environment, storage = ''):
	"""
	Hook For Readme
	"""
	_storage = storage
	github_link = environment['github_link']
	package_name = environment['github_repo']
	_storage = _storage + PYTHON_INSTALLATION.format(package_name = environment['project_name'],
													github_link = environment['github_link'],
													git_folder = environment['project_name'])
	readme(working_path, file, environment, _storage)




def setup_py(working_path, file, environment):
	"""
	Creating Custom Triggers For Setup.py file python
	"""
	pass

def gitignore_py(working_path, file, environment):
	"""
	Hook for gitignore File
	"""
	pass

# Html Css Javascript Configurations

def _index_html(working_path, file, environment):
	"""
	Index.html
	"""
	pass


# General Formatting Hooks

def readme(working_path, file, environment, storage):
	"""
	This is used to create simple readme file
	"""
	_storage = storage
	Contrib = Contributing.format(github_link = environment['github_link'])
	_storage = _storage + Contrib
	write_to_file(working_path, file, environment ,_storage)


def license(working_path, file, environment):
	"""
	Hook for license
	"""
	pass

def project_format(working_path, file, environment):
	"""
	Project Naming Formatter
	"""
	pass

def authors(working_path, file, environment):
	"""
	Hook For authors
	"""
	pass

def editor_config(working_path, file, environment):
	"""
	For Editor Config Hook
	"""
	pass
