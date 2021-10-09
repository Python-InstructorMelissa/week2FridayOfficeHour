import random

class GuessTheNumber:
    def __init__(self):
        self.answer = 0
        self.leave = 0

    def getRandomNumber(self):
        self.answer = random.randint(1,25)
        self.answer
        return self.answer

    # def print(self):
    #     print(self.answer)
    
    def checkInput(self, choice):
        if choice == self.answer:
            message = print("You guessed correct!!\n")
            message = print("Thank you for playing\nExiting to main screen\n\n")
            self.leave = 1
            return self.leave
        else:
            message = print("Sorry that was incorrect\n\n")
            self.leave = 0
            return self.leave

    def start(self):
        player = input("What shall we call you player?\n  ")
        player = player.split()
        player = player[0]
        self.getRandomNumber()
        # self.print()
        game = True
        while game:
            choice = input(f"\n\n{player}, please chose a number between 1-25\n  ")
            choice = choice.split()
            message = print(f"\nYou have chosen: {choice[0]}\nn")
            self.checkInput(int(choice[0]))
            if self.leave == 1:
                game = False
            