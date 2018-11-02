"""
This is Mapper module contains array of file to create
"""

# Wordpress Theme Structure
WORDPRESS_THEME = [{'assets':[{'css': []},
							  {'images': []},
							  {'js': []}
							 ]},
					{'inc': []},
					{'template-parts': [{'footer': []},
										{'header': []},
										{'navigation': []},
										{'page': []},
										{'post': []}
										]},
					{'languages': []},
					'404.php',
					'archive.php',
					'comments.php',
					'footer.php',
					'front-page.php',
					'functions.php',
					'header.php',
					'index.php',
					'page.php',
					'Readme.txt',
					'rtl.css',
					'screenshot.png',
					'search.php',
					'searchform.php',
					'sidebar.php',
					'single.php',
					'style.css']


# Python Standard Project
# Project directory will be created directly

PYTHON_PROJ = ['setup.py',
			   'setup.cfg',
			   'tox.ini',
			   '.gitattributes',
			   '.gitignore',
			   'Authors',
			   'Contributing',
			   {'{0}':['_compat.py']},
			   'License',
			   {'tests':[]},
			   {'docs':[]}]

# Html Css Javascript Template
HTCSJS = ['Authors.txt',
		  'Contributing.md',
		  'License',
		  '.editorconfig',
		  {'dist':['index.html',
		  		   {'css':['index.css']},
		  		   {'js' :['index.js']}
		  		  ]},
		  {'build':[{'release':[]}]},
		  {'src':[]},
		  {'tests': []}
		 ]

# Standard Javascript Library
JSLIB =['Authors.txt',
		  'Contributing.md',
		  'License',
		  '.editorconfig',
		  {'dist':[]},
		  {'build':[{'release':[]}]},
		  {'src':[]},
		  {'tests': []}]

# Simple Html CSS JavaScript

SHTML = ['inxex.html',
		 {'css':['index.css']},
		 {'js':['index.js']}]