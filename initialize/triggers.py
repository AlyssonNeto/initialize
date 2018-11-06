#! /usr/bin/python3
from initialize.utils import InvalidTrigger, _input
from initialize.mappers import (PYTHON_PROJ, WORDPRESS_THEME, HTCSJS, JSLIB, SHTML,
								WORDPRESS_PLUGIN)
from datetime import datetime
from initialize._triggers import readme_py, setup_py,

class Trigger(object):
	"""
	This are functional triggers that can be assigned
	which will invoke when working with file creation
	"""
	def __init__(self, category):
		super(Trigger, self).__init__()
		self.category = category
		self._triggers = {}
		self._filters= {}

	@staticmethod
	def clis(enviornment):
		"""
		Ads Enviornment Variables
		"""
		license = _input("Select License Templates", default = 'MIT')
		year = _input("Enter Year", default=datetime.now().year)
		author = _input("Enter Author Of Repo", allow_none = False)
		quick_description = _input("Small Description")
		version = _input("Enter Version", default = '0.1.0')


		if enviornment['option'] == 'wp_theme':
			# enviornment related to ws_theme

		if enviornment['option'] == 'python':
			# getting if Python enviornment is set
			packages = _input("Enter Packages", default=enviornment['project_name'])
			enviornment['packages'] = [package.strip() for package in packages.split(',')]

		enviornment['license'] = license
		enviornment['year'] = year
		enviornment['author'] = author
		enviornment['desc'] = quick_description
		enviornment['version'] = version


	def add_trigger(self, name, trigger):
		"""
		This is used to add trigger to cetogery
		"""
		if not callable(trigger):
			raise InvalidTrigger("Improper Trigger Provided"
								 " Trigger Should Be Callable")
		self._triggers[name] = trigger

	def add_filter(self, name, trigger):
		"""
		This is used to add trigger to cetogery
		"""
		if not callable(trigger):
			raise InvalidTrigger("Improper Trigger Provided"
								 " Trigger Should Be Callable")
		self._filters[name] = trigger

	def process_trigger(self, name):
		"""
		This is used to
		"""
		if name in self._triggers:
			self._triggers[name]();

	def process_env(self, name):
		"""
		This is used to
		"""
		if name in self._triggers:
			self._env[name]();

	def process_filter(self, name):
		"""
		This is used to
		"""
		if name in self._triggers:
			self._filters[name]();

	def remove_trigger(self, name):
		"""
		This is used to remove trigger
		"""
		self._triggers.pop(name,None)

class JavascriptTrigger(Trigger):
	"""
	Triggers For javascript
	"""
	def __init__(self, category):
		super(JavascriptTrigger, self).__init__(category)

	@staticmethod
	def clis(enviornment):
		"""
		Adds Enviornment Variables
		"""
		pass




javascript 	= Trigger('javascript')
python 		= Trigger('python')
html 		= Trigger('html')
shtml 		= Trigger('shtml')
wp_theme 	= Trigger('wp_theme')
wp_plugin 	= Trigger('wp_plugin')



