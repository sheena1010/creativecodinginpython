# make a geometric rainbow pattern
import turtle
# pick order of colors for the hexagon
colors = ['red', 'yellow', 'blue', 'orange', \
'green', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black') # turn background black
# make 64 pentagons, each 8 degrees apart
for n in range(64):
# make pentagon
    for i in range(5):
        shelly.color(colors[i]) # pick color at position i
        shelly.forward(30)
        shelly.left(72)
    # add a center shift fwd 5 each iteration and 15deg turn before the next triangle
    shelly.forward(n*3)
    shelly.right(32)
# hide turtle to finish the drawing
shelly.hideturtle()
