#Import the pygame zero library
import pgzrun
from random import randint

#Pygame Standard for deciding the title of your game window
TITLE = " Shoot Me"

#Pygame Standard for deciding the width and height of the game window in pixels
WIDTH = 600
HEIGHT = 600

message=""

straw=Actor('strawberry')
straw.pos=50,50

def draw():
    screen.clear()
    screen.fill(color=("black"))

    straw.draw()
    screen.draw.text(message,center=(400,20),fontsize=30)

def place_straw():
    straw.x=randint(50,WIDTH-50)
    straw.y=randint(50,HEIGHT - 50)

def on_mouse_down(pos):
    global message
    if straw.collidepoint(pos):
        place_straw()
    else:
        message="You missed"

place_straw()
pgzrun.go()