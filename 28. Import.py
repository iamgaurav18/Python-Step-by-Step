# Import in python is similar to #include header_file in C/C++. Python modules can get access to code from another module by importing the file/function using import. The import statement is the most common way of invoking the import machinery, but it is not the only way.

# import module_name

# When the import is used, it searches for the module initially in the local scope by calling __import__() function. The value returned by the function is then reflected in the output of the initial code.

import math   # this will import entire module

print(math.sqrt(64))

#what if we want to import only selective methods of a module

from math import pi

print(pi)

#if you want to include allmethods and variables from a module then you can do it using from math import * but this is not recommended as this might cause unwanted issues if you are importing other modules as well with all variables and modules.

# you can use as keyword in case the name of the module is big and hard to write multiple times
# import pandas as pd

# inorder to get the details about the package you imported and modulesof it use dir
print(dir(math))
print(math.__doc__)

# in order to use and existing programs funxtionality you can import that program and use it using import as well