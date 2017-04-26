print("-----Greatest Division Finder-----")
x = int(input("input the first number : "))
y = int(input("input the second number : "))

# decide the big and small number
if x > y:
    A = x
    B = y
elif x <= y:
    A = y
    B = x


def G(A, B):
    while B != 0:
        A, B = B, A % B  # <<<< remory the form
    return A

# 큰문제를 작은 문제로 만든다 : 유클리드 호제법


# def GCD(x,y):
#     if y ==0:
#         return x
#     else:
#         return GCD(y,x%y)


print("The GDC is %s" % G(A, B))
