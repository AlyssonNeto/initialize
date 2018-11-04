#! /usr/bin/python3


# Predefined Errors

class InvalidTrigger(ValueError):
	"""
	This is raised when trigger of invalid type is raised
	"""
	def __init__(self, msg):
		super(InvalidTrigger,self).__init__(msg)

def printusage():
	print("\n"
			"usage: initialize [options] category\n\n"
			"options:\n"
			"	q : for quite \n"
			"\n"
			"category:\n"
			"	javascript: for javascript standard libray structure\n"
			"	python: for python standard libray structure\n"
			"	html: for html standard libray structure\n"
			"	ws_theme: for standard ws_theme structure\n")
