#Docsrting are like comments but the only difference is that they are not ignored by interpreter
def square(n):
    '''This is a method which returns the square of a number. it takes a integer number as and input'''
    return n*n

print(square(5))

print(square.__doc__)

#one thing to keep in mind is that doc string is always at the start of a function. it will be written before any line of code

# PEP-8 Python Enhancement Proposal 8
# if you do import this, you will get a Poem of name : Zen of Python which will basically guide you how to write python code in a better way