class ReadingList:
    def __init__(self, title):
        self.title = title
        self.books = []

    def add_book(self, title, count=1):
        for _ in range(count):
            self.books.append(title)

    def titles(self):
        return self.books[:]

    def count(self):
        return len(self.books)

personal = ReadingList("Personal")
personal.add_book("Python Basics")
personal.add_book("OOP")

team = ReadingList("Team")
team.add_book("Testing")

external = personal.titles()
external.append("Outside")

print(personal.count())
print(team.count())
