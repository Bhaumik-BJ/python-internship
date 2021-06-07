class Arith:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multiply(self):
        return self.x * self.y

    def subtract(self):
        return self.x - self.y

    def display(self):
        print("Addition of Two Numbers is: ", a.add() )
        print("Multiplication of Two Numbers is: ", a.multiply())
        print("Subtract of Two Numbers is: ", a.subtract())

a = Arith(10, 20)
a.display()
