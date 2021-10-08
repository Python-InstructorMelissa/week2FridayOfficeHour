from classes.player import Player
import time
from os import system, name


def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

playerName = str(input('Hello, please let us know your name  '))
player = Player(playerName)
clear()

playing = True
print(f'\nWelcome {player.name}\n')
# clear()
while playing:
    message = input(f' How are you feeling today {player.name}?  ')
    playing = False
