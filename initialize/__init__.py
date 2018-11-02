#! /usr/bin/python3

import sys
from sys import argv
from os.path import join
from os import getcwd
from sys import path
from initialize.utils import InvalidTrigger
from initialize.triggers import Trigger
from initialize.mappers import PYTHON_PROJ, WORDPRESS_THEME, HTCSJS, JSLIB, SHTML


# Main Path is
main_path = getcwd()

# main options
standard_main_options = ['javascript', 'python' , 'html', 'ws_theme']
standard_sub_options = ['-q']

# Adding Specific triggers
javascript = Trigger('javascript')
python = Trigger('python')
html = Trigger('html')
ws_theme = Trigger('ws_theme')


def createworkingenviornment():
	"""
	This function will create workig enviornment for
	other functions to work
	"""
	if len(argv) > 1:
		pass
	else:
		print("\n\n"
			"usage initialize [options] category\n"
			"options:\n"
			"q : for quite \n"
			"\n"
			"category:\n"
			"javascript: for javascript standard libray structure\n"
			"python: for python standard libray structure\n"
			"html: for html standard libray structure\n"
			"ws_theme: for standard ws_theme structure\n")
		return





def create_files_and_folder():
	"""
	This is used to create Files and Folder
	for package directory
	"""
	pass

def _append_path():
	"""
	This is used to append path to the working
	directory and create files and folder
	"""
	pass


