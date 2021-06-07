class cal1:

    def setdata(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3


    def display(self):
        sum =  self.n1+self.n2+self.n3
        print('Ans is: ', sum)


c1 = cal1()
c1.setdata(10,20,30)
c1.display()