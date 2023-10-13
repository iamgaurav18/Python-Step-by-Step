a=4
b="4"
#both of them are comparision operator
print(a is b)  # this will compare the location of the object in memory

print(a==b)   # this will compare the exact value
#in this case both the outputs will be false

a=[1,2,3]
b=[1,2,3]

print(a is b)  # will return false because both of the lists are stored in a different locations
print(a==b)    # will return true as both of the lists are equal

a=3
b=3
print(a is b)   #here it will return true as python stores (any immutable objects, like strings or contant int or tuples) constants at same location
print(a==b)     # it will also return true