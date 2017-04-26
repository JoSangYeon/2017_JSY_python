n = int(input("n을 입력하세요 : "))
for k in range(1, n + 1):
    print(" " * (n + 1 - k), end="")
    print("*" * k, end="")
    print()
