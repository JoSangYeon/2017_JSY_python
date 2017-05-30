# 묵찌빠
print("-----묵찌빠 게임을 시작합니다-----")
print("게임을 종료하려면 end를 입력하세요.")
d = "0"
import random

# 가위바위보에서 이겼을때의 상황


def win():
    print("당신이 공격할 차례입니다.")
    d = input("묵, 찌, 빠 중 하나를 입력하세요: ")
    rand = random.randint(1, 3)
    if rand == 1:
        print("컴퓨터 : 찌")
        if d == "묵":
            win()
        elif d == "찌":
            print("이겼습니다.")
        elif d == "빠":
            lose()
    elif rand == 2:
        print("컴퓨터: 묵")
        if d == "찌":
            lose()
        elif d == "묵":
            print("이겼습니다.")
        elif d == "보":
            win()

    elif rand == 3:

        print("컴퓨터: 빠")
        if d == "빠":
            print("이겼습니다")
        elif d == "묵":
            lose()
        elif d == "찌":
            win()


def lose():
    print("컴퓨터가 공격할 차례입니다.")
    d = input("묵, 찌, 빠 중 하나를 입력하세요: ")

    rand = random.randint(1, 3)

    if rand == 1:

        print("컴퓨터: 묵")

        if d == "찌":
            lose()

        elif d == "빠":
            win()

        elif d == "묵":
            print("졌습니다.")

    elif rand == 2:

        print("컴퓨터: 묵")

        if d == "찌":
            lose()

        elif d == "묵":
            print("졌습니다.")

        elif d == "빠":
            win()

    elif rand == 3:

        print("컴퓨터: 빠")

        if d == "찌":
            win()

        elif d == "묵":
            print("졌습니다")
            print()
            print("--------------------")

        elif d == "보":
            lose()


def draw():
    print("가위바위보를 할 차례입니다.")
    d = input("가위, 바위, 보 중 입력하세요: ")

    rand = random.randint(1, 3)

    if rand == 1:

        print("컴퓨터: 가위")

        if d == "가위":
            draw()

        elif d == "바위":
            win()

        elif d == "보":
            lose()

    elif rand == 2:

        print("컴퓨터: 바위")

        if d == "가위":
            lose()

        elif d == "바위":
            draw()

        elif d == "보":
            win()

    elif rand == 3:

        print("컴퓨터: 보")

        if d == "가위":
            win()

        elif d == "바위":
            lose()

        elif d == "보":
            draw()


while 1:
    draw()
