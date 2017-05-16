year = int(input('윤년 판별을 원하는 년도를 입력하세요: '))
yun = 'Nothing'


if year%4 == 0:
    yun=True
    if year%100 == 0:
        yun = False
        if year%400 == 0:
            yun = True
else:
    yun = False

if yun == False:
    print(year,'년은 윤년이 아닙니다.')
else:
    print(year,'년은 윤년입니다.')
