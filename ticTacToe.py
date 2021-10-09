
currentPlayer = 'blue'
gamestate = ["", "", "", "", "", "", "", "", ""]

def winner(cP):
    print(f"The {cP} has Won!")

def draw():
    print("The game ended in a draw!")

def cPTurn(cP):
    print(f"It's {cp}'s turn")

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def handleChoice(choice):
    gameState[choice] = currentPlayer
    print(f"{currentPlayer} placed and x in cell {choice}")

def changePlayer():
    if currentPlayer == "blue":
        currentPlayer == "red"
    print(f"It is now {currentPlayer}'s turn")

