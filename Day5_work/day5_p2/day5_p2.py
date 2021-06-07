class cal2:

    def setdata(self, r):
        self.r = r


    def area(self):
        area = 3.14 * self.r * self.r
        print('Area of circle is: ', area)


c2 = cal2()
c2.setdata(2)
c2.area()