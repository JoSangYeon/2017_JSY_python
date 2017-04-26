print("-----최대공약수를 판별할 두 수를 입력하세요-----")
x = int(input("첫번째 수 : "))
y = int(input("두번째 수 : "))
G = 0
for j in range(1, x + 1):
    if y % j == 0 and x % j == 0:
        G = j

print("최대공약수는 %d입니다" % (G))
