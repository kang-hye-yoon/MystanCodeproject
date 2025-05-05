"""
File: CollectNewspaperKarel.py
Name: 姜譿允
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def go_to_newspaper():
    """
    Pre-condition: Karel is at (4,3) facing East
    Post-condition: Karel is at (3,6) facing East
    """
    for i in range(2):
        move()
    turn_right()
    move()
    turn_left()
    move()


def turn_right():
    """
    Karel will turn three times
    """
    for i in range(3):
        turn_left()


def main():
    """
    Pre-condition: Karel is at (4,3) facing East, no beeper
    Post-condition: Karel is at (4,3) facing East, with one beeper
    """
    go_to_newspaper()
    pick_beeper()
    bring_newspaper_back()


def bring_newspaper_back():
    """
    Pre-condition: Karel is at (3,6) facing East
    Post-condition: Karel is at (4,3) facing East
    """
    for i in range(2):
        turn_left()
    move()
    turn_right()
    move()
    turn_left()
    for i in range(2):
        move()
    for i in range(2):
        turn_left()
    put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
