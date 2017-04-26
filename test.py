size = int(input("Please enter the size of Square : "))

for i in range(1, size):
    if i == 1:
        print("*" * size)
    if i == size - 1:
        print("*" * size)
    else:
        print("*" + "+" * (size - 2) + "*")
