import time
print("------------윤년판별기--------------")
print("      종료하시려면 0을 입력하세요.     ")
year = 1230897341290783429078341279
yoon = False
while year != 0:
    year = int(input("윤년을 판별할 연도를 입력하세요 : "))

    if year % 4 == 0:
        yoon = True
        if year % 100 == 0:
            yoon = False
            if year % 400 == 0:
                yoon = True

    if yoon == True:
        print("입력한 연도는 윤년입니다.")
    elif yoon == False:
        print('입력한 연도는 윤년이 아닙니다.')


# 문장을 논리영어로
# 알고리즘을 세세하게 작성
# 이 전에 우리말 논리를 명쾌하게
