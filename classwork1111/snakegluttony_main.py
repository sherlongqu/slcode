import turtle

caption_width = 500
caption_height = 500

if __name__ =='__main__':
    turtle.setup(caption_width,caption_height)
    turtle.title("GameSnakegluttony")
    turtle.hideturtle()
    turtle.tracer()
    turtle.done()
    def draw_block(color,posx,posy,width = 10):
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
    draw_block("blue",200,200)