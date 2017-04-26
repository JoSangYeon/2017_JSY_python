import random

a = random.randint(1, 100000000)
b = random.randint(1, 100000000)
c = random.randint(1, 100000000)

max = (b if b > a else a) if b > c or a > c else c

if a == max:
    print("a is max and value is %d" % (max))

if b == max:
    print("b is max and value is %d" % (max))

if c == max:
    print("c is max and value is %d" % (max))
