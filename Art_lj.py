# make a geometric rainbow pattern
import turtle
# pick order of colors for the hexagon
colors = ['red', 'yellow', 'blue', 'orange', \
'green', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black') # turn background black
# make 8 triangles, each 30 degrees apart
for n in range(8):
# make triangle by repeating 2 times
    for i in range(2):
        shelly.color(colors[i]) # pick color at position i
        shelly.forward(100)
        shelly.left(120)
    # add a turn before the next triangle
    shelly.right(45)

# get ready to draw 8 circles
shelly.penup()
shelly.color('white')
# repeat 8 times to match the 8 triangles
for i in range(8):
    shelly.forward(220)
    shelly.pendown()
    shelly.circle(5)
    shelly.penup()
    shelly.backward(220)
    shelly.right(45)
# hide turtle to finish the drawing
shelly.hideturtle()