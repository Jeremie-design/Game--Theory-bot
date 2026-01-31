import pgzrun

# Window dimensions
WIDTH = 400
HEIGHT = 400

def draw():
    screen.fill((0, 0, 0)) # Fill screen with black
    
    # Define the square: Rect(x, y, width, height)
    my_square = Rect((150, 150), (100, 100))
    
    # Draw an outline of the square
    screen.draw.rect(my_square, (255, 255, 255))
    
    # Alternatively, draw a filled square
    # screen.draw.filled_rect(my_square, (0, 128, 255))

pgzrun.go()
