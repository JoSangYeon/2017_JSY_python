print("-----함수 그래프 출력기-----")
range_start = int(input("함수 정의역의 시작점을 입력하세요 : "))
range_end = int(input("함수 정의역의 끝점을 입력하세요 : "))
import math
import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed(100)
t.forward(-500)
t.forward(1000)
t.home()
t.right(90)
t.forward(-500)
t.forward(1000)
t.home()
t.pensize(4)
t.penup()


def f(x):
    y = 50 * math.tan(x / 40)
    return y


for x in range(range_start, range_end):
    t.goto(x, f(x))
    t.dot(4)
    t.pendown()


input()
