print("-----야구게임을 시작합니다----")
import random

# 정답과 변수 설정
a = list(range(1, 10))
random.shuffle(a)
answer = [a[0], a[1], a[2]]
count = 0
sn = 0
on = 0

# a = set()
# while a.__len__() < 3:
#     a1 = random.randint(1,9)
#     a2 = random.randint(1,9)
#     a3 = random.randint(1,9)
#     a.add(a1)
#     a.add(a2)
#     a.add(a3)
# 이러면 2개만 뽑히는 오류 발생

while (1):  # 맞출 때까지 아래의 항목을 반복
    while (1):
        user = input("정답을 입력하세요 : ")
        if len(user) != 3:  # 에러처리부분
            print("정답은 세 자리수 숫자여야 합니다.")
        else:
            user = [int(user[0]), int(user[1]), int(user[2])]  # 사용자 리스트 작성
            break

# 스트라이크 개수 세기
    for i in range(3):
        if answer[i] == user[i]:  # 정답 리스트의 i 번쨰에 있는 숫자가 사용자가 입력한 리스트의 i 번째에 있는 와 같으면
            sn = sn + 1  # 스트라이크 개수 + 1

# 아웃 개수 세기
    for k in user:
        # 사용자 리스트에 입려된 숫자가 정답 리스트에 없으면 >> count(k) == 0:
        if answer.count(k) == 0:
            on = on + 1

# 볼 개수 세기
    bn = 3 - sn - on  # 스트라이크 볼 아웃 합쳐서 3개를 넘지 않음 볼 알고리즘 복잡;

# 결과 출력 및 개수 초기화
    print("\n%d스트라이크 %d볼 %d아웃입니다.\n" % (sn, bn, on))
    count = count + 1
    if sn == 3:
        print("정답입니다!", "%d번 만에 성공하셨습니다." % (count))
        break
    sn = 0
    bn = 0
    on = 0
    print("---------------------")
