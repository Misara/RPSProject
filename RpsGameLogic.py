# -*- coding: utf-8 -*-
"""
This is the file for the game logif for RPS
"""

PTS_ROCK = 3;
PTS_PAPER = 2;
PTS_SCISSORS = 1;

# functions
def prompt_move(player):
    """ prompt user for next move """
def win_round(p1, p2):
    """ checks win state, returns winning player """
def win_game(p1, p2):
    """ checks if either player has reached 10 points, wining game """
def assign_pts(p1, p2):
    """ assigns points based on win and past performance """
    
# initalize
p1 = {};
p1['total_pts'] = 0;
p2 = {};
p2['total_pts'] = 0;
  
# loop until win:
while win_game(p1, p2) == 0:
    # request move from p1
    prompt_move(p1);
    # request move from p2
    prompt_move(p2);
    # check win condition
    win_round(p1, p2);
    # assign points
    assign_pts(p1, p2);
    
