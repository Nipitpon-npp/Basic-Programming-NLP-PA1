from stanfordkarel import *

def main():
    for i in range(2):
        go_to_corner()
        diagonal_put_beeper()


def go_to_corner():
    while front_is_clear():
        move()
    put_beeper()
    turn_back()
    
def diagonal_put_beeper():
    while front_is_clear() and right_is_clear():
        move_right()
        move_left()
        put_beeper()
    else:
        turn_left()

def move_left():
    turn_left()
    move()

def move_right():
    turn_right()
    move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_back():
    for i in range(2):
        turn_left()

    
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('worlds/5x5.w')