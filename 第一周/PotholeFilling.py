"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    #Algorithm
    for i in range(3):
        move()
        turn_right()
        move()
        put_beeper()
        turn_left()
        turn_left()
        move()
        turn_right()
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
