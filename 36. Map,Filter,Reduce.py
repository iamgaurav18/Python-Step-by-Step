def cube(a):
    return a*a*a

l=[1,2,3,4,5]
m=list(map(cube,l))  #this will return a list of cubes of all numbers in list l
print(m)   #map will apply function in all list numbers

def fil(a):
    return a>2

n=list(filter(fil,l))  #this will reurn a list of all the value that will return true from the function
print(n)

from functools import reduce

c=[1,2,3,4,5,6]
s=reduce(lambda x,y:x+y,c)   #this will apply the specified function on list (here first two will be added and placed at first position then again first two will be added,, that how entire list will be reduced )
print(s)     # 1+2=3 [3,3,4,5,6]--> 3+3=6 [6,4,5,6]-->6+4=10 [10,5,6]--> 10+5=15 [15,6]--> 15+6=21