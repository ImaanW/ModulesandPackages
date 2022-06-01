# OBJECT ORIENTATION
# Using Objects
# a class is a template , abstract and idea of a thing
# objects need to be built to make the idea real(implementation) being built, instantiated incidences

# USING OBJECTS
# from account(module) import Account (Uppercase= class) - enstanciating an object
# some_account = Acount(1000.00) - calling a constuctor inside of the bank acoount class - creating a variable which points to an class

# methods can be within a class
# __class__. __name__ ask class and name

# hassattr(object,name ) asking what the object can do

# a class is declared using a class
# membership by indentation of it won't be classed in the class
# class names are capitalised
# We define functions in out class we call them methods
# first argument passed is object all methods have the first parameter as the object
# the constructor Methods called __init__ (called as we build) get the ground running
# The destructor is called __del__
# all classes are usually declared in a dedicated separate file -  1 class - 1 file
# methods/functions typically return

# DEFINING CLASSES
# public attributes are references by class.attribute
# ._ makes it semiprivate
# .__ super private
# usually in a module with the same name as the class

# class can inherit

# DEFINING METHODS
# methods are functions defined within a class
# convection with underscores - reminder
# one underscore private to a module/class
# two underscores have a special meaning
# first argument methods is object
# usually called self but can be anything

# A constructor - a special method to initialise and be ready to be functional/ready to be used
#__init__ is an example
# instructor is called through using the class name in and passing something through the brackets
# the init mentod is being called implicitly

# special methods
# dundascore - built in methods

# PROPERTIES

#PROPERTIES AND DECORATORS IN PYTHON
# buiilt in properties is are usally called this, warpper

#Inheretance
# all about repurposing
# class is a kind of C, class C is a kind of A
# put what you are inheriteing from in brackets