class Team:
    def __init__(self, teamName):
        self.teamName = teamName
        self.redMembers = []
        self.blueMembers = []

    def addMembers(self):
        if len(self.redMembers) < len(self.blueMembers):
            self.redMembers.append(self)
            return "Red Team"
        if len(self.redMembers) > len(self.blueMembers):
            self.blueMembers.append(self)
            return "Blue Team"
        else:
            self.blueMembers.append(self)
            return "Blue Team"

    def blueTeamAdd(self, choice):
        self.blueMembers.append(choice)

    def redTeamAdd(self, choice):
        self.redMembers.append(choice)

    def printRed(self):
        memberNames = []
        for n in self.redMembers:
            memberNames.append(n.name)
        print(f'For the Red Team we have: {memberNames}')

    def printBlue(self):
        memberNames = []
        for n in self.blueMembers:
            memberNames.append(n.name)
        print(f'For the Blue Team we have: {memberNames}')

