import turtle

def draw(color,posx,posy,width = 10):
        turtle.up()
        turtle.goto(posx,posy)
        turtle.down()
        turtle.color(color)
        turtle.begin_fill()
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.end_fill()
        turtle.up()

turtle.setup(500,500)
turtle.title("sherlongtest1")
turtle.hideturtle()
turtle.tracer(False)
turtle.done()

while True :
    draw("red",100,100)