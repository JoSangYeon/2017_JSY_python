n = int(input("Please input the number : "))
def sigma(n):
    if n == 1:
        return n
    else :
        return n + sigma(n-1)

print(sigma(n))
