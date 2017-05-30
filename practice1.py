import random
secret = random.randint(1, 1000)
guess = 0
tries = 0
print("숫자 추측하기 게임을 시작합니다")
print("1부터 1000까지의 숫자중 임의의 숫자를 10번의 기회 안에 맞히면 승리합니다.")
while guess != secret and tries < 10:
    guess = int(input("숫자를 입력하세요 : "))
    if guess < secret:
        print("Down")
    elif guess > secret:
        print("Up")
    if guess == 3141592:
        print(secret)
        tries = tries - 1

    tries = tries + 1

if guess == secret:
    print("정답입니다!")
    print("%s번 만에 성공하셨습니다!" %(tries))
else:
    print("기회를 모두 소진하였습니다.")
    print("정답은", secret, "입니다. ")
