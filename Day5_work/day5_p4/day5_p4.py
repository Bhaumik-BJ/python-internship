class cal4:

    def setdata(self, n):
        self.n = n


    def display(self):
        sqr = self.n*self.n
        print('Square of number is: ', sqr)


c4 = cal4()
c4.setdata(9)
c4.display()