def Euclid():
    for i in range(1,x+1):
        if (x%i==0):
            if (y%i==0):
                Z.append(i)
    Z.sort(reverse=True)
    return Z[0]

a = int(input('a를 입력하세요.: '))
b = int(input('b를 입력하세요.: '))

AB = [a, b]
AB.sort()
x = AB[0]
y = AB[1]
Z = []

print('최대공약수는', end=(' '))
print(Euclid(), end=(' '))
print('입니다.')
