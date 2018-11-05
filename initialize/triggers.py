#! /usr/bin/python3
from initialize.utils import InvalidTrigger

class Trigger(object):
	"""
	This are functional triggers that can be assigned
	which will invoke when working with file creation
	"""
	def __init__(self, category):
		super(Trigger, self).__init__()
		self.category = category
		self._triggers = []

	def add(self, trigger):
		"""
		This is used to add trigger to cetogery
		"""
		if not callable(trigger):
			raise InvalidTrigger("Improper Trigger Provided"
								 " Trigger Should Be Callable")

		self._triggers.append(trigger)

javascript 	= Trigger('javascript')
python 		= Trigger('python')
html 		= Trigger('html')
shtml 		= Trigger('shtml')
wp_theme 	= Trigger('wp_theme')
wp_plugin 	= Trigger('wp_plugin')
