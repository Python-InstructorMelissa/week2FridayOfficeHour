from classes.player import Player
from classes.team import Team
import time
import random
from os import system, name


def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

playerName01 = str(input("Hello, please tell us player 1's name  "))
player1 = Player(playerName01)
clear()
playerName02 = str(input("Hello, please tell us player 2's name  "))
player2 = Player(playerName02)
clear()

red = Team('Red Team')
blue = Team('Blue Team')


playing = True
print(f'\nWelcome, gamers \n{player1.name} you are player 1 \n{player2.name} you are player 2\n\n')
# clear()
while playing:
    message = input(f'How are you feeling today {player1.name}?\n  ')
    message = input(f'How are you feeling today {player2.name}?\n  ')
    clear()
    message = input(f' Shall we play a game?\n  ')
    message = message.split()
    if message[0] == 'n':
        playing = False
    else:
        # game = input(f'Tic Tac Toe')
        rng = random.randint(1,2)
        if rng == 1:
            message  = input(f'{player1.name} please chose 1 for Team Blue or 2 for Team Red\n  ')
            # error = input(f'Your choice {message}')
            if message[0] == 1:
                blue.blueTeamAdd(player1)
                red.redTeamAdd(player2)
            else:
                red.redTeamAdd(player1)
                blue.blueTeamAdd(player2)
        else:
            message  = input(f'{player2.name} please chose 1 for Team Blue or 2 for Team Red\n  ')
            # error = input(f'Your choice{message}')
            if message[0] == 1:
                blue.blueTeamAdd(player2)
                red.redTeamAdd(player1)
            else:
                red.redTeamAdd(player2)
                blue.blueTeamAdd(player1)
        red.printRed()
        blue.printBlue()
        clear()
        print("\n\n|  1  ||  2  ||  3  |\n_________________\n  4  |  5  |  6  \n_________________\n  7  |  8  |  9  \n\n")
        game = input(f"{blue.teamName} Please chose a cell #")
        if game[0] == "1":
            print(f"{player1.name} chose cell #1")
            print("\n\n  X  |  2  |  3  \n_________________\n  4  |  5  |  6  \n_________________\n  7  |  8  |  9  \n\n")
        game = input(f"{red.teamName} Please chose a cell #")
        # playing = False
