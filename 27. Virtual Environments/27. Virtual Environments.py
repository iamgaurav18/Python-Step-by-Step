# A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most Python developers use.

# > python -m venv myenv
# to create a virtual environment in the present directory

#in order to use that virtual environment we need to first activate it

# myenv\Scripts\activate is used to activate the virtual environment created by you

# You can also deactivate you venv using "deactivate"

#now you can install packages of your choice and versions in this environment and use them as you want

# for examplae i will install numpy
# pip3 install numpy

# >>> import numpy as np
# >>> np.__version__
# '1.26.0'

# pip freeze is used to get all the packages installed in your env

# pip freeze >requirement.txt will create a file with all those package details to share with other to use same packages

# to create a file within the Venv type New-Item -Path .\main.py -ItemType file