print('요일을 판별해보자!!')
print()
year = int(input('년도를 입력하세요: '))
month = int(input('달을 입력하세요: '))
date = int(input('일을 입력하세요: '))
print()


day = 0    #1년 1월 1일을 0일로 시작합니다


#윤년일때 366일을 아닐때 365일을 더합니다.
for i in range(1, year):
    if ((i % 4 == 0) and (i % 100 != 0)) or (i % 400 ==0):
        day += 366
    else:
        day += 365


# 윤년일때와 아닐때의 각자 다른 달 수를 if문으로 계산합니다.
for i in range(1, month):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400==0):    #윤년일때
            if i == 1:
                day += 31
            if i == 2:
                day += 29
            if i ==3:
                day += 31
            if i ==4:
                day += 30
            if i ==5:
                day += 31
            if i ==6:
                day += 30
            if i ==7:
                day += 31
            if i ==8:
                day += 31
            if i ==9:
                day += 30
            if i ==10:
                day += 31
            if i ==11:
                day += 30
            if i ==12:
                day += 31
    else:                                                             #윤년이 아닐때
            if i == 1:
                day += 31
            if i == 2:
                day += 28
            if i ==3:
                day += 31
            if i ==4:
                day += 30
            if i ==5:
                day += 31
            if i ==6:
                day += 30
            if i ==7:
                day += 31
            if i ==8:
                day += 31
            if i ==9:
                day += 30
            if i ==10:
                day += 31
            if i ==11:
                day += 30
            if i ==12:
                day += 31


#1년 1월 1일이 0일째이기 때문에 date(날짜)에서 1을 뺍니다.
day = day + (date-1)
total_day = (day)%7


#요일 추정 결과를 출력합니다.
if total_day == 0:
    print(year,'년', month, '월', date, '일은 월요일입니다.')
if total_day == 1:
    print(year,'년', month, '월', date, '일은 화요일입니다.')
if total_day == 2:
    print(year,'년', month, '월', date, '일은 수요일입니다.')
if total_day == 3:
    print(year,'년', month, '월', date, '일은 목요일입니다.')
if total_day == 4:
    print(year,'년', month, '월', date, '일은 금요일입니다.')
if total_day == 5:
    print(year,'년', month, '월', date, '일은 토요일입니다.')
if total_day == 6:
    print(year,'년', month, '월', date, '일은 일요일입니다.')
print('1년 1월 1일로 부터 총', day, '일이 지났습니다.')
