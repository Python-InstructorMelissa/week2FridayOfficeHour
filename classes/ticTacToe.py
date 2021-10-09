import random

red = "Red Team"
blue = "Blue Team"

class TicTacToe:

    def __init__(self):
        self.board = []

    def createBoard(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def getRandomTeam(self):
        return random.randint(0, 1)

    def swapTeam(self, team):
        return 'X' if team == 'O' else 'O'

    def showBoard(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def choseSpot(self, row, col, team):
        self.board[row][col] = team

    def isWin(self, team):
        win = None
        n = len(self.board)
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != team:
                    win = False
                    break
            if win:
                return win
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != team:
                    win = False
                    break
            if win:
                return win
        win = True
        for i in range(n):
            if self.board[i][i] != team:
                win = False
                break
        if win:
            return win
        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != team:
                win = False
                break
        if win:
            return win
        return False
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def boardFilled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True



    def start(self):
        self.createBoard()
        if self.getRandomTeam() == 1:
            print(f"{red} will be player X\n{blue} will be player O\n")
            team = "X"
        else: 
            print(f"{blue} will be player X\n{red} will be player O\n")
            team = "O"
        while True:
            print(f"{team} turn")
            self.showBoard()
            row, col = list(
                map(int, input("Enter row and column numbers to chose spot: Please enter like this: 1 3  ").split()))
            print()
            self.choseSpot(row - 1, col - 1, team)
            if self.isWin(team):
                print(f"{team} Team wins the game!")
                break
            if self.boardFilled():
                print("Match Draw!")
                break
            team = self.swapTeam(team)
        print()
        self.showBoard()
