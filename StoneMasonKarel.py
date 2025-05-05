"""
File: StoneMasonKarel.py
Name: 姜譿允
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def turn_right():
    """
    Karel will turn left three times
    """
    for i in range(3):
        turn_left()


def fill_up_line():
    """
    Pre-condition: Karel is at the bottom of the avenue
    Post-condition: Karel is at the top of the avenue
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()
    if not on_beeper():
        put_beeper()
    turn_back()


def turn_back():
    """
    Pre-condition: Karel is at the top of the avenue
    Post-condition: karel is at the bottom of the avenue
    """
    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    turn_left()



def main():
    """
    Pre-condition: Karel is at (1,1) facing East
    Post-condition: karel is at (1,13) facing East
    """
    while front_is_clear():
        fill_up_line()
        walk()
    fill_up_line()



def walk():
    """
    Karel will move four times
    """
    for i in range(4):
        move()




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
