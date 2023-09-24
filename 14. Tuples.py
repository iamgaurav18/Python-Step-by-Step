#tuple is also similar to lists except the fact that it is immutable
#it also supports indexing
tup=(1,2,3,4,5,6,7,8,9)
print(type(tup),tup)

#it supports slicing similar to list

print(tup[1:5])

#count in tuple
print(tup.count(1))    #similar to index

#index in tuple
print(tup.index(5))   #index(element to find, start index, end index)

#you can use all methods of lists on a tuple by converting a tuple into list and then again in to tuple