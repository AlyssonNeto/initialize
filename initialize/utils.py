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

def printmessage(message, customizations):
	"""
	Used to print Message to console
	"""
	if '-q' in customizations['customizations']:
		pass
	else:
		print(message)

def create_badges_table():
	"""
	This Function is used to create Badges Table inside
	Readme
	"""
	pass

def _input(message, allow_none = True, default = None):
	"""
	This is used to take input
	"""
	message = _prepare_input(message, default)
	while True:
		value = input(message)
		if default is None and not allow_none and value == '':
			print("Value Required")
		elif default is not None and value == '' and allow_none:
			return value

def _prepare_input(message, default = None):
	"""
	Used to prepare input string
	"""
	if default is not None:
		message = message + ' [' + default + ']: '
		return message
	return message
