import turtle
turtle.Screen().bgcolor("Green")
turtle.Screen().setup(500,750)
polygon=turtle.Turtle()
num_sides=6
len_sides=70
angl=360.0/num_sides
for i in range(num_sides):
    polygon.forward(len_sides)
    polygon.right(angl)
turtle.done()