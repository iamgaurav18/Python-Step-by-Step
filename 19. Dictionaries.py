dict={"name":"Gaurav","lname":"Vishwakarma","age":24}
#dict is a collection of key value pairs. dict is an ordered object

print(dict)
print(dict["name"])  # this will throw error if key doesn't exist
print(dict.get("lname")) # this wont throw any kind of error instead it will print None

print(dict.keys()) #this will print all the keys
print(dict.values()) #this will print all the values

for key in dict.keys():
    print(f"The value corresponding to {key} is {dict[key]}")

for key,value in dict.items():
    print(f"The value corresponding to {key} is {value}")