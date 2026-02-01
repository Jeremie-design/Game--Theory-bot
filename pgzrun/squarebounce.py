import pgzrun


WIDTH = 600
HEIGHT = 600

x = 300
y = 300
size = 50
dx = 3  
dy = 3  

def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(Rect((x, y), (size, size)), "red")

def update():
    global x, y, dx, dy
    x += dx
    y += dy
    if x + size > WIDTH or x < 0:
        dx *= -1
    if y + size > HEIGHT or y < 0:
        dy *= -1
pgzrun.go()
