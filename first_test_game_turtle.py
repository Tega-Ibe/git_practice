import turtle
from tkinter import messagebox

# Gain access to the game engine function 
from first_test_game import *

# Some global variables supporting tne vraphical interface 

# The first dot selected by the player when creating a line
initial_dot = None

dot_radius = 10 # Can for larger or smaller dots

def square_to_point(sq):
    """ Compute the (x, y) coordinates of the center of a square.
        Used to properly place the square's owner when it becomes
        captured."""
    
    if sq == "LeftTop":
        return (200, 400)
    elif sq == "RightTop":
        return (400, 400)
    elif sq == "LeftBottom":
        return (200, 200)
    elif sq == "RightBottom":
        return (400, 200)
    
def hit(x, y):
    """ Returns the dot (if any) that the point (x, y) is within.
        Returns None if the point (x, y) does not overlap any dot.
        Used when a player clicks the mouse over the board to
        determine which dot (if any) was selected. """
    
    dot = None # Default result 
    if 90 < x < 110 and 490 < y < 510:
        dot = "Northwest"
    elif 290 < x < 310 and 490 < y < 510:
        dot = "North"
    elif 490 < x < 510 and 490 < y < 510:
        dot = "Northeast"
    elif 90 < x < 110 and 290 < y < 310:
        dot = "West"
    elif 290 < x < 310 and 290 < y < 310:
        dot = "Center"
    elif 490 < x < 510 and 290 < y < 310:
        dot = "East"
    elif 90 < x < 110 and 90 < y < 110:
        dot = "Southwest"
    elif 290 < x < 310 and 90 < y < 110:
        dot = "South"
    elif 490 < x < 510 and 90 < y < 110:
        dot = "Southeast"
    return dot
