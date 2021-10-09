from classes.player import Player
from classes.team import Team
from  classes.ticTacToe import TicTacToe
from classes.guessTheNumber import GuessTheNumber
import time
import random
from os import system, name

red = Team('Red Team')
blue = Team('Blue Team')
playing = True

def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

message = input("Welcome to our game application please hit enter to continue\n  ")

while playing:
    # message = input(f'How are you feeling today {player1.name}?\n  ')
    # message = input(f'How are you feeling today {player2.name}?\n  ')
    # clear()
    message = input(f'\nShall we play a game?\n  ')
    message = message.split()
    if message[0] == 'n':
        message = print("Thank you for visiting please come again!")
        playing = False
    else:
        gameList = input("Please chose a game from this list by typing the coresponding number:\n\n1. Tic Tac Toe\n2. Number Guessing Game\n  ")
        gameList = gameList.split()
        if gameList[0] == '1':
            message = print("Entering Tic Tac Toe\n")
            clear()
            playerName01 = str(input("Welcome, please tell us player 1's name  \n"))
            player1 = Player(playerName01)
            playerName02 = str(input("\n\nPlease tell us player 2's name  \n"))
            player2 = Player(playerName02)
            clear()
            print(f'\nWelcome, gamers \n{player1.name} you are player 1 \n{player2.name} you are player 2\n\n')
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
            ttt = TicTacToe()
            ttt.start()
            message = input(f'Would you like to play another game?\n  ')
            message = message.split()
            if message[0] == 'n':
                message = print("Thank you for playing!!!")
                playing = False
        if gameList[0] == '2':
            ngg = GuessTheNumber()
            ngg.start()
        else:
            message = input(f"We are still creating new games please type exit to leave the application\n  ")
            if message[0] == 'exit':
                message = print("Thank you for comming")
                playing = False
            else:
                playing = False