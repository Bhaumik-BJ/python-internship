class cal5:

    def __init__(self, l, b):
        self.l = l
        self.b = b


    def CalArea(self):
        return self.l*self.b


    def display(self):
        print("Area of Recatangle is: ", c5.CalArea())



c5 = cal5(10,10)
c5.display()