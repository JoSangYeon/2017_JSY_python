print("----------요일 판별기----------")
print("종료하시려면 0을 입력하세요")
print()
today = input("오늘의 날자를 입력하세요(예 >> 20171225) : ")
destination = int(input("몇일 후의 요일을 알고싶으신가요?"))

y = int(today[0:4])
m = int(today[5:6])
d = int(today[7:8])

m30 = [4, 6, 9, 11]
m31 = [1, 3, 5, 7, 8, 10, 12]
m28 = [2]
yoon = False
n = 0
w = ["월", '화', '수', '목', '금', '토', '일']

def chkyoon(y):
    # 400으로 나눠지면 반드시 윤년이고, 100으로 나눠지면 4로 반드시 나눠진다.
    return y % 400 == 0 or y % 100 != 0 and y % 4 == 0

# 년 누적 날자
for a in range(1, y):
    if chkyoon(a) == True:
        n = n + 366
    else:
        n = n + 365

# 월 누적 날자
for b in range(1, m):
    if b in m30:
        n = n + 30
    if b in m31:
        n = n + 31
    if b in m28:
        if chkyoon(y) == True:
            n = n + 29
        else:
            n = n + 28

# 일 누적 날자
n = n + d - 1

#최종누산
n = n + destination
n = n % 7

print("%s요일입니다." % w[n])
