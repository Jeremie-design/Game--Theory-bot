import pgzrun


colors = ["red","blue","green","yellow","cyan","grey","white","magenta"]
WIDTH = 600
HEIGHT = 500
index = 0


x = 300
y = 300
size = 50
dx = 3
dy = 3

def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_circle((x,y), size , colors[index])
    #screen.draw.filled_rect(Rect((x, y), (size, size)), "red")

def update():
    global x, y, dx, dy, index
    x += dx
    y += dy
    if x + size > WIDTH or x < 0:
        dx *= -1 
        index = (index + 1) %len(colors)
        print(index)
    if y + size > HEIGHT or y < 0:
        dy *= -1 
        index = (index + 1) %len(colors)
        print(index)
        
        print(index)



pgzrun.go()




