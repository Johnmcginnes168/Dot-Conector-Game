#######################################
#
#   Import Libraries And Set Variables
#
#######################################

import pgzrun
from random import randint, shuffle
import time

#Screen Dimensions
WIDTH = 400
HEIGHT = 400

#Game State Variables
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
        actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
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
        screen.draw.text("Click to Restart", center=(WIDTH //2, HEIGHT //2 + 40), fontsize=30, color = "white")
        return
    elif game_state == "lost":
        screen.draw.text("You Lose!", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color = "red")
        screen.draw.text("Click to Restart", center=(WIDTH //2, HEIGHT //2 + 40), fontsize=30, color = "white")

    #Draw Numbered Dots
    number = 1
    for dot in dots:
        if dot.image == "dot":
            screen.draw.text(str(number),(dot.pos[0], dot.pos[1] + 12))
            number += 1
        dot.draw()

    #Draw Lines    
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0 , 0))

    #Timer Function
    elapsed = time.time() - start_time
    remaining  = max(0, int(time_limit - elapsed))
    screen.draw.text(f"Time: {remaining}", (10,10), color = "white")

#######################################
#
#   Game Functions
#
#######################################

def update():
    global game_state
    if game_state == "playing":
        elapsed = time.time() - start_time
        if elapsed > time_limit:
            game_state = "lost"
    

def on_mouse_down(pos):
    global next_dot, lines, game_state

    #Allow Restart After Game Over
    if game_state in ["won", "lost"]:
        create_dots()
        return
    
    if game_state != "playing":
        return

    real_dots = [dot for dot in dots if dot.image == "dot"]

    if next_dot < len(real_dots):
        expected_dot = real_dots[next_dot]
    else:
        expected_dot = None
    
    if expected_dot and expected_dot.collidepoint(pos):
        if next_dot > 0:
            lines.append((real_dots[next_dot - 1].pos, expected_dot.pos))
        next_dot += 1
        
        if next_dot >= len(real_dots):
            game_state = "won"

    else:
        # Check if clicked on a wrong dot or decoy
        for dot in dots:
            if dot.collidepoint(pos):
                if dot.image != "dot" or dot != expected_dot:
                    game_state = "lost"
                    return

        # Reset on incorrect click
        lines = []
        next_dot = 0
        
#######################################
#
#   Start Game
#
#######################################
create_dots()
pgzrun.go()
