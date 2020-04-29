'''
first_test_game.py

Provides the logic for a simplified connect the dots game.
The code in this module determines and enforces the rules
of the game. Callers are responsible for the game's
presentation component, that is, the user experience.

The playing surface consist pf a 3x3 grid of dots:

   @   @   @
   
   @   @   @
   
   @   @   @
   
The game allows two players, X and Y, to alternatively add horizontal and
vertical lines to connect the dots.The following shows a game in progress:

   @---@   @
       |   |
   @   @   @
           |
   @   @---@

When a player completes a square, that player wins the square and
retains control of the next turn. The following shows a game in
which a player y has completed a square:

   @---@   @
       |   |
   @   @---@   
       | Y |
   @   @---@
   
If a player conects two dots and does not complete a square,
control passes to the other player. A player must add a line 
during his/her turn. The game ends when all the dots have been 
connected. The player with more squares wins the game, and the
gane is a draw if both players ha e two squares each.

The game engine manages 12 lines. Each line is distinguished by it's 
name (a string) as shown below:

   @---'Northwest_North'---@---'North_Northeast'---@
   |                       |                       |
   |                       |                       |
   |                       |                       |
'Northwest_West'       'North_Center'          'Northeast_East'
   |                       |                       |
   |                       |                       |
   |                       |                       |
   @---'West_Center'-------@------'Center_East'----@
   |                       |                       |
   |                       |                       |
   |                       |                       |
'West_Southeast'      'Center_South'          'East_Southeast'
   |                       |                       |
   |                       |                       |
   |                       |                       |
   @---'Southwest_South'---@---'South_Southeast'---@
   
The game engine manages four squares. Each square is distinguished by
it's name (a string) as shown here:

   @------------@------------@
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   @------------@------------@
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   |            |            |
   @------------@------------@
   
The stirng 'X' represents player X and the string 'Y' represents
player Y.

'''

#---------------------------------------------------------------
# Global variables that maintain the state of the current game.
# These variables are meant to be used only within this file;
# The underscore prefix discourages their access outside of this 
# module.
#---------------------------------------------------------------

# Boolean variables that keep track of whether or not a line
# exists between two dots; for example, if 
# _nw_n is true, this means the line identified as
# 'Northwest_North' exists.

#   @---_nw_n---@---_n_ne_---@
#   |           |            |
# _nw_w       _n_c         _ne_e
#   |           |            |
#   @           @            @
#   |           |            |
# _w_sw         _c_s        _e_se
#   |           |            |
#   @---_sw_s---@---_se_e----@
#

# Initially, no lines exist anywhere