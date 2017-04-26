import random

s = set()

while s.__len__() < 5:
    ball1 = random.randint(1, 45)
    s.add(ball1)

    ball2 = random.randint(1, 45)
    s.add(ball2)

    ball3 = random.randint(1, 45)
    s.add(ball3)

    ball4 = random.randint(1, 45)
    s.add(ball4)

    ball5 = random.randint(1, 45)
    s.add(ball5)


print(ball1, ball2, ball3, ball4, ball5)
