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
_nw_n, _n_ne = False, False
_nw_w, _n_c, _ne_e = False, False, False
_w_c, _c_e = False, False
_w_sw, _c_s, _e_se = False, False, False
_sw_s, _s_se = False, False

# The player whose turn it is currently (player X or player Y)
# The value of this variable should be either the string 'X' or
# the string 'Y'

_current_player = 'X'

# Stores the owner of the given squares.
# If _leftbottom_owner equals the string 'X', that means
# player X own the left-botto  square. Initially none of the 
# squares have an owner, hence their owners are each None.

_lefttop_owner, _righttop_owner = None, None
_leftbottom_owner, _rightbottom_owner = None, None

#-------------------------------------------------------------
# Functions used only by functions within ths file.
# Note the names begin with an underscore to discourage access
# outside of this module.
#-------------------------------------------------------------

def _update_square(sq):
    """ Updates the owner of square sq, if possible.
        sq must be one of the strings 'LeftTop', 'RightTop',
        'LeftBottom', or 'RightBottom'.
        The function checks to see
           1) if the square currently is not owned by a player and
           2) if all the lines are in place to complete a square.
        If both conditions are met, it marks the square with the
        current palyer and return True. If no e of the players
        already owns the square, or if not all the four lines exist to
        complete a square, the function simply returns False."""
    
    # The function may affect one of the following variables:
    global _lefttop_owner, _righttop_owner, _leftbottom_owner, \
           _rightbottom_owner
    
    if sq == 'LeftTop' and _lefttop_owner == None \
       and _nw_n and _nw_w and _n_c and _w_c:
        _lefttop_owner = _current_player
        return True
    elif sq == 'RightTop' and _righttop_owner == None \
         and _n_ne and _ne_e and _c_e and _n_c:
        _righttop_owner = _current_player
        return True
    elif sq == 'LeftBottom' and _leftbottom_owner == None \
         and _w_c and _c_s and _sw_s and _w_sw:
        _leftbottom_owner = _current_player
        return True
    elif sq == 'RightBottom' and _rightbottom_owner == None \
         and _c_e and _e_se and _s_se and _c_s:
        _rightbottom_owner = _current_player
        return True 
    else:
        return False #wners remains unchanged
    
def _update_squares():
    """ Attempts to update the owner of all square that a new line
        might affect. Returns True if one or more squares recieves a
        new owner; otherwis2, the function returns False."""
    lt = _update_square('LeftTop')
    rt = _update_square('RightTop')
    lb = _update_square('LeftBottom')
    rb = _update_square('RightBottom')
    return lt or rt or lb or rb

#---------------------------------------------------------------
# Functions that reveal or control the state of the currnet game.
# These functions are meant to be used outside of this module.
#---------------------------------------------------------------

def add_line(line):
    """ Attempts to add a line between the two dots.
        The parameter 'line' must be one of 'Northwest_North,
        North_Northeast', etc.; that is, a string representing
        a line on the game board.
        If the line is not present, the function adds the line 
        and returns True.
        If the line is already present, the function does not 
        change the state of the board and returns False. """
    # The function can change one of the following global variables
    # maintainig the state of the game.
    
    global _nw_n, _n_ne, _nw_w, _n_c, _ne_e, _w_c, _c_e, \
           _w_sw, _c_s, _e_se, _sw_s, _s_se, _current_player
    
    line_added = False # Unsuccessful by default
    if line == 'Northwest_North' and not _nw_n:
        _nw_n = True
        line_added = True
    elif line == 'North_Northeast' and not _n_ne:
        _n_ne = True
        line_added = True
    elif line == 'Northwest_West' and not _nw_w:
        _nw_w = True
        line_added = True
    elif line == 'North_Center' and not _n_c:
        _n_c = True
        line_added = True
    elif line == 'Northeast_East' and not _ne_e:
        _ne_e = True
        line_added = True
    elif line == 'West_Center' and not _w_c:
        _w_c = True
        line_added = True
    elif line == 'Center_East' and not _c_e:
        _c_e = True
        line_added = True
    elif line == 'West_Southwest' and not _w_sw:
        _w_sw = True
        line_added = True
    elif line == 'Center_South' and not _c_s:
        _c_s = True
        line_added = True
    elif line == 'East_Southeast' and not _e_se:
        _e_se = True
        line_added = True
    elif line == 'Southwest_South' and not _sw_s:
        _sw_s = True
        line_added = True
    elif line == 'South_Southeast' and not _s_se:
        _s_se = True
        line_added = True
    # If the line was added successfully,
    # check to see if it contains a square
    if line_added and not _update_squares():
        # Turn moves to other player uppon a successful move
        if _current_player == 'X':
            __current_player = 'Y'
        else:
            _current_player = 'X'
    return line_added

def square_owner(sq):
    """ Returns the player who owns the given swuare
        sq must be one of the strings 'LeftTop', 'RightTop',
        'LeftTop', or 'RightBottom'.
        Returns None if the square has no owner."""
    if sq == 'LeftTop':
        return _lefttop_owner
    elif sq == 'RightTop':
        return _righttop_owner
    elif sq == 'LeftBottom':
        return _leftbottom_owner
    elif sq == 'RightBottom':
        return _rightbottom_owner
    else:
        return None
    
def check_line(line):
    """ Returns True if the line exists on the game board.
        The parameter line must be one of 'Northwest_North',
        'North_Northeast', etc.; that is, a string representing
        a line on the game board.
        If the function returns False if the line does not yet
        exist. """
    
    if line == 'Northwest_North':
        return _nw_n
    elif line == 'North_Northeast':
        return _n_ne
    elif line == 'Northwest_West':
        return _nw_w
    elif line == 'North_Center':
        return _n_c
    elif line == 'Northeast_East':
        return _ne_e
    elif line == 'West_Center':
        return _w_c
    elif line == 'Center_East':
        return _c_e
    elif line == 'West_Southwest':
        return _w_sw
    elif line == 'Center_South':
        return _c_s
    elif line == 'East_Southeast':
        return _e_se
    elif line == 'Southwest_South':
        return _sw_s
    elif line == 'South_Southeast':
        return _s_se
    else:
        return False    
    
def winner():
    """ Returns the winner, 'X' or 'Y', or 'Draw' if the game
        board is full and X and Y both own two squares. Returns
        None if open squares still exist, and so the game can
        continue. """
    # Count the player squares
    x_count, y_count = 0, 0
    
    if _lefttop_owner == 'X':
        x_count += 1
    elif _lefttop_owner == 'Y':
        y_count += 1
    if _righttop_owner == 'X':
        x_count += 1
    elif _righttop_owner == 'Y':
        y_count += 1
    if _rightbottom_owner == 'X':
        x_count += 1
    elif _rightbottom_owner == 'Y':
        y_count += 1
    if _leftbottom_owner == 'X':
        x_count += 1
    elif _leftbottom_owner == 'Y':
        y_count += 1
    if x_count + y_count == 4: # All squares filled
        if x_count > y_count:
            return 'X' # Player X won
        elif x_count < y_count:
            return 'Y' # Player Y won
        else:
            return 'Draw' # Tie game, no winner
    else:
        return None # No winner or draw; the game continues
    
    
def initialize_board():
    """ Makes the playimg board for a new game:
          1) clears all the lines from the board
          2) makes all the squares empty, and
          3) sets the current player to X 
        This function does not return a value to the caller."""
    # All of the following global variables are affected:
    global _nw_n, _n_ne, _nw_w, _n_c, _ne_e, _w_c, _c_e, \
           _w_sw, _c_s, _e_se, _sw_s, _s_se, _current_player, \
           _lefttop_owner, _righttop_owner, \
           _leftbottom_owner, _rightbottom_owner
    _nw_n = _n_ne = _nw_w = _n_c = _ne_e = _w_c = _c_e = _w_sw \
        = _c_s = _e_se = _sw_s = _s_se = False
    
    # Clear all the square (neither player owns any squares)
    _lefttop_owner = _righttop_owner = _leftbottom_owner \
        = _rightbottom_owner = None
    
    # X always begins 
    _current_player = 'X'
    
def current_player():
    """ Returns the player whose turn it is to move."""
    return _current_player()