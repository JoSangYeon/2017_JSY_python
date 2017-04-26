n = int(input("컴퓨터를 얼마나 고문시킬까요? : "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, "*", j, "=", (i * j))
