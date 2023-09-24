#before python 3.6 we were using this format to display values within the string
s="My name is {} {} and I am from {}"
name="Gaurav"
lname="Vishwakarma"
city="Kanpur"
print(s.format(name,lname,city))

#but after 3.6 f-strings came into existance 

print(f"My name is {name} {lname} and I am from {city}")

n=43.222454646
print(f"decimal value upto 2 decimal {n:.2f}")

#we can also save f-strings in a variable 
#if you want to print f-strings as it is 

print(f"My name is {{name}} {{lname}} and I am from {{city}}")