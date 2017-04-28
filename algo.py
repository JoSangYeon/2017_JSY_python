m30 = [4, 6, 9, 11]
m31 = [1, 3, 5, 7, 8, 10, 12]
m28 = [2]
w = ["월", '화', '수', '목', '금', '토', '일']


def chkyoon(y):
    return y % 400 == 0 or y % 100 != 0 and y % 4 == 0


date = input("기준일의 날자를 입력하세요(예 >> 20171225) : ")
y = int(date[0:4])
m = int(date[5:6])
d = int(date[7:8])
n = int(input("기준일로부터 며칠 후의 날자와 요일을 알고싶습니까? : "))

while(1):
    if chkyoon(y) == True:
        if n - 366 > 0:
            n = n - 366
            y = y + 1
        else:
            break
    if chkyoon(y) == False:
        if n - 365 > 0:
            n = n - 365
            y = y + 1
        else:
            break

while(1)
    if m in m30:
        if n - 30 > 0:
            n = n - 30
            if m > 12:
                m = 1
                y = y + 1
            else:
                m = m + 1
    if m in m31:
        if n - 31 > 0:
            if m > 12:
                n = n - 31
                m = 1
                y = y + 1
            else:
                m = m + 1
    if m in m28:
        if chkyoon(y) == True:
            if n - 29 > 0:
                m =
