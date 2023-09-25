#as its name it is similar to sets in maths. it will only have distincts objects. it is unordered. it can have multiple data types
s={2,3,4,5,6,7,3,4,5,2,9}
print(s)

a=set()  #this will create and empty set
a={1,2,3,4}
b={5,6,7}

a.union(b)

print(a.union(b)) # this wont effect set a

a.update(b)  #this will add elemnts of set b  that are not in a in set a

print(a)

#similarly we have intersection and intersection_update

c=a.intersection(b)
print(c)
c.intersection_update(a)
print(c)

#difference and difference_update

print(a.difference(b))

#isdisjoint checks if two sets are disjoint
print(a.isdisjoint(b))

#issuperset checks if a set is superset of another set

print(a.issuperset(b))

#issubset checks if a set is a subset
print(b.issubset(a))

#add() used to add an element to set

a.add(10)

#update can be used to add multiple values as explained earlier

#remove this will remove an element from set. it will throw an error if that item does not exist

a.remove(10)

#discard does the same job without throwing any error

a.discard(10)

#pop is used to randomly remove one element 
d=a.pop()
print(d)

#del is used to delete a set

del c

#clear is used to clear entire set
a.clear()