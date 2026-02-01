#Trigonometry: Draw a ball that moves in a circle around the center of the window. Change the color of the ball as it moves, depending on its location. Use 4 colors for the top left, top right, bottom left, and bottom right quadrants. Or, for a ♦ challenge, see if you can create a smooth gradient of changing colors instead. 

import pgzrun

WIDTH = 600
HEIGHT = 600

x = 300
y = 100
dx = 2
dy = 1.5
ball_size = 20

def draw():

    screen.clear()
    screen.fill("black")
    if x < WIDTH / 2 and y < HEIGHT / 2:
        color = "red"
    elif x >= WIDTH / 2 and y < HEIGHT / 2:
        color = "blue"
    elif x < WIDTH / 2 and y >= HEIGHT / 2:
        color = "green"
    else:
        color = "yellow"
    screen.draw.filled_circle((x, y), ball_size, color)
    screen.draw.circle((300, 300), 270, "white")

def update():
    global x, y, dx, dy
    x += dx
    y += dy
    if x < 100 or x > 500:
        dx = -dx
    if y < 100 or y > 500:
        dy = -dy

pgzrun.go()
