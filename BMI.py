import time
print("--------팩트폭력 BMI 측정기--------")
time.sleep(1)
print("--------컴퓨터는 정확합니다.--------")
time.sleep(1)

while(1):
    while(1):
        height = input("\n\n당신의 키를 입력해주세요. [m단위로] 저장되지 않습니다.\n>>>")
        try :
            height = float(height)
            break
        except :
            print("숫자를 입력하세요. 제발.\n")

    while(1):
        weight = input("\n당신의 몸무게를 입력해주세요. [kg단위로] 저장되지 않습니다.\n>>>")
        try :
            weight = float(weight)
            break
        except:
            print("몸무게가 숫자가 아니시군요. 대단하십니다.\n")

    BMI = weight/((height)**2)

    if BMI < 18.5:
        print("계산중...")
        time.sleep(2)
        print("\n마른 체형이시군요! 밥좀 많이 드세요. BMI는 %s입니다." %(BMI))
    elif 18.5 <= BMI <= 25.0:
        print("계산중...")
        time.sleep(2)
        print("\n표준 체형이시군요. 아주 좋습니다. BMI는 %s입니다." %(BMI))
    elif 25.0 < BMI < 30.0:
        print("계산중...")
        time.sleep(2)
        print("\n통통하시네요. 귀엽습니다. BMI는 %s입니다." %(BMI))
    elif BMI >= 30.0:
        print("계산중...")
        time.sleep(2)
        print("\n고도비만이시네요... 밥좀 그만 드세요. BMI는 %s입니다." %(BMI))

    print("-------------------------------------------------------------")
