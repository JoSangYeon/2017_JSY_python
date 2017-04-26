import random
import time
start = time.time()
n = int(input("리스트의 범위 : "))
l = list(range(n))
random.shuffle(l)
print(l.sort())
print(time.time() - start)
