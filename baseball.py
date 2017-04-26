print("-----야구게임을 시작합니다----")
import random

#정답과 변수 설정
a = list(range(1, 10))
random.shuffle(a)
answer = [a[0], a[1], a[2]]
count = 0
sn = 0
on = 0

# a = set()
# while a.__len__() < 2:
#     a1 = random.randint(1,9)
#     a2 = random.randint(1,9)
#     a3 = random.randint(1,9)
#     a.add(a1)
#     a.add(a2)
#     a.add(a3)
# 이러면 2개만 뽑히는 오류 발생

#사용자의 추측 입력받음
while (1):
    while (1):
        user = input("정답을 입력하세요 : ")
        if len(user) != 3:
            print("정답은 세 자리수 숫자여야 합니다.")
        else:
            user = [int(user[0]), int(user[1]), int(user[2])]
            break

#스트라이크 개수 세기
    for i in range(3):
        if answer[i] == user[i]:
            sn = sn + 1

#아웃 개수 세기
    for k in user:
        if answer.count(k) == 0:
            on = on + 1

#볼 개수 세기
    bn = 3 - sn - on

#결과 출력 및 개수 초기화
    print("\n%d스트라이크 %d볼 %d아웃입니다.\n" % (sn, bn, on))
    count = count + 1
    if sn ==3:
        print("정답입니다!", "%d번 만에 성공하셨습니다." % (count))
        break
    sn = 0
    bn = 0
    on = 0
    print("---------------------")
