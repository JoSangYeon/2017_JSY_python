import turtle
t = turtle.Turtle()
s = turtle.Screen()

t.speed(3)
t.pensize(3)

t.penup()
t.goto(0, -150)
t.pendown()

t.forward(300)  #집 밑부분을 그립니다.
t.left(90)
t.forward(250)
t.left(90)
t.forward(600)
t.left(90)
t.forward(250)
t.left(90)
t.forward(300)

t.penup()
t.goto(-300, 100)
t.pendown()

t.goto(0,300)   #집 지붕 부분을 그립니다.
t.goto(300, 100)

t.penup()
t.goto(-200,30)
t.pendown()

x=-200  #좌표를 저장
y=30

for i in range(4):  #창문을 그립니다.
          t.forward(80)
          t.right(90)

t.pensize(1)    # 창문틀을 그립니다.

t.goto(x+40, y)
t.goto(x+40, y-80)

t.penup()
t.goto(x+80,y-40)
t.pendown()
t.goto(x,y-40)

x = 150
y = 30

t.color('brown')    #문을 그립니다.
t.pensize(4)
t.penup()
t.goto(x, y)
t.pendown()

for u in range(2):  # 문틀을 그립니다.
    t.forward(80)
    t.right(90)
    t.forward(180)
    t.right(90)

t.color('black')    # 문손잡이를 그립니다.
t.penup()
t.goto(x+20, y-90)
t.pendown()
t.dot(20)

x=-200
y=150

t.color('green')    #제 이름 '조상연'의 초성 'JSY'를 그립니다.
t.speed(3)
t.pensize(1)
t.penup()
t.goto(x,y)
t.pendown()

t.forward(30)   # J
t.forward(-15)
t.right(90)
t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(10)
t.right(90)

t.penup()
t.goto(x+70,y)
t.pendown()

t.forward(-30)  # S
t.right(90)
t.forward(20)
t.right(-90)
t.forward(30)
t.right(90)
t.forward(20)
t.right(-90)
t.forward(-30)

t.penup()
t.goto(x+80, y)
t.pendown()

t.goto(x+100, y-20)   # Y
t.goto(x+120, y)
t.penup()
t.pendown()
t.goto(x+100, y-20)
t.goto(x+100, y-40)

t.penup()           #터틀 그래픽스로 집그리기 완성입니다 ^^
t.goto(x+120, y-40)
t.dot(6)
t.penup()
t.goto(0,0)
