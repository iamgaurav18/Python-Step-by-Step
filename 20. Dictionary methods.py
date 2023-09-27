d={1:23,2:34,3:45}
e={5:56}

d.update(e)
print(d)

e.clear()
print(e)

d.pop(1)
print(d)

d.popitem()
print(d)