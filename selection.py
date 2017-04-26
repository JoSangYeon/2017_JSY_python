import random
import time
n = int(input("Please input the range of list : "))
l = list(range(n))
random.shuffle(l)


def select(l, n):
    select_num = l[0]
    select_idx = 0
    for i in range(n):
        if l[i] > select_num:
            select_num = l[i]
            select_idx = i
    l[n - 1], l[select_idx] = select_num, l[n - 1]  # <<<


def select_sort(l, n):
    for i in range(n):
        select(l, n - i)
    print(l)


start = time.time()
select_sort(l, n)
print(time.time() - start)
