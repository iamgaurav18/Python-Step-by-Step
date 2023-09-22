#lists are ordered collections of data items of single or multiple types under a single name
#lists are mutable 
l=[1,2,"a",3,5,7,9,12,43,55,65,757,78]
print(l)

#we can use index to access any item
print(l[2])

if 2 in l:  #in keywords checks if a item is in list. similarly we can use in for strings too
    print(True)

#slicing in licing
print(l[1:])  # it will print from 2nd value from start to last
print(l[1:-1])  # negative indexing can be considered as Length of list - index (13-1) so it will print from 2nd value to 2nd last
print(l[0::2]) # this will only print alternative items from start to end

#list comprehension

a=[i for i in range(10) if i%2==0] # this will create a list of even numbers within 0 to 10
print(a)