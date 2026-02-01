import pgzrun

WIDTH = 600
HEIGHT = 600
index = 0
x = 150
y = 150
size = 50
dy = 3  
c_x = x +100
c_y = y -50

def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(Rect((x, y), (200, 100)), "white")
    screen.draw.filled_circle((c_x,y +50 ), 30 , "red")

    screen.draw.filled_rect(Rect((150, 150), (10, 400)), "grey")


def update():
    global y,dy
    y += dy
    if y + size > 350 or y < 153:
        dy *= -1 


pgzrun.go()


