""""this tripple double quotes is documentation used to describe my function"""
# WHAT ARE MODULES?
# A module is a file containing code,Usually written in Python
# usually with a .py filename suffix(Some modules are built-in)
# a module might be byte-code
# python will create a .pyc file if none exists
# held in a subdirectory _pycache_ from Python 3.2


# WHAT ARE PACKAGES?
# A package is a collection of modules (folders with files in)
# A directory containing a set of modules is a Package
# the difference is a file called __init__.py(with a dundascore) can be empty but used to create directory
# often empty
# can contain initialisation code
# can contain a list of public interfaces as attributes __all__

# MULTIPLE SOURCE FILES? WHY BOTHER?
#  maintainability, functionality, Encapsulation & Hiding information, support concurrent development

# HOW DOES PYTHON FIND A MODULE?
# the initial file is from sys.path
# modified by sys.path.append(dirname)
# print sys.path - will show all the places it will look
# sys.path.append('./demomodules) - appending and referencing to a particular file/place will make it also look there.
# import sys

# IMPORTING A MODULE
# import mymodoule - at the top of file , can also import multiple in a list format, , ,
# print my module - print(mymodule.attribute)
# you can print all variables and function names of a module print (dir(mymodule)

# IMPORTING A NAME
# from (mymodule) import *   (beware of name collisions) but can suck in any/all code into file
# specify specific object names - such as of a function or class
# from (mymodule) import (my_func1)
# import modulename.packagename (no.py)
# or use an allias ...
# from mymodule import mayj_function as mymaths (here renaming alias to shortern how) *good way to do it

# clases have Capital such as True,False and None

# THE MAIN TRICK
# when importing code/function, the code in the og file will run aswell.
# create a def main():
# if __name__ =="__main__"
# if this file is directly run, then it will run both modules - unless we have the main trick check in the first module
# which will say if name is equal to main run, if not it will only run from import (we want)


