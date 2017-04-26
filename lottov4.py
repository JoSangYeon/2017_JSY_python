import random

lotto_num_set = set()

while lotto_num_set.__len__() < 5:
    lotto_num = random.randint(1,45)
    lotto_num_set.add(lotto_num)

print(sorted(lotto_num_set))
