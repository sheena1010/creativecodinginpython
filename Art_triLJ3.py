# make a geometric rainbow pattern
import turtle
# pick order of colors for the hexagon
colors = ['red', 'yellow', 'blue', 'orange', \
'green', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black') # turn background black
# make 8 triangles, each 30 degrees apart
for n in range(8):
# make triangle
    for i in range(2):
        shelly.color(colors[i]) # pick color at position i
        shelly.forward(100)
        shelly.left(120)
    # add a turn before the next triangle
    shelly.right(45)
# hide turtle to finish the drawing
shelly.hideturtle()
