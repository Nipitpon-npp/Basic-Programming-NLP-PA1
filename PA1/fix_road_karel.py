from stanfordkarel import *

def main():
    while front_is_clear() and facing_east():
        move()
        if right_is_clear():
            go_to_bottom_of_hole()
            fill_hole()
            at_road_level()
        
def go_to_bottom_of_hole():
    turn_right()
    long_move()
    turn_back()
    
def fill_hole():
    while left_is_blocked() and right_is_blocked():
        put_beeper()
        move()

def at_road_level():
    if left_is_clear() and right_is_clear():
        turn_right()

def long_move():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_back():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('worlds/fix_road1.w')