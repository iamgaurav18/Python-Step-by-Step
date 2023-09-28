a=input("ENter a number :")
try:
    for i in range(1,11):
        print(f"{int(a)}x{int(i)}={int(a*i)}")
except Exception as e:     #you can also avoid writing Exception as e if you never intend to use it 
    print(type(e).__name__)     #to print the type of exceptions

print("Excepiton handled")