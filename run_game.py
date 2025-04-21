#######################################
#
#   Import Libraries And Set Variables
#
#######################################

import pgzrun
from random import randint
import time

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
next_dot = 0
start_time = time.time()
time_limit = 30 #30 Second Time Limit
game_state = "playing"

#######################################
#
#   Create Actors
#
#######################################

def create_dots():
    global dots, next_dot, lines, start_time, game_state

    dots = []
    lines = []
    next_dot = 0
    start_time = time.time()
    game_state = "playing"

    for i in range(15):
        if i < 10:
            actor = Actor("dot")
        else:
            actor = Actor("red-dot")
        actor.pos randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        dots.append(actor)

    shuffle(dots)
    
    
#######################################
#
#   Main Draw Function
#
#######################################

def draw():
    screen.fill("black")

    if game_state == "won":
        screen.draw.text("You Win!", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color = "green")
        screen.draw.text("Click to Restart", center=(WIDTH //2, HEIGHT //2 + 40), fontsize=30, color = "yellow")
        return
    
    number = 1
    for dot in dots:
        if dot.image == "dot"
            screen.draw.text(str(number),(dot.pos[0], dot.pos[1] + 12))
            number += 1
        dot.draw()
        
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0 , 0))

    #Timer Function
    elapsed = time.time() - start_time
    remaining  = max(0, int(time_limit - elapsed))
    screen.draw.text(f"Time: {remaining}", (10,10) color = "white")

#######################################
#
#   Game Functions
#
#######################################

def on_mouse_down(pos):
    global next_dot
    global lines

    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot += 1

    else:
        lines = []
        next_dot = 0
        
pgzrun.go()
