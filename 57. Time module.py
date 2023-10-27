import time

def count():
    for i in range(50000):
        i=i+1
    return i

t=time.time()       # time.time() returns the total number of seconds that have been passed till present from 1970
print(count())
t2=time.time()
print(f"Time  taken by function count : {t2-t}")
time.sleep(3)       # this will make the next line of code be executed after 3 seconds
print("This message is printted after 3 seconds")

t3=time.localtime()    # this will return the local time in seconds
ftime=time.strftime("%d-%m-%Y %H:%M:%S",t3)       # this will print the local time in your desired format
print(ftime)