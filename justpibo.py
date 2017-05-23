import math
import time
n = int(input("Please input the number : "))
def jufi(n):
    result = int((1/math.sqrt(5)) * ((((1 + math.sqrt(5))/2)**n) - (((1 - math.sqrt(5))/2)**n)))
    return result

start = time.time()
print(pibo(n))
print("Time Passed : ",time.time() - start,"sec")
