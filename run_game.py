#######################################
#
#   Import Libraries And Set Variables
#
#######################################

import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0

#######################################
#
#   Create Actors
#
#######################################

for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), \
                randint(20, HEIGHT - 20)
    dots.append(actor)
    
#######################################
#
#   Main Draw Function
#
#######################################

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.dar.text(str(number), \
                        (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1

    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0 , 0))
pgzrun.go()
