# import turtle 
# turtle.Screen().bgcolor("red")
# turtle.Screen().setup(500,650)
# Polygon=turtle.Turtle()
# num_side=7
# num_lenght=85
# angle=360.0/num_side
# for i in range(num_side):
#     Polygon.forward(num_lenght)
#     Polygon.right(angle)
# turtle.done()

# import turtle
# turtle.Screen().bgcolor("blue")
# star=turtle.Turtle()
# star.forward(100)
# star.left(120)
# star.forward(100)
# star.left(120)
# star.forward(100)
# star.penup()
# star.right(150)
# star.forward(50)
# star.pendown()
# star.right(90)
# star.forward(100)
# star.right(120)
# star.forward(100)
# star.right(120)
# star.forward(100)
# turtle.done()

import turtle
a=turtle.Screen()
a.bgcolor("yellow")
x=turtle.Turtle()
y=0
while True:
    for i in range(4):
        x.forward(y+1)
        x.left(90)
        y=y-5
    y=y+1 