class Player: 
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def add_score(self, points):
        self.score += points
        return self.score

ana = Player("Ana", 10)
ben = Player("Ben")

ana.add_score(5)
ben.add_score(7)

print(ana.score)
print(ben.score)
