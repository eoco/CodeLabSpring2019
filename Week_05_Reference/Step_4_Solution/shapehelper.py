import turtle

t = turtle.Pen()

def custom_circle(red, green, blue, size):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

def custom_square(red, green, bl)ue, size):
    t.color(red, green, blue)
    t.begin_fill()
    for i in range(1, 5):
        t.forward(size)
        t.left(90)
    t.end_fill()


custom_circle(1, 1, 0, 100)
t.up()
t.forward(100)
t.down()
custom_square(0, 0, 1, 100)

turtle.exitonclick()
