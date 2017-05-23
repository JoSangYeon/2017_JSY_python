import math
import time

n = int(input("Please input number : "))

def lofi(n):
    if (n == 1 or n == 2):
        return 1
    fn = 0
    fn_1 = 1
    fn_2 = 1
    for i in range(n-2):
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn
    return fn

def jufi(n):
    result = int((1/math.sqrt(5)) * ((((1 + math.sqrt(5))/2)**n) - (((1 - math.sqrt(5))/2)**n)))
    return result

def refi(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return refi(n-1) + refi(n-2)

print("jufi start")
start = time.time()
print(jufi(n))
print("Time Passed : ",time.time() - start,"sec\n")

print("lofi start")
start = time.time()
print(lofi(n))
print("Time Passed : ",time.time() - start,"sec\n")

print("refi start")
start = time.time()
print(refi(n))
print("Time Passed : ",time.time() - start,"sec\n")
