import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print("숫자 추측하기 게임을 시작합니다")
print("1부터 99까지의 숫자중 임의의 숫자를 6번의 기회 안에 맞히면 승리합니다.")
while guess != secret and tries < 6:
    guess = int(input("숫자를 입력하세요 : "))
    if guess < secret:
        print("입력한 숫자는 정답보다 작습니다.")
    elif guess > secret:
        print("입력한 숫자는 정답보다 큽니다.")
    if guess == 3141592:
        print(secret)

    tries = tries + 1

if guess == secret:
    print("정답입니다!")
else:
    print("기회를 모두 소진하였습니다.")
    print("정답은", secret, "입니다. ")
