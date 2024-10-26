import turtle
turtle.Screen().bgcolor("Cyan")
turtle.Screen().title("Pyramid by Sunkanmi")
pen=turtle.Turtle()
Size=0
while True:
    for i in range(4):
        pen.forward(Size+1)
        pen.left(90)
        Size=Size-5
    Size=Size+1