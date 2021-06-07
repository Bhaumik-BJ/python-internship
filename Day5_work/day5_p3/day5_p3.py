class cal3:

    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t


    def callinterest(self):
        interest =self.p*self.r*self.t/100
        print('Simple Interest is: ', interest)


c3 = cal3(100000,5,1)
c3.callinterest()