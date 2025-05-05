"""
File: StepUp.py
Name: 姜譿允
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


def turn_right():
    #Karel will turn left 3 times
    for i in range(3):
        turn_left()


def go_up():
    """
    Pre-condition: Karel is at (1,1) facing East
    Post-condition: Karel is at (2,3) facing East
    """
    move()
    pick_beeper()
    move()
    turn_left()
    move()


def main():
    """
    Pre-condition: karel is at (1,1) facing East
    Post-condition: Karel is at (2,5) facing East
    """
    #algorithm
    go_up()
    turn_right()
    move()
    put_99_beeper()
    move()



def put_99_beeper():
    """
    Pre-condition: no beeper
    Post-condition: 99 beepers
    """
    for i in range(99):
        put_beeper()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
