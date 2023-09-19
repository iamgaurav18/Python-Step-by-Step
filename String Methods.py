#Strings are immutable
a="gaurav"

#upper and lower
print(a.upper())
print(a.lower())

#Replace all occurances 
print(a.replace("a","i"))

#Splitting a string based ona character it could be space also

print(a.split("a"))

#capitaliize method: it will capitalize the first character of a string
print(a.capitalize())

#center : it will print the string n-len of string left from right side 
print(a.center(50))

#Count : it will return the count of a substring that is present in a string
print(a.count('a'))

#endswith : to check if a string ends wiht a substring
print(a.endswith('u'))

#we can even check for a substring if it is ending with a substring 
print(a.endswith('r',1,4))

#find() it will return first occurance of a substring in a string
print(a.find('a')) # even if 'a' is not there in Gaurav it will return -1 

#we have a similar method index to find index of a substring in a string.
print(a.index('u'))  # this will throw an exception since e is not present in Gaurav.

#isalnum check if string is alphanumeric
print(a.isalnum())
print(a.isalpha())
print(a.isnumeric())

#isprintable return true if all the character in that string are printable
print("\nguarav".isprintable()) #this will return false since \n is not printable

#isspace return true if string contains only spaces
print("   ".isspace())

#startwith returns true if a string starts with a substring
print(a.startswith('G')) # it is case sensitive

#swapcase it will swap cases of each character in a string
print("balLE BaLle".swapcase())