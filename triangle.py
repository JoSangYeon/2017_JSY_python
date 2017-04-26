print("삼각형의 세 변을 입력하세요.")
a = float(input())
b = float(input())
c = float(input())
tri = [a,b,c]
tri.sort()
x = tri[0]
y = tri[1]
z = tri[2]
if x+y<z:
    print("삼각형이 아닙니다.")
elif x**2+y**2==z**2:
    print("입력한 세 변을 가진 삼각형은 직각삼각형입니다.")
elif x**2+y**2>z**2:
    print("입력한 세 변을 가진 삼각형은 예각삼각형입니다.")
elif x**2+y**2<z**2:
    print("입력한 세 변을 가진 삼각형은 둔각삼각형입니다.")
