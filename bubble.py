import random
import time
n = int(input("Please input the range of list : "))
l = list(range(n))
random.shuffle(l)


def bubble_sort(l, n):
    for i in range(n):
        for j in range(1, n):
            print(l)
            if l[j - 1] > l[j]:
                l[j - 1], l[j] = l[j], l[j - 1]
    print(l)


start = time.time()
bubble_sort(l, n)
print(time.time() - start)
