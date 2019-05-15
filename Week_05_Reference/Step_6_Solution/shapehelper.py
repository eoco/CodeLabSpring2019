import turtle


def custom_circle(pen, red, green, blue, size):
    pen.color(red, green, blue)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()


def custom_square(pen, red, green, blue, size):
    pen.color(red, green, blue)
    pen.begin_fill()
    for i in range(1, 5):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()


if __name__ == '__main__':
    t = turtle.Pen()
    custom_circle(t, 1, 0, 0, 200)
    custom_square(t, 0, 0, 1, 100)
    turtle.write("import me in the shell for best results!") # turtle has a 'write' command to write text to canvas. This command can take additional arguments affecting font, size and placement
    print("You can import this into a python shell to help draw in Turtle") # this will write a line to the shell for the user to read
    turtle.exitonclick()
