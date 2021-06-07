class Publisher:

    def PUB1(self, name):
        self.name =name
        print("Book Name is: ", self.name)

class Book(Publisher):

    def PUB2(self, page_no):
        self.page_no =page_no
        print("Book Page Number is: ", self.page_no)



class Tape(Publisher):

    def PUB3(self, Playing):
        self.playing = playing
        Print("playing: ", self.playing)


p = Tape()
p.PUB3("10")
p.PUB1("Python programming")
p.PUB2("20")
