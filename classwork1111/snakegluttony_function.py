import random
import turtle

caption_width = 500
caption_height = 500

if __name__ =='__main__':
    turtle.setup(caption_width,caption_height)
    turtle.title("GameSnakegluttony")
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.done()

snake = [[0,0],[10,0],[20,0],[30,0],[40,0]]

###
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

###
def draw_snake(_color = "black"):
    for each in snake:
        draw_block(_color,each[0],each[1])

moveDir = [-10,0]

def move_snake():
    while hit():
        global food_pos, next_pos
        turtle.clear()
        next_pos = []
        next_pos[0] = snake[0][0] + moveDir[0]
        next_pos[1] = snake[0][1] + moveDir[1]
        snake.insert(0,list(next_pos))
        if next_pos != food_pos:
            snake.pop()
        else:
            food_pos = [random.randrange(-24,24) * 10,random.randrange(-24,24) * 10]
        draw_snake()
        turtle.ontimer(move_snake,100)
    else:
        return 1

###
def change_direction(dx,dy):
    moveDir[0] = dx
    moveDir[1] = dy

def register_keys():
    turtle.listen()
    turtle.onkey(lambda: change_direction(-10,0), 'Left')
    turtle.onkey(lambda: change_direction(10,0), 'Right')
    turtle.onkey(lambda: change_direction(0,10), 'Up')
    turtle.onkey(lambda: change_direction(0,-10), 'Down')

def draw_food(px,py):
    draw_block('red',px,py)

food_pos = [random.randrange(-24,24) * 10,random.randrange(-24,24) * 10]
px = food_pos[0]
py = food_pos[1]


###
def hit_self():
    if snake[0] in snake[1:]:
        return True
    else:
        return False

###
def hit_wall():
    if snake[0][0] >= caption_width // 2 or snake[0][0] <= -(caption_width // 2) \
        or snake[0][1] >= caption_height //2 or snake[0][1] <= -(caption_height // 2):
        return True
    else:
        return False

###
def hit():
    return hit_self() or hit_wall()