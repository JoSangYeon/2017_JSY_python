import time

n = input("Please input the number : ")

def lopi(n):
    if (n == 1 or n == 2):
        return 1
    fn = 0
    fn_1 = 1
    fn_2 = 1
    for i in range(n+1):
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn
    return fn

start = time.time()
print(lopi(n))
print("Time passed : ",time.time() - start,"sec")
