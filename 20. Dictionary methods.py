d={1:23,2:34,3:45}
e={5:56}

d.update(e)  # this will add key values at the end of the dict
print(d)

e.clear()   # this will clear the entire dictionary
print(e)

d.pop(1)    #this will delete the specified item with its value from dict
print(d)

d.popitem()  #this will delete the last item
print(d)

del e         #this will delete entire dict

del d[2]       #this will also delete specified key with its value