l=[34,2,3,44,1,32,4535,42]

print(l)

l.append(31)   #this will add the value at the end of the list
print(l)

l.sort()       #this will sort the list 
print(l)

l.sort(reverse=True)   # this will sort the list in reverse order
print(l)

l.reverse()        #this will reverse the original list 
print(l)

print(l.index(1))    # this will returnthe index of a item in list

print(l.count(2))    # return the count of a item in list

m=l   #this will create a list m with a reference of l, it means if you change anything in m it will get reflected in l too
m=l.copy()   # this will create a seperate list from l with the same contents as l and can be changed without changing l

l.insert(2, 99)    # this will add 99 at the index two i the list
print(l)

l.extend(m)
print(l)         # this will add the values in list m at the end of list l

#we can also add two lists 

k=l+m
print(k)

a=[1,2,3,4,5,10]
print(a.pop()) #this will print the element from the last of a list and also remove it from the list
print(a.pop(2)) #this will remove the element at the specified positon from the list