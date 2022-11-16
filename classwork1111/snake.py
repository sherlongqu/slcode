import random
import turtle


global window_length
window_length = 500
global window_width
window_width = 500
global window_step
window_step = 10
global window_name
window_name = "snake"

global window_start_coordinate_x
window_start_coordinate_x = int(window_length / 2 * -1)
global window_start_coordinate_y
window_start_coordinate_y = int(window_width / 2 * -1)

global window_end_coordinate_x
window_end_coordinate_x = int(window_length / 2 + 1)
global window_end_coordinate_y
window_end_coordinate_y = int(window_width / 2 + 1)

global point_x
point_x = list(range(window_start_coordinate_x,window_end_coordinate_x,window_step))
global point_y
point_y = list(range(window_start_coordinate_y,window_end_coordinate_y,window_step))


snake_length = []
snake_body_x = []
snake_body_y = []


class draw():


    def draw_background_grid(color):

        for dbglength in list(point_y):
            turtle.up()
            turtle.goto(int(window_length / 2 * -1),dbglength)
            turtle.down()
            turtle.color(color)
            turtle.forward(window_length)

        turtle.left(90)

        for dbgwidth in list(point_x):
            turtle.up()
            turtle.goto(dbgwidth,int(window_width / 2 * -1))
            turtle.down()
            turtle.color(color)
            turtle.forward(window_width)


    def draw_block(color,locationx,locationy):

        turtle.up()
        turtle.goto(locationx,locationy)
        turtle.down()
        turtle.color(color)
        turtle.begin_fill()
        for dbstep in [1,2,3,4]:
            turtle.forward(window_step)
            turtle.right(90)
        turtle.end_fill()
        turtle.up()


    def draw_food():

        dfcolor = "red"
        dflocationx = random.choice(point_x)
        dflocationy = random.choice(point_y)
        draw.draw_block(dfcolor,dflocationx,dflocationy)


    def draw_snake():

        dscolor = "black"
        draw.draw_block(dscolor,snake_body_x,snake_body_y)


def snake():

    global snake_length
    snake_length = 5
    global snake_body_x
    snake_body_x = list(range(int(snake_length / 2 * -1) * window_step,int(snake_length / 2) * window_step,window_step))
    global snake_body_y
    snake_body_y = list(range(int(snake_length / 2 * -1) * window_step,int(snake_length / 2) * window_step,window_step))


class operate():


    def operate_keyboard():

        123


def window():

    turtle.setup(int(window_length),int(window_width))
    turtle.title(window_name)
    turtle.hideturtle()
    turtle.tracer(False)


def test():

    window()
    draw.draw_background_grid("gainsboro")
    draw.draw_food()
    draw.draw_snake()
    turtle.done()

test()