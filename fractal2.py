import turtle, queue
import copy

t = turtle.Turtle()

angle = 30
t.speed("slowest")
t.pensize(5)

if __name__ == "__main__":
    linelength = int(input("Please input the linelength : "))
    t.left(90)
    tq = queue.Queue()
    lq = queue.Queue()
    tq.put(t.clone())
    lq.put(linelength)
    t.hideturtle()
    while not tq.empty() :
        cur_turtle = tq.get()
        cur_length = lq.get()
        if cur_length <= 0 :
            cur_turtle.hideturtle()
            continue
        cur_turtle.forward(cur_length)
        cur_turtle.left(angle)
        tq.put(cur_turtle.clone())
        lq.put(cur_length - 10)
        cur_turtle.right(angle * 2)
        tq.put(cur_turtle.clone())
        lq.put(cur_length - 10)
        cur_turtle.left(angle)
        cur_turtle.backward(cur_length)
        cur_turtle.hideturtle()
    input("Please input stop : ")
