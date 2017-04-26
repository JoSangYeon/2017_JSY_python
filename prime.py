import math
n = int(input("숫자를 입력하세요 : "))


def is_prime_number(k):
    for i in range(2, k):
        if k % i == 0:
            return False
    return True


for i in range(2, n + 1):
    prime = is_prime_number(i)
    if prime == True:
        print(i, end=", ")
