# make a geometric rainbow pattern
import turtle
# pick order of colors for the hexagon
colors = ['red', 'yellow', 'blue', 'orange', \
'green', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black') # turn background black
# make 36 triangles, each 30 degrees apart
for n in range(36):
# make triangle
    for i in range(3):
        shelly.color(colors[i]) # pick color at position i
        shelly.forward(100)
        shelly.left(120)
    # add a center shift fwd 5 each iteration and 30deg turn before the next triangle
    shelly.forward(n*5)
    shelly.right(30)
# hide turtle to finish the drawing
shelly.hideturtle()
