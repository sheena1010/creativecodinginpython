# make a geometric rainbow pattern
import turtle
# pick order of colors for the hexagon
colors = ['red', 'yellow', 'blue', 'orange', \
'green', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black') # turn background black
# make 128 triangles, each 360/128 degrees apart
for n in range(128):
# make triangle
    for i in range(3):
        shelly.color(colors[i]) # pick color at position i
        shelly.forward(30)
        shelly.left(120)
    # add a center shift fwd 5 each iteration and 30deg turn before the next triangle
    shelly.forward(n*5)
    shelly.right(2.8125)
# hide turtle to finish the drawing
shelly.hideturtle()
