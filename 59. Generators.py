def generator():           # these are the functions that will only generate a value everytime they are called, this helps in saving memory
    for i in range(10):
        yield i

g=generator()
print(g)               # this will print type of object
print(next(g))         # it will only return 0
print(next(g))         # it will return 1
print(next(g))         # it will return 2
print(next(g))         # it will return 3

for j in g:
    print(j)           # we can call generator in this way also, this will print till the last value