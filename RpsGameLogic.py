# -*- coding: utf-8 -*-
"""
This is the file for the game logic for RPS
"""

PTS_ROCK = 3;
PTS_PAPER = 2;
PTS_SCISSORS = 1;

# functions
def init_player(name):
    """ initialize player """
    p = {}
    p['total_pts'] = 0
    p['wins_game'] = 0
    p['prev_move'] = 0
    p['move_used'] = 0
    p['name'] = name
    p['round'] = {}
    
    return p

def update_player(p):
    """ update values before proceeding to the next round """
    # update number of times move used 
    if p['prev_move'] == p['round']['move']:
        p['move_used'] += 1
    else:
        p['move_used'] = 0
    # update previous move
    p['prev_move'] = p['round']['move']
    
    return p

    
def prompt_move(player):
    """ prompt user for next move """
    move_valid = 0
    # process strings for consistency
    while move_valid == 0:
        move = input(player['name']+' make your move: ')
        move = move.strip()
        move = move.lower()
        
        # check for invlaid string
        if move == 'rock' or move == 'paper' or move == 'scissors':
            move_valid = 1
            player['round']['move'] = move
        else:
            print('That move is invalid, please try again')
    
def win_round(p1, p2):
    """ checks win state, returns winning player """
    p1_move = p1['round']['move']
    p2_move = p2['round']['move']
    # check win states
    # TODO figure out a more efficient way to do this
    if p1_move == 'rock':
        if p2_move == 'rock':
            p1['round']['wins_round'] = 0
            p2['round']['wins_round'] = 0
            return
        if p2_move == 'paper':
            p1['round']['wins_round'] = 0
            p2['round']['wins_round'] = 1
            return
        if p2_move == 'scissors':
            p1['round']['wins_round'] = 1
            p2['round']['wins_round'] = 0
            return
            
    elif p1_move == 'paper':
        if p2_move == 'rock':
            p1['round']['wins_round'] = 1
            p2['round']['wins_round'] = 0
            return
        if p2_move == 'paper':
            p1['round']['wins_round'] = 0
            p2['round']['wins_round'] = 0
            return
        if p2_move == 'scissors':
            p1['round']['wins_round'] = 0
            p2['round']['wins_round'] = 1
            return
    
    elif p1_move == 'scissors':
        if p2_move == 'rock':
            p1['round']['wins_round'] = 0
            p2['round']['wins_round'] = 1
            return
        if p2_move == 'paper':
            p1['round']['wins_round'] = 1
            p2['round']['wins_round'] = 0
            return
        if p2_move == 'scissors':
            p1['round']['wins_round'] = 0
            p2['round']['wins_round'] = 0
            return
    else:
        raise Exception('This case should not be reachable in win_round')
        
    
def win_game(p1, p2):
    """ checks if either player has reached 10 points, wining game """
    # win condition is first to 10 pts
    if p1['total_pts'] >= 10:
        p1['wins_game'] = 1
        return 1;
    elif p2['total_pts'] >= 10:
        p2['wins_game'] = 1
        return 1;
    else:
        return 0;
    
def assign_pts(p1, p2):
    """ assigns points based on win and past performance """
    if p1['round']['wins_round']:
        # assign consicutivity points
        p1['total_pts'] += p1['move_used']
        # assign move points
        if p1['round']['move'] == 'rock':
            p1['total_pts'] += PTS_ROCK
        elif p1['round']['move'] == 'paper':
            p1['total_pts'] += PTS_PAPER
        elif p1['round']['move'] == 'scissors':
            p1['total_pts'] += PTS_SCISSORS
        print(p1['name']+' wins the round')

    elif p2['round']['wins_round']:
        # assign consecutivity points
        p2['total_pts'] += p2['move_used']
        # assign move points
        if p2['round']['move'] == 'rock':
            p2['total_pts'] += PTS_ROCK
        elif p2['round']['move'] == 'paper':
            p2['total_pts'] += PTS_PAPER
        elif p2['round']['move'] == 'scissors':
            p2['total_pts'] += PTS_SCISSORS
        print(p2['name']+' wins the round')
    
    else:
        print('Tie, nobody gets any points')
    
def report_win(p1, p2):
    """ report winner to players """
    if p1['wins_game']:
        print(p1['name']+' wins!')
    elif p2['wins_game']:
        print(p2['name']+' wins!')
    else:
        raise Exception('This case should not be reachable in report_win')

def restart():
    """ option to play again """
    re = input('Play again? [y/n]: ')
    re.strip()
    re.lower()
    if re == 'y':
        return 1
    else:
        return 0

# loop until manual stop
while True:    
    # initalize
    p1_name = input('Player 1, please enter name: ')
    p2_name = input('Player 2, please enter name: ')
    p1 = init_player(p1_name)
    p2 = init_player(p2_name)

    # loop until win:
    while win_game(p1, p2) == 0:
        # request move from p1
        prompt_move(p1)
        # request move from p2
        prompt_move(p2)
        print(p1['round']['move'])
        # check win condition
        win_round(p1, p2)
        # update player info
        p1 = update_player(p1)
        p2 = update_player(p2)
        # assign points
        assign_pts(p1, p2)
        print(p1['name']+' has '+p1['total_pts']+' points')
        print(p2['name']+' has '+p2['total_pts']+' points')
 
    report_win(p1, p2)
    
    # prompt for new game
    if restart() != 1:
        break
