import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
angle = 30
t.speed("slowest")
t.pensize(5)

def fractal(t, linelength):
    if linelength > 0:
        t.forward(linelength)
        t.left(angle)
        fractal(t,linelength-10)
        t.right(angle)
        t.right(angle)
        fractal(t,linelength-10)
        t.left(angle)
        t.backward(linelength)


if __name__ == "__main__":
    linelength = int(input("Please input the linelength : "))
    t.left(90)
    t2.forward(100)
    fractal(t,linelength)
    input("Please input stop : ")
