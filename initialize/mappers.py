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
					'License',
					'style.css']


# Python Standard Project
# Project directory will be created directly

PYTHON_PROJ = ['setup.py',
			   'setup.cfg',
			   'tox.ini',
			   '.travis.yml',
			   '.gitattributes',
			   '.gitignore',
			   'Authors',
			   'Contributing',
			   'Readme.rst',
			   {'{0}':['_compat.py']},
			   'License',
			   {'tests':[]},
			   {'docs':[]}]

# Html Css Javascript Template
HTCSJS = ['Authors.txt',
		  'Contributing.md',
		  'License',
		  '.editorconfig',
		  'Readme.md',
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
		  'Readme.md',
		  {'dist':[]},
		  {'build':[{'release':[]}]},
		  {'src':[]},
		  {'tests': []}]

# Simple Html CSS JavaScript

SHTML = ['inxex.html',
		 'Readme',
		 'License',
		 {'css':['index.css']},
		 {'js':['index.js']}]

WORDPRESS_PLUGIN = ['{0}.php',
					'uninstall.php',
					'License',
					{'languages': [] },
					{'includes':[]},
					{'admin':[{'js':[]},
							  {'css':[]},
							  {'images':[]}]},
					{'public':[{'js':[]},
							  {'css':[]},
							  {'images':[]}]}]
