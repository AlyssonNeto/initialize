# A Template Directory To Keep Track of  Templates


# ------------------License
License = """License
=======
{0}
"""

# -----------------This is Installation Text
# ----------------- package_name, github_link
PYTHON_INSTALLATION = """Installation
============

The `Python Packaging Guide`_ contains general information about how to manage
your project and dependencies.

.. _Python Packaging Guide: https://packaging.python.org/current/

Released version
----------------

Install or upgrade using pip. ::

    pip install -U {package_name}

Development
-----------

The latest code is available from `GitHub`_. Clone the repository then install
using pip. ::

    git clone {github_link}
    pip install -e ./{git_folder}

Or install the latest build from an `archive`_. ::

    pip install -U {github_link}/tarball/master

.. _GitHub: {github_link}
.. _archive: {github_link}/archive/master.tar.gz


"""



Contributing = """Contributing
=============

One Can Contribute to this project by **creating a issue at issue** at `{github_link}` Or **creating a pull request**

Pull Request Process
--------------------

1. Ensure any install or build dependencies are removed before the end of the layer when doing a
   build.
2. Checkout pull requests list at `{github_link}/pulls` to ensure that you are not dublicating anybody's work
3. Update the README.md with details of changes to the interface, this includes new environment
   variables, exposed ports, useful file locations and container parameters.
4. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
5. You may merge the Pull Request in once you have the sign-off of by other developers, or if you
   do not have permission to do that, you may request the one of maintainers of project to merge it for you.

Development Process
-------------------

* Create a local copy of repository in our machiene
* Install dependencies which are currently used by project
* Make Changes To your Project
* Write atleast Basic Test which covers your changes
* Improve docs with your changes
* Create a coverage report
* Pull...

How To issue
------------
While registering a issue it will be beneficial if creator of issue desribe following things about issue

* operating system he used
* steps to generte error or bug
* if not know steps in what function or method bug generated


"""


# Templates For index.html

INDEX_HTML = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Hello World</title>
	<link rel="stylesheet" href="css/index.css">
</head>
<body>

	<script src="js/index.js"></script>
</body>
</html>"""


# travis templates


# gitignore templates
# Taken From Github don't know from where but will be updated
# here when found


EditorConfig = """# http://EditorConfig.org

#################
# Common Settings
#################

# This file is the top-most EditorConfig file
root = true

# All Files
[*]
charset = utf-8
end_of_line = crlf
indent_style = space
indent_size = 4
insert_final_newline = false
trim_trailing_whitespace = true

#########################
# File Extension Settings
#########################

# Visual Studio Solution Files
[*.sln]
indent_style = tab

# Visual Studio XML Project Files
[*.{csproj,vbproj,vcxproj,vcxproj.filters,proj,projitems,shproj}]
indent_size = 2

# XML Configuration Files
[*.{xml,config,props,targets,nuspec,resx,ruleset,vsixmanifest,vsct}]
indent_size = 2

# JSON Files
[*.{json,json5}]
indent_size = 2

# YAML Files
[*.{yml,yaml}]
indent_size = 2

# Markdown Files
[*.md]
trim_trailing_whitespace = false

# Web Files
[*.{htm,html,js,ts,tsx,css,sass,scss,less,svg,vue}]
indent_size = 2
insert_final_newline = true

# Batch Files
[*.{cmd,bat}]

# Bash Files
[*.sh]
end_of_line = lf
"""
