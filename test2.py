n = int(input("Please input the number of table : "))
print("----------------")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i + (n - 1) * (j - 1), end=" ")
    print()
