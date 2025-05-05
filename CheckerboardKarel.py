"""
File: CheckerboardKarel.py
Name: 姜譿允
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def turn_right():
    """
    Karel will turn left three times
    """
    for i in range(3):
        turn_left()


def main():
    """
    Pre-condition: Karel is at (1,1) facing East
    Post-condition: Kareal is at (1,8) facing East
    """
    while front_is_clear():
        building_upward_in_steps()
        placing_with_gaps_downward()

def building_upward_in_steps():
    """
    Karel will put beepers in every other slot as it goes up
    """
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
    turn_right()


def placing_with_gaps_downward():
    """
    Karel will put beepers in every other slot as it goes down
    """
    move()
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
    turn_left()
    if front_is_clear():
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
