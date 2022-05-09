print('삼각형의 각 변을 입력하세요.(단 c<=b<=a 이다)')
print('삼각형의 결정 조건은 b+c>a 입니다(단 a는 가장 긴변)')

print()
a = float(input('첫번째 변의 길이를 입력하세요.: '))
b = float(input('두번째 변의 길이를 입력하세요.: '))
c = float(input('세번째 변의 길이를 입력하세요.: '))

#입력받은 a,b,c값을 리스트 ABC에 넣습니다.
ABC = [a, b, c]
# sort문으로 a,b,c를 정렬합니다.
ABC.sort()
x = ABC[0]
y = ABC[1]
z = ABC[2]

def angle(x,y,z):
    # 각 조건에 맞았을때 출력하게끔 합니다.
    if x+y>z and z**2==x**2+y**2:
        print('직각삼각형입니다.')
        return 1
    elif x+y>z and z**2>x**2+y**2:
        print('둔각삼각형입니다.')
        return 2
    elif x+y>z and z**2<x**2+y**2:
        print('예각삼각형입니다.')
        return 0
    if x+y<=z:
        print('삼각형이 될 수 없는 조건입니다.')
        return 3


print(angle(x,y,z))
