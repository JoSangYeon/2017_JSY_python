import random
import easygui
secret = random.randint(1, 99)
guess = 0
tries = 0
easygui.msgbox("숫자 추측하기 게임을 시작합니다, 1부터 99까지의 숫자중 임의의 숫자를 6번의 기회 안에 맞히면 승리합니다.")
while guess != secret and tries < 6:
    guess = easygui.integerbox("숫자를 입력하세요.")
    if not guess:
        break
    if guess < secret:
        easygui.msgbox(str(guess) + " 입력한 숫자는 정답보다 작습니다.")
    elif guess > secret:
        easygui.msgbox(str(guess) + " 입력한 숫자는 정답보다 큽니다.")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("정답입니다!")
else:
    easygui.msgbox("기회를 모두 소진하였습니다. 정답은 " + str(secret) + " 입니다 .")
