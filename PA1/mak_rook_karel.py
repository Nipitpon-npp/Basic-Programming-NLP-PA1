from stanfordkarel import *

def main():
    while facing_east() or facing_west():
        put_beeper()
        for i in range(2):
            if front_is_clear():
                move()
            elif front_is_blocked() and facing_east():
                turn_left()
                if front_is_clear() and facing_north():
                    move()
                    turn_left()
            elif front_is_blocked() and facing_west():
                turn_right()
                if front_is_clear() and facing_north():
                    move()
                    turn_right()

def turn_right():
    for i in range(3):
        turn_left()
    
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('worlds/5x5.w')